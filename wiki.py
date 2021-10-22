import wikipediaapi
import wikipedia

class WikiFetch:
    '''This class will get the titles and content of each titles
    '''

    def __init__(self, keyword):
        self.keyword = keyword
        self.fetched = []

    def getTitles(self):
        return wikipedia.search(self.keyword)

    def getContent(self):

        fetched = [ i.replace(' ','_')for i in self.getTitles()]
        cont = []

        for i in fetched:

            wiki_wiki = wikipediaapi.Wikipedia('en')
            page_py = wiki_wiki.page(i)
            cont.append(page_py.summary[:1536])
        
        return cont
        



# pan = WikiFetch(keyword='Linux kernel')
# print(pan.getTitles())
# print(pan.getContent())