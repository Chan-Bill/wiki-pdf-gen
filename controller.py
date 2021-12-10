from view import View
from model import Models
from model.file_folders import Folders


class Controller:

    def __init__(self):
        
        self.view = View()
        self.model = Models()
    
    def main(self):
        self.init_temp_folders()
        self.view.main()
        self.file_creation()

    def file_creation(self):
        self.model.all_inputs(self.view.keyword, self.view.query_count)
        self.model.generate_file_and_export()

    def init_temp_folders(self):
        Folders()


if __name__ == '__main__':
    wiki_gen = Controller()
    wiki_gen.main()