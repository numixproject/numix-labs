from PIL import Image, ImageDraw, ImageColor
import StringIO
import colorsys


def clamp(x):
    return max(0, min(x, 255)) * 1.0


def parse(color):
    try:
        c = ImageColor.getrgb(color)
    except ValueError:
        return

    return (clamp(c[0]), clamp(c[1]), clamp(c[2]))


def formathex(rgb):
    return "#{0:02x}{1:02x}{2:02x}".format(int(rgb[0]), int(rgb[1]), int(rgb[2]))


def tohex(color):
    c = parse(color)

    if c:
        return formathex(c)


def torgb(color):
    c = parse(color)

    if c:
        return "rgb({0}, {1}, {2})".format(c[0], c[1], c[2])


def tohsl(color):
    c = parse(color)

    if c:
        hls = colorsys.rgb_to_hls(c[0] / 255, c[1] / 255, c[2] / 255)

        return "hsl({0}, {1}%, {2}%)".format(round(hls[0] * 360, 2), round(hls[2] * 100, 2), round(hls[1] * 100, 2))


def tohsv(color):
    c = parse(color)

    if c:
        hsv = colorsys.rgb_to_hsv(c[0] / 255, c[1] / 255, c[2] / 255)

        return "hsv({0}, {1}%, {2}%)".format(round(hsv[0] * 360, 2), round(hsv[1] * 100, 2), round(hsv[2] * 100, 2))


def lighten(color, percentage):
    c = parse(color)

    if c:
        hls1 = colorsys.rgb_to_hls(c[0] / 255, c[1] / 255, c[2] / 255)
        hls2 = (hls1[0], (hls1[1] + (percentage / 100)), hls1[2])
        rgb = colorsys.hls_to_rgb(hls2[0], hls2[1], hls2[2])

        return formathex((clamp(rgb[0] * 255), clamp(rgb[1] * 255), clamp(rgb[2] * 255)))


def darken(color, percentage):
    return lighten(color, percentage * -1)


def image(color):
    img = Image.new('RGB', (120, 120))
    draw = ImageDraw.Draw(img)

    try:
        draw.rectangle((0, 0, 120, 120), fill=color)
    except ValueError:
        return

    output = StringIO.StringIO()

    img.save(output, 'JPEG')

    return output.getvalue()
