q1 = """When was the world's first official motor race held?
a. 1989
b. 1895 
c. 1967
d. 1998"""

q2 = """Who invented the gas-powered internal combustion engine?
a. Henry Ford
b. Karl Benz
c. Nicolaus Otto 
d. Rudolf Diesel"""

q3 = """How many colours were there for Ford Model T?
a. one 
b. six
c. four
d. seven"""

q4 = """When was the first gas-driven car made?
a. 1885
b. 1760
c. 1807
d. 1910"""

q5 = """Which of these cars is driven by secret agent James Bond?
a. chitty chitty bang bang
b. Herbie
c. aston martin DB5
d. Delorean DMC-12"""

questions = {q1:"b", q2:"c", q3:"a", q4:"a", q5:"c"}

name = input("enter your name:")
print("hello", name, "welcome to car quiz")
score = 0
for i in questions:
    print()
    print(i)
    f1 = input("Do you want to skip this question (yes/no)")
    if f1 == "yes":
        continue
    ans = input("enter the answer (a/b/c/d):")
    if ans == questions[i]:
        print("correct answer, you got 1 point")
        score += 1
        print("Current score is:", score)
    else:
        print("wrong answer, lost 1 point")
        score -= 1
        print("Current score is:", score)
    f2 = input("Do you want to quit (yes/no):")
    if f2 == "yes":
        break



print("Final score is:", score)
