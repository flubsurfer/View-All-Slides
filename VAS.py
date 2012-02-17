#!/usr/bin/python
import httplib
from urlparse import urlparse
import urllib2
import urllib
from BeautifulSoup import BeautifulSoup
import re


#PARSE CURRENT URL
url= "PUT URL IN BETWEEN THESE QUOTES"

#START LOOP
while 1 == 1:

#WHEN CURRENT URL IS FOUND (EXAMPLE)
	urlcomponents = urlparse(url)
	page = urllib2.urlopen(url).read()
	soup = BeautifulSoup(page)
	soup.prettify()


#FIND TITLE USING BEAUTIFUL SOUP TAG PARSING 
	title = soup.findAll('title') 
	# [<title>Page title</title>,


#FIND TITLE, DESCRIPTION, AND KEYWORDS USING META TAGS
	title2=''; description=''; keywords=''
# Try to get the slide title from the meta tag named title
	try:
		title2 = soup.findAll('meta', attrs={'property':re.compile("title|og:title", re.I)})[0].get('content')
	except:
		pass
# If the meta tag does not exist, grab the title from the title tag.
	if not title2:
		title2 = soup.title.string
	#description = soup.findAll('meta', attrs={'name':re.compile("^description$", re.I)})[0].get('content')
	#keywords = soup.findAll('meta', attrs={'name':re.compile("^keywords$", re.I)})[0].get('content')


#FIND SLIDE NAME
	try:
		slidename  = soup.findAll('input', attrs={'name':re.compile("title", re.I)}) 
	#slidename = soup.findAll ("input", {"name": "print-slide-title"})
		for slidename in slidename:
			cleanslidename = slidename['value']	
	except:
		pass
	if not slidename:
		slidename = soup.findAll('div', attrs={'class':re.compile("cptn", re.I)}) 
	if not slidename:
		slidename = title2

						  
#GET PARAGRAPH								 
	para = soup.findAll('p') 

					
#SHORTEN FOUND SLIDE NAME SINCE IT WONT ALWAYS MATCH UP WITH IMG ALT TAGS								 
	shortsn = slidename[0:10]


#FIND PIC URLS
	picurls = soup.findAll('img')


#SPECIFY WHICH PIC URL BY MATCHING IMAGE ASSOCIATED TEXT WITH SHORTENED TITLE
	specificpic=''
	try:
		specificpic = soup.findAll('img', {'alt' : re.compile(shortenedtitle)})
	except:
		pass
	if not specificpic:
		specificpic = picurls[1]

	for specificpic in specificpic:
		picture = specificpic['src']


#FIND NEXT SLIDE URLS
	nextslideurls=''
	try:
		nextslideurls = soup.findAll('li', {'class' : re.compile("next", re.I)})
	except:
		pass
	if not nextslideurls:
			nextslideurls = soup.findAll('a', {'class' : re.compile("next", re.I)})	
	if not nextslideurls:
			nextslideurls = soup.findAll('a', {'id' : re.compile("next", re.I)})
	if not nextslideurls:
			nextslideurls = soup.findAll('span', {'class' : re.compile("next", re.I)})

	
#SINCE IT MAY PRINT MORE THAN ONE RESULT FOR NEXT SLIDE URL. I MADE THIS VARIABLE TO ONLY PRINT THE FIRST ITEM IN THE RESULTS	
	nextslideurl=''
	try:
		nextslideurl = nextslideurls[1]
	except:
		pass
	if not nextslideurl:
		nextslideurl = nextslideurls


#REMOVE TAGS AND JUST LEAVE URL
	cleannextslideurl=''
	for nextslideurl in nextslideurl:
		cleannextslideurl = nextslideurl['href']


#PUT TOGETHER FULL NEXT SLIDE USING URL PARSE AND NEXTSLIDEURL
	fullnextslideurl = "http://" + urlcomponents.netloc + cleannextslideurl
	
	

#WHATEVER RESULTS I WANT PRINTED
#MAKE FULLNEXTSLIDEURL THE NEW URL TO PARSE AND ITERATE 
	print slidename
	print specificpic
	print para
	url = fullnextslideurl


#OPEN SLIDE IN BROWSER




	


