import urllib
import json


def find(name):
    try:
        url = 'https://api.github.com/users/{0}'.format(urllib.quote_plus(name.encode('utf-8')))
    except UnicodeDecodeError:
        url = 'https://api.github.com/users/{0}'.format(urllib.quote_plus(unicode(name, 'utf-8').encode('utf-8')))

    results = json.loads(urllib.urlopen(url).read())

    if results.get('name'):
        return '{0} is from {1}. He has {2} public repos and {3} public gists. {4} people follow him and he is following {5} people on GitHub.'.format(results.get('name'), results.get('location'), results.get('public_repos'), results.get('public_gists'), results.get('followers'), results.get('following'))
