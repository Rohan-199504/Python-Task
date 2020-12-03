#convert from JSON to Python
import json
 # json
x = '{"name":"Jeff", "age":30, "place":"New York"}'

#parse x using[json.loads()]
y = json.loads(x)
print(y['age'])


#convert from Python to JSON

# Python object (dict):
a = {
    "name":"Jeff",
    "age":30,
    "place":"New York"
}
#conversion
b = json.dumps(a)
print(b)


#converting all python Objects containing all the legal data types
import json
student = {
    "name":"Aryan",
    "std":10,
    "passed":True,
    "failed":False,
    "subjects":("math", "science"),
    "scholarship": None,
    "bicycle" : [
        {"brand":"Hero", "model":"Street Fighter"},
        {"brand":"TATA", "model":"Falcon"}
    ]
}
r = json.dumps(student)
print(r)
