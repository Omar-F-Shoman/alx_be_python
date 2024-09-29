FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsuis = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR 
    return celsuis

def convert_to_fahrenheit(celsius):
    fehrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32 
    return fehrenheit


try:
    temperature = int(input("Enter the temperature to convert: "))
    c_or_f = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    
    if c_or_f == "C":
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {result}°F")

    elif c_or_f == "F":
        result2 = convert_to_celsius(temperature)
        print(f"{temperature}°F is {result2}°C")

    else:
        print(f"Invalid temperature. Please enter a numeric value.")

except:
      print(f"Invalid temperature. Please enter a numeric value.")
