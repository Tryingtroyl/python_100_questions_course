from pprint import pprint
import json

with open("files/company1.json", "r") as file:
    d=json.loads(file.read())
    
pprint(d)
