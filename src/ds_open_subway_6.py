
import os
import src.mylib
import urlparse
import requests
import lxml
import lxml.etree
import StringIO

def doIt():
    #make raw url
    _url='http://openAPI.seoul.go.kr:8088/'
    keyPath=os.path.join(os.getcwd(), 'src', 'key.properties')
    key=src.mylib.getKey(keyPath)
    KEY=str(key['dataseoul'])
    TYPE='xml'
    SERVICE='CardSubwayStatisticsService'
    START_INDEX=1
    END_INDEX=5
    USE_MON='201306' #line number

    #make real url for parmas
    params=os.path.join(_url,KEY,TYPE,SERVICE,str(START_INDEX),str(END_INDEX),USE_MON)
    
    url=urlparse.urljoin(_url,params)
    url_real = ''
    for i in params:
        if i=='\\':
            url_real += '/'
        else:
            url_real += i

    _maxIter=2
    _iter=0

    while _iter<_maxIter:
        params=os.path.join(_url,KEY,TYPE,SERVICE,str(START_INDEX),str(END_INDEX),USE_MON)
        response = requests.get(params).text
        print response
        START_INDEX+=5
        END_INDEX+=5
        _iter+=1        

if __name__ == "__main__":
    doIt()