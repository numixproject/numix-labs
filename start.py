#! /usr/bin/python2

import subprocess as cmd
import json as js
import urllib2 as link
api_url = "https://api.github.com/repos/shimmerproject/Numix/releases"

def version_pull():
	f=link.urlopen(api_url)
	json_object=js.loads(f.read())
	return json_object[0]["tag_name"]

x = version_pull()

tar_url = "https://github.com/shimmerproject/Numix/archive/%s.tar.gz" %x

def package_finalize():
	cmd.call(['./pkgfin.sh',tar_url,x])

package_finalize()
