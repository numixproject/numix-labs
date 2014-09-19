#!/usr/bin/python3

from os import chdir, getcwd, listdir, makedirs, path 
from subprocess import call

# Avoids removing actual icon repos
if not path.exists("numix-check"):
	makedirs("numix-check")
	chdir("numix-check")
else:
	print("'numix-check' directory exists")
	exit()

# Icon Repos
repos = ["https://github.com/numixproject/numix-icon-theme-circle.git",
		"https://Foggalong@bitbucket.org/numixproject/numix-icon-theme-square.git",
		"https://github.com/numixproject/numix-wiki.git",
		"https://github.com/numixproject/numix-icon-theme-utouch.git",
		"https://github.com/numixproject/numix-icon-theme-shine.git"]

# Gets needed documents
call(["curl", "-s", "-o", "hc.txt", "https://raw.githubusercontent.com/Foggalong/hardcode-fixer/master/data/list/tofix.txt"])
for repo in repos:
	call(["git", "clone", repo])

# Getting support lists
full, circle, square, fold, utouch, shine = [], [], [], [], [], []
for icon in listdir(getcwd()+"/numix-icon-theme-circle/Numix-Circle/48x48/apps/"):
	if icon.replace(".svg","") in full:
		circle.append(icon.replace(".svg",""))
	else:
		full.append(icon.replace(".svg","")); circle.append(icon.replace(".svg",""))

for icon in listdir(getcwd()+"/numix-icon-theme-square/Numix-Square/48x48/apps/"):
	if icon.replace(".svg","") in full:
		square.append(icon.replace(".svg",""))
	else:
		full.append(icon.replace(".svg","")); square.append(icon.replace(".svg",""))

for icon in listdir(getcwd()+"/numix-wiki/Numix-Fold/Desktop/"):
	if icon.replace(".svg","") in full:
		fold.append(icon.replace(".svg",""))
	else:
		full.append(icon.replace(".svg","")); fold.append(icon.replace(".svg",""))

for icon in listdir(getcwd()+"/numix-icon-theme-utouch/Numix-uTouch/48x48/apps/"):
	if icon.replace(".svg","") in full:
		utouch.append(icon.replace(".svg",""))
	else:
		full.append(icon.replace(".svg","")); utouch.append(icon.replace(".svg",""))

for icon in listdir(getcwd()+"/numix-icon-theme-shine/Numix-Shine/48x48/applications/"):
	if icon.replace(".svg","") in full:
		shine.append(icon.replace(".svg",""))
	else:
		full.append(icon.replace(".svg","")); shine.append(icon.replace(".svg",""))

full.sort(key=str.lower); circle.sort(key=str.lower); square.sort(key=str.lower); fold.sort(key=str.lower); utouch.sort(key=str.lower); shine.sort(key=str.lower)

# Hardcoded
hc_list = []
target = open("hc.txt", 'r')
for line in target:
	if "|" in line and line.split("|")[4] in full:
		hc_list.append(line.split("|")[4])
target.close()

# Master list
master = []
for icon in full:
	temp = [icon]
	# Circle
	if icon in circle:
		temp.append("✔")
	else:
		temp.append("")
	# Square
	if icon in square:
		temp.append("✔")
	else:
		temp.append("")
	# Fold
	if icon in fold:
		temp.append("✔")
	else:
		temp.append("")
	# uTouch
	if icon in utouch:
		temp.append("✔")
	else:
		temp.append("")
	# Shine
	if icon in shine:
		temp.append("✔")
	else:
		temp.append("")
	# Hardcoded
	if icon in hc_list:
		temp.append("✔")
	else:
		temp.append("")
	master.append(temp)

# To file
target = open("/home/josh/Desktop/list.csv", 'w')
target.truncate()
target.write("Application,Circle,Square,Fold,uTouch,Shine,Hardcoded\n")
for line in master:
	target.write(",".join(line)+"\n")
# target.write("Percentage,%d,%d,%d,%d,%d,%d" % (len(circle)/len(full), len(square)/len(full), len(fold)/len(full), len(utouch)/len(full), len(shine)/len(full), len(hc_list)/len(full)))
target.close()


# Cleanum
call(["rm", "hc.txt"])
for repo in repos:
	call(["rm", "-rf", repo.split("/numixproject/")[1].replace(".git","")])
chdir("../")
call(["rm", "-rf", "numix-check"])