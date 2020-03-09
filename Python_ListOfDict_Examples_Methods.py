# List of dict

lod = [{'AN':10, 'Name': 'Ajay'},
       {'AN':20, 'Name': 'Ramesh'},
      ]

print(lod) # print the list of dict

print(lod[0]) # Access 0 index of list ---> Access 

print(lod[-1]) # Access last index, in this case 1st index of the list

print(lod[0]['AN']) # 10 -> Value of AN of 0th index

print(lod[1]['Name']) # Ramesh -> Value of Name of 1st index

print(lod[1].keys()) #dict_keys(['AN', 'Name']) -> list of keys of 1st index 

print(lod[1].values()) #dict_values([20, 'Ramesh']) -> list of values of 1st index

lod[1]['AN'] = '30' # assign new value to existing key
print(lod)#[{'AN': 10, 'Name': 'Ajay'}, {'AN': '30', 'Name': 'Ramesh'}]

lod.append({'AN': 40}) # Insert new dictionary into list
print(lod) # [{'AN': 10, 'Name': 'Ajay'}, {'AN': '30', 'Name': 'Ramesh'}, {'AN': 40}]

lod[2]['Name'] = 'Vijay' # Insert new value into dict
print(lod) #[{'AN': 10, 'Name': 'Ajay'}, {'AN': '30', 'Name': 'Ramesh'}, {'AN': 40, 'Name': 'Vijay'}]

print("get()************************")

x = lod[1].get('AN') # Key exists, return value
print(x) #30

x = lod[1].get('Bal') # Key don't exists, return None
print(x)

x = lod[1].get('Bal', 90000) # key don't exists, print alternative user defined value from passed argument '90000'
print(x)

print(lod[1]) #get() method dont alter dict values

print("setdefault************************")
y = lod[0].setdefault('AN')
print(y) #10 Key exists, return value

y = lod[0].setdefault('Bal')
print(y) # None Key don't exists, return None
print(lod[0])#{'AN': 10, 'Name': 'Ajay', 'Bal': None}

y = lod[0].setdefault('Avg', 90000) # key don't exists, print alternative user defined value passed argument as a2nd argument in setdeafault method '90000'
print(y) #90000
print(lod[0]) #{'AN': 10, 'Name': 'Ajay', 'Bal': None, 'Avg': 90000}

print("pop************************")

print(lod[1]) #{'AN': '30', 'Name': 'Ramesh'}
lod[1].pop('AN')
print(lod[1]) #{'Name': 'Ramesh'}

#lod[1].pop() # Error as pop in dict expect 1 argument. Key to be poped
#print(lod[1])

#lod[1].pop('Bal') # Key error as key dont exists in dict
#print(lod[1]) # Key error

x = lod[1].pop('bal', 90000) # Since the key dont exists, instead of errow display user defined value passed as the 2nd argument in pop method
print(x, lod[1]) #90000 {'Name': 'Ramesh'}

print("update************************")

print(lod) #[{'AN': 10, 'Name': 'Ajay', 'Bal': None, 'Avg': 90000}, {'Name': 'Ramesh'}, {'AN': 40, 'Name': 'Vijay'}]
lod[0].update(lod[1]) #Merge two dict# Updates the value of lod[1] dict to lod[0] dict
print(lod[0])#{'AN': 10, 'Name': 'Ramesh', 'Bal': None, 'Avg': 90000} Updates the value of lod[1] dict to lod[0] dict
print(lod[1])# {'Name': 'Ramesh'} lod[1] is unchanged by update method

print("clear************************")

print(lod) #[{'AN': 10, 'Name': 'Ramesh', 'Bal': None, 'Avg': 90000}, {'Name': 'Ramesh'}, {'AN': 40, 'Name': 'Vijay'}]
print(lod[0]) #{'AN': 10, 'Name': 'Ramesh', 'Bal': None, 'Avg': 90000}
lod[0].clear()
print(lod) #[{}, {'Name': 'Ramesh'}, {'AN': 40, 'Name': 'Vijay'}]

print("copy************************")

print(lod[1])#{'Name': 'Ramesh'}
lod_copy = lod[1].copy()
print(lod_copy) #{'Name': 'Ramesh'}






   

        

