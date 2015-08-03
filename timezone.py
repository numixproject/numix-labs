import urllib
import json
import yaml
import time
import datetime

config = yaml.load(open('config.yaml', 'r'))

GEOCODE_URL = 'https://maps.googleapis.com/maps/api/geocode/json?key=' + config.get('map_geocode_api_key')
TIMEZONE_URL = 'https://maps.googleapis.com/maps/api/timezone/json?key=' + config.get('map_timezone_api_key')


def query(name):
    try:
        geocode = GEOCODE_URL + '&address=' + urllib.quote_plus(name.encode('utf-8'))
    except UnicodeEncodeError:
        geocode = GEOCODE_URL + '&address=' + urllib.quote_plus(unicode(name, 'utf-8').encode('utf-8'))

    geocode_results = json.loads(urllib.urlopen(geocode).read())

    if geocode_results.get('status') == 'OK':
        results = geocode_results.get('results')[0]
        location = results.get('geometry').get('location')
        address = results.get('formatted_address')
        timestamp = time.time()

        timezone = TIMEZONE_URL + '&location=' + str(location.get('lat')) + ',' + str(location.get('lng')) + '&timestamp=' + str(timestamp)

        timezone_results = json.loads(urllib.urlopen(timezone).read())

        if timezone_results.get('status') == 'OK':
            readabletime = datetime.datetime.fromtimestamp(timestamp + timezone_results.get('rawOffset') + timezone_results.get('dstOffset')).strftime('%A, %d %B %Y, %I:%M %p')

            return 'It\'s {0} in {1} - {2} ({3})'.format(readabletime, address, timezone_results.get('timeZoneId'), timezone_results.get('timeZoneName'))
