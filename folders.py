import os
import shutil


class Folders:
    
    def __init__(self):
        
        self.make_body_dir()
        self.make_generated_dir()

    def make_body_dir(self):
        if not self.find_body_dir():
            os.mkdir('body')
        else:
            self.remake_body_dir()

    def find_body_dir(self):
        return os.path.exists('body')

    def remake_body_dir(self):
        shutil.rmtree('body')
        os.mkdir('body')
    
    def make_generated_dir(self):
        if not self.find_generated_dir():
            os.mkdir('generated')

    def find_generated_dir(self):
        return os.path.exists('generated')