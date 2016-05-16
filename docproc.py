from nltk.corpus import stopwords as sw


class DocProc:
    """Text Processing for vector of documents."""

#Initialises the text processing instance.
    def __init__(self):
        self.stopWords=sw.words('english')

#Tokenises a list of documents where each document is a string.
    def tokenize(self,docs):
        wordDocVector=[]
        for doc in docs:
            wordList=re.sub('[^\w]',' ',doc).split()
            wordDocVector.append(wordList)
        return wordDocVector

#Removes stop words from the vector space documents.
    def remove_stopwords(self,wordDocVector):
        finalDocVector = []
        for doc in wordDocVector:
            doc=[word.lower() for word in doc if not word.lower() in self.stopWords]
            finalDocVector.append(doc)
        return finalDocVector

#Adds new stopword to the stopword list.
    def add_new_stopword(self,string):
        self.stopWords.append(string)

# Encode documents to utf-8 format
    def docEncode(self,docs):
        tmpDocs=[]
        for doc in docs:
            doc=unicode(doc,"utf-8")
            tmpDocs.append(doc)
        return tmpDocs
