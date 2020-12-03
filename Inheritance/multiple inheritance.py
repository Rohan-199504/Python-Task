class Employee:

    def __init__ (self, name , age , email):
        self.name=name
        self.age=age
        self.email=email

    def print_details(self):
        print(f"Name of the employee: {self.name}")
        print(f"Age of the employee: {self.age}")
        print(f"Email of the Employee: {self.email}")


class Director:

    def __init__ (self, name , age , email , sal):
        self.name = name
        self.age = age
        self.email = email
        self.sal=sal

    def print_details(self):
        print(f"Name of the employee: {self.name}")
        print(f"Age of the employee: {self.age}")
        print(f"Email of the Employee: {self.email}")
        print(f"Salary of the employee: {self.sal}")

class Developer(Director,Employee):

    def __init__ (self, name, age, email, sal , language):
        self.name = name
        self.age = age
        self.email = email
        self.sal = sal
        self.language=language

    def print_details(self):
        print(f"Name of the employee: {self.name}")
        print(f"Age of the employee: {self.age}")
        print(f"Email of the Employee: {self.email}")
        print(f"Language of the employee: {self.language}")

d=Developer("Eve", 23, "eve@xyz.com", 600, "javascript")
d.print_details()