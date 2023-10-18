#!/bin/env python3
# -*- author: lanxuage -*-
import sys
import requests

sys.path.append("..")

from randssl import randssl
from requests.adapters import HTTPAdapter


class RandsslAdapter(HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        context = randssl()
        kwargs["ssl_context"] = context
        return super(RandsslAdapter, self).init_poolmanager(*args, **kwargs)


with requests.Session() as sess:
    sess.mount(prefix="https://www.baidu.com", adapter=RandsslAdapter())
    resp = sess.get(url="https://www.baidu.com")
    print(resp.content)