import re
import yaml

from libs import request


config = yaml.load(open('config.yaml', 'r'))


def matches(text):
    return re.match('(@\S+\s+)?location\s+of\s+(.+)', text, re.IGNORECASE)


def decode(text):
    g = matches(text).groups()

    if g and g[1]:
        return [g[1]]


def raw(q):
    results = request.ajax('https://maps.googleapis.com/maps/api/geocode/json?key=' + config.get('map_geocode_api_key') + '&address=' + request.quote_plus(q))

    if results and results.get('status') == 'OK':
        return results.get('results')[0]


def query(m, q):
    r = raw(q)

    if r:
        location = r.get('geometry').get('location')

        return '{0} is located at {1} N latitude and {2} E longitude.'.format(r.get('formatted_address'), str(location.get('lat')), str(location.get('lng')))
