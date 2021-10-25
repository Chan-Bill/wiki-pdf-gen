import wikipedia


class Open_File:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()


class WikiFetch:
    '''This will pass a 'keyword' that will be used to search.
    '''

    def __init__(self, keyword, queries):
        self.keyword = keyword
        self.queries = queries

    def getTitles(self):
        self.title = wikipedia.search(self.keyword, self.queries)
        return self.title

    def getContent(self):
        self.fetched = [i.replace(' ','_')for i in self.getTitles()]
        return self.fetched

if __name__ == '__main__':
    pan = WikiFetch(keyword='Linux kernel')
    print(pan.getTitles())
    pan.getContent()