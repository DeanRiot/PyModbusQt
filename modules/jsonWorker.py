import json


def readFile():
    with open("data.json", "r") as jsonFile:
        data = json.load(jsonFile)
        return data


def writeFile(jsonData):
    with open("data.json", "w") as jsonFile:
        json.dump(jsonData, jsonFile)
