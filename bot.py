from wiki import WikiFetch
from pdf import CreatePDF

keyword = 'Linux'
# print('''
# **** PDF GENERATOR FOR COURSEHERO UNLOCK ****
# ****         Author : BillT BSME         ****
# ''')

# keyword = input('Enter Topic: ')


engine = WikiFetch(keyword)
file = CreatePDF('P', 'mm', 'A4', 'helvetica', '', 12)

titles = engine.getTitles()
contents = engine.getContent()

for i in range(len(titles)):
    file.writePage(5, titles[i], contents[i], i, len(titles))


    



