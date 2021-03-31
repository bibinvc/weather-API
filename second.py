import tkinter as tk
import requests
import time
def getWeather(parameter):
    location=textField.get()
    
    api="https://api.openweathermap.org/data/2.5/forecast?q="+location+ "&appid=29d798894ead64442d8273e5fb62e561"
    list_data=[]
    data=requests.get(api).json()
    for i in range(0,40):
        temp=int(data['list'][i]['main']['temp_max']-275.15)
        dt=data['list'][i]['dt_txt']
        final_info="\n"+"date:"+str(dt)+"\t"+"max temperature:\t"+str(temp)+"°C"
        list_data.append(final_info)
    
    label1.config(text=list_data)

    discri_ption="WEATHER DETAILS"
     

    label2.config(text=discri_ption)

parameter=tk.Tk()
parameter.geometry("400x800")
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
