#! /bin/bash                 
                      
# ==================================================
# = This Script only works with the corresponding  =
# = python scripts and only works for              =
# = Numix-Themes at the moment.                    =
# ==================================================


url=$1
version=$2
cd SOURCES
wget ${url} -O ${version}.zip
folder=$(unzip ${version}.zip | grep -m1 'creating:' | cut -d' ' -f5-)
mv $folder Numix-themes


