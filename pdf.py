import json
import os
from PIL import Image
from PyPDF2 import PdfMerger

with open('jsonfile.json', 'r') as file:
    data = json.load(file)

for doc in data['documents']:
    identifier = doc['document']['identificador']
    files = doc['document']['files']
    
    pdf_path = f'{identifier}.pdf'
    pdf = PdfMerger()
    
    for file in files:
        image = Image.open(file)
        pdf_path_temp = f'{os.path.splitext(file)[0]}.pdf'
        image.save(pdf_path_temp, 'PDF')
        pdf.append(open(pdf_path_temp, 'rb'))
        os.remove(pdf_path_temp)
    
    with open(pdf_path, 'wb') as file:
        pdf.write(file)