# programe For each directory you find create a dictonary that contains the folders as keys and files as values.

import os
import task1.py
def getListOfFiles(dirName):
     
    listOfFile = os.listdir(dirName)
    allFiles = list()
    
    for entry in listOfFile:
        
        fullPath = os.path.join(dirName, entry)
         
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles        
 
 
def main():
    
    dirName = '/home/Downloads';
    
    
    listOfFiles = getListOfFiles(dirName)
    
    
    for elem in listOfFiles:
        print(elem)
 
    print ("******")
    
    
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(dirName):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]
        
        
      
    for elem in listOfFiles:
        print(elem)    
        
        
        
        
if __name__ == '__main__':
    main()




# file name and chasr count in given files

import string 
text = open('book1.txt')
letters = string.ascii_lowercase
for i in text:
  text_lower = i.lower()
  text_nospace = text_lower.replace(" ", "")
  text_nopunctuation = text_nospace.strip(string.punctuation)
  for a in letters:
    if a in text_nopunctuation:
      num = text_nopunctuation.count(a)
      print(a, num)

print(filename,num)
