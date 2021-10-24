import os
import requests
import shutil
import wikipediaapi
from time import sleep
from wiki import WikiFetch
from wiki import Open_File
from pdf import CreatePDF


# Create folders
if not os.path.exists('body'):
    os.mkdir('body')
else:
    shutil.rmtree('body')
    os.mkdir('body')

if not os.path.exists('generated'):
    os.mkdir('generated')

# Loadbar
def loadbar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='>'):
	percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration/float(total)))
	filledLength = int(length * iteration // total)
	bar = fill * filledLength + '-' * (length - filledLength)
	print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
	if iteration == total:
		print()


# Welcome Page
print('''
**** PDF GENERATOR FOR COURSEHERO UNLOCK ****
****  Author : BillT BSME  Version: 1.0  ****
''')

# Enter your topic of choice
keyword = input('Enter Topic: ')
print('')

# Wikipedia Object
crawler = WikiFetch(keyword)
# Getting all the titles from the topic
page_titles = crawler.getTitles()
# Generating all the contents each title
page_content = crawler.getContent()
# Summary iteration
count_titles = len(page_content)
loadbar(0, count_titles, prefix='PDF-Generating:', suffix='Complete', length=count_titles)
for i in page_content:

    try:
        wiki_wiki = wikipediaapi.Wikipedia('en')
        page_py = wiki_wiki.page(i)
        
        with Open_File(f'body/sample_{page_content.index(i)}.txt', 'w') as f:
            f.write(page_py.summary)

    except requests.exceptions.ConnectionError:
        shutil.rmtree('body')
        print('Something else went wrong')
    
    sleep(0.1)
    loadbar(page_content.index(i) + 1, count_titles, prefix='PDF-Generating:', suffix='Complete', length=count_titles)


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

# Delete body files
shutil.rmtree('body')

# Closing Message
current_dir = os.getcwd()
print(f'Generated PDF files : {current_dir}/generated')
print('')
input('Press ENTER to exit')




    



