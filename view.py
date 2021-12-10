import os
import shutil

class View:
    
    def __init__(self):
        
        pass

    def main(self):
        self._welcomer()
        self._ask_keyword()
        self._ask_how_many()
        
    def _welcomer(self):
        print('''
        ********** Random PDF Generator from Wikipedia ************
        **********           Version: 1.5              ************

        Source Code: https://github.com/Christian-Bill/wiki-pdf-gen
        ''')

    def _ask_keyword(self):
        self.keyword = input('Enter Topic: ')

    def _ask_how_many(self):
        print('How many files?')
        self._validate_query()

    def _validate_query(self):
        try:
            self._is_query_integer()
        except ValueError:
            self._ask_again()

    def _is_query_integer(self):
        query_count = 0
        self.query_count = int(input('Enter here: '))
        print('')

    def _ask_again(self):
        print('ValueError: Type a number')
        self._ask_how_many()