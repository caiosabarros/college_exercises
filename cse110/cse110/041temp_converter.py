#Hi, today we're building a converter from F to C

fahrenheit_temperature = float(input('What is the temperature in Fahrenheit? '))
celsius_temperature =  (fahrenheit_temperature - 32) * 5 / 9

print(f'The temperature in Celsius is {celsius_temperature:.1f} degrees.')
