#	      	    y			    x     
list = [10, "list", 20, "method", "print", 10.6]
#        0    1      2     3         4       5
print(list)# Print all list
print(list[1]) # list - Indexing
print(list[1] + list[4]) # listprint - Concatenate string
print(list[0] + list[-1]) # 20.6 - Concatenate integer
print(list[::-1]) # Reverse the list
print(list[1:3]) # list, 20
print(list[1:-1]) # list, 20, method, print
print(list[-4:3]) # 20
print(list[0:2]) # 10, list
print(list[-1:-4]) # no output
print(list[-1:-4:-1]) # 10.6, print, method
print(list)# Print all list
list[1] = "New List"
print("list[1] is changed to ::" + str(list[1]))
print("Updated list is ::" + str(list))

print("##############For loop to iterate on list------------->")
for i in list:
 print(i)
 input()

