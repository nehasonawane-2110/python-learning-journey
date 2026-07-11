# Convert temp from Celsius to Fahrenheit. (C/5 = (F-32)/9)
celsius = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32
# Temperature scales increase at different rates
# 5°C = 9°F (difference in scale size)
# 32°F is the freezing point of water
print(f'Temperature in fahrenheit is: {fahrenheit}')
