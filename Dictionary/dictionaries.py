# dictionaries

dict = {"brand": "BMW","model": "M5","year": 2019}

print(dict)

#access items (model)
#1
x=dict["brand"]
print(x)

#2 get method
x=dict.get("model")
print(x)

#Change values:
dict["year"] = 2020
print (dict)


#loops:
# to print only key part:
for x in dict:
    print(x)

# to print value part:
for x in dict:
    print(dict[x])

#loop through both key and value:

for x, y in dict.items():
    print(x, y)

# key exists in dict:

if "model" in dict:
    print("Yes, 'model' is one of the key in dictionary")
