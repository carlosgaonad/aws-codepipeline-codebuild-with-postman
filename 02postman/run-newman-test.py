import os
import sys
import json
import subprocess


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
        # get id and image tag of each service
        lambdatid = indexval['lambda']['image']['id']
        lambdatag = indexval['lambda']['image']['tag']
        
        path = args[0]+"/"+args[1]+"/"+args[2]+"/"+args[3]+"/"+lambdatid+"/"+lambdatag
        #Check if exist the repository path with the correct files
        isExist = os.path.exists(path)
        isExistcollection=os.path.exists(path+"/postman_collection.json")
        isExistEnvironment=os.path.exists(path+"/postman_environment.json")
        #print("URL : "+ args[0]+"/"+args[1]+"/"+args[2]+"/"+args[3]+"/"+lambdatid+"/"+lambdatag + "   Exist="+str(isExist))
        
        if isExist & isExistcollection & isExistEnvironment:
            #Crear directorio newman/servicio
            #tempnewmanurl = "newman/"+args[2]+"/"+lambdatid+"/"+lambdatag
            tempnewmanurl = "newman/"+args[2]+"/"+lambdatid
            subprocess.run(["mkdir", tempnewmanurl])
            #command = "newman run postman_collection.json --environment postman_environment.json -r junit --reporter-junit-export " + tempnewmanurl
            #process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
            #process.wait()
        else:
            print("Directory or files not fount in "+path+ ", please check your repository")


if __name__ == "__main__":
    main()