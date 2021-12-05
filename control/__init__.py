
import requests
import wikipedia
from control.file_export import Export
from control.body_txt import TxtGeneration
from control.body_pdf import PdfGeneration


class Controls:

    def __init__(self, keyword, query_count):

        self.keyword = keyword
        self.query_count = query_count

        self.try_wiki_doc_gen()

    def try_wiki_doc_gen(self):
        try:
            self.write_pages()
            Export()
        except requests.exceptions.ConnectionError:
            self.error_message('ConnectionError: Please check your network connection', 'Press Enter to exit')

    def error_message(message, enter):
        print(f'{message}')
        input(enter) 

    def write_pages(self):
        self.create_body_file()  
        self.create_pdf_file()

    def create_body_file(self):
        self.available_articles()      
        TxtGeneration(self.fetched)

    def available_articles(self):
        self.fetched = [i.replace(' ','_')for i in self.find_articles()]

    def find_articles(self):
        self.titles = wikipedia.search(self.keyword, results=self.query_count)
        return self.titles

    def create_pdf_file(self):
        self.find_articles()
        PdfGeneration(self.titles)
