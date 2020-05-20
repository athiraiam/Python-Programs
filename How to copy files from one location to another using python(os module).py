import os

filename = "/home/athira/Desktop/Practise/Assignment/All_Data/Pdf_Status.txt"
src_fld = "/home/athira/Desktop/Practise/Assignment/All_Data/part7"
dest_fld= "/home/athira/Desktop/input"
fr = open(filename, "r")
counter = 0
for i in fr.readlines():
    file = i.strip()
    cmd = "cp"+ " "+ src_fld+"/"+file+" "+ dest_fld
    os.system(cmd)
    counter = counter + 1
print("Copied " + str(counter)+ "files into path "+dest_fld)  


