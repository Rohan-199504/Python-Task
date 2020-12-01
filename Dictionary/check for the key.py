#to check whether the given key already exists in a dictionary

bike_details={'brand' : 'bajaj' , 'model' : 'pulsar' , 'cc' : '220' }
print(bike_details)
"""
if 'cc' in bike_details.keys():
    print("Key exists")
else:
    print("No")
     
"""
#iterate dict using for loop

for i in bike_details:
    print(i, bike_details[i])