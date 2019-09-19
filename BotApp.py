import tkinter as tk
import requests
from nltk.chat.util import Chat, reflections
import requests
import time
from datetime import datetime
from functions import *
from data import *; 
import eliza

HEIGHT = 500
WIDTH = 600

iteration = 1

chat = Chat(pairs, reflections)

#функция вывода текста в лейблwor
def mprint(text):
	global iteration
	label['text'] = ("iteration: " + str(iteration) + "\n" + text)
	iteration = iteration + 1

activateElisa = 0
#главная функция в которой обрабатываются событи
def main(text):
	global activateElisa
	
	if(text=="info"):
		mprint(helpInfo)
	elif(str.lower(text)=="hello elisa"):
		activateElisa = 1
		mprint(eliza.eliza_chatbot.respond(str(text)))
	if(activateElisa==1):
		if(text=="quit"):
			activateElisa=0
		mprint(eliza.eliza_chatbot.respond(str(text)))

	else:
		if (chat.respond(str(text))):
			mprint(chat.respond(str(text)))
		else:
			if (isQuestion(text)):
				if (typeQuestion(text)):
					mprint(typeQuestion(text))
				else:
					try:
						mprint(eliza.eliza_chatbot.respond(str(text)))
					except:
						mprint("Sorry, I don't clearly understand. Let's talk about something else. By the way, " + str(random.choise(compliments)))


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='background.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Send", font=40, command=lambda: main(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, wraplength=300)
label.place(relwidth=1, relheight=1)

root.mainloop()

