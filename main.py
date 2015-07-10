import sidLibs


print "Enter URL"
url=raw_input("> ")
ret = sidLibs.pullVersion(url)
sidLibs.dataEx(ret[0],ret[1])
