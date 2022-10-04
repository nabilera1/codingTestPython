def reverse(x, y, z):
    return z, y, x



def checkYear(연도):
    if (연도 % 4) == 0:
        if (연도 % 100) == 0:
            if (연도 % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


연도 = 2022
if (checkYear(연도)):
    print("Leap Year")
else:
    print("Not a Leap Year")
