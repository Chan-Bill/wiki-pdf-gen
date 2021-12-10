import shutil
from fpdf import FPDF


class CreatePDF(FPDF):

    def chapter_title(self, title):
        self.set_title_style(title)
        self.set_essay_style()
        self.ln()

    def set_title_style(self, title):
        self.set_font("Times", size=12)
        self.cell(0, 5, title, ln=True, align='C')

    def set_essay_style(self):
        self.set_font("Times", size=12)
        self.cell(0, 7, 'Essay', ln=True, align='C')

    def chapter_body(self, filepath):
        txt = self.scan_body_file(filepath)
        self.set_body_style(txt)
        self.ln()
        self.set_exerpt_style()

    def scan_body_file(self, filepath):
        with open(filepath, "rb") as fh:
            txt = fh.read().decode("latin-1")
        return txt

    def set_body_style(self, txt):
        self.set_font("Times", size=12)
        self.multi_cell(0, 5, txt)

    def set_exerpt_style(self):
        self.set_font(style="I")
        self.cell(0, 5, "(end of excerpt)")

    def print_chapter(self, filepath):
        self.chapter_body(filepath)


class PdfGeneration:
        
    def __init__(self, page_titles):
        
        self.page_titles = page_titles
    
        self.proceed_pdf_gen()

    def proceed_pdf_gen(self):
        for self.title in self.page_titles:
            self.generating_pdf()
        shutil.rmtree('body')

    def generating_pdf(self):
        self.create_filenames()
        self.pdf_final_path()

    def create_filenames(self):
        self.txt_filename = self.page_titles.index(self.title)
        self.pdf_filename = self.title

    def pdf_final_path(self):
        locals()[self.title] = CreatePDF()
        locals()[self.title].add_page()
        locals()[self.title].chapter_title(self.title)
        locals()[self.title].print_chapter(f'./body/sample_{self.txt_filename}.txt')
        locals()[self.title].output(f'./generated/Eng-Essay_{self.pdf_filename}.pdf')