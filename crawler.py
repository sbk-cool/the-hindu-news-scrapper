import urllib2
import requests
from bs4 import BeautifulSoup
import re
import ssl

class Crawler:
    """Crawls today's The Hindu page to get all articles links."""

#Initialises the soup and pagelist to null values.
    def __init__(self):
        self.soup=None
        self.pagelist=[]

#Gets the page with given url. Returns True if the page is found or else False.
    def get_page(self,url):
        try:
            req=urllib2.Request(url)
            gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)  # Only for gangstas
            response=urllib2.urlopen(req,context=gcontext)
        except (urllib2.HTTPError,urllib2.URLError):
            return False
        else:
            the_page=response.read()
            self.soup=BeautifulSoup(the_page,"html.parser")
            return True


#crawls the page to get hyperlinks
    def crawl(self,the_page):
        webLinks=[]
        tags=the_page('a')
        for tag in tags:
            store=tag.get('href',None)
            webLinks.append(store)
        return webLinks
#Gets the pagelist in the todays's paper url.
    def get_pagelist(self):
        url='http://www.thehindu.com/todays-paper/'
        if(self.get_page(url)!=True):
            print "Cannot get page list"
            exit()
        navbar=self.soup.find("div",{"id":"tpnav-bar"})
        links=navbar.find_all("a")
        links.pop(0)
        for link in links:
            if(self.get_page(link['href'])!=True):
                continue
            tmplist=self.crawl(self.return_soup())
            tmplist=list(set(tmplist))
            self.pagelist.extend(tmplist)
        self.pagelist=list(set(self.pagelist))

#Returns pagelist
    def return_pagelist(self):
        return self.pagelist
#Returns soup
    def return_soup(self):
        return self.soup
