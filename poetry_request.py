#!/usr/bin/env python
# coding: utf-8

import certifi
import urllib3
import json

http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',
                           ca_certs=certifi.where())


def poetry_query():
    request_url = 'https://api.apiopen.top/singlePoetry'
    response_text = http.request('GET', request_url)
    response = json.loads(response_text.data.decode('utf-8'))
    return response
