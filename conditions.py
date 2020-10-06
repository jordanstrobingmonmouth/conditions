import sys

temp = int(input("Please enter the current temperature: (Enter 999 to stop) "))


while temp != 999:
    if temp > 90:
        print("Wear shorts")
    elif temp > 70:
        print("Short sleeves are fine")
    elif temp > 50:
        print("Wear a jacket")
    elif temp > 32:
        print("Wear a heavy coat")
    else:
        print("Stay inside")
    temp = int(input("Please enter another temperature: (Enter 999 to stop) "))

if temp == 999:
    sys.exit()
