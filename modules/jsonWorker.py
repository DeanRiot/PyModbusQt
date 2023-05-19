import json


def readFile():
    with open("commands.json", "r") as jsonFile:
        data = json.load(jsonFile)
        return data


def writeFile(jsonData):
    with open("commands.json", "w") as jsonFile:
        json.dump(jsonData, jsonFile)
