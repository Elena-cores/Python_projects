import json

fp = open("data.json", "r")

obj = json.load(fp)
print(obj)
print(type(obj))





fp.close()