import os
import sys
import json

def main():
    args = sys.argv[1:] #Stating by 0
    servicesapi = []

    with open("cdk.json","r") as file:
        jsonData = json.load(file)
        #print(jsonData)
        #print(jsonData['context']['Service']['resources'])
        servicesapi = [x for x in jsonData['context']['Service']['resources']]
    
    #print(len(servicesapi))
    for indexval in servicesapi:
        #print(indexval['lambda']['image'])
        lambdatid = indexval['lambda']['image']['id']
        lambdatag = indexval['lambda']['image']['tag']
        
        path = args[0]+"/"+args[1]+"/"+args[2]+"/"+args[3]+"/"+lambdatid+"/"+lambdatag
        isExist = os.path.exists(path)
        print("URL : "+ args[0]+"/"+args[1]+"/"+args[2]+"/"+args[3]+"/"+lambdatid+"/"+lambdatag + "   Exist="+str(isExist))

if __name__ == "__main__":
    main()