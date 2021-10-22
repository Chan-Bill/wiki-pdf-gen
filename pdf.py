from fpdf import FPDF


class CreatePDF:

    def __init__(self, layout, unit, format, font, chr, f_size):
        self.layout = layout
        self.unit = unit
        self.format = format
        self.font = font
        self.chr = chr
        self.f_size = f_size

        self.pdf = FPDF(self.layout, self.unit, self.format)

    def writePage(self, cell_w, cell_h, text, file_no):
        self.pdf.add_page()
        self.pdf.set_font(self.font, self.chr, self.f_size)
        self.pdf.cell(cell_w, cell_h, text)
        return self.pdf.output(f'pdf_{file_no}.pdf')


# pan = CreatePDF('P', 'mm', 'Letter', 'times', '', 16)

# pan.writePage(40, 10, 'hello world', 5)