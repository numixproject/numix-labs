import json
import logging
import urllib
import urllib2
import yaml

# for sending images
import multipart

# standard app engine imports
from google.appengine.api import urlfetch
from google.appengine.ext import ndb
import webapp2

# plugins
from plugins import intro
from plugins import geocode
from plugins import timezone
from plugins import ghuser
from plugins import showcolor
from plugins import luminance
from plugins import convertcolor
from plugins import duckduckgo
from plugins import simsimi


BASE_URL = 'https://api.telegram.org/bot' + yaml.load(open('config.yaml', 'r')).get('bot_token') + '/'


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

        message = body['message']
        message_id = message.get('message_id')
        text = message.get('text')
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

        else:

            def query(q, m):
                for plugin in (intro, geocode, timezone, ghuser, showcolor, luminance, convertcolor):
                    matches = plugin.matches(q)

                    if matches:
                        try:
                            decode = getattr(plugin, 'decode')
                        except AttributeError:
                            decode = False

                        if decode:
                            args = decode(text)

                            if args:
                                return plugin.query(m, *args)
                        else:
                            return plugin.query(m)

            back = query(text, message)

            if isinstance(back, dict) and (back.get('text') or back.get('image')):
                reply(back.get('text'), back.get('image'))
            elif isinstance(back, str):
                reply(back)
            else:
                if getEnabled(chat_id):
                    back = duckduckgo.query(message)

                    if not back:
                        back = simsimi.query(message)

                    if back:
                        reply(back)
                    else:
                        reply('What are you even talking about?')
                else:
                    logging.info('not enabled for chat_id {}'.format(chat_id))


# ================================

app = webapp2.WSGIApplication([
    ('/me', MeHandler),
    ('/updates', GetUpdatesHandler),
    ('/set_webhook', SetWebhookHandler),
    ('/webhook', WebhookHandler),
], debug=True)
