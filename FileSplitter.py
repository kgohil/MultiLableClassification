# This Program reads news articles and splits them in different text snippets containing varying amount of information
import re

# Reads File
def fileRead(path):
    f = open(path, mode='r')
    lines = f.readlines()
    f.close()
    return lines

# Extracts and writes the title twice along with the first 500 words of the news article
def fileWrite2T500(lines, name):
    path = 'D:/Dump/Data2T500/' + name
    f = open(path.strip(), 'w')
    wordList = re.sub("[^\w]", " ", ' '.join(lines)).split()
    #f.write(str(wordList[0:500]))
    for i in range(0,30):
        try:
            f.write(str(wordList[i])+' ')
        except:
            f.flush()
    for i in range(0,500):
        try:
            f.write(str(wordList[i])+' ')
        except:
            f.flush()
    #f.write(str(lines[0:20]))
    #f.write(str(lines[0:500]))
    f.close()

# Extracts and writes the first 1000 words of the news article
def fileWrite1000(lines, name):
    path = 'D:/Dump/DataT1000/' + name
    f = open(path.strip(), 'w')
    wordList = re.sub("[^\w]", " ", ' '.join(lines)).split()
    for i in range(0,1000):
        try:
            f.write(str(wordList[i])+' ')
        except:
            f.flush()
    f.close()

# Extracts and writes the title twice along with the entire news article laying more emphasis on the title
def fileWrite2T(lines, name):
    path = 'D:/Dump/Data2T/' + name
    f = open(path.strip(), 'w')
    wordList = re.sub("[^\w]", " ", ' '.join(lines)).split()
    for i in range(0,30):
        try:
            f.write(str(wordList[i])+' ')
        except:
            f.flush()
    for i in range(0,len(wordList)):
        try:
            f.write(str(wordList[i])+' ')
        except:
            f.flush()
    f.close()

# This gets the list of News files to be split
fileNames = fileRead('D:/Dump/finalDataList.txt')
# defines the path on which the text snippets will be stored
filePath = 'D:/Dump/buss_sports_tech_pol_food_health_science/'
for index, names in enumerate(fileNames):
    names = fileNames[index]
    path = filePath + names
    f = open(path.strip())
    lines = f.readlines()
    fileWrite2T500(lines, names)
    fileWrite1000(lines, names)
    fileWrite2T(lines, names)
    f.close()
