from tkinter import *
import requests
import json
from datetime import datetime
 
# Initialize Window
root = Tk()
root.geometry("550x550")  # size of the window by default
root.resizable(0, 0)  # to make the window size fixed
root.title("Weather App - AskPython.com")

# Functions to fetch and display weather info
city_value = StringVar()

def time_format_for_location(utc_with_tz, timezone):
    local_time = datetime.utcfromtimestamp(utc_with_tz + timezone)
    return local_time.strftime('%H:%M:%S')

def get_current_date_time():
    # Get the current date and time
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    day_str = now.strftime("%A")
    time_str = now.strftime("%H:%M:%S")
    return date_str, day_str, time_str

def showWeather():
    api_key = "33968a60da7e90f392bf53e3c4d07546"  # sample API
    city_name = city_value.get()
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid=' + api_key

    response = requests.get(weather_url)
    weather_info = response.json()

    #tfield.delete("1.0", "end")  # to clear the text field for every new output

    if weather_info['cod'] == 200:
        kelvin = 273  # value of kelvin
        temp = int(weather_info['main']['temp'] - kelvin)
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed'] * 3.6
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']
        sunrise_time = time_format_for_location(sunrise, timezone)
        sunset_time = time_format_for_location(sunset, timezone)
        date_str, day_str, time_str = get_current_date_time()

        weather = f"\nWeather of: {city_name}\nDate: {date_str}\nDay: {day_str}\nCurrent Time: {time_str}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"

    tfield.insert(INSERT, weather)  # to insert or send value in our Text Field to display output

# Frontend part of code - Interface
city_head = Label(root, text='Enter City Name', font='Arial 12 bold').pack(pady=10)
inp_city = Entry(root, textvariable=city_value, width=24, font='Arial 14 bold').pack()
Button(root, command=showWeather, text="Check Weather", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5).pack(pady=20)
weather_now = Label(root, text="The Weather is:", font='Arial 12 bold').pack(pady=10)
tfield = Text(root, width=46, height=20)
tfield.pack()

root.mainloop()
