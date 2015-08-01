import urllib
import json

def find(name):
    url = 'https://api.github.com/users/{0}'.format(name)

    results = json.loads(urllib.urlopen(url).read())

    if results.get('name'):
        return '{0} is from {1}. He has {2} public repos and {3} public gists. {4} people follow him and he is following {5} people on GitHub.'.format(results.get('name'), results.get('location'), results.get('public_repos'), results.get('public_gists'), results.get('followers'), results.get('following'))
