# pip install textblob PyDictionary pyttsx3 time threading os
GEOMETRY= "650x700+400+1"

import tkinter as tk

# importing message boxes like showinfo, showerror, askyesno from tkinter.messagebox
from tkinter.messagebox import showerror, askyesno, askokcancel

from tkinter import messagebox

from tkinter import ttk

#importing the PyDictionary library
from PyDictionary import PyDictionary

# word corrector
from textblob import TextBlob

# this package converts text to speech
import pyttsx3

from tkinter.scrolledtext import ScrolledText

import threading

import time
import os
if os.path.isfile("documents/time.txt")==False:
     file = open("documents/time.txt", 'a') 
     
if os.path.isfile("documents/words.txt")==False:
     file = open("documents/words.txt", 'a') 
     
full_history = []
search_time=[]

# creating window
with open("documents/words.txt") as file:
    for line in file:
        full_history.append(line.strip("\n")) 
with open("documents/time.txt") as file:
    for line in file:
        search_time.append(line.strip("\n")) 



window=tk.Tk()
window.title("Audio Dictionnary With Spell Checks")
window.config( bg="grey")
window.geometry(GEOMETRY)

close=False


# close Option
def on_closing():  
        global close
        close=True
        if messagebox.askyesno(title="Quit", message="ARE YOU SURE YOU WANT TO QUIT?"):
            
            window.destroy()

            
window.protocol("WM_DELETE_WINDOW", on_closing)

# creating two tabs 
parent_tab=ttk.Notebook(window)
tab1=ttk.Frame(parent_tab)
tab2=ttk.Frame(parent_tab)
tab3=ttk.Frame(parent_tab)
parent_tab.add(tab1, text="Audio-Dictionary")
parent_tab.add(tab3,text="Recent")
parent_tab.add(tab2,text="Setings")

parent_tab.pack(expand=1, fill="both")

# setting icon
icon=tk.PhotoImage(file="images/icon.png")
window.iconphoto(True,icon)


# TAB1
##############################################################################################################################
# top label image 
audio_image=tk.PhotoImage(file="images/audio.png")
audio=tk.Label(tab1,image=audio_image).pack(side="top",fill="x")

# creating input label
input_label=tk.Label(tab1,text="Input Word:",justify="left", font=("Gabriola", 25)).pack(side="top")

loading=tk.Label(tab1,text="",justify="left", font=("Gabriola", 10))
loading.pack(side="top")

# creating word entry box
entry = tk.Entry(tab1, bg="lightgrey", width=45, font=("Cambria", 15), bd=5)
entry.pack(side="top", expand=1, fill="x")

entry.bind('<Return>', lambda event: search())
# function for searching the word meaning

# open the file in read mode


# TAB3
recent_image=tk.PhotoImage(file="images/recent.png")
recent_label=tk.Label(tab3,image=recent_image,bd=40).pack(side="top",fill="x")

recent_search=tk.Label(tab3,text="Most Recent Search:",justify="left", font=("Ink Free", 20)).pack(side="top")

recent_box = tk.Text(tab3,state="disabled", bg="lightgrey", width=45, font=("Candara", 25), height=8, bd=5, blockcursor=True)
recent_box.pack(side="top", expand=1, fill="x")


def switch_tab(notebook, tab_index):
    parent_tab.select(tab_index)

def research1():
    entry.delete(0,tk.END)
    entry.insert(tk.END,full_history[0])
    switch_tab(parent_tab,0)
    search()
 
def research2():
    entry.delete(0,tk.END)
    entry.insert(tk.END,full_history[1])
    switch_tab(parent_tab,0)
    search()

def research3():
    entry.delete(0,tk.END)
    entry.insert(tk.END,full_history[2])
    switch_tab(parent_tab,0)
    search()

def research4():
    entry.delete(0,tk.END)
    entry.insert(tk.END,full_history[3])
    switch_tab(parent_tab,0)
    search()

def research5():
    entry.delete(0,tk.END)
    entry.insert(tk.END,full_history[4])
    switch_tab(parent_tab,0)
    search()

def research6():
    entry.delete(0,tk.END)
    entry.insert(tk.END,full_history[5])
    switch_tab(parent_tab,0)
    search()

def research7():
    entry.delete(0,tk.END)
    entry.insert(tk.END,full_history[6])
    switch_tab(parent_tab,0)
    search()

def research8():
    entry.delete(0,tk.END)
    entry.insert(tk.END,full_history[7])
    switch_tab(parent_tab,0)
    search()

first_word=tk.Button(recent_box,text="" ,command=research1,bg="lightgrey", font=("Ariel",15))
first_word.pack (side="top",fill="x")

second_word=tk.Button(recent_box,text="",command=research2,bg="lightgrey", font=("Ariel",15))
second_word.pack (side="top",fill="x")

third_word=tk.Button(recent_box,text="",command=research3,bg="lightgrey", font=("Ariel",15))
third_word.pack (side="top",fill="x")
fourth_word=tk.Button(recent_box ,text="",command=research4,bg="lightgrey", font=("Ariel",15))
fourth_word.pack (side="top",fill="x")
fifth_word=tk.Button(recent_box,text="",command=research5,bg="lightgrey", font=("Ariel",15))
fifth_word.pack (side="top",fill="x")
sixth_word=tk.Button(recent_box,text="",command=research6,bg="lightgrey", font=("Ariel",15))
sixth_word.pack (side="top",fill="x")
seventh_word=tk.Button(recent_box,text="",command=research7,bg="lightgrey", font=("Ariel",15))
seventh_word.pack (side="top",fill="x")
eight_word=tk.Button(recent_box,text="",command=research8,bg="lightgrey", font=("Ariel",15))
eight_word.pack (side="top",fill="x")


def validating():
    full_history.reverse()
    search_time.reverse()
    if 0 < len(full_history) and  0 < len(search_time):
        first_word.config(text=f"{full_history[0]}          {search_time[0]}")
    if  1 < len(full_history) and  1 < len(search_time):
        second_word.config(text=f"{full_history[1]}          {search_time[1]}")
    if  2 < len(full_history) and 2 < len(search_time):
        third_word.config(text=f"{full_history[2]}          {search_time[2]}")
    if  3 < len(full_history) and  3 < len(search_time):
        fourth_word.config(text=f"{full_history[3]}          {search_time[3]}")
    if  4 < len(full_history) and  4 < len(search_time):
        fifth_word.config(text=f"{full_history[4]}          {search_time[4]}")    
    if  5 < len(full_history) and  5 < len(search_time):
        sixth_word.config(text=f"{full_history[5]}          {search_time[5]}")  
    if  6 < len(full_history) and  6 < len(search_time):
        seventh_word.config(text=f"{full_history[6]}          {search_time[6]}")  
    if  7 < len(full_history) and  7 < len(search_time):
        eight_word.config(text=f"{full_history[7]}          {search_time[7]}")  
    else:
        return
  
validating()

def search():
    def search_synthesis():
        current_time=time.ctime()
        loading.config(text="Loading....↻")
        # getting the word from the entry using the get(), changing it to lowercase and also stripping it of any spaces
        word = entry.get().lower().strip().replace(' ', '')

        

        corrected_word = TextBlob(word).correct() 

        # checking if the word variable is empty
        if word == '' :
            # message box to display if the word variable is empty
            showerror(title='Error', message='Please enter the word you want to search for!!')
            return  # Exit the function if the word is empty
        
        # checking if the word variable has numbers and symbols
        if word.isalpha()==False :
            # message box to display if the word variable has symbols and digits
            showerror(title='Error', message=f'Sorry, cannot search for the meaning of "{word}", Please enter a valid word.')
            return  # Exit the function if the word is empty

        try:
            word = entry.get().lower().strip()
            meaning_box.config(state="normal")
            # creating a dictionary object
            dictionary = PyDictionary()

            # passing a word to the dictionary object
            meanings = dictionary.meaning(word)

            # previewing word
        
            corrected_word = TextBlob(word).correct() #Getting the object for the word
            preview.insert(1.0,corrected_word)
            preview.config(state="normal")
            preview.delete(1.0,tk.END)
            preview.insert(1.0,word)
            preview.config(state="disabled")
            
            if meanings:
                full_history.append(word)
                search_time.append(current_time)
                recent_box.config(state="disabled")
                file = open("documents/time.txt", "a")
                file.write(f"{current_time}\n")
                file.close()
                file = open("documents/words.txt", "a")
                file.write(f"{word}\n")
                file.close()
                validating()
                
                # Clearing the content in the Text widget
                meaning_box.delete('1.0', tk.END)
                
                # Inserting content (meanings) in the Text widget
                for pos, meaning in enumerate(meanings, start=1):
                    meaning_box.insert(tk.END, f"{pos}. {meaning.capitalize()}:\n")
                    meaning_box.insert(tk.END, f"{', '.join(meanings[meaning])}\n\n")
                
                # enabling the audio button to normal state
                read_button.config(state=tk.NORMAL)
                meaning_box.config(state="disabled")
                loading.config(text="") 
                return
            else:
                # checking for a possible word and returning it to the user
                corrected_word = TextBlob(word).correct()
                correct_meaning=PyDictionary.meaning(corrected_word) 
                meaning_box.config(state="disabled")


                if correct_meaning:
                    if askyesno(title='Error', message=f'"{word}" was not found in the dictionary!. Do you mean "{corrected_word}"?'):  
                        loading.config(text="")
                        entry.delete(0,tk.END)
                        entry.insert(tk.END,corrected_word)
                        search()
                    return
                

                # if there isnt anyword ahow error
                else:
                    loading.config(text="")
                    if ConnectionError:
                        showerror(title='Error', message='There is a problem with your internet connection! Please check it and then try again.')
                        return
                    
                    askokcancel(title='Error', message=f'"{word}" was not found in the dictionary!.')
                    return
                   
                          


        except FileNotFoundError:
            showerror(title='Error', message=f'Some files were not found!!! Please make sure you have all required files and try again')
            return
        
        # catching all errors
        except KeyError:
            showerror(title='Error', message=f'"{word}" was not found in the dictionary!')
            return
        
        # no internet connectivity
        except ConnectionError:
            showerror(title='Error', message='There is a problem with your internet connection! Please check it and then try again.')
            return
        
        # catching the rest of the exceptions
        except Exception as e:
            showerror(title='Error', message=f'An error occurred: {str(e)}')
            return
    

    
    search_thread = threading.Thread(target=search_synthesis)
    search_thread.start()
    
# function to read text
# function to turn textual data into audio data


def speak():
    
    # Define a function to perform speech synthesis
    def perform_speech_synthesis():
            # getting the word from the entry
            word = entry.get().strip()

            if not word:
                showerror(title='Error', message='Please enter a word to speak!')
                return

            # initializing the pyttsx3 object
            engine = pyttsx3.init()


            # gets the speaking rate
            rate = engine.getProperty('rate')

            # setting the speaking rate
            engine.setProperty('rate', 125)
    
            # getting the available voices
            voices = engine.getProperty('voices')

            
            # choosing voice           
            voice = selected_voice.get()
            # setting the voice
            engine.setProperty('voice', voices[voice].id)

            # creating a dictionary object
            dictionary = PyDictionary()

            # passing a word to the dictionary object
            meanings = dictionary.meaning(word)

            if meanings:
                    
                    # Speak the word
                    engine.say(word)
                    # Speak each meaning
                    for part_of_speech, meaning_list in meanings.items():
                        engine.say(part_of_speech)
                        for meaning in meaning_list:
                            engine.say(meaning)
            else:
                loading.config(text="Reading🔊")
                engine.say("No meanings found for the word.")
                loading.config(text="")


            # this function processes the voice 

                
            if engine._inLoop:
                 engine.endLoop()
                 loading.config(text="")

            # this function processes the voice 
            else:
                loading.config(text="Reading🔊")
                engine.runAndWait()
                loading.config(text="")
        
    # Create a new thread for speech synthesis
    speech_thread = threading.Thread(target=perform_speech_synthesis)
    speech_thread.start()






# creating area to preview word
preview=tk.Text(tab1 , width=10,height=1,bg="#ececec", font=("Times New Roman",20),state="disabled")
preview.pack(pady=10)
    



# creating search button
search_image=tk.PhotoImage(file="images/search.png")
search_button=tk.Button(tab1, bg="#f5f3ed",width=50, height=30, bd=5, image=search_image,command=search).pack(side="top")



# creating meaning label 
meaning_image=tk.PhotoImage(file="images/meaning_image.png")
meaning_label=tk.Label(tab1,image=meaning_image).pack(side="top")



# creating read button
read_image=tk.PhotoImage(file="images/read_man.png")
read_button = tk.Button(tab1, bg="#70c2f2", width=110, height=300, bd=5, image=read_image, command=speak)
read_button.pack(side="left")

# creating meaning box
meaning_box = ScrolledText(tab1,state="disabled", bg="lightgrey", width=45, font=("Candara", 15), height=15, bd=5, blockcursor=True)
meaning_box.pack(side="top", expand=1, fill="x")

########################################################################################################################################################





#SETTINGS
################################################################################################################################################

# choosing input label colour
entry_colour=tk.Label(tab2,text="Choose entry and meaning theme",justify="left", font=("Gabriola", 35)).pack(side="top")

selected_meaning_colour=tk.IntVar()
default_mode=tk.Radiobutton(tab2,text="default", variable=selected_meaning_colour,value=0, font=10).pack (side="top")

dark_mode=tk.Radiobutton(tab2,text="dark", variable=selected_meaning_colour,value=1, font=10).pack (side="top")

light_mode=tk.Radiobutton(tab2,text="light", variable=selected_meaning_colour,value=2, font=10).pack (side="top")


# function to change colour of entry
def theme():
        window.bell()
        if askyesno(title="Apply", message="Are you sure you want to apply this change?"):
            # collecting values from checkboxes
            if selected_meaning_colour.get()==1:
                    entry.config(bg="black", fg="white")
                    meaning_box.config(bg="black", fg="white")


            elif selected_meaning_colour.get()==2:
                    entry.config(bg="white", fg="black")
                    meaning_box.config(bg="white", fg="black")
            
            else:
                entry.config(bg="lightgrey", fg="black")
                meaning_box.config(bg="lightgrey", fg="black")


# button for applying entry change
apply_button=tk.Button(tab2, text="Apply",command=theme, bd=5,bg="lightblue").pack(side="top")



# choosing between male and female voice
Choose_voice=tk.Label(tab2,text="Choose voice",justify="left", font=("Gabriola", 35)).pack(side="top")
selected_voice=tk.IntVar()

male_voice=tk.Radiobutton(tab2,text="Male", variable=selected_voice ,value=0, font=10).pack (side="top")


# female_voice
female_voice=tk.Radiobutton(tab2,text="Female", variable=selected_voice,value=1, font=10)
female_voice.pack (side="top")

selected_voice.set(1)






    # read first character

 
 



 







# research_button=tk.Button(tab3,width=15,bg="lightblue", height=1 ,bd=5,text="search", command=research)
# research_button.pack(side="right")





is_running=False

# clearing history
def show_full_history():
    def boolean():
        history_window.destroy()
        global is_running
        is_running=False
    
    
    
    global is_running
    if is_running == False:
        history_window=tk.Tk()
        history_window.title("History")
        history_window.geometry("540x500+1+100")
        history_window.resizable(False,False)
        full=ScrolledText(history_window,fg="black",state="disabled", background="#f2ffff", bd=1,font=("Javanese Text",20),padx=12)
        full.pack(side="top", fill="both")

        full.config(state="normal")
        full_history.reverse()
        search_time.reverse()
        for line in zip(full_history,search_time):
            full.insert(1.0, f"{line}\n")
        full_history.reverse()
        search_time.reverse()

        
            

        
      
                
            
      
        full.config(state="disabled")
        is_running=True

        history_window.protocol("WM_DELETE_WINDOW", boolean)
            
    else:
            return




def clear_history():
    window.bell()
    if askyesno(title="Clear History", message=f"Are you sure you want to clear history?\n All data erased will be lost!!"):
        full_history.clear()
        file = open("documents/words.txt", "w")
        file.__del__()
        file.close()   
        search_time.clear()
        file = open("documents/time.txt", "w")
        file.__del__()
        file.close() 
        first_word.config(text="")
        second_word.config(text="")
        third_word.config(text="")
        fourth_word.config(text="")
        fifth_word.config(text="")
        sixth_word.config(text="")
        seventh_word.config(text="")
        eight_word.config(text="")


# clear history button
clear=tk.Button(tab3,width=10, height=1 ,bd=5,bg="#ff6060",text="Clear History" ,command=clear_history)
clear.pack(side="left")
show_button=tk.Button(tab3,width=15,bg="lightblue", height=1 ,bd=5,text="View Full History", command=show_full_history)
show_button.pack(side="left")



# running window
window.mainloop()
