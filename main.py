from bs4 import BeautifulSoup as bs
from random import *
from tkinter import *
from tkinter.ttk import *
import re
import time
import urllib3

## create main window of app
# main window object called "root"
root = Tk()
entrantList = Tk()

# title and size
root.title("FA Watcher Raffle")
root.geometry('350x200')
entrantList.title("Entrants")
entrantList.geometry('200x900')

# urllib3 init
http = urllib3.PoolManager()

# set up GUI elements | main window
mainListLabel = Label(root, text="Get followers list from:")
unameText = Text(root, height=1, width=30)
submit_button = Button(root, text="submit",command=lambda:unameSubmit())

sndLabel = Label(root, text="Manual entries")
newEntrantText = Text(root, height=1, width=30)
entrant_submit_button = Button(root, text="submit",command=lambda:update_list_10())

countVar = IntVar()
entrant_count = Label(root, textvariable=countVar)

strVar = StringVar()
winning_entrant = Label(root, textvariable=strVar)

# set up GUI elements | list window
frame = Frame(entrantList)
entrantsListbox = Listbox(frame, height=800, width=30)
scrollbar = Scrollbar(frame, orient=VERTICAL)

randomizeButton = Button(root, text="shuffle", command=lambda:shuffler())

# FUNCTION TIME
def unameSubmit():
	uname = unameText.get("1.0", "end-1c")
	url = f'https://www.furaffinity.net/watchlist/to/' + uname + '/1'
	# print("URL with username: " + uname + " | " + url)

	userlist = parse_http(url)
	updatelist(userlist)

def increment_pagenum(url):
	pattern = r"\/(\d+)\b"
	baseurl = re.sub(pattern, '', url)

	matchobj = re.search(pattern, url)
	pagenum = int(matchobj.group().strip('/')) + 1

	return baseurl + '/%d' % pagenum

def parse_http(url):
	# NOTE trying to get the followers list for amazinarts is giving links from the main page of FA
	lst = []

	lst = parse_http_helper(url, lst)
	while len(lst) % 200 == 0:
		url = increment_pagenum(url)
		lst = parse_http_helper(url, lst)

	return lst

def parse_http_helper(url, lst):
	response = http.request('GET', url)
	soup = bs(response.data, 'html.parser')
	content = soup('a')

	for i in content:
		lst.append(str(i.string))

	return lst

def updatelist(lst):
	# completely replaces what's already in the second list
	entrantsListbox.delete(0,'end')
	entrantsListbox.insert('end',*lst)
	entrantsListbox.pack()
	list_count()

def update_list_10():
	entrant = newEntrantText.get("1.0", "end-1c")
	#for i in range(0,10):
	entrantsListbox.insert(0, entrant)
	entrantsListbox.pack()
	list_count()

def list_count():
	countVar.set(len(list(entrantsListbox.get("0", "end"))))
	strVar.set(entrantsListbox.get(0))

def shuffler():
	lst = list(entrantsListbox.get("0", "end"))
	# shuffle it hard yo
	for i in range(0,10):
		shuffle(lst)
		updatelist(lst)

def packer():
	# display all GUI elements | main window
	mainListLabel.pack()
	unameText.pack()
	submit_button.pack()

	sndLabel.pack()
	newEntrantText.pack()
	entrant_submit_button.pack()

	entrant_count.pack()
	winning_entrant.pack()

	randomizeButton.pack()

def displayGUI():
	# display all GUI elements | list window
	frame.pack()
	entrantsListbox.pack(side=LEFT)
	scrollbar.pack(side=RIGHT,fill=Y)
	entrantsListbox.configure(yscrollcommand=scrollbar.set)
	scrollbar.config(command=entrantsListbox.yview)

# call main loop
packer()
displayGUI()
root.mainloop()