#adding 10 to  argument
x = lambda a : a + 10
print(x(7))

#multiply argument a & b
x = lambda a, b : a * b
print(x(3 , 7))

#summerizing argument a ,b & c
x = lambda a, b, c : a + b + c
print(x(3, 8, 10))

#maping
l=[2, 8 , 4, 9]
print(l)
new_list = list(map(lambda x : x + 10, l))
print(new_list)

# filter
l=[2, 8 , 4, 9, 15, 20]
print(l)
new_list = list(filter(lambda x : x < 10, l))
print(new_list)