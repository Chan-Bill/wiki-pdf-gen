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


class TxtGeneration:

    def __init__(self, all_articles):

        self.all_articles = all_articles

        self.proceed_txt_gen()
        
    def proceed_txt_gen(self):
        for self.article in tqdm(self.all_articles):
            self.write_to_txt()

    def write_to_txt(self):
        self.search_contents()
        self.try_to_encode_txt()
        sleep(0.1)

    def search_contents(self):
        wiki_wiki = wikipediaapi.Wikipedia('en')
        self.page = wiki_wiki.page(self.article)
        self.txt_filename = self.all_articles.index(self.article)

    def try_to_encode_txt(self):
        try:
            self.encode_body_txt()
        except UnicodeEncodeError:
            self.error_message('Something else went wrong', 'Press Enter to Refresh')

    def encode_body_txt(self):
        with Open_File(f'body/sample_{self.txt_filename}.txt', 'w') as f:
                f.write(self.page.summary)

    def error_message(message, enter):
        print(f'{message}')
        input(enter)