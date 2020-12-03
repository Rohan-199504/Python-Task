class Employee:

    def __init__(self, name, email, sal):
         self.name=name
         self.email=email
         self.sal=sal

    def print_details(self):
        print(f"Name:{self.name}")
        print(f"email:{self.email}")
        print(f"Sal:{self.sal}")

class Developer(Employee):

    def __init__(self,name,email,sal,lang):
        super().__init__(name,email,sal)
        self.lang=lang

    def print_details(self):
        super().print_details()
        print(f"Language of the employee:{self.lang}")




d=Developer("many", "many@gmail.com", 500, "c#")
d.print_details()

