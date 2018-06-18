#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import urllib.parse

def HttpGet(url, headers) :
    print(url)
    request = urllib.request.Request(url, data=None, method='GET')

    fp = urllib.request.urlopen(request)
    mybytes = fp.read()
    # note that Python3 does not read the html code as string
    # but as html code bytearray, convert to string with
    mystr = mybytes.decode("utf8")
    fp.close()
    mystr

def HttpPost(url, data, headers) :
    # 创建一个request,放入我们的地址、数据、头
    request = urllib.request.Request(url, data)
    if len(headers) > 0:
        for header, value in headers.items():
            request.add_header(header, value)

    # 访问
    try:
        result = urllib.request.urlopen(request).read().decode('utf-8')
        return result
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.info())
        print(e.geturl())
        print(e.read())

