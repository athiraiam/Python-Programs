import PyPDF4
import re
import io
"""
Identity specific text in pdf and retrieve its page number using Python(PyPDF4 module)
"""  
def identify_text(pdf_file_path,specific_text):
    pdfFileObj = open(pdf_file_path, 'rb')
    pdfReader = PyPDF4.PdfFileReader(pdfFileObj)

    print("------------------")
    page = pdfReader.getNumPages()
    print(page)
    print(type(page))
    print("------------------")
    for i in range(page):
        pageObj = pdfReader.getPage(i)
        pages_text = pageObj.extractText()
        for line in io.StringIO(pages_text):
            exp = specific_text
            if re.match(exp, line, re.I):
                print(repr(line))
                page = pdfReader.getNumPages()
                print(page)

pdf_file_path = '12-7-PDF-20100621144718P030016434342001.pdf'
specific_text = "IDENTITY|description|issuer"
identify_text(pdf_file_path,specific_text)
