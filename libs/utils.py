#!/usr/bin/python
# -*- coding: utf -*-

def slugify(value):
    import unicodedata, re

    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
    value = unicode(re.sub('[^\w\s-]', '', value).strip().lower())
    return re.sub('[-\s]+', '-', value)