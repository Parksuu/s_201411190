import os
import urlparse
import requests
import lxml
import lxml.etree
import StringIO
import mylib

def doIt():
    keyPath=os.path.join(os.getcwd(), 'src', 'key.properties')
    key=mylib.getKey(keyPath)
    KEY=str(key['dataseoul'])
    TYPE='xml'
    SERVICE='SearchSTNBySubwayLineService'
    START_INDEX=str(1)
    END_INDEX=str(10)
    LINE_NUM=str(2)

    params=os.path.join(KEY,TYPE,SERVICE,START_INDEX,END_INDEX,LINE_NUM)
    url_real = ''
    for i in params:
        if i=='\\':
            url_real += '/'
        else:
            url_real += i
    
    
    _url='http://openAPI.seoul.go.kr:8088/'
    url=urlparse.urljoin(_url,url_real)
    
    
    data=requests.get(url).text
    tree=lxml.etree.fromstring(data.encode('utf-8'))
    nodes=tree.xpath('//STATION_NM')
   

    for node in nodes:
        print node.text


        
if __name__ == "__main__":
    doIt()