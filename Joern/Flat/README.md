# Numix Flat Themes
Way back we had a second set of GTK themes called the Numix Flat themes. They were self-described modern flat themes with light, dark, and mixed variants. It supported Gnome, Unity, XFCE and Openbox. These themes haven't been supported since 2014 but the source is archived here for reference.

### Manual installation
Extract the zip file to the themes directory i.e. `/usr/share/themes/`

To set the theme in Gnome, run the following commands in Terminal,

```
gsettings set org.gnome.desktop.interface gtk-theme "THEME HERE"
gsettings set org.gnome.desktop.wm.preferences theme "THEME HERE"
```

To set the theme in XFCE, run the following commands in Terminal,

```
xfconf-query -c xsettings -p /Net/ThemeName -s "THEME HERE"
xfconf-query -c xfwm4 -p /general/theme -s "THEME HERE"
```

In each case replace `THEME HERE` with `Numix Flat`, `Numix Flat Light`, or `Numix Flat Dark` as applicable.

### Requirements
* GTK+ 3.6 or above
* Murrine theme engine

### Code and license
Numix Flat was original maintained as part of [Shimmer Project](https://github.com/shimmerproject) and was created by:
* [Simon Steinbeiß](https://github.com/ochosi)
* [Joern Konopka](https://github.com/cldx)
* [Georgi Karavasilev](https://github.com/me4oslav)
* [David Barr](https://github.com/davidphilipbarr)

License: GPL-3.0+
