import json
import logging
import random
import urllib
import urllib2
import re
import yaml

# for sending images
import multipart

# standard app engine imports
from google.appengine.api import urlfetch
from google.appengine.ext import ndb
import webapp2

import ghuser
import timezone
import color
import search

BASE_URL = 'https://api.telegram.org/bot' + yaml.load(open("config.yaml", "r")).get("bot_token") + '/'
NUMIX_COLOR = '#F1544D'


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
                try:
                    encoded_msg = msg.encode('utf-8')
                except UnicodeEncodeError:
                    encoded_msg = unicode(msg, 'utf-8').encode('utf-8')

                resp = urllib2.urlopen(BASE_URL + 'sendMessage', urllib.urlencode({
                    'chat_id': str(chat_id),
                    'text': encoded_msg,
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
                reply('Geronimo!')
                setEnabled(chat_id, True)
            elif text == '/stop':
                reply('Goodbye, cruel world!')
                setEnabled(chat_id, False)

        # CUSTOMIZE FROM HERE

        elif re.search('who\s+(r|are)\s+(u|you)', text, re.IGNORECASE):
            reply('I am numibot, {0}. https://github.com/numixproject/numibot'.format(random.choice(['I know stuff', 'learn to love me'])))
        elif re.search('who\s+(m|am)\s+i', text, re.IGNORECASE):
            try:
                encoded_reply = 'You are {0} {1} ({2}), you need to remember stuff!'.format(fr.get('first_name'), fr.get('last_name'), fr.get('username'))
            except UnicodeEncodeError:
                encoded_reply = 'Now I have to tell you that?'

            reply(encoded_reply)
        elif re.search('\\b(hello|hola|hi|hey)\\b', text, re.IGNORECASE):
            reply('Hello {0}!'.format(random.choice([fr.get('first_name'), fr.get('username'), 'sweetie'])))
        elif re.match('numix\s+(color|colour|hex|red)', text, re.IGNORECASE):
            reply(NUMIX_COLOR)
        elif re.search('show\s+(((#|(rgb|hsl)\().+)|((.+\s+)?(color|colour)(\s+.+)?))', text, re.IGNORECASE):
            c = re.search('show\s+(((#|(rgb|hsl)\().+)|((.+\s+)?(color|colour)(\s+.+)?))', text, re.IGNORECASE).groups()[0]

            if (re.match('(color|colour)\s+(.+)', c, re.IGNORECASE)):
                c = re.match('(color|colour)\s+(.+)', c, re.IGNORECASE).groups()[1]
            elif (re.match('(.+)\s+(color|colour)', c, re.IGNORECASE)):
                c = re.match('(.+)\s+(color|colour)', c, re.IGNORECASE).groups()[0]

            if re.match('numix(\s+(hex|red))?', c, re.IGNORECASE):
                c = NUMIX_COLOR

            image = color.image(c)

            if image:
                reply(img=image)
            else:
                reply("What kind of color is that?")
        elif re.search('(hex|rgb|hsl|hsv)\s+((of|for)\s+)?(.+)', text, re.IGNORECASE):
            groups = re.search('(hex|rgb|hsl|hsv)\s+((of|for)\s+)?(.+)', text, re.IGNORECASE).groups()
            type = groups[0]
            c = groups[3]

            val = getattr(color, 'to{0}'.format(type.lower()))(c)

            if val:
                reply(val)
            else:
                reply("I don't know dude.")
        elif re.search('(darken|lighten)\s+(.+[^(\s+by\s+|\s+\d])\s+[^\d]*(\d+)%?', text, re.IGNORECASE):
            groups = re.search('(darken|lighten)\s+(.+[^(\s+by\s+|\s+\d])\s+[^\d]*(\d+)%?', text, re.IGNORECASE).groups()
            type = groups[0]
            c = groups[1]
            p = int(groups[2])

            val = getattr(color, type.lower())(c, p)

            if val:
                reply(val)
            else:
                reply("What are you telling me to do exactly?")
        elif re.search('(\S+)\s+on\s+(github|gh)', text, re.IGNORECASE):
            name = re.search('(\S+)\s+on\s+(github|gh)', text, re.IGNORECASE).groups()[1]

            username = fr.get('username') if name == 'me' or name == 'Me' else name

            result = ghuser.find(username)

            if result:
                reply(result)
            else:
                reply("Couldn\'t find {0}. Does he even exist?".format(username))
        elif re.search('time\s+(at|in)\s+(.+)', text, re.IGNORECASE):
            place = re.search('time\s+(at|in)\s+(.+)', text, re.IGNORECASE).groups()[1]

            result = timezone.query(place)

            if result:
                reply(result)
            else:
                reply("Where is that place, again?")
        elif re.match('(what|who|where|why|when)\s+(is|are)\s+(.+)', text, re.IGNORECASE):
            result = search.query(text)

            if result:
                reply(result)
            else:
                reply("I don't have an answer for that!")
        else:
            if getEnabled(chat_id):
                try:
                    resp1 = json.load(urllib2.urlopen('http://www.simsimi.com/requestChat?lc=en&ft=1.0&req=' + urllib.quote_plus(text.encode('utf-8'))))
                    back = resp1.get('res')
                except (urllib2.HTTPError, UnicodeEncodeError), err:
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
