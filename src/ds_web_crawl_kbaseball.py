
import requests
import lxml.etree

r = requests.get('http://www.kbreport.com/main')
_htmlTree = lxml.etree.HTML(r.text)
nodes = _htmlTree.xpath("//div[@class='main-stats-box']//table[@class='ms-1-con stop10-table']//tr")
print "테이블 행 갯수: ", len(nodes)
counter=0
for teams in nodes:
    for cols in teams:
        if cols.xpath('.//a/text()'):
            print cols.xpath('.//a/text()')[0],
        else:
            print cols.text.strip(),
    print
    
print "-------------------------" 

nodes = _htmlTree.xpath("//div[@class='main-stats-box']//table[@class='ms-2-con stop10-table']//tr")
counter=0
for teams in nodes:
    for cols in teams:
        if cols.xpath('.//a/text()'):
            print cols.xpath('.//a/text()')[0],
        else:
            print cols.text.strip(),
    print
    
print "-------------------------" 
    
nodes = _htmlTree.xpath("//div[@class='main-stats-box']//table[@class='ms-3-con stop10-table']//tr")
counter=0
for teams in nodes:
    for cols in teams:
        if cols.xpath('.//a/text()'):
            print cols.xpath('.//a/text()')[0],
        else:
            print cols.text.strip(),
    print
  
print "-------------------------"  
    
nodes = _htmlTree.xpath("//div[@class='main-stats-box']//table[@class='ms-4-con stop10-table']//tr")
counter=0
for teams in nodes:
    for cols in teams:
        if cols.xpath('.//a/text()'):
            print cols.xpath('.//a/text()')[0],
        else:
            print cols.text.strip(),
    print