# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 18:38:05 2020

@author: chris
"""

from tkinter import filedialog
from tkinter import *
import os.path
import json

steamFolder = 'C:\Program Files (x86)\Steam\steamapps\common\Factorio'
baseFolder = ''
setConfigStartscreen = False

def startUp():
    #Checks config file for Factorio base folder and users mod folder
    file_name = 'config.json'
    try:
        file = open(file_name, 'r')
        #config = file.read()
        config = json.load(file)
        file.close()
    except IOError:
        file = open(file_name, 'w')
        config = {}
        config['modFolder'] = 'tempPath'
        config['baseFolder'] = 'tempPath'
        config['steamFolder'] = 'C:\Program Files (x86)\Steam\steamapps\common\Factorio'
        file.write(json.dumps(config))
        file.close()
    
    return(config)

def browse():
    folder_selected = filedialog.askdirectory()
    output.delete(0.0, END)
    output.insert(END, folder_selected)


def checkForFactiorioFolder():
    os.path.isfile(fname) 
    if os.path.exists(steamFolder):
        baseFolder = 'C:\Program Files (x86)\Steam\steamapps\common\Factorio\data\base\prototypes'
    else:
        #Factorio is not installed in standard steam folder, user needs to specify correct folder.
        setConfigStartscreen = True
        

def hide(state):

    if state == 0:
        showBaseButtons()
        
    if state ==4:
        showModButtons()
    
    currentFrame[0].grid_forget()
    frames[state].grid(row=0, column=1 ,sticky=W)
    frames[state].grid_propagate(0)
    currentFrame[0] = frames[state]
    
def showBaseButtons():
    baseItemsButton.grid(row=1, column=0, sticky=W, padx=10)
    baseRecipesButton.grid(row=2, column=0, sticky=W, padx=10)
    baseTechsButton.grid(row=3, column=0, sticky=W, padx=10)
    
def showModButtons():
    modItemsButton.grid(row=5, column=0, sticky=W, padx=10)
    modRecipesButton.grid(row=6, column=0, sticky=W, padx=10)
    modTechsButton.grid(row=7, column=0, sticky=W, padx=10)

frames = []
currentFrame = []


window = Tk()
window.title("Testing")    
window.geometry('{}x{}'.format(460, 500))


#Setting up the frames

#Navigation panel
navigationFrame = Frame(window, width=115, height=450, bg="blue")

#Base Frame
baseFrame = Frame(window, width=345, height=450, bg="cyan")
frames.append(baseFrame) #0

#Base Items Frame
baseItemsFrame = Frame(window, width=345, height=450, bg="magenta")
frames.append(baseItemsFrame) #1

#Base Recipes Frame
baseRecipesFrame = Frame(window, width=345, height=450, bg="chartreuse4")
frames.append(baseRecipesFrame) #2

#Base Technologies Frame
baseTechsFrame = Frame(window, width=345, height=450, bg="pink")
frames.append(baseTechsFrame) #3

#Mod Frame
modFrame = Frame(window, width=345, height=450, bg="grey")
frames.append(modFrame) #4

#Mod Items Frame
modItemsFrame = Frame(window, width=345, height=450, bg="brown")
frames.append(modItemsFrame) #5

#Mod Recipes Frame
modRecipesFrame = Frame(window, width=345, height=450, bg="snow")
frames.append(modRecipesFrame) #6

#Mod Technologies Frame
modTechsFrame = Frame(window, width=345, height=450, bg="RosyBrown4")
frames.append(modTechsFrame) #7



mainFrame = Frame(window, width=345, height=450, bg="red")
frames.append(mainFrame) #8
testFrame = Frame(window, width=345, height=450, bg="green")
frames.append(testFrame) #9

#Config Frame
configFrame = Frame(window, width=345, height=450, bg="yellow")
frames.append(configFrame) #10

currentFrame.append(mainFrame)


#Set up navigationFrame contents
    
baseButton = Button(navigationFrame, text="Base", width=15, command=lambda: hide(0)) .grid(row=0, column=0, sticky=W)    

#Create Base mod buttons
baseItemsButton = Button(navigationFrame, text="Items", width=15, command=lambda: hide(1))
baseItemsButton.grid(row=1, column=0, sticky=W, padx=10)
baseRecipesButton = Button(navigationFrame, text="Recipes", width=15, command=lambda: hide(2))
baseRecipesButton.grid(row=2, column=0, sticky=W, padx=10)
baseTechsButton = Button(navigationFrame, text="Technologies", width=15, command=lambda: hide(3))
baseTechsButton.grid(row=3, column=0, sticky=W, padx=10)



modButton = Button(navigationFrame, text="Mod", width=15, command=lambda: hide(4)) .grid(row=4, column=0, sticky=W)    

#Create Mod buttons
modItemsButton = Button(navigationFrame, text="Items", width=15, command=lambda: hide(5))
modItemsButton.grid(row=5, column=0, sticky=W, padx=10)
modRecipesButton = Button(navigationFrame, text="Recipes", width=15, command=lambda: hide(6))
modRecipesButton.grid(row=6, column=0, sticky=W, padx=10)
modTechsButton = Button(navigationFrame, text="Technologies", width=15, command=lambda: hide(7))
modTechsButton.grid(row=7, column=0, sticky=W, padx=10)





#Create config button
configButton = Button(navigationFrame, text="Config", width=15, command=lambda: hide(10))
configButton.grid(column=0, sticky=W)

#Set up mainFrame contents
Button(mainFrame, text="Browse", width=8, command=browse) .grid(row=0, column=0, sticky=W)  
output = Text(mainFrame, width=15, height=2, background="grey")
Button(mainFrame, text="Hide Frame", width=8, command=lambda: hide(1)) .grid(row=3, column=0, sticky=W) 
output.grid(row=1, column=0, sticky=W)    
output.insert(END, "Testing")


#Set up testFrame contents
Button(testFrame, text="Hide Frame", width=15, command=lambda: hide(0)) .grid(row=0, column=0, sticky=W) 
Label(testFrame, text="Hopla", width=15) .grid(row=1, column= 0, sticky=W)


#Set up configFrame contents




# layout all of the main containers
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(1, weight=1)



navigationFrame.grid(row=0, column=0 ,sticky=W)
navigationFrame.grid_propagate(0)

mainFrame.grid(row=0, column=1 ,sticky=W)
mainFrame.grid_propagate(0)

testFrame.grid(row=0, column=1 ,sticky=W)
testFrame.grid_propagate(0)
testFrame.grid_forget()

configFrame.grid(row=0, column=1, sticky=W)
configFrame.grid_propagate(0)







config = startUp()

if config['modFolder'] == 'tempPath' or config['baseFolder'] == 'tempPath':
    setConfigStartscreen = True

if config['modFolder'] == 'tempPath':
    modItemsButton.grid_forget()
    modRecipesButton.grid_forget()
    modTechsButton.grid_forget()
    
if config['baseFolder'] == 'tempPath':
    baseItemsButton.grid_forget()
    baseRecipesButton.grid_forget()
    baseTechsButton.grid_forget()


if setConfigStartscreen:
    mainFrame.grid_forget()
    currentFrame[0] = configFrame
    
else:
    configFrame.grid_forget()
    currentFrame[0] = mainFrame

window.mainloop()

