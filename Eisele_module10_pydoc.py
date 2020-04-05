'''
__author__ = "Brandon Eisele <BEISELE98@live.seminolestate.edu>"
__date__ = 5 April 2020
'''

#Imports
import re
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename

fullString = ""

def info():
    '''
    Returns list if author and file information
    @return list Info_list
    '''
    Author = "Brandon Eisele"
    Date_Created = "4/5/2020"
    Program_Name = "Eisele_module10_pydoc"
    Purpose = "Add unit testing to word count application"
    Info_List = [Author, Date_Created, Program_Name, Purpose]

    return Info_List

def fullStringToList():
    '''
    Returns list format of string, segmented based on newlines
    @return list wordList
    '''
    wordList = fullString.split('\n')
    return wordList

def returnWordCount():
    '''
    Returns number of items in word list
    @return int list_len
    '''
    list = fullStringToList()
    list_len = len(list)
    return list_len

#Create tkinter root windows and set minimum size to display window name
root = Tk()
root.minsize(300,0)

#open file from tkinter window and use previously written word counter on contents. Display output in tkinter window
def OpenFile():
    '''
    Function for UI 'open file' element for word count program. Once file has been opened,
    html characters are stripped out of the file and all words are set to lower case.
    All words are counted, and the top 20 are created as a label and pushed to the UI.
    @return UI label to root window
    '''
    fileToRead = askopenfilename(initialdir="D:/School/CurrentClasses/CEN3024/Module 10+8 Assignment/", filetypes =(("HTML File", "*.html"),("All Files","*.*")), title = "Choose a file.")
    wordCount = {}
    global fullString

    with open (fileToRead) as file:
        for line in file:
            line = re.sub("<[^>]+>", "", line)
            splitline = line.split(' ')
            for item in splitline:
                item = item.replace("--", " ")
                item = re.sub("[^a-z-A-Z]", "", item)
                item = item.lower()
                if item != "":
                    if item in wordCount:
                        wordCount[item] = wordCount[item] + 1
                    else:
                        wordCount[item] = 1

    sorted_wordCount = sorted(wordCount.items(), key =
                 lambda kv:(kv[1], kv[0]), reverse=True)

    count = 1
    fullString = ""
    for item in sorted_wordCount:
        if count < 20:
            fullString = fullString + str(count) + ": " + str(item) + '\n'
        elif count == 20:
            fullString = fullString + str(count) + ": " + str(item)
        else:
            break
        count = count + 1

    global label
    label.destroy()
    fileName = fileToRead.split('/')
    fileName = fileName[len(fileName)-1]
    label = ttk.Label(root, text="Top 20 Words For: " + fileName + '\n' + fullString,foreground="black",font=("Times New Roman", 16))
    label.pack()

#Create initial tkinter window with basic open and exit functions
Title = root.title("Find Top 20")
label = ttk.Label(root, text="Choose a File to Display The Top 20 Words",foreground="black",font=("Times New Roman", 24))
label.pack()
menu = Menu(root)
root.config(menu=menu)
file = Menu(menu)
file.add_command(label = 'Open', command = OpenFile)
file.add_command(label = 'Exit', command = lambda:exit())
file.add_command(label = 'Word Count', command = returnWordCount())
menu.add_cascade(label = 'File', menu = file)
root.mainloop()
