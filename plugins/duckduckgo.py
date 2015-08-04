from libs import request


def matches(text):
    return text


def raw(m):
    results = request.ajax('http://api.duckduckgo.com/?format=json&t=numibot&no_html=1&skip_disambig=1&q=' + request.quote_plus(m.get('text')))

    if results and results.get('AbstractText'):
        return results


def query(m):
    results = raw(m)

    if results:
        return results.get('AbstractText') + '\n\n' + results.get('AbstractURL') + '\n\n(via DuckDuckGo)'
