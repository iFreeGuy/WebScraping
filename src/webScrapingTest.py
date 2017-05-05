
#pylint: disable-msg=W0312
#pylint: disable-msg=C0301
#pylint: disable-msg=C0111
#pylint: disable-msg=C0103

#pip install requests
#pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

#http://creativeworks.tistory.com/entry/PYTHON-3-Tutorials-24-%EC%9B%B9-%ED%81%AC%EB%A1%A4%EB%9F%AClike-Google-%EB%A7%8C%EB%93%A4%EA%B8%B0-1-How-to-build-a-web-crawler

def spider(max_pages):
	page = 0
	while page < max_pages:
		#url = 'http://creativeworks.tistory.com/' + str(page)
		url = 'http://lxml.de/cssselect.html'
		print('\n... Trying to url: %s\n' % url)
		source_code = requests.get(url)
		plain_text = source_code.text
		soup = BeautifulSoup(plain_text, 'lxml')
		for link in soup.select('a'):
			print (link)
			print ('----->> %s\n' % link.get('href'))
		page += 1
		

spider(1)
