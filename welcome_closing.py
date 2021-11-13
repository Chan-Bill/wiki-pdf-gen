import os
import shutil


class WelcomePage:
    
    def __init__(self):
        
        self.welcomer()
        
    def welcomer(self):
        print('''
        ********** Random PDF Generator from Wikipedia ************
        **********           Version: 1.3              ************

        Source Code: https://github.com/Christian-Bill/wiki-pdf-gen
        ''')

    def ask_keyword(self):
        keyword = input('Enter Topic: ')
        print('How many files?')
        return keyword

    def validate_query(self):
        query_count = 0
        while True:
            try:
                query_count = int(input('Enter here: '))
                print('')
                break
            except ValueError:
                print('ValueError: Type a number')
        return query_count


class Closing:

    def __init__(self):

        self.filename = 'doc'
        self.number = 0
        self.output_path = ''

        self.create_unique_filename()
        self.zip_folders()
        self.show_path()

    def create_unique_filename(self):
        while os.path.exists(self.output_path):
            self.calculate_unique_name()

    def calculate_unique_name(self):
        self.number += 1
        self.output_path = f'{self.filename}-{self.number}.zip'

    def zip_folders(self):
        shutil.make_archive(f'{self.filename}-{self.number}', 'zip', 'generated')
        shutil.rmtree('generated')

    def show_path(self):
        current_dir = os.getcwd()
        print(f'Generated PDF files : {current_dir}/{self.output_path}')
        self.close()

    def close(self):
        print('')
        input('Press ENTER to exit')