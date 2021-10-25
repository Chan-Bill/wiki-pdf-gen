import os
import shutil
import platform
import requests
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
**** Random PDF Generator from Wikipedia ****
****           Version: 1.2              ****

Source Code: https://github.com/Christian-Bill/wiki-doc-gen
''')

# Enter your topic of choice
keyword = input('Enter Topic: ')
print('How many files you want? Max = 50')
query_count = int(input('Enter here: '))
print('')


if query_count > 50:
    print('Max = 50')
    query_count = int(input('Enter here: '))
    print('')

else:

    try:
        # Wikipedia Object
        crawler = WikiFetch(keyword, query_count)
        # Getting all the titles from the topic
        page_titles = crawler.getTitles()
        # Generating all the contents each title
        page_content = crawler.getContent()
        # Summary iteration
        count_titles = len(page_content)
        loadbar(0, count_titles, prefix=f'Generating {query_count} files:', suffix='Complete', length=count_titles)
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
            loadbar(page_content.index(i) + 1, count_titles, prefix=f'Generating {query_count} files:', suffix='Complete', length=count_titles)



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
        if platform.system() == 'Linux' or 'Darwin':
            print(f'Generated PDF files : {current_dir}/generated')
            print('')
            input('Press ENTER to exit')
        else:
            print(f'Generated PDF files : {current_dir}\generated')
            print('')
            input('Press ENTER to exit')        

    except requests.exceptions.ConnectionError:
        shutil.rmtree('body')
        print('ConnectionError: Please check your network connection')
        input('Press ENTER to exit')

if __name__ == '__main__':
    pass




    



