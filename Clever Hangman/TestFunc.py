'''
Created on Nov 4, 2018

@author: baileyheit
'''
# def getNewWordList(currentTemplate, letterGuess, wordList):
#     currTempList = ''.split(currentTemplate)
#     for i in wordList:
#         t = dict()
#         wordTemp = []
#         for i in wordList:
#             wordL = list(i)
#             p = []
#             for n in wordL:
#                 if n == letterGuess:
#                     p.append(n)
#                 else:
#                     p.append('_')
#             print(p)
#             ' so now i have a list of characters that fit a template in word'
#             if p not in wordTemp:
#                 f = ''.join(p)
#                 wordTemp.append(p)
#                 e = ''.join(wordL)
#                 t[f] = [e]
#             else:
#                 f = ''.join(p)
#                 e = ''.join(wordL)
#                 t[f] += [e]
#     met = 0
#     winninglist = [] 
#     winningkey = ''
#     for key in t:
#         i = t[key]
#         p = len(i)
#         if p >= met:
#             met = p
#             winninglist = i
#             winningkey = key
#         if p == met:
#             if i.count('_') < winningkey.count('_'):
#                 met = p
#                 winninglist = i
#     print(winningkey)
#     return (winningkey, winninglist)

def createTemplate(currentTemplate, letterGuess, word):
    curList = list(currentTemplate)
    wordList = list(word)
    print(wordList)
    for i in range(len(wordList)): 
        if letterGuess == wordList[i]:
            curList[i] = letterGuess
    cur = ''.join(curList)
    return cur 


# def debug(currentTemplate, letterGuess, wordList):
#     f = handleUserInputDebugMode()
#     g = getNewWordList(currentTemplate, letterGuess, wordList)
#     if f == True:
#         t = dict()
#         wordTemp = []
#         for i in wordList:
#             for i in wordList:
#                 wordL = list(i)
#                 p = []
#                 for n in wordL:
#                     if n == letterGuess:
#                         p.append(n)
#                     else:
#                         p.append('_')
#                 ' so now i have a list of characters that fit a template in word'
#                 if p not in wordTemp:
#                     f = ''.join(p)
#                     wordTemp.append(p)
#                     e = ''.join(wordL)
#                     t[f] = [e]
#                 else:
#                     f = ''.join(p)
#                     e = ''.join(wordL)
#                     t[f] += [e]
#         keylen = 0
#         for key in t:
#             print(key + ' : ' + str(len(t[key]))) + '\n'
#             keylen += 1
#         print("# keys = " + str(keylen))
DEBUG = False 
def getNewWordList(currentTemplate, letterGuess, wordList):
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

if __name__ == '__main__':
    print(getNewWordList('_O__', 'O', [ "OBOE", "NOON", "ODOR", "ROOM", "SOLO", "TRIO", "GOTO", "OATH", "OXEN", "PICK", "FRAT", "HOOP"]))
