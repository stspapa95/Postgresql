# Created by Stergios Papathanasiou
# os.rename deletes the initial file. Please backup.
import sys, os
sys.path.insert(1, 'D:\\My Files\\Automate_the_boring_stuff\\venv\Lib\\site-packages\\pdfminer')
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
path = open(r'D:\test.pdf', 'rb')
parser = PDFParser(path)
doc = PDFDocument(parser)

print(doc.info)
title = doc.info[0]
title_final = title.get('Title')
title_final_new = str(title_final, 'utf-8')
path.close()
new_file = os.path.join('D:\Test_folder', title_final_new + '.pdf')
os.rename('D:\\test.pdf', new_file)










