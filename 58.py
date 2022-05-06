import json

with open("files/company1.json","r+") as file:
    d=json.loads(file.read())
    d["employees"].append({"firstName":"Adarsh", "lastName":"Verma"})
    file.seek(0)
    json.dump(d,file,indent=4)
