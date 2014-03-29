Introduction
============
This is an installer for the Numix icon themes, designed to fix the problems of hardcoded icons. Icon themes are downloaded from GitHub to ensure they are the latest version.


Installation
============
Run the ./INSTALL script to install all the icon themes and fix as many of the hardcoded icons as possible. If run as root, the script will copy the iconsets to /usr/share/icons to made them available to all users. Run ./UNINSTALL as root to restore defaults icons.


Other Sources
=============
If you want the latest icon packages but aren't so keen on using this installer than othe roptions are available! For Ubuntu based distros the Numix icon themes are all available to install via a PPA repository. Open a terminal and run:

    sudo add-apt-repository ppa:numix/ppa
    sudo apt-get update
    sudo apt-get install numix-icon-theme numix-icon-theme-circle 

You can also install the ```numix-icon-theme-utouch``` and ```numix-icon-theme-shine``` packages but neither are currently actively maintained.

For Fedora based distros they are available through [Fedora Utils](http://satya164.github.io/fedorautils/). Open a terminal, install Fedora Utils and then run:

    sudo fedorautils -e install_numix


Tips
====
* If you're only interested in fixing the hardcoded icons running ```hc-fix.py -f``` will do just that.
* This installer hasn't being thoroughly tested so something could go wrong


Known issues
============
* Have to close and open file for truncate to work
