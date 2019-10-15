'''
Created on Nov 6, 2018

@author: baileyheit
'''

''' wordList: list of characters with letters currect
    letter = letterGuess
    wordToGuess = secretword... word user is trying to guess
    guessList = currentTemplate... word to guess as list of characters
    secretList = 
def getNewWordList(currentTemplate, letterGuess, wordList): 
    dict = {}
    for word in currentTemplate:'''

'''def getNewWordList(currentTemplate, letterGuess, wordList):
    dict = {}
    for word in currentTemplate:
        answer = ''
        for i in word:
            for j in wordList:
                if i == j and i != letterGuess:
                    answer += j 
                if i == letterGuess:
                    answer += i
                elif i not in wordList:
                    answer += '_'
            if answer not in dict:
                dict[answer] = ''
            if answer in dict: 
                dict[answer] += word + ' '
    
    maxi = 0
    x = ''
    for keys, values in dict.items():
        if len(values) > max:
            maxi = len(values)
            x = keys
    newlist = []
    for a in dict.keys():
        if a == x:
            for value in dict[a].split():
                newlist.append(value)
            
def gmode():                
    if gmode == "t":
        print
        print ("Dictionary of Categories and # words: ")
        for blanks in dic0:
            print (blanks, len(dic0[blanks])
    
       
def getNewWordList(currentTemplate, letterGuess, wordList):
    dic0 = {}
    lista = []
    for w in wordList:
        newnew = changeWord(w, letter, guessList)
        if newnew not in dic0:
            dic0[newnew] = [w]
        else: 
            dic0[newnew] += [w]
        if len(dic0[newnew]) > len(lista)  
            lista = dic0[newnew]'''
            
'''            
def getNewWordList(currentTemplate, letterGuess, wordList):
    currTempList = ''.split(currentTemplate)
    for i in wordList:
        t = dict()
        wordTemp = []
        for i in wordList:
            wordL = list(i)
            p = []
            for n in wordL:
                if n == letterGuess:
                    p.append(n)
                else:
                    p.append('_')
            ' so now i have a list of characters that fit a template in word'
            if p not in wordTemp:
                f = ''.join(p)
                wordTemp.append(p)
                e = ''.join(wordL)
                t[f] = [e]
            else:
                f = ''.join(p)
                e = ''.join(wordL)
                t[f] += [e]

    met = 0
    winninglist = [] 
    winningkey = ''
    for key in t:
        i = t[key]
        p = len(i)
        if p >= met:
            met = p
            winninglist = i
            winningkey = key
        if p == met:
            if i.count('_') < winningkey.count('_'):
                met = p
                winninglist = i
    print(t)
    return (winningkey, winninglist)

'''
            
'''def getNewWordList(currentTemplate,letterGuess,wordList):
    dict = {}
    for word in wordList:
        answer = ''
        for i in word:
            for j in currentTemplate:
                if i == j and i != letterGuess:
                    answer += j 
                if i == letterGuess:
                    answer += i
                elif i not in c:
                    answer += '_'
            if answer not in dict:
                dict[answer] = ''
            if answer in dict: 
                dict[answer] += word + ' '
    maxi = 0
    x = ''
    for keys,values in dict.items():
        if len(values) > maxi:
            maxi = len(values)
            x = keys
    newlist = []
    for a in dict.keys():
        if a == x:
            for value in dict[a].split():
                newlist.append(value)
                
    return (x,newlist)
    print(dict)
    met = 0
    winninglist = [] 
    winningkey = ''
    for key in dict:
        i = dict[key]
        p = len(i)
        if p >= met:
            met = p
            winninglist = i
            winningkey = key
        if p == met:
            if i.count('_') < winningkey.count('_'):
                met = p
                winninglist = i
    return (winningkey, winninglist)'''
    
'''def getNewWordList(currentTemplate, letterGuess, wordList):
    dict = {}
    for word in wordList:
        answer = ''
        for i in word:
            for j in currentTemplate:
                if i == j and i != letterGuess:
                    answer += j 

            if i == letterGuess:
                answer += i
            if i not in currentTemplate:
                answer += '_'
        if answer not in dict:
            dict[answer] = ''
        if answer in dict: 
            dict[answer] += word + ' '
    maxi = 0
    x = ''
    for keys,values in dict.items():
        if len(values) > maxi:
            maxi = len(values)
            x = keys
    newlist = []
    for a in dict.keys():
        if a == x:
            for value in dict[a].split():
                newlist.append(value)
    return (x,newlist)'''

# def getNewWordList(currentTemplate, letterGuess, wordList):
#     dict = {}
#     for word in wordList:
#         answer = ''
#         for i in range(len(word)):
#             if word[i] == currentTemplate[i] and word[i] != letterGuess:
#                 answer += currentTemplate[i]
#                 print(1,word[i])
#             elif word[i] == letterGuess: 
#                 answer += word[i]
#                 print(2,word[i])
#             elif word[i] != letterGuess and word[i] not in currentTemplate:
#                 answer += '_'
#                 print(3,word[i])
#         if answer not in dict:
#             dict[answer] = ''
# #         if answer in dict: 
# #             dict[answer] += word + ' '
# #     maxi = 0
# #     x = ''
# #     for keys,values in dict.items():
# #         if len(values) > maxi:
# #             maxi = len(values)
# #             x = keys
# #     newlist = []
# #     for a in dict.keys():
# #         if a == x:
# #             for value in dict[a].split():
# #                 newlist.append(value)
# #     return (x,newlist)
# 
# def createTemplate(currentTemplate, letterGuess, word):
#     curList = list(currentTemplate)
#     wordList = list(word)
#     for i in range(len(wordList)): 
#         if letterGuess == wordList[i]:
#             curList[i] = letterGuess
#     cur = ''.join(curList)
#     return cur 
# 
# # def getNewWordList(currentTemplate, letterGuess, wordList):
# #     dict = {}
# #     for word in wordList:
# #         p = False
# #         for i in range(len(word)):
#             if currentTemplate[i] != '_' and currentTemplate[i] != word[i]:
#                 p = True
#             if word[i] in currentTemplate and currentTemplate[i] == '_':
#                 p = True 
#         if p:
#             continue
#         answer = createTemplate(currentTemplate, letterGuess, word)
# #         answer = ''
# #         for i in range(len(word)):
# #             if word[i] == currentTemplate[i] and word[i] != letterGuess:
# #                 answer += currentTemplate[i]
# #             elif word[i] == letterGuess: 
# #                 answer += word[i]
# #             elif word[i] != letterGuess and word[i] not in currentTemplate:
# #                 answer += '_'
#         if answer not in dict:
#             dict[answer] = ''
#         if answer in dict: 
#             dict[answer] += word + ' '
#     maxi = 0
#     x = ''
#     for keys,values in dict.items():
#         if len(values) > maxi:
#             maxi = len(values)
#             x = keys
#     newlist = []
#     for a in dict.keys():
#         if a == x:
#             for value in dict[a].split():
#                 newlist.append(value)
#     return (x,newlist)
# 
# def getNewWordList(currentTemplate, letterGuess, wordList):
#     dict = {}
#     for word in wordList:
# #         p = False
# #         for i in range(len(word)):
# #             if currentTemplate[i] != '_' and currentTemplate[i] != word[i]:
# #                 p = True
# #             if word[i] in currentTemplate and currentTemplate[i] == '_':
# #                 p = True 
# #         if p:
# #             continue
#         answer = createTemplate(currentTemplate, letterGuess, word)
# #         answer = ''
# #         for i in range(len(word)):
# #             if word[i] == currentTemplate[i] and word[i] != letterGuess:
# #                 answer += currentTemplate[i]
# #             elif word[i] == letterGuess: 
# #                 answer += word[i]
# #             elif word[i] != letterGuess and word[i] not in currentTemplate:
# #                 answer += '_'
#         if answer not in dict:
#             dict[answer] = []
#         dict[answer].append(word)
#     maxi = 0
#     x = ''
#     for keys,values in dict.items():
#         if len(values) > maxi:
#             maxi = len(values)
#             x = keys
#     newlist = dict[x]
# #     if DEBUG:
#     for key,value in dict.items():
#         print(key, ":", len(value))
# #         newlist = []
# #         for a in dict.keys():
# #             for value in dict[a].split():
# #                 newlist.append(value)
#     return (x.strip(), newlist)
length = 5
hangmanWord = ['_'] * length
print(hangmanWord)


# if __name__ == '__main__':
#     print(getNewWordList('____', 'O', [ "OBOE", "NOON", "ODOR", "ROOM", "SOLO", "TRIO", "GOTO", "OATH", "OXEN", "PICK", "FRAT", "HOOP"]))
#     print(getNewWordList('_O__','E', ['OBOE', 'NOON', 'ODOR', 'ROOM', 'SOLO', 'TRIO', 'GOTO', 'OATH', 'OXEN', 'PICK', 'FRAT', 'HOOP']))
#     print(getNewWordList('_OO_','E', ['OBOE', 'NOON', 'ODOR', 'ROOM', 'SOLO', 'TRIO', 'GOTO', 'OATH', 'OXEN', 'PICK', 'FRAT', 'HOOP']))