Introduction
============
This is an installer for the Numix icon themes, designed to fix the problems of hardcoded icons. It was originally developed (poorly) in Python but this is an experimental fork of the one Faenza uses written in Bash. It is **not** a stable installer and isn't designed to be used by the general public.


Installation
============
Run the ./INSTALL script to choose the distribution logo (Ubuntu, by default) and the Gnome menu icon. If run as root, the script will copy the iconsets to /usr/share/icons to made them available to all users. Some default icons used by Rhythmbox may be also replaced.
Run ./UNINSTALL as root to restore defaults icons.


Launchpad PPA
=============
The Numix icon themes are available to install for Ubuntu users via a PPA repository. Open a terminal and run :

    sudo add-apt-repository ppa:numix/ppa
    sudo apt-get update
    sudo apt-get install numix-icon-theme numix-icon-theme-circle 

You can also install the "numix-icon-theme-utouch" and numix-icon-theme-shine" packages but neither are currently actively maintained.


Tips
====
* Don't use this installer.


Known issues
============
* The installer doens't work at all.


