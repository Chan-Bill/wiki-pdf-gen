import wikipediaapi
from wiki import WikiFetch
from wiki import Open_File
from pdf import CreatePDF

print('''
**** PDF GENERATOR FOR COURSEHERO UNLOCK ****
****  Author : BillT BSME  Version: 1.0  ****
''')

keyword = input('Enter Topic: ')

# Wikipedia Scrape
# Creating wikifetch object
crawler = WikiFetch(keyword)
# Getting all the titles from the topic
page_titles = crawler.getTitles()
# Generating all the contents each title
page_content = crawler.getContent()
for i in page_content:

    wiki_wiki = wikipediaapi.Wikipedia('en')
    page_py = wiki_wiki.page(i)
    
    with Open_File(f'body/sample_{page_content.index(i)}.txt', 'w') as f:
        f.write(page_py.summary)


# Pdf Generation
for i in page_titles:
    # Creating createpdf object
    locals()[i] = CreatePDF()
    # Add page before writing
    locals()[i].add_page()
    # Printing the titles
    locals()[i].chapter_title(i)
    # Printing the body
    locals()[i].print_chapter(f'body/sample_{page_titles.index(i)}.txt')
    # Generate PDF file
    locals()[i].output(f'generated/Eng-Essay_{i}.pdf')

    



