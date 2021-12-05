import os
import shutil
from control import Controls
from control.file_folders import Folders

class View:
    
    def __init__(self):
        
        self.welcomer()
        self.ask_keyword()
        self.ask_how_many()
        Controls(self.keyword, self.query_count)
        
    def welcomer(self):
        print('''
        ********** Random PDF Generator from Wikipedia ************
        **********           Version: 1.5              ************

        Source Code: https://github.com/Christian-Bill/wiki-pdf-gen
        ''')

    def ask_keyword(self):
        self.keyword = input('Enter Topic: ')

    def ask_how_many(self):
        print('How many files?')
        self.validate_query()

    def validate_query(self):
        try:
            self.is_query_integer()
        except ValueError:
            self.ask_again()

    def is_query_integer(self):
        query_count = 0
        self.query_count = int(input('Enter here: '))
        print('')

    def ask_again(self):
        print('ValueError: Type a number')
        self.ask_how_many()

    

if __name__ == '__main__':
    Folders()
    View()