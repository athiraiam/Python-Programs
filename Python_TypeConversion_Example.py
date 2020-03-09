#Type Conversion
# Float to int

data = 10.45
print(type(data))# float
out = int(data)
print(out) # 10
print(type(out))#int

#string to int

data = "5"
print(type(data))# float
out = int(data)
print(out) # 10
print(type(out))#int

# Reverse a strng using type conversion

data = 5648
print("Original data is " +str(data)+ " which is of type: " + str(type(out)))
out = str(data)
print("Converting to :: "+ str(type(out)))
rev = int(out[::-1])
print("Converting to :: "+ str(type(rev)))
print("Reverse data is ::" + str(rev)) #8465


