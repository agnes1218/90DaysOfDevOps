import json
dict = { "name " : "Agnes" , "Age" : "24"}
obj = json.dumps(dict, indent=1)
print(obj)