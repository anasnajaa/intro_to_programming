import tkinter as tk
import requests

HEIGHT = 500
WIDTH = 600

def get_weather(city):
    key = ''
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = f"{weather['name']}\n{weather['weather'][0]['description']}\n{weather['main']['temp']}"


root = tk.Tk()

# bg_img = tk.PhotoImage(file='./landscape.png')
# bg_label = tk.Label(root, image=bg_6img)
# bg_label.place(relwifth=1,relheight=1)

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=.75, relheight=.08, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=.65, relheight=1)

btn = tk.Button(frame, text='Get Weather', font=40, command=lambda: get_weather(entry.get()))
btn.place(relx=0.7, relwidth=.3, relheight=1)



lower_frame = tk.Frame(root, bg='#80c1ff', bd=5)
lower_frame.place(relx=0.5, rely=.25, relwidth=.75, relheight=.6,anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

# btn.pack(side='left', fill='both', expand=True)
# btn.grid(row=0, column=0)



# label.pack(side='left')
# label.grid(row=0, column=1)



root.mainloop()

