#! /bin/bash

url=$1
version=$2
cd SOURCES
wget ${url} -O ${version}.zip
folder=$(unzip ${version}.zip | grep -m1 'creating:' | cut -d' ' -f5-)
mv $folder Numix-themes

