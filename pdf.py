from fpdf import FPDF


class CreatePDF:
    '''layout -> Page Layout, unit -> Unit Measurement,
        format -> Kind of Paper, font -> font style,
        chr -> font format, f_size -> font size
    '''

    def __init__(self, layout, unit, format, font, chr, f_size):
        self.layout = layout
        self.unit = unit
        self.format = format
        self.font = font
        self.chr = chr
        self.f_size = f_size

    def writePage(self, cell_h, title, con, file_no, files_count):

        filename = []
        for i in range(files_count + 1):
            filename.append(f'file_{i}')

        for i in filename:
            locals()[i] = FPDF(self.layout, self.unit, self.format)
            locals()[i].add_page()
            locals()[i].set_font(self.font, self.chr, self.f_size)
            locals()[i].cell(0, cell_h, title, ln=True, align='C')
            locals()[i].cell(0, cell_h, 'Essay', ln=True, align='C')

            locals()[i].multi_cell(0, cell_h, con, align='J', border=1)
            return locals()[i].output(f'generated/English-{title}-Essay_{file_no + 1}.pdf')


# pan = CreatePDF('P', 'mm', 'Letter', 'times', '', 16)
# pan.writePage(40, 10, 'hello world', 5, 6)