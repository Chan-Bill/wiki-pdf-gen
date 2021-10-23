from fpdf import FPDF


class CreatePDF(FPDF):

    def chapter_title(self, title):
        # Setting font: Times 12
        self.set_font("Times", size=12)
        # Printing centered text:
        self.cell(0, 10, title, ln=True, align='C')
        # Performing a line break:
        self.ln()

    def chapter_body(self, filepath):
        # Reading text file:
        with open(filepath, "rb") as fh:
            txt = fh.read().decode("latin-1")
        # Setting font: Times 12
        self.set_font("Times", size=12)
        # Printing justified text:
        self.multi_cell(0, 5, txt)
        # Performing a line break:
        self.ln()
        # Final mention in italics:
        self.set_font(style="I")
        self.cell(0, 5, "(end of excerpt)")

    def print_chapter(self, filepath):
        self.chapter_body(filepath)

# pan = CreatePDF('P', 'mm', 'Letter', 'times', '', 16)
# pan.writePage(40, 10, 'hello world', 5, 6)