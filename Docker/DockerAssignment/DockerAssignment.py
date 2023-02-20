import os
import socket
from collections import Counter

Counter = Counter()


def getNumberOfWords(file):
    totalwordcount = 0
    with open(file, 'r') as file:
        for line in file:
            if (line != '\n'):
                if (file.name.endswith("IF.txt")):
                    Counter.update(line.replace("Â", "").split())
                totalwordcount = totalwordcount + len(line.replace("Â", "").split())
    return totalwordcount

def getMyIPAdress():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    return IPAddr

WordCountOfTextFiles = {}
path ="/home/data"
if os.path.exists(path + "/" +"result.txt"):
  os.remove(path + "/" +"result.txt")
stringAtOutput="a. text file at location: /home/data \n"
for eachFile in os.listdir(path):
    if eachFile.endswith(".txt"):
        stringAtOutput=stringAtOutput+eachFile+"\n"
        WordCountOfTextFiles[eachFile] = getNumberOfWords(path + "/" + eachFile)
		
stringAtOutput=stringAtOutput+"\n"
stringAtOutput=stringAtOutput+"b. Read the two text files and count total number of words in each text files\n"
TotalNumberOfWordsInAllFiles = 0
AllFilesNames = ""
for eachkey in WordCountOfTextFiles.keys():
    AllFilesNames = AllFilesNames + eachkey + ","
    TotalNumberOfWordsInAllFiles = TotalNumberOfWordsInAllFiles + WordCountOfTextFiles.get(eachkey)
    stringAtOutput = stringAtOutput +"total number of words in [" + eachkey + "] is : " + str(WordCountOfTextFiles.get(eachkey))+"\n"

stringAtOutput = stringAtOutput +"\n"
stringAtOutput = stringAtOutput +"c. grand total (total number of words in both files)\n"
stringAtOutput = stringAtOutput +"total number of words in both files [" + AllFilesNames[0:len(AllFilesNames) - 1] + "] is: " + str(TotalNumberOfWordsInAllFiles)+"\n"

stringAtOutput = stringAtOutput +"\n"
stringAtOutput = stringAtOutput +"d. top 3 words with maximum number of counts in IF.txt\n"
stringAtOutput = stringAtOutput +str(Counter.most_common(3))+"\n"

stringAtOutput = stringAtOutput +"\n"
stringAtOutput = stringAtOutput +"e. IP address \n"
stringAtOutput = stringAtOutput +"Your Computer IP Address is:" + getMyIPAdress()

resultsTextFile = open(path + "/" +"result.txt","w")
resultsTextFile.write(stringAtOutput)
resultsTextFile.close()
for eachline in open(path + "/" +"result.txt","r").readlines():
    print(eachline.replace("\n",""))