import re

from libs import colorman


def matches(text):
    return re.search('(darken|lighten)\s+(.+[^(\s+by\s+|\s+\d])\s+[^\d]*(\d+)%?', text, re.IGNORECASE)


def decode(text):
    g = matches(text).groups()

    if g:
        return [g[0], g[1], int(g[2])]


def query(m, t, c, p):
    if t and c and p:
        return getattr(colorman, t.lower())(c, p)
