#Extract pdf table to excel
"""
To extract pdf table to excel using python(tabula and pandas)
"""

import tabula
import pandas as pd
import os.path
file = "/home/athira/Desktop/20100621144718P030016434342001.pdf"
out = file.split("/")
out = os.path.splitext(out[-1])
ack = out[0]

all_values = tabula.read_pdf(file, pages='12')
all_values = all_values[0].values.tolist()
data = []
column = ["ACK_ID", "Plan Year", "Identity of Issue", "Description of Investment", "Cost", "Current Value"]
data.insert(0, column)
for val in all_values:
        m =[]
        m = [ack,None , val[2], val[1], val[4], val[6]]
        data.append(m)  
print(data)        

df = pd.DataFrame(data)

writer = pd.ExcelWriter('output.xlsx')
df.to_excel(writer,sheet_name='excel',index=None, header=False)
workbook  = writer.book
worksheet= writer.sheets['excel']
worksheet.set_column(1,5, 22)

writer.save()

