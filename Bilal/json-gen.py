from os import path, listdir
from sys import exit
import json
directory = "/usr/share/icons/Numix-Circle/48x48/apps/"
db = "data.json"

# read the old db file if it exists
if not path.exists(db):
    fw = open(db, "w")
    fw.write("{}")
    fw.close()
fo = open(db)
try:
    data = json.loads(fo.read())
except ValueError:
    if len(fo.read().strip()) == 0:
        data = {}
    else:
        exit("The JSON file is invalid")
fo.close()

for filename in listdir(directory):
    if path.isfile(directory + filename):
        icon = path.splitext(path.basename(filename))[0]
        if not path.islink(directory + filename):
            if icon not in data.keys():
                data[icon] = {"linux": {"root": icon, "symlinks": []}}
        else:
            real_icon = path.splitext(path.basename(path.realpath(directory + filename)))[0]
            if real_icon not in data.keys():
                data[real_icon] = {"linux": {"root": real_icon, "symlinks": []}}
            if data[real_icon]["linux"]["root"] != icon:
                if icon not in data[real_icon]["linux"]["symlinks"]:
                    data[real_icon]["linux"]["symlinks"].append(icon)

# clean empty symlinks keys
for icon in data:
    if data[icon]["linux"]:
        root = data[icon]["linux"]
        if "symlinks" in root.keys() and len(root["symlinks"]) == 0:
            del data[icon]["linux"]["symlinks"]
        else:
            sorted(data[icon]["linux"]["symlinks"], key=lambda icon_name: icon_name.lower())
sorted(data, key=lambda icon_name: icon_name.lower())

with open(db, 'w') as fp:
    json.dump(data, fp, sort_keys=True, indent=4)
