# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 19:31:21 2020

@author: Christoffer
"""

import os
import json

def remove(listobj):
    cnt = 0
    objectList = []
    for elements in listobj:
        if elements == "  {\n":
            objectList.append(cnt)
        if elements == "  },\n" or elements == "  }\n":
            objectList.append(cnt)
        cnt = cnt + 1
    return(objectList)

def replace(listobj):
    #listobj = [element.replace('=', ':') for element in listobj]
    listobj = [element.strip() for element in listobj]

    return(listobj)

def dictify(listobj):
    newDict = {}
    lastKey = ''
    concValue = ''
    closingBracket = True
    cnt = 0
    cnt2 = 0
    tmpArray = []
    tmpDict = {}
    separator = 0
#    for elements in listobj:
#        #print(elements)
#        if elements.find('=') > 0 and closingBracket == True:
#            #print("1")
#            separator = elements.find('=')
#            key = elements[0:separator]
#            value = elements[separator+1:len(elements)]
#            newDict[key] = value
#            lastKey = key
#            concValue = ''
#            cnt = 0
#        elif elements.find('{') >= 0 and cnt2 > 0:
#            #print('2')
#            closingBracket = False
#            cnt = cnt + 1
#            concValue = concValue + elements + '\n'
#        elif elements.find('}') >= 0:
#            #print('3')
#            cnt = cnt -1
#            if cnt == 0:
#                closingBracket = True
#            concValue = concValue + elements + '\n'
#            #print(concValue)
#            #print(lastKey)
#            newDict[lastKey] = concValue
#        else:
#            #print("4")
#            concValue = concValue + elements + '\n'
#            #print(concValue)
#        cnt2 = cnt2 + 1
    

    for x in range(len(listobj)):
        if x > 0:
            #Checks if the value is another table
            if listobj[x] == '{':
                print('trigg')
                print(x)
                tmpArray = []
                tmpDict = {}
                closingBracket = False
                
                for y in range(x +1, len(listobj)):
                    if listobj[y] == '}' or listobj[y] == '},':
                        print('break: ' + str(y))
                        print(listobj[y])
                        break
                    else:
                        #print('append: ' + str(y))
                        #print(listobj[y])
                        tmpArray.append(listobj[y])
                print(tmpArray)
                #newDict[lastKey] = dictify(tmpArray)
                closingBracket = True
                continue
            #Checks if the line is a "normal" key/value pair, no nested tables
            elif listobj[x].find('=') > 0 and not (listobj[x].find('{') >= 0 and listobj[x].find('=') >= 0 and listobj[x].find('}') >= 0):
                separator = listobj[x].find('=')
                key = listobj[x][0:separator]
                value = listobj[x][separator+1:len(listobj[x])]
                newDict[key] = value
                lastKey = key
                concValue = ''
                cnt = 0
            #Checks if the line is a nested table
            elif listobj[x].find('{') >= 0 and listobj[x].find('=') >= 0 and listobj[x].find('}') >= 0:
                #{ size = 64, filename = "__base__/graphics/icons/mip/coal.png",   scale = 0.25, mipmap_count = 4 },
                #['{ size = 64', ' filename = "__base__/graphics/icons/mip/coal-1.png"', ' scale = 0.25', ' mipmap_count = 4 }', '']
                #print('test3')
                #newDict = {}
                tmpArray = []
                tmpArray = listobj[x].split(',')
                tmpArray = [element.replace('{', '') for element in listobj]
                tmpArray = [element.replace('}', '') for element in listobj]
                #newDict[lastKey] = dictify(tmpArray)
                
                #print(tmpArray)
                separator = listobj[x].find('=')
                key = listobj[x][0:separator]
                value = listobj[x][separator+1:len(listobj[x])]

        elif listobj[x].find('=') > 0 and not (listobj[x].find('{') >= 0 and listobj[x].find('=') >= 0 and listobj[x].find('}') >= 0):
            print('trigg???')
            separator = listobj[x].find('=')
            key = listobj[x][0:separator]
            value = listobj[x][separator+1:len(listobj[x])]
            newDict[key] = value
            lastKey = key
            concValue = ''
            cnt = 0
        elif (listobj[x].find('{') >= 0 and listobj[x].find('=') >= 0 and listobj[x].find('}') >= 0):
            print('test')
    return(newDict)    


def removeExtend(listobj):
    if listobj[0] == 'data:extend(\n':
        listLen = len(listobj)
        listobj.pop(listLen-1)
        listobj.pop(listLen-2)
        listobj.pop(0)
        listobj.pop(0)
        
    return(listobj)
    
def writeDictToLuaFile(listobj):
    file_name = r"C:\Users\Christoffer\Documents\test2.lua"
    file = open(file_name, 'w') 
    
    file.write('data:extend(\n')
    file.write('{\n')
    
    listLen = len(listobj)
    
    for x in range(listLen):
        file.write('  {\n')
        for key, value in listobj[x].items():
            #print(value)
            file.write('    ' + key + '=' + value + '\n')
        if x >= (listLen-1):
            file.write('  }\n')
        else:
            file.write('  },\n')
    file.write('}\n')
    file.write(')')

    

path = r"C:\Users\Christoffer\Documents"
path = path + r"\demo-turret.lua"

file = open(path, 'r')
fileLines = file.readlines()
file.close()

fileLen = len(fileLines)

newFile = removeExtend(fileLines)
listOfIndexes = remove(newFile)
newFile = replace(newFile)
elements = len(listOfIndexes) / 2

itemList = []
for i in range(int(elements)):
    itemList.append(dictify(newFile[listOfIndexes[(i*2)]:listOfIndexes[(i*2)+1]+1]))


newlist = newFile[listOfIndexes[0]:listOfIndexes[1]+1]
#newDict = dictify(newlist)
#writeDictToLuaFile(itemList)




#file_name = r"C:\Users\Christoffer\Documents\test2.lua"
#file = open(file_name, 'w') 
#
#for line in fileLines:
#    file.write(line)
#
#
#file.close()




    
    
