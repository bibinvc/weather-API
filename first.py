import tkinter as tk
import requests

def getWeather(parameter):
    location=textField.get()
    api="https://api.openweathermap.org/data/2.5/weather?q="+location+ "&appid=29d798894ead64442d8273e5fb62e561"
    data=requests.get(api).json()
    temp=int(data['main']['temp']-275.15)
    speed=data['wind']['speed']
    deg=data['wind']['deg']
    discri_ption="WEATHER DETAILS"
    final_info="\n"+"temperature:\t"+str(temp)+"°C" + "\n\n" + "speed:\t" + str(speed) + "\n"+ "deg:\t" + str(deg)
    label1.config(text=final_info)
    label2.config(text=discri_ption)

parameter=tk.Tk()
parameter.geometry("400x400")
parameter.title("WEATHER")

textField=tk.Entry(parameter,justify='center', width=40)
textField.pack(pady=30)
textField.focus()
textField.bind('<Return>',getWeather)


label2=tk.Label(parameter)
label2.pack()
label1=tk.Label(parameter)
label1.pack()

parameter.mainloop()
