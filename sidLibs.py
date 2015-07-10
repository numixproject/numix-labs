#importing json libs and url request libs for version control

from json import loads
from urllib2 import urlopen
from subprocess import call

#pulls version and zip url from the repo
def pullVersion(url):
	apiInit=urlopen(url)
	jsonObj=loads(apiInit.read())
	version = jsonObj[0]['tag_name']
	zipUrl = jsonObj[0]['zipball_url']
	return version,zipUrl
 
def dataEx(version,zipUrl):
	call(['mkdir','SOURCES','SPECS'])
	call(["./pull.sh",zipUrl,version])
