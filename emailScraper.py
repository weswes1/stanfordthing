import requests, re, string
pattern = re.compile("https://")

isascii = lambda s: len(s) == len(s.encode())

def getURL():
	while True:
		try:
			URL=input("Enter the URL you would like to scrape, enclosed in parentheses ")
			match = pattern.match(URL)
			if match and isascii(URL) and type(URL)==str:
				return URL
		except NameError:
			print("Begin the email with https:// and use only ASCII2 characters, be sure to enclose in parentheses")
			continue

def is200(URL):
	if (requests.get(URL,timeout=10).status_code == 200):
		return True
	return False
URL = "https://mathematics.stanford.edu/people/graduate-students/"

getURL()

