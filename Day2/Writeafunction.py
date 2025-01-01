def is_leap(year):
    leap = False
    
    if year % 100:
        return False
    elif year % 400:
        return True
    elif year % 4:
        return True
    else:
        False

    if 1900 <= year <= 10**5:
        print(is_leap(year))
    else:
        print("Year out of range")
year = int(input())
print(is_leap(year))
