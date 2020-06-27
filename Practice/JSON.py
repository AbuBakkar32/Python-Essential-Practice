import requests
count = 0
url = "http://py4e-data.dr-chuck.net/comments_464745.json"
link = requests.get(url).json()
print(link)

for item in link["comments"]:
    number = int(item["count"])
    count = count + number
print(count)
