from libs import request


def matches(text):
    return text


def raw(m):
    return request.ajax('http://www.simsimi.com/requestChat?lc=en&ft=1.0&req=' + request.quote_plus(m.get('text')))


def query(m):
    results = raw(m)

    if results:
        reply = results.get('res')

        if not reply:
            return
        elif 'I HAVE NO RESPONSE' in reply:
            return
        else:
            return reply
