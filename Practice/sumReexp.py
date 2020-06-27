import re

file = open('sumReexp.txt', 'r')
sum = 0

for line in file:
    numbers = re.findall('[0-9]+', line)
    for number in numbers:
        sum = sum + int(number)

print(sum)
