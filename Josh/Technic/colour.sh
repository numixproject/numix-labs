#!/bin/bash

# This script allows you to take the symbols in this icon theme and
# recolour them all to any colour you like. It does not at present have
# a method for reverting changes so to get back to the multicoloured
# you must reinstall the package default. To use simply run this script
# and specify the 6 digit hex code of the colour you wish to use, or one
# of the default colours. For example, entering 'd64937' or 'red' would
# make all your icons the Numix red! 

# Copyright (C) 2014
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License (version 3+) as
# published by the Free Software Foundation. You should have received
# a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

# Paints the icons all the same
function painter() {
    for dir in scalable/*; do
        for file in "$dir"/*; do
            if [ -L "$file" ]; then
                : # pass
            else
                sed -i "s/#[a-fA-F0-9]\{6\}\"/#$1\"/g" "$file"
                sed -i "s/fill:#[a-fA-F0-9]\{6\}/fill:#$1/g" "$file"
            fi
        done
    done    
}

# Picks a from hex or a default
function picker() {
    # Converts to lower case
    1="${1,,}"
    case "$1" in
        # Defaults
        black)
            painter 2d2d2d;;
        white)
            painter f9f9f9;;
        red)
            painter d64937;;
        blue)
            painter 268bd2;;
        yellow)
            painter ebad1b;;
        green)
            painter 27ae60;;
        purple)
            painter 9f44ad;;
        # Hex Code
        [a-f0-9]"{6}")
            painter "$1";;
        # Invalid
        *)
            echo "'$1' is not a valid colour!"
            exit 1;;
    esac
}

# Run
read -p "Enter a colour: " ans
picker "$ans"
echo -e "Icons recoloured!"
