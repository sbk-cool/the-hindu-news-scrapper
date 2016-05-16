from crawler import Crawler
from articledb import ArticleDb
from docproc import DocProc
from bs4 import BeautifulSoup
import re

class MainEngine:
    """By default, saves articles to database collection."""

# Initialises and gets the necessary done.
    def __init__(self):
        crwl=Crawler()
        crwl.get_pagelist()
        self.pagelist=crwl.return_pagelist()
        self.soup=crwl.return_soup()
        self.articledb=ArticleDb('localhost',27017)
        self.articledb.init_backend('testdb','testcol')
        self.final_docs=[]
        self.error_pagelist=[]

# Gets articles.
    def get_docs(self):
        crwl=Crawler()
        for page in self.pagelist:
            if page != '#' and page != 'mailto:web.thehindu@thehindu.co.in' and page !=None:
                crwl.get_page(page)
                soup=crwl.return_soup()
                content=soup.find("div",{"class":"article-text"})
                if content != None:
                    div=content.find('div',id='articleKeywords')
                    if div != None:
                        div.decompose()
                    div=content.find('div',id='addshare')
                    if div != None:
                        div.decompose()
                    div=content.find('div',{'class':'rel-block-sec'})
                    if div != None:
                        div.decompose()
                    div=content.find('div',{'class':'photo-caption'})
                    if div != None:
                        div.decompose()
                    div=content.find('div',{'class':'related-column'})
                    if div != None:
                        div.decompose()
                    x=[s.extract() for s in content('script')]
                    text=content.text
                    text=re.sub('[\n]+',' ',text)
                    text=re.sub('[ ]+',' ',text)
                    text=text.strip()
                    if(len(text)<=10):
                        self.error_pagelist.append(page)
                    else:
                        self.final_docs.append(text)


# Saves article list to articledb database collection.
    def save_docs(self):
        self.articledb.insert_doc(self.final_docs)

# Executes the MainEngine.
def main():
    x=MainEngine()
    x.get_docs()
    x.save_docs()


if __name=="__main__":
    main()
