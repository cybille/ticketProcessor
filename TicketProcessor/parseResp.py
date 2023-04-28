import json

parsedResponse=" "

def parse(response):
    parsedResponse= response.get("choices")[0]["text"]
  
    return parsedResponse

def parseUsingFields(response, listName,fieldName):
    parsedResponse= response.get(listName)[0][fieldName]
    return parsedResponse