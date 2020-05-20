# dict of list
# list of dict
# list of list

lod = {'a':['AN', 10], 'b': ['Name', 'Vijay']}

print(lod['a']) #['AN', 10]
print(lod['a'][1]) #10
lod['a'].append(20)
print(lod) #{'a': ['AN', 10, 20], 'b': ['Name', 'Vijay']}

lod['a'].insert(0, '100')
print(lod) #{'a': ['100', 'AN', 10, 20], 'b': ['Name', 'Vijay']}

x = lod['a'].pop()
print(x, lod) #20 {'a': ['100', 'AN', 10], 'b': ['Name', 'Vijay']}

lod['a'].remove('100')
print(lod) #{'a': ['AN', 10, 10, 10], 'b': ['Name', 'Vijay', 'Name', 'Vijay']}

x = lod['b'].index('Name')
print(x) #0

x  = lod['a'].count(10)
print(x)
#list - append, insert, pop, remove, index, index with offset, count, copy, extend










