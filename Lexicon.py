from tkinter import filedialog
from tkinter import ttk
from tkinter import*
import re


#Setting up GUI and the Gui table
root = Tk()
root.geometry('750x500')
tree = ttk.Treeview(root)

#Loads file using dialog boxes
def load():
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("txt files", "*.txt"),("cpp files","*.cpp"),("all files","*.*")))
    loadFile = open(root.filename, "r")
    #finds out how much lines is in the file
    count = len(loadFile.readlines(  ))
    #creates an array of empty list based on the amount of lines in the files
    lst = [[] for i in range(0, count)]
    lineNum = 0
    lineChrIndx = 0
    lineStr = ""
    identStr= ""
    operStr=""
    prev=""
    loadFile = open(root.filename, "r")
    while 1:
        # read character by character
        char = loadFile.read(1)
        #base case
        if not char:
            break
        #if statments directing program how to group together characters
        if(char != "\n" ):
            lineStr+=char
        if(char.isalpha() == False and prev.isalpha() == True ):
            identStr += " "
        if(char.isalpha() == True):
            identStr+=char
        if(char.isdigit() and prev != '/'):
            identStr+=char
        if(char.isdigit() and prev == '/'):
            identStr+=prev
            identStr+=char
            identStr += " "
        if(detect_special_character(char) == True and char != "/"):
           operStr +=char
           operStr +=" "
         #when char pointer reach the end of the line it appends elements to a list within a list
        if(char == "\n" ):
            lst[lineNum].append(lineStr)
            lst[lineNum].append(operStr)
            lst[lineNum].append(identStr)
            lineStr = ""
            identStr = ""
            operStr = ""
            lineNum += 1
        prev=char

    #populates gui table
    count2 = 0
    for stuff in lst:
       tree.insert(parent='',index='end', iid=count2, text="", values=(stuff[0], stuff[1], stuff[2]))
       count2 += 1

#define colums
tree['columns'] = ('Original String', 'Operator', 'Identifier')

#format colums
tree.column("#0", width=0, minwidth=25)
tree.column("Original String", anchor=W, width=220)
tree.column('Operator', anchor=CENTER, width=160)
tree.column('Identifier',anchor=W, width=220)

#create heading
tree.heading("#0",text="", anchor=W)
tree.heading("Original String",text="Original String", anchor=W)
tree.heading('Operator', text='Operator', anchor=CENTER)
tree.heading('Identifier',text='Identifier',anchor=W)


#The thing that actauly pins the gui table to the initial gui window
tree.pack(pady=20)

#function i made to test buttons
def hello():
    print("hello!")
#function to return true or false base if it detects specail characters
def detect_special_character(pass_string):
  regex= re.compile('[@_!#$%^&*()<>?/\|}{~:+=-]')
  if(regex.search(pass_string) == None):
    res = False
  else:
    res = True
  return(res)
#same as above but one just for math expressions, ended up not using
def detect_math_character(pass_string):
    regex= re.compile('[+=-*/()!]')
    if(regex.search(pass_string) == None):
        res = False
    else:
        res = True
    return(res)

#pins menu bar to main window gui
menubar = Menu(root)

# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=load)
filemenu.add_command(label="Save", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# create more pulldown menus
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=hello)
editmenu.add_command(label="Copy", command=hello)
editmenu.add_command(label="Paste", command=hello)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=hello)
menubar.add_cascade(label="Help", menu=helpmenu)

# display the menu
root.config(menu=menubar)

#loops the gui window
root.mainloop()
