from tkinter import *
from tkinter.ttk import *
import urllib3
from bs4 import BeautifulSoup as bs
from random import *
import re

# urllib3 init
http = urllib3.PoolManager()

# FUNCTION TIME
def test_soup(url):
	response = http.request('GET', url)
	soup = bs(response.data, 'html.parser')
	content = soup('a')
	print(soup)

	lst = []
	for i in content:
		lst.append(str(i.string))
	return lst

def increment_pagenum(url):
	pattern = r"\/(\d+)\b"
	baseurl = re.sub(pattern, '', url)

	matchobj = re.search(pattern, url)
	pagenum = int(matchobj.group().strip('/')) + 1

	return baseurl + '/%d' % pagenum

def displaymatch(match):
	if match is None:
		return None
	return '<Match: %r, groups=%r>' % (match.group(0), match.groups())

url = f'https://www.furaffinity.net/watchlist/to/revertigone/112'
# userlist = test_soup(url)
print(increment_pagenum(url))