#create a class
class my_class:
    x = 5

#create object
p1 = my_class()
print(p1.x)


# the __init__ () function
class student:

    def __init__(self, name, std):
        self.name = name
        self.std = std


s1 = student("Frank", 9)

print(s1.name)
print(s1.std)



# object method
class student:

    def __init__(self, name, std):
        self.name = name
        self.std = std

    def print_details(self):
        print(f"Name:{self.name}")
        print(f"Std:{self.std}")


s1 = student("Jack", 7)
s1.print_details()


# modify object
class student:

    def __init__(self, name, std):
        self.name = name
        self.std = std

    def print_details(self):
        print(f"Name:{self.name}")
        print(f"Std:{self.std}")


s1 = student("Jack", 7)

s1.std = 8

s1.print_details()