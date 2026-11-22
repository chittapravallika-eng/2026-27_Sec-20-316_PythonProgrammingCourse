def convert(c):
    f = (c * 9/5) + 32
    return f
c = float(input("Enter temperature in Celsius: "))
print("Temperature in Fahrenheit:", convert(c))