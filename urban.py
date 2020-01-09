from requests import get
from bs4 import BeautifulSoup
from sys import argv
from re import sub

term = argv[1]

url = "https://www.urbandictionary.com/define.php?term={}".format(term)

html = get(url).text

soup = BeautifulSoup(html, 'html.parser')

mydivs = soup.findAll("div", {"class": "meaning"})

c = 1
for i in mydivs:
	print("{}: ".format(c) + sub('&apos', "'", i.text))
	c+=1