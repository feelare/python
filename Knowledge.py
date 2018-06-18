#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import HttpClient

class Knowledge :
    url  = "http://www.gintong.com/knowledge"
    def __init__(self, id, columnType):
        self.id = id
        self.columnType = columnType

    def get(self, headers):
        knowUrl = url + "/knowledge/" + id + "/" + columnType
        knowDetail = HttpClient.HttpGet(knowUrl, headers)
        return knowDetail