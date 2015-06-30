from json import loads
from urllib2 import urlopen
from subprocess import call

def pullVersion(url):
	apiInit=urlopen(url)
	jsonObj=loads(apiInit.read())
	version = jsonObj[0]['tag_name']
	zipUrl = jsonObj[0]['zipball_url']
	return version,zipUrl
 
def makeDirectories(version,zipUrl):
	call(['mkdir','SOURCES','SPECS'])
	call(["./pull.sh",zipUrl,version])
