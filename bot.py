from wiki import WikiFetch
from pdf import CreatePDF

keyword = 'SSD'

engine = WikiFetch(keyword)
file = CreatePDF('P', 'mm', 'Letter', 'helvetica', '', 16)

titles = engine.getTitles()

for i in range(len(titles)):
    file.writePage(40, 10, titles[i], i, len(titles))

