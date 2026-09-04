import json
with open("data.json","r") as file:
    data=json.load(file)
    print("name:",data["name"])
    print("age:",data["age"])
    print("course:",data["course"])
    print("marks:",data["marks"])