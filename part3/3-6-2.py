import requests

with open('dataset_3378_2.txt') as inf:
    url = inf.readline().strip()
print(url)
r = requests.get(url)

number = len(r.text.splitlines())

print(number)
