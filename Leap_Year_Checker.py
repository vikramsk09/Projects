# Leap Year Checker

year = int(input("Enter the year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is Not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is Not a leap year")























































































