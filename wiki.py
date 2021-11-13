import os
import shutil
import wikipedia
import wikipediaapi
from tqdm import tqdm
from time import sleep


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

    def __init__(self, keyword, queries):

        self.keyword = keyword
        self.queries = queries

    def available_articles(self):
        self.fetched = [i.replace(' ','_')for i in self.find_articles()]
        return self.fetched

    def find_articles(self):
        self.titles = wikipedia.search(self.keyword, results=self.queries)
        return self.titles


class TxtGeneration:

    def __init__(self, all_articles):

        self.all_articles = all_articles

        self.proceed_txt_gen(all_articles)
        
    def proceed_txt_gen(self, all_articles):
        for article in tqdm(self.all_articles):
            self.write_to_txt(article, all_articles)

    def write_to_txt(self, article, all_articles):
        page, txt_filename =  self.search_contents(article, all_articles)
        self.try_to_encode_txt(page, txt_filename)
        sleep(0.1)

    def search_contents(self, article, all_articles):
        wiki_wiki = wikipediaapi.Wikipedia('en')
        page = wiki_wiki.page(article)
        txt_filename = all_articles.index(article)
        return [page, txt_filename]

    def try_to_encode_txt(self, page, txt_filename):
        try:
            self.encode_body_txt(page, txt_filename)
        except UnicodeEncodeError:
            self.error_message('Something else went wrong', 'Press Enter to Refresh')

    def encode_body_txt(self, page, txt_filename):
        with Open_File(f'body/sample_{txt_filename}.txt', 'w') as f:
                f.write(page.summary)

    def error_message(message, enter):
        print(f'{message}')
        input(enter) 


if __name__ == '__main__':
    pass
