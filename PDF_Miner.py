# Created by SP
# os.rename 'deletes' the initial file. Please backup.
import os
import sys
import chardet
sys.path.insert(1, 'D:\\My Files\\Automate_the_boring_stuff\\venv\Lib\\site-packages\\pdfminer')
# Sys path to read pdfminer
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument

os.chdir(input('Enter the path of your files: '))
for file in os.listdir("."):      #Get all files
    if file.endswith(".pdf"):     # Get only pdf files in that dir
        path = open(file, 'rb')
        parser = PDFParser(path)
        doc = PDFDocument(parser)
        title = doc.info[0]
        title_final = title.get('Title')              # Gets the title of the PDF in bytes format
        name = title_final
        detection = chardet.detect(name)              # Detects the encoding of the current PDF file
        print(detection)                              # Prints the encoding as a dictionary
        get_encoding = detection.get('encoding')      # Gets the value of the 'encoding' key
        if get_encoding == 'ascii':
            title_final_new = str(title_final, encoding='UTF-8')
            print(title_final_new)
            path.close()
            new_file = os.path.join('D:\Test_folder', title_final_new + '.pdf')
            os.rename(file, new_file)
        elif get_encoding == 'UTF-16':
            title_final_new = str(title_final, encoding='UTF-16')
            print(title_final_new)
            path.close()
            new_file = os.path.join('D:\Test_folder', title_final_new + '.pdf')
            os.rename(file, new_file)