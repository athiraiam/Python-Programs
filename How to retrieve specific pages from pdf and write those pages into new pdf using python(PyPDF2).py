from PyPDF2 import PdfFileWriter, PdfFileReader
"""
Retrieve specific pages from pdf and write those pages into new pdf using python(PyPDF2)
"""

def save_pdf_pages(input, out_file, *pages):
    output = PdfFileWriter()
    input_pdf = PdfFileReader(open(input, "rb"))
    output_file = open(out_file, "wb")
    try:
        for p in pages:
            output.addPage(input_pdf.getPage(p-1))
        output.write(output_file)
        print(pages, "pages are written into new file =>", out_file)
    except:
        print("Page range is not present.")

input = "20100630131112P040111878658001.pdf"
out_file = "Output.pdf"
save_pdf_pages(input, out_file,1,2,3,10)

