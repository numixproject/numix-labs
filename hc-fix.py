#!/usr/bin/python3

# **Preamble**
# This updater code is released under the GPL v3. The license
# is included with the rest of the icon suit on GitHub. This
# script is written and maintained by Joshua Fogg for Numix.

from os import environ, execlpe, geteuid, listdir
from os.path import expanduser
from sys import executable, argv

# Checks user isn't running as root
euid = geteuid()
if euid == 0:
	print("Don't run this as root!")
	print("The root password will be asked for when needed.")
	exit()
else:
	pass

# no rooting: /home/josh/.local/share/applications/
print("Fixing local application icons...")
local_launchers = listdir(expanduser("~")+"/.local/share/applications")

# List of known local applications that use hardcoded icons
local_hardcoded = [
	["Bastion.desktop","steam","steam_icon_107100"],
	["Dota 2.desktop","steam","steam_icon_570"],
	["Kerbal Space Program.desktop","steam","steam_icon_220200"],
	["Left 4 Dead 2.desktop","steam","steam_icon_550"],
	["Left 4 Dead 2 Beta.desktop","steam","steam_icon_223530"],
	["python2.6.desktop","/usr/share/pixmaps/python2.6.xpm","python2.6"],
	["python2.7.desktop","/usr/share/pixmaps/python2.7.xpm","python2.7"],
	["python3.0.desktop","/usr/share/pixmaps/python3.0.xpm","python3.0"],
	["python3.1.desktop","/usr/share/pixmaps/python3.1.xpm","python3.1"],
	["python3.2.desktop","/usr/share/pixmaps/python3.2.xpm","python3.2"],
	["python3.3.desktop","/usr/share/pixmaps/python3.3.xpm","python3.3"],
	["python3.4.desktop","/usr/share/pixmaps/python3.4.xpm","python3.4"],
]

for launcher in local_hardcoded:
	if launcher[0] in local_launchers:
		print("Fixing "+launcher[0].replace(".desktop","..."))
		desktop_file = open(expanduser("~")+"/.local/share/applications/"+launcher[0], 'r+')
		lines = [line for line in desktop_file]
		desktop_file.close()
		# Have to open and close so truncate works. It's a bug I'm working on.
		desktop_file = open(expanduser("~")+"/.local/share/applications/"+launcher[0], 'r+')
		desktop_file.truncate()
		desktop_file.flush()
		for n in range(0, len(lines)):
			if "Icon="+launcher[1] in lines[n]:
				lines.pop(n)
				lines.insert(n, "Icon="+launcher[2]+"\n")
		for line in lines:
			desktop_file.write(line)
		desktop_file.close()
	else:
		pass

# warning_message = """
# Because fixing hardcoded icons means changing the icon
# lines of .desktop files in /usr/share/applications
# root privlages are needed. Asking for root password...\n"""

# euid = geteuid()
# if euid != 0:
#     print(warning_message)
#     args = ['sudo', executable] + argv + [environ]
#     execlpe('sudo', *args)

# print("\nAquired root!")
# print("The script will now fix the hardcoded icons...")