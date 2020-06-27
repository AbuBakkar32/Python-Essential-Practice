import urllib.request, urllib.parse, urllib.error

URL = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in URL:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
