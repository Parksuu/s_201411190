#!/usr/bin/env python
# coding: utf-8
import os
import requests
import urlparse
import urllib
import src.mylib

def doIt():
    # (1) service + operation
    SERVICE='ArpltnInforInqireSvc'
    OPERATION_NAME='getMinuDustFrcstDspth'
    params1=os.path.join(SERVICE,OPERATION_NAME)
    # (2) query params encoding
    _d=dict()
    _d['dataTerm']='month'
    params2 = urllib.urlencode(_d)
    # (3) add my service key
    keyPath=os.path.join(os.getcwd(), 'src', 'key.properties')
    key=src.mylib.getKey(keyPath)
    keygokr=key['gokr'] # keygokr='8Bx4C1%2B...'
    params=params1+'?'+'serviceKey='+keygokr+'&'+params2
    # (4) make a full url
    _url='http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc'

    url=urlparse.urljoin(_url,params)
    url_real = ''
    
    for i in url:
        if i=='\\':
            url_real += '/'
        else:
            url_real += i
    # (5) get data
    data=requests.get(url_real).text
    print data[:300]

if __name__ == "__main__":
    doIt()