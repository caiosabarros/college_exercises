

temp = float(input("What is the temperature? " ))
scale = input("Fahrenheit or Celsius (F/C)? ")

if scale == "C" or scale == "c":
    temp = ((9 * temp) / 5) + 32

def find_wind_chill(temp, speed):
    #FORMULA IN https://www.weather.gov/media/safety/windchillchart3.pdf
    wind_chill = 35.74 + 0.6215 * temp - 35.75 * (speed ** 0.16) + 0.4275 * temp * (speed ** 0.16)
    print(f"At temperature {temp} F, and wind speed {speed} mph, the windchill is: {round(wind_chill,2)} F")

counter = 5
while counter != 65:
    find_wind_chill(temp, counter)
    counter += 5

