#sets in python:

set={"apple","banana","mango"}
print(set)

# to check whether banana is present in the set:
set={"apple","banana","mango"}

print("banana" in set)


#add items by using add() method:

set.add("orange")
print(set)

# update, if we want add multiple items in that case we use update() method

set.update(["orange","grapes", "cherry"])
print(set)

#remove
set = {"apple","banana","mango"}

set.remove("banana") # we can also use discard method() as well
print(set)

#remove last element
set = {"apple","banana","mango"}

x=set.pop()
print(x)
print(set)

# to delete
set = {"apple","banana","mango"}



del set
print(set)

#join two sets, 2metods to do so
#union() method

set1 = {"a", "b" , "c"}
set2 = {1 , 2 , 3}

set3 = set1.union(set2)
print(set3)

# update() method

set1 = {"a", "b" , "c"}
set2 = {1 , 2 , 3}

set1.update(set2)
print(set1)