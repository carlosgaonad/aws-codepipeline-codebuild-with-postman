import os
import sys
import json
import subprocess


def main():
    args = sys.argv[1:] #Stating by 0
    servicesapi = []
    APIFOLDER = args[2]

    with open("cdk.json","r") as file:
        jsonData = json.load(file)
        #print(jsonData)
        #print(jsonData['context']['Service']['resources'])
        servicesapi = [x for x in jsonData['context']['Service']['resources']]
    
    #Create API Folder to store all collections taken from collections repository
    os.system("mkdir "+ APIFOLDER)
    for indexval in servicesapi:
        #print(indexval['lambda']['image'])
        # get id and image tag of each service
        lambdatid = indexval['lambda']['image']['id']
        lambdatag = indexval['lambda']['image']['tag']
        
        pathDir = args[0]+"/"+args[1]+"/"+args[2]+"/"+args[3]+"/"+lambdatid+"/"+lambdatag
        pathCollection = pathDir+"/postman_collection.json"
        pathEnvironment = pathDir+"/postman_environment.json"
        #Destination path APIgateway/serviceID
        destinationpath = APIFOLDER+"/"+lambdatid
        #Check if exist the repository path with the correct files
        isExist = os.path.exists(pathDir)
        isExistcollection=os.path.exists(pathCollection)
        isExistEnvironment=os.path.exists(pathEnvironment)
        #print("URL : "+ args[0]+"/"+args[1]+"/"+args[2]+"/"+args[3]+"/"+lambdatid+"/"+lambdatag + "   Exist="+str(isExist))
        
        if isExist & isExistcollection & isExistEnvironment:
            #Crear directorio newman/servicio
            #tempnewmanurl = "newman/"+args[2]+"/"+lambdatid+"/"+lambdatag
            tempnewmanurl = "newman/"+args[2]+"/"+lambdatid+"/"
            os.system("mkdir "+tempnewmanurl )
            os.system("cp "+pathCollection+" "+destinationpath )
            os.system("cp "+pathEnvironment+" "+destinationpath )
            #subprocess.run(["mkdir", tempnewmanurl])
            #os.system("echo '******************************************** PATH '")
            #os.system("ls -lrt "+pathCollection)

            #command = "newman run ./"+ pathCollection +" --environment ./"+pathEnvironment+" -r junit --reporter-junit-export " + tempnewmanurl
            #print("Ready to run command = "+ command)
            #- newman run PetStoreAPI.postman_collection.json --environment PetStoreAPIEnvironment.postman_environment.json -r junit
            #result = subprocess.run(command.split(" "), shell=True, capture_output=True, text=True)
            #print(result)
            #process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
            #process.wait()
        else:
            print("Directory or files not found in "+pathDir+ ", please check your repository")


if __name__ == "__main__":
    main()