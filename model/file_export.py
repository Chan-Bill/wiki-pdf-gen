import os
import shutil


class Export:

    def __init__(self):

        self.default_file_and_path()
        self.zipping_process()       

    def default_file_and_path(self):
        self.filename = 'doc'
        self.number = 1
        self.output_name = ''

    def zipping_process(self):
        self.create_unique_filename()
        self.zip_folders()
        self.show_path()

    def create_unique_filename(self):
        while os.path.exists(f'{self.filename}-{self.number}.zip'):
            self.calculate_unique_name()

    def calculate_unique_name(self):
        self.number += 1
        self.output_name = f'{self.filename}-{self.number}.zip'

    def zip_folders(self):
        shutil.make_archive(f'{self.filename}-{self.number}', 'zip', 'generated')
        shutil.rmtree('generated')

    def show_path(self):
        current_dir = os.getcwd()
        print(f'Generated PDF files : {current_dir}/{self.output_name}')
        self.close()

    def close(self):
        print('')
        input('Press ENTER to exit')