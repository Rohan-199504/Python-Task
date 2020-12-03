class Students:

    def __init__(self, name, sex, sec):
         self.name=name
         self.sex=sex
         self.sec=sec

    def print_details(self):
        print(f"Name:{self.name}")
        print(f"Sex:{self.sex}")
        print(f"Sec:{self.sec}")
"""
s1 = Students("adam", "male", "a")
s2 = Students("eve", "female", "a")
s1.print_details()
s2.print_details()
"""

