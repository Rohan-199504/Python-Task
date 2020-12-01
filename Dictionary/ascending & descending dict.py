import operator
d = {"math": 1,"sci": 2,"lit" : 3, "hist": 4}
print("original =", d)
Asc =  dict(sorted(d.items(),key=operator.itemgetter(1)))
print("ascending=",Asc)

Dsc = dict(sorted(d.items(),key=operator.itemgetter(1), reverse=True))
print("descenging=",Dsc)