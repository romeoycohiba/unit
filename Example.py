from PyPDF2 import PdfReader
import pandas as pd

# Open the PDF file
with open(r'C:\Users\Ilija\Desktop\Analiza potrosnje\Izvod banke_1.pdf','rb') as pdf_file:
    # Create a PDF reader object
    pdf_reader = PdfReader(pdf_file)
    
    # Get the number of pages in the PDF file
    num_pages = len(pdf_reader.pages)   
 #   print(pdf_reader.pages[1])


    text = pdf_reader.pages[3].extract_text()
'''
    # Loop through each page and extract the text
    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        page_text = page.extract_text()
        print(f'Page {page_num + 1}: {page_text}')
'''


# Split the text into lines
lines = text.strip().split('\n')

print("Duzina je:",len(lines),lines)

for item in lines[:]:
    if item == ' ' or item == '  ':
        lines.remove(item)

print("Duzina je:",len(lines),lines)
