import re

from libs import colorman


def matches(text):
    return re.search('(hex|rgb|hsl|hsv)\s+((of|for)\s+)?(.+)', text, re.IGNORECASE)


def decode(text):
    g = matches(text).groups()

    if g:
        return [g[0], g[3]]


def query(m, t, c):
    if t and c:
        return getattr(colorman, 'to{0}'.format(t.lower()))(c)
