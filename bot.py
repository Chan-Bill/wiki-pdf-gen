import requests
from folders import Folders
from pdf import CreatePDF, PdfGeneration
from welcome_closing import WelcomePage, Closing
from wiki import Open_File, WikiFetch, TxtGeneration


class RunApp:

    def __init__(self):

        Folders()
        self.keyword, self.query_count = self.init_page()
        self.crawler = WikiFetch(self.keyword, self.query_count)
        self.create_body_file()
        self.create_pdf_file()
        self.try_wiki_doc_gen()

    def init_page(self):
        welcome = WelcomePage()
        keyword = welcome.ask_keyword()
        query_count = welcome.validate_query()
        return [keyword, query_count]   

    def try_wiki_doc_gen(self):
        try:
            self.wiki_doc_gen()
        except requests.exceptions.ConnectionError:
            error_message('ConnectionError: Please check your network connection', 'Press Enter to exit')

    def wiki_doc_gen(self):
        self.create_body_file()  
        self.create_pdf_file()
        Closing()

    def create_body_file(self):
        all_articles = self.crawler.available_articles()      
        TxtGeneration(all_articles)

    def create_pdf_file(self):
        page_titles = self.crawler.find_articles()
        PdfGeneration(page_titles)


if __name__ == '__main__':
    # keyword = 'war'
    # query_count = 2
    RunApp()



    





    



