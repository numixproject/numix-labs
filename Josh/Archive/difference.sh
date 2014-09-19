#!/bin/bash

d2="/home/josh/Programs/Icons/apps/"
d1="/home/josh/Programs/Icons/numix-icon-theme-square/Numix-Square/48x48/apps"
d3="/home/josh/Programs/Icons/diff"

#cd "${d1}"
#for file in * ; do
#    if [ ! -f "${d2}/${file}" ] ; then
#        cp "${file}" "${d3}"
#    fi
#done
#cd -

cd "${d2}"
for file in * ; do
    file=$(echo $file | sed -e 's/\..*//').svg
    if [ ! -f "${d1}/${file}" ] ; then
        cp $(echo $file | sed -e 's/\..*//').svg "${d3}"
    fi
done
cd -

