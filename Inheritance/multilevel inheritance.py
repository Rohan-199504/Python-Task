class Employee:

    def __init__ (self, name , age , email):
        self.name=name
        self.age=age
        self.email=email

    def print_details(self):
        print(f"Name of the employee {self.name}")
        print(f"Age of the employee {self.age}")
        print(f"Email of the Employee {self.email}")


class Director(Employee):

    def __init__ (self, name , age , email , sal):
        super().__init__ (name, age, email)
        self.sal=sal

    def print_details(self):
        super().print_details()
        print(f"Salary of the employee: {self.sal}")

class Developer(Director):

    def __init__ (self, name, age, email, sal , language):
        super(). __init__ (name, age, email, sal)
        self.language=language

    def print_details(self):
        super().print_details()
        print(f"Language of the employee: {self.language}")

d=Developer("Eve", 23, "eve@gmail.com", 600, "java")
d.print_details()