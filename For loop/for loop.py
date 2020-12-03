cars = ("Bentley", "Benz", "Buggati")
for x in cars:
    print(x)

#looping through a string

for x in "buggati":
    print(x)


#break statement
#1
cars = ("Bentley", "Benz", "Buggati")
for x in cars:
    print(x)
    if x == "Benz":
        break

# 2
cars = ("Bentley", "Benz", "Buggati")
for x in cars:

    if x == "Benz":
        break
    print(x)



#continue statement
cars = ("Bentley", "Benz", "Buggati")
for x in cars:
    if x == "Benz":
        continue
    print(x)



#range function

for x in range(6):
    print(x)



#assing starting range
for x in range(2,6):
    print(x)


#adding third parameter in range
for x in range(2, 30, 3):
    print(x)


#else for loop
for x in range(6):
    print(x)
else:
    print("Finally finished!")


#nested loops
adj = ["red", "blue", "black"]
cars = ["Bentley", "Benz", "Buggati"]
for x in adj:
 for y in cars:
    print(x,y)