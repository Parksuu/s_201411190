
import os
import mylib
import urlparse
import requests
import lxml
import lxml.etree
import StringIO

def doIt():
    #make raw url
    _url='http://openAPI.seoul.go.kr:8088/'
    keyPath=os.path.join(os.getcwd(), 'src', 'key.properties')
    key=mylib.getKey(keyPath)
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

            

    #open
    data=requests.get(url_real).text
    tree=lxml.etree.fromstring(data.encode('utf-8'))
    nodes=tree.xpath('//STATION_NM')

    #print
    for node in nodes:
        print node.text

if __name__ == "__main__":
    doIt()