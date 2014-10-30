#!/usr/bin/js
(function () {
    "use strict";
    var icon = readline();
    var color = icon.replace(/.*<!-- color: (#(?:[0-9a-fA-F]{3}){1,2}) -->.*/, "$1");
    if (color === icon) color = icon.replace(/.*fill="(#(?:[0-9a-fA-F]{3}){1,2})".*/, "$1");
    if (color === icon) color = icon.replace(/.*stroke="(#(?:[0-9a-fA-F]{3}){1,2})".*/, "$1");
    if (color === icon) throw new Error("This icon does not specify a colour");
    print(color);
})();
