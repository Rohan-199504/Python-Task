#write a python function to find the max of three numbers

def maxoftwo (a,b):

    if a>b:
        return a
    return b
def maxofthree (a,b,c):
    return maxoftwo(a,maxoftwo(b,c))
print(maxofthree (78,23,99))