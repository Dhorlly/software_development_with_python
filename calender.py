##
#A gregorian calender leap or common year generator
#

print("Calender!!!")

year = int(input("Enter the year: "))

if year < 1582:
    print("Not within the Gregorian calender period")
else:
    if year % 4 != 0:
        print("Common year")
    elif year % 100 != 0:
        print("Leap year")
    elif year % 400 != 0:
        print("Common year")
    else:
        print("Leap year")
