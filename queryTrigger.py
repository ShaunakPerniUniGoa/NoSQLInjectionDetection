import json
import pymongo
import os

print(os.path)
print(os.listdir())

with open("No-SQL_Gen/No-SqlDataset.json", "r") as queryFile:
    data = json.load(queryFile)

print(queryFile)