def is_leap(year):
    leap = False
    
    if year % 100:
        return False
    elif year % 400:
        return True 
    else:
        False

year = int(input())
print(is_leap(year))
