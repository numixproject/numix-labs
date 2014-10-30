AutoTouch
=========

To use AutoTouch, make a folder called icons and put any SVGs into it in the format of:

```
<!-- color: #rrggbb --><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48">$ICON</svg>
```

This format is the Numix Technicolor icon format. It means that you can automatically generate uTouch icons just by having an existing single-colored icon with a defined background color. AutoTouch will calculate the gradient and opacity of the white triangle overlay for you.

All you need to do to run the script is:

1. Install the package `js` (NOT `nodejs`). If you don't use Arch Linux and it's not in your distro's repos, manually install the [Arch Linux package](https://www.archlinux.org/packages/extra/x86_64/js/) by extracting the tar.xz into the root of your filesystem. Make sure to pick the right architecture!

2. Install the package `svgcleaner` from the AUR (you can use `yaourt`). If you don't use Arch Linux and it's not in your distro's repos, manually install the AUR package by compiling it and then extracting the resulting tar.xz into the root of your filesystem.

3. Run `./autotouch-all` to automatically "uTouchify" all the icons anywhere inside the current folder. It's best to put them in a seperate icons folder, though.
