#!/usr/bin/env js

/*
 * Do not try to run this in a browser; it won't work without modifying the
 * code.
 *
 * Usage from a Linux console:
 * cat technic-icon.svg | autotouch.js > utouch-icon.svg
 *
 * You need to have "js" installed - at least that's the package name on Arch
 * Linux. Probably the same on other distributions. This is NOT the same as
 * NodeJS - it might work, but it probably won't. Sorry.
 *
 * You should always svgclean the icons outputted by this application. Use
 * Numix Project's svgclean wrapper for svgcleaner-cli; it can be found in their
 * numix-tools GitHub repo. The autotouch-all script does this for you, so you
 * don't have to.
 */
 
(function () {
    "use strict";
    var defaultIcon = "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 48 48\"><defs><radialGradient id=\"0\" cx=\"24\" cy=\"24\" r=\"23.437\" gradientUnits=\"userSpaceOnUse\"><stop stop-color=\"$COLOR\"/><stop offset=\"1\" stop-color=\"$DARK_COLOR\"/></radialGradient><mask id=\"1\">$TECHNIC</mask></defs><g mask=\"url(#1)\"><path d=\"m 47.44 11.547 l 0 24.906 c 0 10.25 0 10.984 -10.984 10.984 l -24.902 0 c -10.988 0 -10.988 -0.734 -10.988 -10.984 l 0 -24.906 c 0 -10.25 0 -10.984 10.988 -10.984 l 24.902 0 c 10.984 0 10.984 0.734 10.984 10.984\" fill=\"url(#0)\"/><path d=\"m 38.27 47.44 c 2.543 -0.012 4.379 -0.082 5.711 -0.441 l -4.23 -7.25 -4.484 7.691 1.191 0 c 0.641 0 1.242 0 1.813 0 z m 1.48 -7.691 -5.125 -8.789 -5.129 8.789 z m 0 0 7.652 0 c 0.031 -0.973 0.039 -2.063 0.039 -3.297 l 0 -1.098 -2.563 -4.395 z m 5.129 -8.789 -5.129 -8.789 -5.125 8.789 z m 0 0 2.563 0 0 -4.395 z m -10.254 0 -5.129 -8.789 -5.125 8.789 z m -10.254 0 -5.129 8.789 10.254 0 z m 0 0 -5.129 -8.789 -5.125 8.789 z m -10.254 0 -5.129 8.789 10.254 0 z m 0 0 -5.129 -8.789 -5.125 8.789 z m -10.254 0 -3.297 5.648 c 0 1.168 0.012 2.211 0.039 3.141 l 8.383 0 z m 0 0 -3.297 -5.648 0 5.648 z m 5.125 8.789 -4.313 7.395 c 1.598 0.293 3.809 0.297 6.879 0.297 l 1.922 0 z m 0 -17.578 -5.125 -8.789 -3.297 5.648 0 3.141 z m 0 0 10.254 0 -5.125 -8.789 z m 5.129 -8.789 -5.129 -8.789 -5.125 8.789 z m 0 0 10.254 0 -5.129 -8.789 z m 5.125 -8.789 -2.352 -4.03 -5.336 0 c -0.078 0 -0.141 0 -0.215 0 l -2.352 4.03 z m 0 0 10.254 0 -2.352 -4.03 -5.551 0 z m 10.254 0 10.254 0 l -2.352 -4.03 c -0.313 0 -0.609 0 -0.941 0 l -4.609 0 z m 0 0 -5.125 8.789 10.254 0 z m 5.129 8.789 10.254 0 -5.129 -8.789 z m 0 0 -5.129 8.789 10.254 0 z m 5.125 8.789 7.691 0 0 -4.395 -2.563 -4.395 z m 5.129 -8.789 2.563 0 0 -1.832 c 0 -0.914 -0.008 -1.75 -0.023 -2.523 z m -15.383 8.789 -5.125 -8.789 -5.129 8.789 z m 10.254 -17.578 7.309 0 c -0.555 -2.758 -1.887 -3.629 -5.03 -3.902 z m -30.762 0 l -2.305 -3.953 c -3.66 0.207 -5.141 0.996 -5.734 3.953 z m -5.125 8.789 l -3.238 -5.555 c -0.043 1.074 -0.059 2.309 -0.059 3.723 l 0 1.832 z m 15.379 26.367 -4.484 7.691 8.973 0 z m 10.254 0 -4.484 7.691 8.973 0 z m -26.898 6.621 -1.602 -2.746 c 0.293 1.316 0.785 2.18 1.602 2.746 z\" fill=\"#fff\" fill-opacity=\"$OPACITY\"/></g></svg>";
    var icon = readline();
    var color = icon.replace(/.*<!-- color: (#[0-9A-Fa-f]{6}) -->.*/, "$1");
    if (color === icon) color = icon.replace(/.*fill="(#(?:[0-9a-fA-F]{3}){1,2})".*/, "$1");
    if (color === icon) color = icon.replace(/.*stroke="(#(?:[0-9a-fA-F]{3}){1,2})".*/, "$1");
    if (color === icon) throw new Error("This icon does not specify a colour");
    var technic = icon;
    technic = technic.replace(/.*<svg.*?>/, "");
    technic = technic.replace(/<\/svg>.*/, "");
    technic = technic.replace(/fill="(#(?:[0-9a-fA-F]{3}){1,2})"/g, "fill=\"#fff\"");
    technic = technic.replace(/stroke="(#(?:[0-9a-fA-F]{3}){1,2})"/g, "stroke=\"#fff\"");
    if (color.length === 7) {
        var red = parseInt(color.substring(1, 3), 16);
        var green = parseInt(color.substring(3, 5), 16);
        var blue = parseInt(color.substring(5, 7), 16);
    } else {
        var red = color[1];
        red += red;
        red = parseInt(red, 16);
        var green = color[2];
        green += green;
        green = parseInt(green, 16);
        var blue = color[3];
        blue += blue;
        blue = parseInt(blue, 16);
    }
    var darkRed = red - 32;
    if (darkRed < 0) darkRed = 0;
    if (darkRed < 16) darkRed = "0" + darkRed.toString(16);
    else darkRed = darkRed.toString(16);
    var darkGreen = green - 32;
    if (darkGreen < 0) darkGreen = 0;
    if (darkGreen < 16) darkGreen = "0" + darkGreen.toString(16);
    else darkGreen = darkGreen.toString(16);
    var darkBlue = blue - 32;
    if (darkBlue < 0) darkBlue = 0;
    if (darkBlue < 16) darkBlue = "0" + darkBlue.toString(16);
    else darkBlue = darkBlue.toString(16);
    var darkColor = "#" + darkRed + darkGreen + darkBlue;
    var opacity = ((red + green + blue) / 18 - 4) / 255;
    var utouch = defaultIcon;
    utouch = utouch.replace("$COLOR", color);
    utouch = utouch.replace("$DARK_COLOR", darkColor);
    utouch = utouch.replace("$TECHNIC", technic);
    utouch = utouch.replace("$OPACITY", opacity);
    print(utouch);
})();
