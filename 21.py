d = {"a": 1, "b": 2, "c": 3}
print(dict((key,value) for key,value in d.items() if d[key]<=1))