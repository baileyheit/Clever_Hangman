'''
Created on Nov 4, 2018

@author: baileyheit
'''
'''
Description:
        You must create a Hangman game that allows the user to play and guess a secret word.  
        See the assignment description for details.
    
@author: Bailey Heit    blh41
'''

import random
DEBUG = False


def handleUserInputDifficulty():
    '''
    This function asks the user if they would like to play the game in (h)ard or (e)asy mode, then returns the 
    corresponding number of misses allowed for the game. 
    '''
    
    
    print("How many misses do you want? Hard has 8 and Easy has 12")
    k = input("(h)ard or (e)asy> ")
    p = 0
    if k == 'h':
        p = 8
        print("you have " + str(p) + " misses to guess word")
        print ('')
    if k == 'e':
        p = 12
        print("you have " + str(p) + " misses to guess word")
        print ('')
    return p
    pass 




def getWord(words, length):
    '''
    Selects the secret word that the user must guess. 
    This is done by randomly selecting a word from words that is of length length.
    '''
    
    x = []
    for s in words:
        if len(s) == length:
            x.append(s)   
    t = len(x)
    m = random.randint(0, len(x)-1)
    secretWord = x[m]
    return secretWord
    pass 




def createDisplayString(lettersGuessed, misses, hangmanWord):
    ' creates outputs that give user information about the game and update every turn '
    alphabet = ['a','b','c','d','e','f','g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o','p','q','r','s','t','u','v','w','x','y','z']
    for m in lettersGuessed:
        if m in lettersGuessed:
            p = alphabet.index(m)
            alphabet[p] = ' '
    f = ''.join(alphabet)
    p1 = ''
    p1 += '''letters not yet guessed: ''' + f 
    p1 += '\n' 
    misses = str(misses)
    p1 += 'misses remaining = ' + misses
    p1 += '\n'
    p1 +=  ' '.join(hangmanWord)

    return p1
    




def handleUserInputLetterGuess(lettersGuessed, displayString):
    '''    
    Prints displayString, then asks the user to input a letter to guess.
    This function handles the user input of the new letter guessed and checks if it is a repeated letter.
    '''

    k = input("letter> ")
    while k in lettersGuessed:
        print("you already guessed that")
        k = input("letter> ")
        print(displayString)
    else:
        lettersGuessed.append(k) 
        f = ''.join(lettersGuessed)
    return k
    pass 




def updateHangmanWord(guessedLetter, secretWord, hangmanWord):
    '''
    Updates hangmanWord according to whether guessedLetter is in secretWord and where in secretWord guessedLetter is in.
    '''
    for x in range(len(secretWord)):
        if secretWord[x] == guessedLetter:
            hangmanWord[x]= guessedLetter
    return hangmanWord
    pass


def processUserGuess(guessedLetter, secretWord, hangmanWord, misses):
    '''
    Uses the information in the parameters to update the user's progress in the hangman game.
    '''
    
    l = []
    hangmanWord = updateHangmanWord(guessedLetter, secretWord, hangmanWord)
    l.append(hangmanWord)
    l.append(misses)
    if guessedLetter in secretWord:
        l.append(True)
    if guessedLetter not in secretWord:
        l.append(False) 
    return l

def handleUserInputDebugMode():
    'user inputs whether they want debug or play mode'
    k = input("Which mode do you want: (d)ebug or (p)lay: ")
    if k == 'd':
        return True
    if k == 'p': 
        return False
    
# def startTemplate(length):
#     dashes = []
#     for _ in range(length):
#         dashes.append("_")
#     dashes = ''.join(dashes)
#     return dashes
#     
def handleUserInputWordLength():
    ' gives user text then user inputs length of word'
    k = input("how many letters in the word you'll guess: ")
    k = int(k)
    return k

def createTemplate(currentTemplate, letterGuess, word):
    'creates template of hangmanword depending on wordlist'
    curList = list(currentTemplate)
    wordList = list(word)

    for i in range(len(wordList)): 
        if letterGuess == wordList[i]:
            curList[i] = letterGuess
    cur = ''.join(curList)
    return cur 

# 
def getNewWordList(currentTemplate, letterGuess, wordList):
    'uses dictionary of word list and current template to  update word list and create new dictionary and find key w most values'
    global DEBUG
    dict = {}
    for word in wordList:
#         p = False
#         for i in range(len(word)):
#             if currentTemplate[i] != '_' and currentTemplate[i] != word[i]:
#                 p = True
#             if word[i] in currentTemplate and currentTemplate[i] == '_':
#                 p = True 
#         if p:
#             continue
        answer = createTemplate(currentTemplate, letterGuess, word)
#         answer = ''
#         for i in range(len(word)):
#             if word[i] == currentTemplate[i] and word[i] != letterGuess:
#                 answer += currentTemplate[i]
#             elif word[i] == letterGuess: 
#                 answer += word[i]
#             elif word[i] != letterGuess and word[i] not in currentTemplate:
#                 answer += '_'
        if answer not in dict:
            dict[answer] = []
        dict[answer].append(word)
    maxi = 0
    x = ''
    for keys,values in dict.items():
        if len(values) > maxi:
            maxi = len(values)
            x = keys
    newlist = dict[x]
    if DEBUG:
        info = dict.items()
        tosort = [(t[0], t[1]) for t in info]
        info = sorted(tosort)
        for i in info:
            print(i[0], ":", len(i[1]))
        print("# keys =", len(info))
    return (x, newlist)


        
def runGame(filename):
    'calls all necessary functions in order so hangman game runs smoothly'
    global DEBUG
    DEBUG = handleUserInputDebugMode()
    
    wordListold = []
    lettersGuessed = []
    f = open(filename)
    for line in f: 
        line = line.strip()
        wordListold.append(line)
    f.close()
    


    wordList = []
    length = handleUserInputWordLength()
    currentTemplate = '_' * length
    for word in wordListold:
        if len(word) == length:
            wordList.append(word)
    misses = handleUserInputDifficulty()
    missesNew = misses
    
    guesses = 0
    
    secretWord = getWord(wordList, length)
    hangmanWord = list(currentTemplate)
    while misses > 0:
        displayString = createDisplayString(lettersGuessed, misses, hangmanWord)
        print(displayString)
        if DEBUG:
            print( '(word is ' +  secretWord + ')')
            print('\n# possible words: ' + str(len(wordList)))
        guessedLetter = handleUserInputLetterGuess(lettersGuessed, displayString)
        letterGuess = guessedLetter
        #updateHangmanWord(guessedLetter, secretWord, hangmanWord)
        l = processUserGuess(guessedLetter, secretWord, hangmanWord, misses)
        
        newword = getNewWordList(currentTemplate, letterGuess, wordList)
        #print(newword)
        wordList = newword[1]
        currentTemplate = newword[0]
        secretWord = getWord(wordList, length)
        hangmanWord = list(currentTemplate)
        
        
        if guessedLetter not in secretWord:
            misses -= 1
            guesses += 1
        else: 
            misses = misses
            guesses += 1
#         handleUserInputLetterGuess(lettersGuessed, displayString)
        if (l[2]) == False:
            print ("you missed: " + guessedLetter + " not in word")
            print('')
        else: 
            print ('')
        if secretWord == ''.join(hangmanWord):
            print ("you guessed the word: " + str(secretWord))
            f = misses - (l[2])
            print ('you made ' + str(guesses) + " guesses with " + str(missesNew - misses) + " misses")
            return True
    if misses == 0:
        print ("you're hung!!")
        print ("word is " + str(secretWord))
        print ('you made ' + str(guesses) + " guesses with " + str(missesNew - misses) + " misses")
        return False 
#    
if __name__ == "__main__":
    '''
    Running Hangman.py should start the game, which is done by calling runGame, therefore, we have provided you this code below.
    '''
    runGame('lowerwords.txt')
#     print(createDisplayString("aeouy", 5, ["p", "a", "_"]))
