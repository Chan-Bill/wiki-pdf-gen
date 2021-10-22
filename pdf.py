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

    def writePage(self, cell_w, cell_h, text, file_no, files_count):

        filename = []
        for i in range(files_count + 1):
            filename.append(f'file_{i}')

        for i in filename:
            locals()[i] = FPDF(self.layout, self.unit, self.format)
            locals()[i].add_page()
            locals()[i].set_font(self.font, self.chr, self.f_size)
            locals()[i].cell(cell_w, cell_h, text)
            return locals()[i].output(f'generated/pdf_{file_no}.pdf')


# pan = CreatePDF('P', 'mm', 'Letter', 'times', '', 16)
# pan.writePage(40, 10, 'hello world', 5, 6)