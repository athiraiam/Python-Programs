#set

data = {10, "name", 30, 30.5}
print(data)# {10, "name", 30, 30.5}
print(type(data)) # <class 'set'> when the value if defined then set will be type
data = {}
print(type(data)) # <class 'dict'> when the value is not defined then set will be dictinary by default

#No duplicates , no order
data = {10, "name", 30, 30.5, None, False, 10}
print(data)# {False, 10, 'name', 30.5, None, 30} - duplicates are not repeated 

#Iterable
for i in data:
 print(i) # sets are unordered the items has no index

#add
data.add(100)
print(data) #{False, 100, 10, 'name', 30, None, 30.5}
data = {“abc”, ‘test’, None, True, 65.4, 44}
print(data)#Set can only have immutable object




