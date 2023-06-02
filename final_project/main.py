import json

data_tambah = {"nama":"Alam","umur":20}

with open("database.json","r") as file :
    data = json.load(file)

data.append(data_tambah)

with open("database.json","w")as file:
    json.dump(data,file)