'''
Author: Mukul Sharma
NUID: sharma.mu@husky.neu.edu
'''

import urlparse
import urllib
from bs4 import BeautifulSoup
import sys
import re
import time

reload(sys)
sys.setdefaultencoding('utf-8')

#Function to extract urls from the current page in list
def getUrls(link, urls, visited):
	sub = []
	
	#Sleep timer for politeness to the server
	time.sleep(1)
	
	soup = BeautifulSoup(urllib.urlopen(link).read())
	for tag in soup.findAll('a', href=True):
		tag['href'] = urlparse.urljoin(url, tag['href'])
		if "http://en.wikipedia.org/wiki/" in tag['href'] and tag['href'] not in visited and "#" not in tag['href']:
			if ":" not in (tag['href'][5:]) and str(tag['href'].find("Main_Page") == -1):
				urls.append(tag['href'])
				visited.append(tag['href'])
				sub.append(tag['href'])
			else:
				continue
	return len(sub)
	

#Main function
def main(url, keyphrase):
	urls = [url]
	crawled = set()
	visited = []
	depth = 0
	pagesRetrieved = 0
	
	#Keep track of level length using this variable
	levelLength = [1, 0, 0, 0, 0]

	while len(urls) > 0:
		while levelLength[depth] > 0:
			levelLength[depth] -= 1
			pagesRetrieved += 1
			currentUrl = urls[0]
			urls.pop(0)

			soup = BeautifulSoup(urllib.urlopen(currentUrl).read())
			if soup is None:
				continue
			'''
			Find the Keyphrase in the current url soup and continue to next iteration
			if the keyphrase concordance in not found
			'''  
			if keyphrase != None:
				if soup.findAll(text=re.compile(keyphrase, re.IGNORECASE)) == []:
					continue
			
			#To make sure no duplicate urls are found we use canonical urls
			canonicalUrl = soup.find('link', {"rel": "canonical"})['href']
			if canonicalUrl not in crawled:
				#add to crawled list
				crawled.add(canonicalUrl)
			else:
				continue
			
			#Stop condition if the total crawled urls reach 1000
			if len(crawled) == 1000:
				f = open("urls.txt", 'w')
				for url in crawled:
					f.write("%s\n" % url)
				f.close()
				print "Crawled 1000 unique urls"
				exit(0)
			
			f = open("urls.txt", "w")
			for url in crawled:
				f.write("%s\n" % url)
			f.close()
			
			#Do not discover sub-urls for the last level, just crawl them
			if depth < 4:
				levelLength[depth + 1] = levelLength[depth + 1] + getUrls(currentUrl, urls, visited)
			else:
				continue
		#Increment the depth
		depth += 1
		'''
		Note: As I use depth variable for array index, I started the depth = 0 and I 
		Stop the program when we are done crawling all 5 depths and depth is equal to 5
		'''
		if depth == 5:
			exit(0)

if len(sys.argv) == 2 or len(sys.argv) == 3:
	url = sys.argv[1]
	if len(sys.argv) == 3:
		keyphrase = sys.argv[2]
		main(url, keyphrase)
	else:
		keyphrase = None
		main(url, keyphrase)
else:
	print "Please supply arguments : 'filename' 'Seed Url' 'Key phrase' "
	exit(0)












