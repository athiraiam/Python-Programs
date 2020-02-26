#
dict = {10: "Ramesh", 20: "Kiran", 30: "Vignesh"}
print(dict) # {10: "Ramesh", 20: "Kiran", 30: "Vignesh"}
#Duplicates will be updated with the lastest value
dict = {10: "Ramesh", 20: "Kiran", 30: "Vignesh", 10:"New Ramesh"}
print(dict) #{10:"New Ramesh", 20: "Kiran", 30: "Vignesh"}
#How to get data from dictionary
print(dict[10]) #New Ramesh   value of the key will be displayed.

# Update
dict[10] = "NewNew Ramesh"
print(dict) #{10:"NewNew Ramesh", 20: "Kiran", 30: "Vignesh"}

#Insert new dict
dict[100] = "InsertNew"
print(dict) #{10:"NewNew Ramesh", 20: "Kiran", 30: "Vignesh", 100: "InsertNew"}

#Keys can be any immutable object - str, int, float, tuple, None, bool
dict = {10:0, 1.7:"a", None:["null","empty"], True:"boolean"}
print(dict)
# dict is iterable but the order might interchange
for i in dict:
 print(i)
 input()
