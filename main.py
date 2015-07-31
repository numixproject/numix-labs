import StringIO
import json
import logging
import random
import urllib
import urllib2
import re
import random

# for sending images
from PIL import Image
import multipart

# standard app engine imports
from google.appengine.api import urlfetch
from google.appengine.ext import ndb
import webapp2

import yaml


BASE_URL = 'https://api.telegram.org/bot' + yaml.load(open("config.yaml", "r")).get("bot_token") + '/'


# ================================

class EnableStatus(ndb.Model):
    # key name: str(chat_id)
    enabled = ndb.BooleanProperty(indexed=False, default=False)


# ================================

def setEnabled(chat_id, yes):
    es = EnableStatus.get_or_insert(str(chat_id))
    es.enabled = yes
    es.put()

def getEnabled(chat_id):
    es = EnableStatus.get_by_id(str(chat_id))
    if es:
        return es.enabled
    return False


# ================================

class MeHandler(webapp2.RequestHandler):
    def get(self):
        urlfetch.set_default_fetch_deadline(60)
        self.response.write(json.dumps(json.load(urllib2.urlopen(BASE_URL + 'getMe'))))


class GetUpdatesHandler(webapp2.RequestHandler):
    def get(self):
        urlfetch.set_default_fetch_deadline(60)
        self.response.write(json.dumps(json.load(urllib2.urlopen(BASE_URL + 'getUpdates'))))


class SetWebhookHandler(webapp2.RequestHandler):
    def get(self):
        urlfetch.set_default_fetch_deadline(60)
        url = self.request.get('url')
        if url:
            self.response.write(json.dumps(json.load(urllib2.urlopen(BASE_URL + 'setWebhook', urllib.urlencode({'url': url})))))


class WebhookHandler(webapp2.RequestHandler):
    def post(self):
        urlfetch.set_default_fetch_deadline(60)
        body = json.loads(self.request.body)
        logging.info('request body:')
        logging.info(body)
        self.response.write(json.dumps(body))

        update_id = body['update_id']
        message = body['message']
        message_id = message.get('message_id')
        date = message.get('date')
        text = message.get('text')
        fr = message.get('from')
        chat = message['chat']
        chat_id = chat['id']

        if not text:
            logging.info('no text')
            return

        def reply(msg=None, img=None):
            if msg:
                resp = urllib2.urlopen(BASE_URL + 'sendMessage', urllib.urlencode({
                    'chat_id': str(chat_id),
                    'text': msg.encode('utf-8'),
                    'disable_web_page_preview': 'true',
                    'reply_to_message_id': str(message_id),
                })).read()
            elif img:
                resp = multipart.post_multipart(BASE_URL + 'sendPhoto', [
                    ('chat_id', str(chat_id)),
                    ('reply_to_message_id', str(message_id)),
                ], [
                    ('photo', 'image.jpg', img),
                ])
            else:
                logging.error('no msg or img specified')
                resp = None

            logging.info('send response:')
            logging.info(resp)

        if text.startswith('/'):
            if text == '/start':
                reply('Bot enabled')
                setEnabled(chat_id, True)
            elif text == '/stop':
                reply('Bot disabled')
                setEnabled(chat_id, False)
            elif text == '/help':
                reply('''Current Commands:
                    1. /start
                    2. /stop
                    3. /help (this menu)
                    4. /image
                    ''')
            elif text == '/image':
                img = Image.new('RGB', (512, 512))
                base = random.randint(0, 16777216)
                pixels = [base+i*j for i in range(512) for j in range(512)]  # generate sample image
                img.putdata(pixels)
                output = StringIO.StringIO()
                img.save(output, 'JPEG')
                reply(img=output.getvalue())
            else:
                reply('Didn\'t get you!')

        # CUSTOMIZE FROM HERE

        elif re.search('who\s+(r|are)\s+(u|you)', text, re.IGNORECASE):
            reply('I am numibot, learn to love me. https://github.com/numixproject/numibot')
        elif re.search('who\s+(m|am)\s+i', text, re.IGNORECASE):
            reply('You are {0} {1} ({2}), you need to remember stuff!'.format(fr.get('first_name'), fr.get('last_name'), fr.get('username')))
        elif re.search('(hello|hola|hi|hey)', text, re.IGNORECASE):
            reply('Hello {0}!'.format(random.choice([ fr.get('first_name'), fr.get('username'), 'sweetie' ])))
        elif re.search('what\s+((is\s+)?(the\s+)?)?(time)', text, re.IGNORECASE):
            reply('Look at the top-right corner of your screen!')
        elif re.search('numix\s+(color|hex)', text, re.IGNORECASE):
            reply('#F1544D')
        elif re.search('hates', text, re.IGNORECASE):
            reply('No. It\'s a lie!')
        elif re.search('(\S+)\s+on\s+(github|gh)', text, re.IGNORECASE):
            matched = re.compile('(\S+)\s+on\s+(github|gh)').match(text)

            if matched:
                groups = matched.groups()

                url = 'https://api.github.com/users/{0}'.format(groups[0])

                gh_response = urllib.urlopen(url)
                gh_results = gh_response.read()
                results = json.loads(gh_results)

                if results.get('name'):
                    reply('{0} is from {1}. He has {2} public repos and {3} public gists. {4} people follow him and he is following {5} people on GitHub.'.format(results.get('name'), results.get('location'), results.get('public_repos'), results.get('public_gists'), results.get('followers'), results.get('following')))
                else:
                    reply("Couldn\'t find {0}. Does he even exist?".format(groups[0]))
        else:
            if getEnabled(chat_id):
                try:
                    resp1 = json.load(urllib2.urlopen('http://www.simsimi.com/requestChat?lc=en&ft=1.0&req=' + urllib.quote_plus(text.encode('utf-8'))))
                    back = resp1.get('res')
                except urllib2.HTTPError, err:
                    logging.error(err)
                    back = str(err)
                if not back:
                    reply('Okay...')
                elif 'I HAVE NO RESPONSE' in back:
                    reply('I\'ve no idea what you are talking about!')
                else:
                    reply(back)
            else:
                logging.info('not enabled for chat_id {}'.format(chat_id))


app = webapp2.WSGIApplication([
    ('/me', MeHandler),
    ('/updates', GetUpdatesHandler),
    ('/set_webhook', SetWebhookHandler),
    ('/webhook', WebhookHandler),
], debug=True)
