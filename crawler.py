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

#Gets the page
    def get_page(self,url):
        req=urllib2.Request(url)
        gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)  # Only for gangstas
        response=urllib2.urlopen(req,context=gcontext)
        the_page=response.read()
        self.soup=BeautifulSoup(the_page,"html.parser")

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
        self.get_page(url)
        navbar=self.soup.find("div",{"id":"tpnav-bar"})
        links=navbar.find_all("a")
        links.pop(0)
        for link in links:
            self.get_page(link['href'])
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
