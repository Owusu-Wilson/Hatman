# Date: Wednesday,July 29,2020
# Author: Owusu Wilson
# Company: Sparrow Labs Inc.
# Type: Console App
# Inspired by Kate Text Editor in Linux
# Has Extended features for python files
#       =====
#      =     =               THE 
#   ===== =  = ====          HATMAN 
#    =  .   .  =             NOTEBOOK 
#    =         =             WRITER 
#     =  __  =
#       ====
#
from datetime import datetime
import os
from inspect import *
#Some Nice Heading
print(" |       =====        |   =      =    ====  =======  =====       =====   ")
print(" |     =       =      |   ==     =   =    =    =     =           =    =  ")
print(" |  ===== =  = ====   |   =  =   =   =    =    =     =           =   =   ")
print(" |    = .    .  =     |   =    = =   =    =    =     =====       = ==    ")
print(" |    =         =     |   =      =   =    =    =     =           =   =   ")
print(" |     =  __  =       |   =      =   =    =    =     =           =    =  ")
print(" |       ====         |   =      =    ====     =     =====  *    =====   ")
#====================================================================================
print("\n\nWelcome to the interactive note writer.\nGives you quick creation and writing of files with text format.\nEnjoy !!!")
#===============================================
#   ||||||    Some Useful Functions       ||||||
#===============================================
def opener():
    '''Asks the user to open the saved file or to just terminate the console'''
    open_preference=input(f"Will you like to open the .{extension} file [{note_name}] now?\n\t\ty/n => Yes/No\n")
    comm=''
    if open_preference=='y':
        if extension=='py':
            comm=f"cmd/k code \"{note_name}\" "
        else:
            regards()
            comm=f"cmd /k start {note_name}"
        os.system(comm)
        
    elif open_preference =='n':
        print("Saved successfully")
    else:
        print("Please enter a correct option.")
        opener()
#===========================================
def batchCreator():
    '''This creates a batch file for the user's file after the python check is made'''
    create_bch_preference=input("Will you like to create an Executionable batch file for your python file\n\t\ty/n => Yes/No\n")
    # bat=f"python {getfile(opener)}\npause"
    bat=f"python {getfile(opener)}\npause"
    if create_bch_preference=='y':
        bat_file=open(note_name+'.bat','x')
        bat_file.write(bat)
        bat_file.close()
    
#===========================================

def regards():
    # Doing the Python file check
    if extension=='py':
        batchCreator()

    #END REGARDS

    print("Thanks for using Hat_Man note_writer for writing your notes")
    print("Exiting Hat_Man - Notebook") #👋👋👋👋
#=======================================================================================================
date_today=datetime.today() 
a=str(date_today)
cut_date=a[:10]
cut_time=a[-2:]
name_seperator=['-','_']
note_date=f"{cut_date[:4]}{name_seperator[1]}{cut_date[5:7]}{name_seperator[1]}{cut_date[-2:]}"
file_name=input("Enter the file name\n")
extension=input("What extension do you need\n")
note_name=''
# correcting the filename
# Making sure there is a filename even if the user does not input a name
def nameChecker():
    '''Corrects the filename.
    \nProvides a filename if user does not to help save time.Appends date on preference.
    No arguments required..
    '''
    date_append_preference=input("Will you like today's date to be included in the file name\n\t\t[Y]es or [N]o\n")
    if file_name=='':
        note_name='new'+ note_date
        note_name+=extension
    else:
        if date_append_preference=='y':
            note_name=file_name+ name_seperator[0]+ note_date + '.'
            note_name+=extension
        elif date_append_preference=='n':
            note_name=file_name + '.'
            note_name+=extension
        else:
            print("Enter a valid input\n")
            nameChecker()
    return note_name

note_name=nameChecker()
print(f"Working on the file {note_name} ...")        #Printing out the generated file name
#=========================================================================
# Asking user to continue writing to the file in the console or an installed editor
def editorPreference():
    '''Means for writing to file created '''
    continuity_preference=input("Do you prefer continuing the editing in the console or your installed editor\n\n\t\t[C]onsole \ [E]ditor \n")
    if continuity_preference=='c':
        print("Write your notes here\n")
        print("Type @d on a new line when you finish writing to continue")
        user_input=input("")
        while True:
            next_input=input("")
            user_input=user_input +" \n" + next_input
            if next_input=="@d":
                break
        user_input=user_input[:-2]  #Splitting the user_input string to take out the loop breaker character i.e. @d
        new_file=open(note_name,'x')
        new_file.write(user_input)
        new_file.close()
        opener()
        regards()
        
    elif continuity_preference=='e':
        new_file=open(note_name,'x')
        new_file.close()
        comm=f"cmd /k start {note_name}"
        regards()
        os.system(comm)
    else:
        editorPreference()
    
editorPreference()





