import re
import yaml
import time
import datetime

from libs import request

import geocode

config = yaml.load(open('config.yaml', 'r'))


def matches(text):
    return re.search('time\s+(at|in)\s+(.+)', text, re.IGNORECASE)


def decode(text):
    g = matches(text).groups()

    if g and g[1]:
        return [g[1]]


def query(m, q):
    results = geocode.raw(q)

    if results:
        location = results.get('geometry').get('location')
        address = results.get('formatted_address')
        timestamp = time.time()

        timezone_results = request.ajax('https://maps.googleapis.com/maps/api/timezone/json?key=' + config.get('map_timezone_api_key') + '&location=' + str(location.get('lat')) + ',' + str(location.get('lng')) + '&timestamp=' + str(timestamp))

        if timezone_results.get('status') == 'OK':
            readabletime = datetime.datetime.fromtimestamp(timestamp + timezone_results.get('rawOffset') + timezone_results.get('dstOffset')).strftime('%A, %d %B %Y, %I:%M %p')

            return 'It\'s {0} in {1} - {2} ({3}).'.format(readabletime, address, timezone_results.get('timeZoneId'), timezone_results.get('timeZoneName'))
