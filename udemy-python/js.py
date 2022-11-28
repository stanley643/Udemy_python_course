import json

x = '{"name":"Stan", "age":"23", "job":"developer"}'
y = json.loads(x)
print(y)