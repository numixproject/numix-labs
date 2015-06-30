import sidLibs


print "Enter URL"
url=raw_input("> ")
ret = sidLibs.pullVersion(url)
sidLibs.makeDirectories(ret[0],ret[1])
