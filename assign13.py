def convert_temp():
    temp_farinhai = float(input("input temperature: "))
def convert_celcius(temp_farinhai):
    convert_temp()
    celcius = (temp_farinhai-32)*(5/9)
    return celcius
def convert_kelvin(celcius):
    convert_temp()
    kelvin = (celcius + 273.15)
    return kelvin
print("temperature in celcius: ",convert_celcius(temp_farinhai))
print("temperature in kelvin: ",convert_kelvin(celcius))
