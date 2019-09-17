import tkinter as tk
import requests
from nltk.chat.util import Chat, reflections
import requests
import time
from datetime import datetime
from data import *; #from functions import *

HEIGHT = 500
WIDTH = 600

chat = Chat(pairs,reflections)

#функция вывода текста в лейбл
def mprint(text):
	label['text'] = text

#главная функция в которой обрабатываются события
def main(text):
	mprint(chat.respond(str(text)))#str(text))

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

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

root.mainloop()



"""
#формат запроса погоды
def format_response(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']

		final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (name, desc, temp)
	except:
		final_str = 'There was a problem retrieving that information'

	return final_str

#поиск погоды (перепесать под бота)
def get_weather(city):
	weather_key = 'a4aa5e3d83ffefaba8c00284de6ef7c3'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weather_key, 'q': city, 'units': 'celsius'}
	response = requests.get(url, params=params)
	weather = response.json()

	label['text'] = format_response(weather)
"""
