import sys , os, time
FUSSERVER = 'http://10.94.217.84'
wordName = sys.argv[1]

def checkForWord():
    r = requests.get(FUSSERVER)
    return wordName in r.text

checkForWord(filename,1048576)
