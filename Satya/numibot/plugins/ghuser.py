import re

from libs import request


def matches(text):
    return re.search('(\S+)\s+on\s+(github|gh)', text, re.IGNORECASE)


def decode(text):
    g = matches(text).groups()

    if g and g[0]:
        return [g[0].lower()]


def raw(q):
    results = request.ajax('https://api.github.com/users/' + request.quote_plus(q))

    if results and results.get('login') == q:
        return results


def query(m, q):
    results = raw(q)

    if results:
        return '{0} is from {1}. He has {2} public repos and {3} public gists. {4} people follow him and he is following {5} people on GitHub.'.format(results.get('name'), results.get('location'), results.get('public_repos'), results.get('public_gists'), results.get('followers'), results.get('following'))
