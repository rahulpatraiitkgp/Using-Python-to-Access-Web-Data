import urllib
import xml.etree.ElementTree as ET

url = 'http://python-data.dr-chuck.net/comments_306570.xml'
data = urllib.urlopen(url).read()
tree = ET.fromstring(data)
counts = tree.findall('comments/comment/count')
total = 0
for count in counts:
    total += int(count.text)

print 'total: ', total