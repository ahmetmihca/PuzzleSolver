def getInput(a):
  if a == "puzzle":    
    return input("Please enter the puzzle: ").lower()  
  if a == "words":
    return input("Please enter the words: ").lower()  

  def checkInput(a):
  while True:
    if a.find("-") != -1:
      b = a.split("-")            
      for i in range (len(b)):
        if len((b)[i]) == len((b)[0]) and b[i].isalpha():
          check = True        
        else:
          check = False           
    else:
      check = False
    break       
  return check 

def printPuzzle(a):
  b = a.split("-")
  for i in b:
    print (i.lower()) 
    
def findWords (puzzle,words):
  b = puzzle.split("-")
  words= words.split(",")
  yatay_wordList = []
  ters_yatay_wordList = []
  duz_sutun_wordList = []
  ters_sutun_wordList = [] 
  for i in range(len(b)):
    yatay_wordList.append(b[i][0:])
    ters_yatay_wordList.append(b[i][::-1])       
  for i in range(len(b[0])):
    A = ""
    for u in range(len(b)):
      A += b[u][i]
    duz_sutun_wordList.append(A)
    ters_sutun_wordList.append(A[::-1])
  for y in range(len(words)):
    check = True
    for x in range(len(yatay_wordList)):    
      if words[y] in yatay_wordList[x]: 
        check = False
        print("Found ",words[y]," at ", "(",x,",", yatay_wordList[x].index(words[y]),")","-","(",x,",",yatay_wordList[x].index(words[y])+len(words[y])-1,")", sep = "")    
    for x in range(len(yatay_wordList)):    
      if words[y] in ters_yatay_wordList[x]:
        check = False
        print("Found ", words[y], " at ", "(", x,",",len(ters_yatay_wordList[x])-1-ters_yatay_wordList[x].index(words[y]),")", "-", "(",x,",",len(ters_yatay_wordList[x])-1-(ters_yatay_wordList[x].index(words[y])+len(words[y])-1),")", sep="")
    for x in range(len(duz_sutun_wordList)):    
      if words[y] in duz_sutun_wordList[x]:
        check = False
        print("Found ", words[y], " at ","(",duz_sutun_wordList[x].index(words[y]),",",x,")","-","(",duz_sutun_wordList[x].index(words[y])+len(words[y])-1,",",x,")",sep = "")
    for x in range(len(ters_sutun_wordList)):    
      if words[y] in ters_sutun_wordList[x]:
        check = False
        print("Found ", words[y], " at ", "(",len(ters_sutun_wordList[x])-1-ters_sutun_wordList[x].index(words[y]), ",",x,")","-","(",len(ters_sutun_wordList[x])-1-(ters_sutun_wordList[x].index(words[y])+len(words[y])-1),",",x,")", sep="")      
    if check:
      print(words[y], "does not exist.")

puzzle = getInput("puzzle")
while not checkInput(puzzle):
  print("Wrong input format.")
  puzzle = getInput("puzzle")

words = getInput("words")
printPuzzle(puzzle)

findWords(puzzle,words)
