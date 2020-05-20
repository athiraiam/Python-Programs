from docx import Document
"""
How to read a table from word document and write into excel file using Python(Pandas)
"""

file_path = "Sample.docx"
document = Document(file_path)
tables = document.tables
all_data = []
for table in tables:    
    for row in table.rows:
        data = []
        for cell in row.cells:
            data.append(cell.text)
        all_data.append(data)
print(all_data)

import pandas as pd
 
df = pd.DataFrame(all_data)
writer = pd.ExcelWriter('output_doc_table_to_excel.xlsx')
df.to_excel(writer,sheet_name='excel',index=None, header=False)
writer.save()



