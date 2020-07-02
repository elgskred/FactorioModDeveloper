# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 18:56:37 2020

@author: chris
"""
from tkinter import *
from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E, Frame, Text, filedialog
import os.path
import json

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
        
    if config['baseFolder'] == 'tempPath':
        config['baseFolder'] = checkForFactiorioFolder()
        
    
    return(config)


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
        self.modFrame(self.master)
        self.configFrame(self.master)
        
        self.changeFrame('base')

        
    def navigationPanel(self, master):
        #Create the navigationPanel
        self.navigationFrame = Frame(master, width=125, height=500, bg="blue", highlightbackground="black", highlightthickness=2)
        
        self.baseButton = Button(self.navigationFrame, text="Base", width=15, command=lambda: self.changeFrame('base')) .grid(row=0, column=0, sticky=W)    
        
        #Create Base mod buttons
        self.baseItemsButton = Button(self.navigationFrame, text="Items", width=15, command=lambda: self.changeFrame(''))
        self.baseItemsButton.grid(row=1, column=0, sticky=W, padx=10)
        self.baseRecipesButton = Button(self.navigationFrame, text="Recipes", width=15, command=lambda: self.changeFrame(2))
        self.baseRecipesButton.grid(row=2, column=0, sticky=W, padx=10)
        self.baseTechsButton = Button(self.navigationFrame, text="Technologies", width=15, command=lambda: self.changeFrame(3))
        self.baseTechsButton.grid(row=3, column=0, sticky=W, padx=10)
        
        
        
        self.modButton = Button(self.navigationFrame, text="Mod", width=15, command=lambda: self.changeFrame('mod')) .grid(row=4, column=0, sticky=W)    
        
        #Create Mod buttons
        self.modItemsButton = Button(self.navigationFrame, text="Items", width=15, command=lambda: self.changeFrame(5))
        self.modItemsButton.grid(row=5, column=0, sticky=W, padx=10)
        self.modRecipesButton = Button(self.navigationFrame, text="Recipes", width=15, command=lambda: self.changeFrame(6))
        self.modRecipesButton.grid(row=6, column=0, sticky=W, padx=10)
        self.modTechsButton = Button(self.navigationFrame, text="Technologies", width=15, command=lambda: self.changeFrame(7))
        self.modTechsButton.grid(row=7, column=0, sticky=W, padx=10)
        
        #Create config button
        self.configButton = Button(self.navigationFrame, text="Config", width=15, command=lambda: self.changeFrame('config'))
        self.configButton.grid(column=0, sticky=W)

        self.navigationFrame.grid(row=0, column=0 ,sticky=W)
        self.navigationFrame.grid_propagate(0)
        
        self.hideBaseButtons()
        self.hideModButtons()


    def add(self, master):
        self.add_button = Button(master, text="+12e", command=lambda: self.update("add"))
        self.add_button.grid(row=2, column=0)
        self.frame = Frame(master, width=100, height=100, bg="red")


    def hideBaseButtons(self):
        self.baseItemsButton.grid_forget()
        self.baseRecipesButton.grid_forget()
        self.baseTechsButton.grid_forget()

    def hideModButtons(self):
        self.modItemsButton.grid_forget()
        self.modRecipesButton.grid_forget()
        self.modTechsButton.grid_forget()
        
    
    def baseFrame(self, master):
        global frames
        #Base Frame
        self.baseFrame = Frame(master, width=675, height=500, bg='red')
        frames['base'] = self.baseFrame

        self.baseFrame.grid(row=0, column=1, sticky=W)
        self.baseFrame.grid_propagate(0)
        
        
    def modFrame(self, master):
        global frames
        #Mod Frame
        self.modFrame = Frame(master, width=675, height=500, bg='green')
        frames['mod'] = self.modFrame
        
        self.modFrame.grid(row=0, column=1, sticky=W)
        self.modFrame.grid_propagate(0)



    def configFrame(self, master):
        global frames
        global config
        #Config Frame
        self.configFrame = Frame(master, width=675, height=500, bg="yellow")
        frames['config'] = self.configFrame
        
        self.configFrame.grid(row=0, column=1, sticky=W)
        self.configFrame.grid_propagate(0)
        
        self.configFactorioFolderLabel = Label(self.configFrame, text='Factorio installation folder:')
        self.configFactorioFolderLabel.grid(row=0, column=0, sticky=W)
        
        self.configFactorioFolderTextbox = Text(self.configFrame, width=60, height=1) 
        self.configFactorioFolderTextbox.grid(row=1, column=0, sticky=W)
        print(config)
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
        
        
        
        
#        if state == 0:
#            showBaseButtons()
#        
#        if state ==4:
#            showModButtons()
        
config = startUp()
frames = {}
  
window = Tk()
my_gui = FactorioModTool(window)
window.mainloop()






#class Calculator:
#
#    def __init__(self, master):
#        self.master = master
#        master.title("Calculator")
#
#        self.total = 0
#        self.entered_number = 0
#
#        self.total_label_text = IntVar()
#        self.total_label_text.set(self.total)
#        self.total_label = Label(master, textvariable=self.total_label_text)
#
#        self.label = Label(master, text="Total:")
#
#        vcmd = master.register(self.validate) # we have to wrap the command
#        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
#
#        self.add_button = Button(master, text="+", command=lambda: self.update("add"))
#        self.subtract_button = Button(master, text="-", command=lambda: self.update("subtract"))
#        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))
#
#        # LAYOUT
#
#        self.label.grid(row=0, column=0, sticky=W)
#        self.total_label.grid(row=0, column=1, columnspan=2, sticky=E)
#
#        self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)
#
#        self.add_button.grid(row=2, column=0)
#        self.subtract_button.grid(row=2, column=1)
#        self.reset_button.grid(row=2, column=2, sticky=W+E)
#
#    def validate(self, new_text):
#        if not new_text: # the field is being cleared
#            self.entered_number = 0
#            return True
#
#        try:
#            self.entered_number = int(new_text)
#            return True
#        except ValueError:
#            return False
#
#    def update(self, method):
#        if method == "add":
#            self.total += self.entered_number
#        elif method == "subtract":
#            self.total -= self.entered_number
#        else: # reset
#            self.total = 0
#
#        self.total_label_text.set(self.total)
#        self.entry.delete(0, END)
#
#root = Tk()
#my_gui = Calculator(root)
#root.mainloop()

