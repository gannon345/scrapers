# coding: utf-8

def cleanup():
    filename = open('wormtest.html', 'r+')
    text = filename.read()
    text = text.decode('utf-8')

    for line in text:
        line.replace(u'â€¦', u'…')
        line.replace(u'â€“', u'–')
        line.replace(u'â€™', u'’')
        line.replace(u'â€œ', u'“')
        line.replace(u'â€', u'”')

    filename.close()