#Write to word document
"""
How to write table (list of list data) into word document using Python
"""
from docx import Document
document = Document()
data = [['Name', 'Qual', 'Branch', 'Course', 'Type'], ['Vijay', 'BE', 'HSR', 'Python', 'Permanent'], ['Ramesh', 'MCA', 'MLR', 'SQL', 'Temp'], ['Ajay', 'MCA', 'HSR', 'Jquery', 'Permanent'], ['Laxman', 'BE', 'KCB', 'Java', 'Temp']]
row = (len(data))
col = len(data[0])
print(row, col)
table = document.add_table(rows=row, cols=col)

for i in range(len(data[0])):
    for j in range(len(data[0])):
        heading_cells = table.rows[i].cells
        heading_cells[j].text = data[i][j]
   
document.save('output_write_table_to_doc.docx')

