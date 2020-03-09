#Tuple immutable
data = (1, 20, "tuple", [12, 30, 40], 20, 20, {1:"one", 1:"two"}, {1,2,9,1})
print(data) #(1, 20, 'tuple', [12, 30, 40], 20, 20, {1: 'two'}, {1, 2, 9})
print(type(data))#<class 'tuple'>
print(data[1]) #20
print(data[::-1])#({1, 2, 9}, {1: 'two'}, 20, 20, [12, 30, 40], 'tuple', 20, 1)
print(data[3])#[12, 30, 40]
print(data[3:])#([12, 30, 40], 20, 20, {1: 'two'}, {1, 2, 9})
