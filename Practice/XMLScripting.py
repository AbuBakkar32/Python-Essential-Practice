import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET


url = input("Enter location: ") # http://py4e-data.dr-chuck.net/comments_464744.xml
if len(url) < 1:
    url = "http://python-data.dr-chuck.net/comments_200531.xml"
print("Retrieving " + url)

xml = urllib.request.urlopen(url).read()
print("Retrieved: " + str(len(xml)) + " characters")

tree = ET.fromstring(xml)

counts = tree.findall('.//count')
print("Count: " + str(len(counts)))

accumulator = 0

for count in counts:
    accumulator += int(count.text)

print("Sum:" + str(accumulator))