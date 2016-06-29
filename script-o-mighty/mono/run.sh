#!/bin/bash

# Fetching app symbols
git clone https://github.com/numixproject/numix-icon-theme-technic.git
mv numix-icon-theme-technic/scalable/apps input/symbols-desktop
rm -rf numix-icon-theme-technic

# Removing symlinks and recolouring
for file in input/symbols-desktop/*; do
	if [ -L "$file" ]; then
		rm "$file"
	else
		sed -i "s/#.\{6\}\"/#f9f9f9\"/g" "$file"
		sed -i "s/fill:#.\{6\}/fill:#f9f9f9/g" "$file"
	fi
done

# Iterating over known templates
for dir in input/templates/*; do
	echo $dir
	if [[ "$dir" == *android* ]]; then
		# Android Themes
		for file in input/symbols-android/*; do
			# Calculates colour codes
			lightRGB=$(cat "$file" | sed "s/-->.*//g" | sed "s/.*#//g")
			darkRGB=$(exec ./darken.py "$lightRGB")
			# Preparing background files
			rm "$dir"/background.svg
			cp "$dir"/gradient.svg "$dir"/background.svg
			# Adding gradient colours
			sed -i "s/ffffff/$lightRGB/g" "$dir"/background.svg
			sed -i "s/000000/$darkRGB/g" "$dir"/background.svg
			# Preparing icon elements
			cp "$file" input/symbols/
			./numix-kit -t $(echo "$dir" | sed "s/.*\///g")
			echo Running with $(echo "$dir" | sed "s/.*\///g")
			rm input/symbols/$(echo $file | sed "s/.*\///g")
		done
	elif [[ "$dir" == *desktop* ]]; then
		# Desktop Themes
		for file in input/symbols-desktop/*; do
			# Calculates colour codes
			lightRGB=$(cat "$file" | sed "s/-->.*//g" | sed "s/.*#//g")
			darkRGB=$(exec ./darken.py "$lightRGB")
			# Preparing background files
			rm "$dir"/background.svg
			cp "$dir"/gradient.svg "$dir"/background.svg
			# Adding gradient colours
			sed -i "s/ffffff/$lightRGB/g" "$dir"/background.svg
			sed -i "s/000000/$darkRGB/g" "$dir"/background.svg
			# Preparing icon elements
			cp "$file" input/symbols/
			echo Running with $(echo "$dir" | sed "s/.*\///g")
			rm input/symbols/$(echo $file | sed "s/.*\///g")
		done
	else
		echo "Unknown icon type"
	fi
done