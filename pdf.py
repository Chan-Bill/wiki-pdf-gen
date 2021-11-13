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
    
        self.proceed_pdf_gen(page_titles)

    def proceed_pdf_gen(self, page_titles):
        for title in page_titles:
            self.generating_pdf(title, page_titles)
        shutil.rmtree('body')

    def generating_pdf(self, title, page_titles):
        txt_filename, pdf_filename = self.create_filenames(title, page_titles)
        self.pdf_final_path(title, txt_filename, pdf_filename)

    def create_filenames(self, title, page_titles):
        txt_filename = page_titles.index(title)
        pdf_filename = title
        return [txt_filename, pdf_filename]

    def pdf_final_path(self, title, txt_filename, pdf_filename):
        locals()[title] = CreatePDF()
        locals()[title].add_page()
        locals()[title].chapter_title(title)
        locals()[title].print_chapter(f'./body/sample_{txt_filename}.txt')
        locals()[title].output(f'./generated/Eng-Essay_{pdf_filename}.pdf')


if __name__ == '__main__':
    pass