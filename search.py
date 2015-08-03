import urllib
import json


def query(name):
    try:
        url = 'http://api.duckduckgo.com/?q={0}&format=json&t=numibot&no_html=1&skip_disambig=1'.format(urllib.quote_plus(name.encode('utf-8')))
    except UnicodeDecodeError:
        url = 'http://api.duckduckgo.com/?q={0}&format=json&t=numibot&no_html=1&skip_disambig=1'.format(urllib.quote_plus(unicode(name, 'utf-8').encode('utf-8')))

    results = json.loads(urllib.urlopen(url).read())

    if results.get('AbstractText'):
        return results.get('AbstractText') + '\n\n' + results.get('AbstractURL') + '\n\n(via DuckDuckGo)'
