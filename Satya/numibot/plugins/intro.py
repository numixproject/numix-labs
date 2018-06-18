import re
import random
import logging


who_u_re = re.compile('who\s+(r|are)\s+(u|you)', re.IGNORECASE)
who_i_re = re.compile('who\s+(m|am)\s+i', re.IGNORECASE)


def matches(text):
    return who_u_re.search(text) or who_i_re.search(text)


def query(m):
    text = m.get('text')

    if who_u_re.search(text):
        return 'I am numibot, {0}. https://github.com/numixproject/numibot'.format(random.choice(['I know stuff', 'learn to love me']))
    elif who_i_re.search(text):
        fr = m.get('from')

        try:
            return 'You are {0} {1} ({2}), you need to remember stuff!'.format(fr.get('first_name'), fr.get('last_name'), fr.get('username'))
        except UnicodeEncodeError as err:
            logging.error(err)

            return 'Now I have to tell you that?'
