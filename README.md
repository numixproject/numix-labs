# Script-O-Mighty

This is something we used to use for generating icon themes. It was dropped because several bugs emerged that were deemed too serious to try and fix. We've decided to now open-source the project so that others can examine the code and possibly find a solution we couldn't. We highly recommend you don't use this unless you know what you're doing & certainly don't use it to generate a theme for general usage because of the previously mentioned bugs.

### BUGS

These things need fixing before icon making can continue:

* No longer works with the librsvg tools in 14.04 (works in 14.10)
* Needs to use recursive intersecting instead of clipping (quite a few DEs don't support clipping)
* Native gradient support, rather than a filter layer or hacky fix

## Introduction

`numix-kit` generates complete icons from predefined SVG templates and symbols.

## Directory structure

    |-- input
    |   |-- symbols
    |   |   |-- file-manager.svg
    |   |   |-- text-editor.svg
    |   |   |-- web-browser.svg
    |   `-- templates
    |       |-- circle
    |       |-- hexagon
    |       `-- square
    |           |-- background.svg
    |           |-- blur.svg
    |           |-- clip.svg
    |           |-- overlay.svg
    |           |-- shadow.svg
    |           `-- template.meta
    `-- output
        |-- circle
        |-- hexagon
        `-- square
            |-- png
            `-- svg

## Templates and symbols

The templates and symbols reside under the `input` directory. The symbols are common to all templates, while the templates are categorized under different folders according to their name.

The SVG files in the `template` directory can have any name, but they must be referenced inside the `template.meta` file.

Each file in the directory are passed to the script as a layer. For example, `background.svg` will be passed as a layer named `background`.

It is a good idea to name the files according to their role, for example `overlay.svg` for the layer that goes on top, `shadow.svg` for the layer that acts as a drop shadow etc.

Also, it is recommended to clean up the SVG files so as to avoid errors as the script is designed to handle simple SVG data, and might have issues with complex files.

### The template.meta file

Each template must contain a `template.meta` file, which describes how to generate the resulting icon.

The syntax follows a simple approach. **Select a layer, and modify it.**

An example `template.meta` file looks like,

    background -> fill(symbol[color])
    symbol -> %drop -> fill(#000) -> filter="blur.svg" -> opacity="0.5" -> clip-path="clip.svg"
    symbol -> transform="translate(0,-1)" -> clip-path="clip.svg"
    %final -> +shadow -> +background -> +drop -> +symbol -> +overlay -> write()

So, let's see what's happening.

In the first line, we select the `background` layer and perform a `fill` operation on it. `fill` is a built-in function in the script.

Here the data passed to `fill` is `symbol[color]`. `symbol[color]` tells the script to take the `color` data from the `symbol`.

Any SVG file can contain these types of data in a simple syntax. For example, the `color` data can be defined inside the symbol as,

```xml
    <!-- color: #d64937 -->
```

Coming to the next line, we are generating a shadow for the symbol here. So, we select the `symbol` and copy into a new layer named `drop`. The `%` in front of the name tells the script to create a new layer.

Then we do a `fill` operation on it with the color `#000`.

Next, we tell the script to add the attribute `filter="blur.svg`. Here the script sees that `blur.svg` is a SVG file name and includes that file in appropriate format. If it's not a file name, it'll directly add that attribute to the layer, as it occurs in the next step with `opacity="0.5"`.

In the last line, we tell the script to create a new empty layer `final`, then add the `shadow` layer to it, then `background` and so on. The `+` in front of the name tells the script to add the layer.

Lastly, we tell the script to `write` the result with `write()`. The `write` function writes the SVG (and PNG if specified) files to the output folder with the same name as the `symbol` layer.

### Cheatsheet

    %layer              create a new layer named `layer`
    +layer              add the layer `layer` to current one
    attr="value"        add the attribute `attr` to the layer (e.g.- transform="translate(0,-1)")
    attr="file.svg"     add the file as an attribute (e.g.- clip-path="clip.svg")
    layer[property]     get `property` from `layer` (passed as an argument)
    fill(#d64937)       do a `fill` operation with the color `#d64937` (note: this is different from the `fill` property)
    write()             write the file to disk

## Ouput folder

The `ouput` folder holds the generated icons categorized under the template name and file type (SVG or PNG).

## Script usage

The usage can be accessed from the script with the `-h` or `--help` parameter.

## Quick guide to SVG

### Shapes in SVG

    rect                <rect x="0" y="0" width="500" height="50"/>
    circle              <circle cx="250" cy="25" r="25"/>
    ellipse             <ellipse cx="250" cy="25" rx="100" ry="25"/>
    line                <line x1="0" y1="0" x2="500" y2="50" stroke="#000"/>
    text                <text font-family="Raleway" font-size="25" fill="#000">Adios</text>
    path                <path d="M50,50 L100,100 A30,50 0 0,1 100,100" stroke="#000">

### Common SVG properties

    height, width       height and width respectively (e.g. - height="64", width="48")
    x, y                x and y coordinates of the element (e.g.- x="0", y="5")
    x1, y1, x2, y2      x and y coordinates of the start and end point of a line (e.g.- x1="0", y1="0", x2="30", y2="50")
    cx, cy              x and y coordinates of the center (e.g.- cx="25", cy="30")
    rx, ry              radius in the x and y axis respectively (e.g.- rx="2", ry="4")
    r                   radius of a circle (e.g. - r="24")
    opacity             opacity of an element (e.g.- opacity="0.5")
    fill                fill color of an element (e.g.- fill="#d64937")
    fill-opacity        opacity of the fill color (e.g.- fill-opacity="0.3")
    stroke              color of the stroke (e.g.- stroke="#000")
    stroke-width        thickness of the stroke (e.g.- stroke-width="2")
    stroke-opacity      opacity of the stroke (e.g.- stroke-opacity="0.7")
    transform           transform an element using commands (e.g.- transform="translate(0,-1) scale(-1, 1)")
    clip-path           clip an element to another shape with the given id (e.g.- clip-path="url(#clip)")
    mask                mask an element with another shape with the given id (e.g.- mask="url(#mask)")
    filter              apply filter with given id to an element (e.g.- filter="url(#blur)")
    font-family         font-family of a text element (e.g.- font-family="Open Sans")
    font-size           font-size of a text element (e.g.- font-size="72")
    d                   draw a path element using commands (e.g.- d="M50,50 L100,100")

### Transform commands

    translate(2,4)      move a shape 2 units along the x-axis and 4 units along the y-axis
    rotate(15)          rotates a shape by 15 degrees around the point 0,0
    rotate(15,40,40)    rotates a shape by 15 degrees around the point 40,40
    scale(2)            scales a shape by 2 times
    scale(2,3)          scales a shape by 2 times in the x-axis and 3 times in the y-axis
    skewX(10)           skews the shape by 10 degreed in the x-axis
    skewY(30)           skews the shape by 30 degreed in the y-axis
    matrix(a,b,c,d,e,f) transforms the shape with the given matrix

### Path Commands

The path commands are used to draw a path element with the `d` attribute. Uppercase commands are relative to the document, while lowercase commands are relative to the current point.

    M   x,y                moveto                      move pen to point x,y without drawing
    L   x,y                lineto                      line from current location to specified point x,y
    H   x                  horizontal lineto           horizontal line to the point x
    V   y                  vertical lineto             vertical line to the point y
    C   x1,y1 x2,y2 x,y    curveto                     cubic bezier curve from current point to x,y
                                                       x1,y1 and x2,y2 are start and end control points controlling how the curve bends
    S   x2,y2 x,y          smooth curveto              cubic bezier curve from current point to x,y
                                                       x2,y2 is the end control point
                                                       start control point is the same as the end control point of the previous curve
    Q   x1,y1 x,y          quadratic curveto           quadratic bezier curve from current point to x,y
                                                       x1,y1 is the control point controlling how the curve bends
    T   x,y                smooth quadratic curveto    quadratic bezier curve from current point to x,y
                                                       the control point is the same as the last control point used
    A   rx,ry              elliptical arc              elliptical arc from the current point to the point x,y
        x-axis-rotation                                rx and ry are the radius in x and y axis
        large-arc-flag,                                x-rotation determines how much the arc is to be rotated around the x-axis
        sweepflag                                      large-arc-flag can be either 0 or 1, neither value changes the arc
        x,y                                            sweep-flag determines the direction to draw the arc in
    Z   closepath                                      closes the path by drawing a line from current point to first point

### SVG filters

Filters can be used to apply a number of different image effects to an element.

#### Blur

```xml
    <feGaussianBlur stdDeviation="0.5"/>
```

*NOTE: The blur radius is controlled by the `stdDeviation` propery. It can take 2 parameters for the blur radius in x and y axis.*

#### Luminance mask

```xml
    <feColorMatrix type="luminanceToAlpha"/>
```

#### Hue rotate

```xml
    <feColorMatrix type="hueRotate" values="60"/>
```

#### Saturate

```xml
    <feColorMatrix type="saturate" values="0.75"/>
```

#### Grayscale

```xml
    <feColorMatrix type="matrix" values="0.3333 0.3333 0.3333 0 0 0.3333 0.3333 0.3333 0 0 0.3333 0.3333 0.3333 0 0 0 0 0 1 0"/>
```

#### Sharpen

```xml
    <feConvolveMatrix order="3 3" preserveAlpha="true" kernelMatrix="0 -1 0 -1 5 -1 0 -1 0"/>
```

#### Edge detect

```xml
    <feConvolveMatrix order="3 3" preserveAlpha="true" kernelMatrix="-5 0 0 0 0 0 0 0 5"/>
```

#### Emboss

```xml
    <feConvolveMatrix order="5 5" preserveAlpha="true" kernelMatrix="-1 0 0 0 0 0 -2 0 0 0 0 0 3 0 0 0 0 0 0 0 0 0 0 0 0"/>
```

#### Brightness

```xml
    <feComponentTransfer><feFuncR type="linear" slope="0.5"/><feFuncG type="linear" slope="0.5"/><feFuncB type="linear" slope="0.5"/></feComponentTransfer>
```

*NOTE: The amount of brightness is controlled by the `slope` property.*

#### Posterize

```xml
    <feComponentTransfer><feFuncR type="discrete" tableValues="0 0.25 0.5 0.75 1"/><feFuncG type="discrete" tableValues="0 0.25 0.5 0.75 1"/><feFuncB type="discrete" tableValues="0 0.25 0.5 0.75 1"/></feComponentTransfer>
```

#### Inverse

```xml
    <feComponentTransfer><feFuncR type="table" tableValues="1 0"/><feFuncG type="table" tableValues="1 0"/><feFuncB type="table" tableValues="1 0"/></feComponentTransfer>
```

#### Discrete

```xml
    <feGaussianBlur stdDeviation="1.5" /><feComponentTransfer><feFuncR type="discrete" tableValues="0 .5 1 1"/><feFuncG type="discrete" tableValues="0 .5 1"/><feFuncB type="discrete" tableValues="0"/></feComponentTransfer>
```

#### X-Ray

```xml
    <feColorMatrix type="matrix" values="0.2126 0.7152 0.0722 0 0 0.2126 0.7152 0.0722 0 0 0.2126 0.7152 0.0722 0 0 0 0 0 1 0" /><feComponentTransfer ><feFuncR type="table" tableValues="1 0"/><feFuncG type="table" tableValues="1 0"/><feFuncB type="table" tableValues="1 0"/></feComponentTransfer>
```

### Resources

1. [An SVG primer for today's browsers](http://www.w3.org/Graphics/SVG/IG/resources/svgprimer.html)
2. [SVG attribute index](http://www.w3.org/TR/SVG/attindex.html)
3. [SVG filter effects](http://www.w3.org/TR/SVG/filters.html)
