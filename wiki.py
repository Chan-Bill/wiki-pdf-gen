import wikipediaapi
import wikipedia

class WikiFetch:
    '''This class will get the titles and content of each titles
    '''

    def __init__(self, keyword):
        self.keyword = keyword

    def getTitles(self):
        self.titles = wikipedia.search(self.keyword)
        print(self.titles)

    def getContent(self):
        
        for i in self.titles:
            wiki_wiki = wikipediaapi.Wikipedia('en')

            page_py = wiki_wiki.page(i)

            if page_py.exists():
                print(page_py.summary)
            else:
                pass


# pan = WikiFetch(keyword='linux')

# pan.getTitles()
# pan.getContent()
