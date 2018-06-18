#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64
import HttpClient
import Knowledge
import json

headers = {
    "User-Agent" : "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)",
    "Content-type" : "application/json;charset=utf-8",
    "Accept" : "text/plain",
    "sessionId" : "xxx",
    "s" : "web"}

loginBody = {"username":"xxx",
             "password":"xxx",
             "vCode":"0",
             "index":"0"}

loginUrl = "http://www.gintong.com/cross/web/login.json"
sessionId = ""

if __name__ == '__main__':
    password = base64.encodebytes(b"sa#123").decode()
    loginBody["username"] = str("feelar@qq.com")
    loginBody["password"] = password
    data = json.dumps(loginBody)
    data = bytes(data, "utf-8")
    response = HttpClient.HttpPost(loginUrl, data, {})
    print(response)
    loginRet = json.loads(response)
    retData = loginRet["responseData"]
    sessionId = retData["sessionId"]
    print("sessionId: " + sessionId)
    headers["sessionId"] = sessionId

    knowUrl = "http://www.gintong.com/knowledge" + "/knowledge/" + "317120814525321" + "/" + "1"
    knowDetail = HttpClient.HttpGet(knowUrl, headers)
    print(knowDetail)