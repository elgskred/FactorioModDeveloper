# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 18:56:37 2020

@author: chris
"""
import tkinter
from tkinter import *
from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E, Frame, Text, filedialog, Checkbutton
import os
import json

def startUp():
    #Checks config file for Factorio base folder and users mod folder
    file_name = 'config.json'
    try:
        file = open(file_name, 'r')
        #config = file.read()
        config = json.load(file)
        print(file)
        file.close()
    except IOError:
        file = open(file_name, 'w')
        config = {}
        config['modFolder'] = 'tempPath'
        config['baseFolder'] = 'tempPath'
        config['steamFolder'] = 'C:\Program Files (x86)\Steam\steamapps\common\Factorio'
        file.write(json.dumps(config))
        file.close()
        
    if config['baseFolder'] == 'tempPath':
        config['baseFolder'] = checkForFactiorioFolder()
        
    
    return(config)

def updateConfig():
    global config
    file_name = 'config.json'
    file = open(file_name, 'w')
    file.write(json.dumps(config))
    file.close()


def checkForFactiorioFolder():
    steamFolder = 'C:\Program Files (x86)\Steam\steamapps\common\Factorio'
    if os.path.exists(steamFolder):
        baseFolder = 'C:\Program Files (x86)\Steam\steamapps\common\Factorio'
    else:
        #Factorio is not installed in standard steam folder, user needs to specify correct folder.
        baseFolder = 'tempPath'
    return(baseFolder)



class FactorioModTool:
    def __init__(self, master):
        self.master = master
        master.title('Factorio ModTool')
        master.geometry('{}x{}'.format(800, 500))
        
        global frames
        
        
        self.navigationPanel(self.master)
        self.baseFrame(self.master)
        self.baseItemsFrame(self.master)
        
        self.modFrame(self.master)
        self.configFrame(self.master)
        
        self.changeFrame('base')

        
    def navigationPanel(self, master):
        #Create the navigationPanel
        self.navigationFrame = Frame(master, width=120, height=500, bg="blue", highlightbackground="black", highlightthickness=2)
        
        self.baseButton = Button(self.navigationFrame, text="Base", width=12, command=lambda: self.changeFrame('base')) .grid(row=0, column=0, sticky=W)    
        
        #Create Base mod buttons
        self.baseItemsButton = Button(self.navigationFrame, text="Items", width=12, command=lambda: self.changeFrame('baseItems'))
        self.baseItemsButton.grid(row=1, column=0, sticky=W, padx=10)
        self.baseRecipesButton = Button(self.navigationFrame, text="Recipes", width=12, command=lambda: self.changeFrame(2))
        self.baseRecipesButton.grid(row=2, column=0, sticky=W, padx=10)
        self.baseTechsButton = Button(self.navigationFrame, text="Technologies", width=12, command=lambda: self.changeFrame(3))
        self.baseTechsButton.grid(row=3, column=0, sticky=W, padx=10)
        
        
        
        self.modButton = Button(self.navigationFrame, text="Mod", width=12, command=lambda: self.changeFrame('mod')) .grid(row=4, column=0, sticky=W)    
        
        #Create Mod buttons
        self.modItemsButton = Button(self.navigationFrame, text="Items", width=12, command=lambda: self.changeFrame(5))
        self.modItemsButton.grid(row=5, column=0, sticky=W, padx=10)
        self.modRecipesButton = Button(self.navigationFrame, text="Recipes", width=12, command=lambda: self.changeFrame(6))
        self.modRecipesButton.grid(row=6, column=0, sticky=W, padx=10)
        self.modTechsButton = Button(self.navigationFrame, text="Technologies", width=12, command=lambda: self.changeFrame(7))
        self.modTechsButton.grid(row=7, column=0, sticky=W, padx=10)
        
        #Create config button
        self.configButton = Button(self.navigationFrame, text="Config", width=12, command=lambda: self.changeFrame('config'))
        self.configButton.grid(column=0, sticky=W)

        self.navigationFrame.grid(row=0, column=0 ,sticky=NW)
        self.navigationFrame.grid_propagate(0)
        
        if config['baseFolder'] != 'tempPath':
            self.showBaseButtons()
        else:
            self.hideBaseButtons()
            
        if config['modFolder'] != 'tempPath':
            self.showModButtons()
        else:
            self.hideModButtons()

    def hideBaseButtons(self):
        self.baseItemsButton.grid_forget()
        self.baseRecipesButton.grid_forget()
        self.baseTechsButton.grid_forget()

    def hideModButtons(self):
        self.modItemsButton.grid_forget()
        self.modRecipesButton.grid_forget()
        self.modTechsButton.grid_forget()
        
    def showBaseButtons(self):
        self.baseItemsButton.grid(row=1, column=0, sticky=W, padx=10)
        self.baseRecipesButton.grid(row=2, column=0, sticky=W, padx=10)
        self.baseTechsButton.grid(row=3, column=0, sticky=W, padx=10)
    
    def showModButtons(self):
        self.modItemsButton.grid(row=5, column=0, sticky=W, padx=10)
        self.modRecipesButton.grid(row=6, column=0, sticky=W, padx=10)
        self.modTechsButton.grid(row=7, column=0, sticky=W, padx=10)
        
    
    def baseFrame(self, master):
        global frames
        global config
        #Base Frame
        self.baseFrame = Frame(master, width=700, height=700, bg='red')
        frames['base'] = self.baseFrame

        self.baseFrame.grid(row=0, column=1, sticky=W)
        self.baseFrame.grid_propagate(0)
        
        #List the files for each category, items/recipes/techs
        
        #Create a frame for each list
        #Item
        self.itemsFrame = Frame(self.baseFrame, highlightbackground="black", highlightthickness=2)
        self.itemsFrame.grid(row=0, column=0, sticky=W, padx=10, pady=5)
        if config['baseFolder'] != 'tempPath':
            path = config['baseFolder'] + r"\data\base\prototypes\item"
            items = os.listdir(path)

        self.itemsLabel = Label(self.itemsFrame, text='Items:')
        self.itemsLabel.grid(row=0, column=0, sticky=W)
        self.itemsChecklist = ChecklistBox(self.itemsFrame, items, bd=1, relief="sunken", background="white")
        self.itemsChecklist.grid(row=1, column=0, sticky=W)
        
        #Recipe
        self.recipesFrame = Frame(self.baseFrame, highlightbackground="black", highlightthickness=2)
        self.recipesFrame.grid(row=0, column=1, sticky=NW, padx=10, pady=5)
        if config['baseFolder'] != 'tempPath':
            path = config['baseFolder'] + r"\data\base\prototypes\recipe"
            recipes = os.listdir(path)

        self.recipesLabel = Label(self.recipesFrame, text='Recipes:')
        self.recipesLabel.grid(row=0, column=0, sticky=NW)
        self.recipesChecklist = ChecklistBox(self.recipesFrame, recipes, bd=1, relief="sunken", background="white")
        self.recipesChecklist.grid(row=1, column=0, sticky=NW)
        
        #Techs
        self.techsFrame = Frame(self.baseFrame, highlightbackground="black", highlightthickness=2)
        self.techsFrame.grid(row=0, column=2, sticky=NW, padx=10, pady=5)
        if config['baseFolder'] != 'tempPath':
            path = config['baseFolder'] + r"\data\base\prototypes\technology"
            techs = os.listdir(path)

        self.techsLabel = Label(self.techsFrame, text='Technologies:')
        self.techsLabel.grid(row=0, column=0, sticky=NW)
        self.techsChecklist = ChecklistBox(self.techsFrame, techs, bd=1, relief="sunken", background="white")
        self.techsChecklist.grid(row=1, column=0, sticky=NW)
        
        
        
        
        
    def baseItemsFrame(self, master):
        global frames
        global config
        
        self.baseItemsFrame = Frame(master, width=700, height=500, bg='pink')
        frames['baseItems'] = self.baseItemsFrame
        
        self.baseItemsFrame.grid(row=0, column=1, sticky=W)
        self.baseItemsFrame.grid_propagate(0)
        
        
        #path = config['baseFolder'] + r"\data\base\prototypes\item"
        path = r"C:\Users\Christoffer\Documents"
        path = path + r"\demo-turret.lua"
        file = open(path, 'r')
        #ff = file.read()
        ff = json.load(file)
        print(ff)
        file.close()
        
        
    def modFrame(self, master):
        global frames
        #Mod Frame
        self.modFrame = Frame(master, width=700, height=500, bg='green')
        frames['mod'] = self.modFrame
        
        self.modFrame.grid(row=0, column=1, sticky=W)
        self.modFrame.grid_propagate(0)



    def configFrame(self, master):
        global frames
        global config
        #Config Frame
        self.configFrame = Frame(master, width=700, height=500, bg="yellow")
        frames['config'] = self.configFrame
        
        self.configFrame.grid(row=0, column=1, sticky=W)
        self.configFrame.grid_propagate(0)
        
        self.configFactorioFolderLabel = Label(self.configFrame, text='Factorio installation folder:')
        self.configFactorioFolderLabel.grid(row=0, column=0, sticky=W)
        
        self.configFactorioFolderTextbox = Text(self.configFrame, width=60, height=1) 
        self.configFactorioFolderTextbox.grid(row=1, column=0, sticky=W)
        if config['baseFolder'] != 'tempPath':
            self.configFactorioFolderTextbox.insert(END, config['baseFolder'])
        
        self.configFactorioFolderBrowse = Button(self.configFrame, text='Browse', command=lambda: self.browseForFolder(self.configFactorioFolderTextbox))
        self.configFactorioFolderBrowse.grid(row=1, column=1, sticky=W, padx=2)
        
    def browseForFolder(self, outputBox):
        folder_selected = filedialog.askdirectory()
        outputBox.delete(0.0, END)
        outputBox.insert(END, folder_selected)
        
        
    def changeFrame(self, fname):
        global frames
        for i in frames:
            if i == fname:
                frames[i].grid(row=0, column=1, sticky=W)
                frames[i].grid_propagate(0)
            else:
                frames[i].grid_forget()
                
        if fname == 'base':
            #List relevant files
            print('tbd')


class ChecklistBox(tkinter.Frame):
    def __init__(self, parent, choices, **kwargs):
        tkinter.Frame.__init__(self, parent, **kwargs)

        self.vars = []
        bg = self.cget("background")
        for choice in choices:
            var = tkinter.StringVar(value=choice)
            self.vars.append(var)
            cb = tkinter.Checkbutton(self, var=var, text=choice,
                                onvalue=choice, offvalue="",
                                anchor="w", width=20, background=bg,
                                relief="flat", highlightthickness=0,
                                command=lambda: self.updateCheckedItems()
            )
            cb.pack(side="top", fill="x", anchor="w")
            
    def setCheckedItems(self):
        print('setChecked')

    def getCheckedItems(self):
        values = []
        for var in self.vars:
            value =  var.get()
            if value:
                values.append(value)
        return values
    
    def updateCheckedItems(self):
        global config
        values = []
        for var in self.vars:
            value = var.get()
            if value:
                values.append(value)
        config['baseFiles'] = values
        updateConfig()
            
    

       
config = startUp()
frames = {}
  
window = Tk()
my_gui = FactorioModTool(window)
window.mainloop()


