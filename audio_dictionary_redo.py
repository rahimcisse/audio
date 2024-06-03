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

full_history = []
history=[]
# creating window

window=tk.Tk()
window.title("Audio Dictionnary With Spell Checks")
window.config( bg="grey")
window.geometry(GEOMETRY)


# close Option
def on_closing():  
        if messagebox.askyesno(title="Quit", message="ARE YOU SURE YOU WANT TO QUIT?"):
            window.destroy()
            SystemExit()
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
image=tk.PhotoImage(file="images/audio.png")
label=tk.Label(tab1,image=image).pack(side="top",fill="x")

# creating input label
input_label=tk.Label(tab1,text="Input Word:",justify="left", font=("Gabriola", 25)).pack(side="top")


# creating word entry box
entry = tk.Entry(tab1, bg="lightgrey", width=45, font=("Cambria", 15), bd=5)
entry.pack(side="top", expand=1, fill="x")

# function for searching the word meaning

def search():
    
    
    # getting the word from the entry using the get(), changing it to lowercase and also stripping it of any spaces
    word = entry.get().lower().strip().replace(' ', '')

    

    b = TextBlob(word).correct() 

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
       
        b = TextBlob(word).correct() #Getting the object for the word
        preview.insert(1.0,b)
        preview.config(state="normal")
        preview.delete(1.0,tk.END)
        preview.insert(1.0,word)
        preview.config(state="disabled")
        
        if meanings:
            history.append(word)
            recent_box.config(state="normal")
            recent_box.insert(1.0,f"{word}\n")
            recent_box.config(state="disabled")
    
            file = open("documents/word.txt", "a")
            file.write(f"{word}\n")
            file.close()
            
            # Clearing the content in the Text widget
            meaning_box.delete('1.0', tk.END)
            
            # Inserting content (meanings) in the Text widget
            for pos, meaning in enumerate(meanings, start=1):
                meaning_box.insert(tk.END, f"{pos}. {meaning.capitalize()}:\n")
                meaning_box.insert(tk.END, f"{', '.join(meanings[meaning])}\n\n")
            
            # enabling the audio button to normal state
            read_button.config(state=tk.NORMAL)
            meaning_box.config(state="disabled")
            return
        else:
            # checking for a possible word and returning it to the user
            b = TextBlob(word).correct()
            correct_meaning=PyDictionary.meaning(b) 
            meaning_box.config(state="disabled")


            if correct_meaning:
                askokcancel(title='Error', message=f'"{word}" was not found in the dictionary!. I think you meant "{b}"')
                return
            

            # if there isnt anyword ahow error
            else:
                askokcancel(title='Error', message=f'"{word}" was not found in the dictionary!.')
                return
                       


            
    # catching all errors
    except KeyError:
        showerror(title='Error', message=f'"{word}" was not found in the dictionary!')
        return
    
    # no internet connectivity
    except ConnectionError:
        showerror(title='Error', message='There is a problem with your internet connection! Please check it.')
        return
    
    # catching the rest of the exceptions
    except Exception as e:
        showerror(title='Error', message=f'An error occurred: {str(e)}')
        return


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
                engine.say("No meanings found for the word.")


            # this function processes the voice 
            if engine._inLoop:
                 engine.endLoop()

            # this function processes the voice 
            else:
                engine.runAndWait()
        
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
entry_colour=tk.Label(tab2,text="Choose theme",justify="left", font=("Gabriola", 35)).pack(side="top")

selected_meaning_colour=tk.IntVar()
default_mode=tk.Radiobutton(tab2,text="default", variable=selected_meaning_colour,value=0, font=10).pack (side="top")

dark_mode=tk.Radiobutton(tab2,text="dark", variable=selected_meaning_colour,value=1, font=10).pack (side="top")

light_mode=tk.Radiobutton(tab2,text="light", variable=selected_meaning_colour,value=2, font=10).pack (side="top")


# function to change colour of entry
def theme():
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
tk.Button(tab2, text="Apply",command=theme, bd=5,bg="lightblue").pack(side="top")



# choosing between male and female voice
Choose_voice=tk.Label(tab2,text="Choose voice",justify="left", font=("Gabriola", 35)).pack(side="top")
selected_voice=tk.IntVar()

male_voice=tk.Radiobutton(tab2,text="Male", variable=selected_voice ,value=0, font=10).pack (side="top")


# female_voice
female_voice=tk.Radiobutton(tab2,text="Female", variable=selected_voice,value=1, font=10)
female_voice.pack (side="top")

selected_voice.set(1)

####################################################################################################################################




# TAB3
############################################################################################################################################
recent_image=tk.PhotoImage(file="images/recent.png")
recent_label=tk.Label(tab3,image=recent_image,bd=40).pack(side="top",fill="x")

recent_search=tk.Label(tab3,text="Most Recent Search:",justify="left", font=("Ink Free", 20)).pack(side="top")

recent_box = tk.Text(tab3,state="disabled", bg="lightgrey", width=45, font=("Candara", 25), height=8, bd=5, blockcursor=True)
recent_box.pack(side="top", expand=1, fill="x")






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
        history_window.geometry("400x500+1+100")
        history_window.resizable(False,False)
        full=ScrolledText(history_window,fg="green",state="disabled", background="white", bd=2,font=("Ariel",20),padx=12)
        full.pack(side="top", fill="x")

        full.config(state="normal")
        with open("documents/word.txt") as file:
            for line in file:
                full.insert(1.0, line)      
        full.config(state="disabled")
        is_running=True

        history_window.protocol("WM_DELETE_WINDOW", boolean)
            
    else:
            return




def clear_history():
    if askyesno(title="Clear History", message=f"Are you sure you want to clear history?\n All data erased will be lost!!"):
        full_history.clear()
        file = open("documents/word.txt", "w")
        file.__del__()
        file.close()   



# clear history button
clear=tk.Button(tab3,width=10, height=1 ,bd=5,text="Clear History" ,command=clear_history)
clear.pack(side="right")
show_button=tk.Button(tab3,width=15,bg="lightblue", height=1 ,bd=5,text="View Full History", command=show_full_history)
show_button.pack(side="right")
#####################################################################################################################################



# running window
window.mainloop()
