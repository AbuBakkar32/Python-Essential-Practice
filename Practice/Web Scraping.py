import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
# context=ctx

"""url = urllib.request.urlopen('https://www.dr-chuck.com').read()
soup = BeautifulSoup(url, 'html.parser')

# Retrieve all of the anchor tags
#for read in soup.find_all(True):
    #print(read)
count = 0
tags = soup('a')
for tag in tags:
    ret = tag.get('href', None)
    count +=1
    print(ret)
print(count)"""

# this is for calculation and count the page value

"""html = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_464742.html").read()
soup = BeautifulSoup(html)
tag = soup("span")
count = 0
sum = 0
for i in tag:
    x = int(i.text)
    count += 1
    sum = sum + x
print(count)
print(sum)"""

# This is another way to scraping the web page

"""url = input('Enter Url: ')
count = int(input("Enter count: "))
position = int(input("Enter position:"))
for i in range(count):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    s = []
    t = []
    for tag in tags:
        x = tag.get('href', None)
        s.append(x)
        y = tag.text
        t.append(y)
print(s[position - 1])
print(t[position - 1])
url = s[position - 1]"""


url = input('Enter - ')
count_num = int(input('Enter count: '))
pos = int(input('Enter position: '))


def parseHtml(url, pos):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    i = 0
    for tag in tags:
        i += 1
        if i == pos:
            return tag.get('href', None)


current_num = 0
while current_num < count_num:
    print('Retrieving: ', url)
    url = parseHtml(url, pos)
    current_num += 1

print('The Last URL of this turn:', url)
