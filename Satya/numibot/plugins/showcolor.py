import re

from libs import colorman


def matches(text):
    return re.search('show\s+(((#|(rgb|hsl|hsv)\().+)|((.+\s+)?(color|colour)(\s+.+)?))', text, re.IGNORECASE)


def decode(text):
    g = matches(text).groups()

    if g:
        return [g[0]]


def raw(c):
    if (re.match('(color|colour)\s+(.+)', c, re.IGNORECASE)):
        c = re.match('(color|colour)\s+(.+)', c, re.IGNORECASE).groups()[1]
    elif (re.match('(.+)\s+(color|colour)', c, re.IGNORECASE)):
        c = re.match('(.+)\s+(color|colour)', c, re.IGNORECASE).groups()[0]

    return colorman.image(c)


def query(m, c):
    return {'image': raw(c)}
