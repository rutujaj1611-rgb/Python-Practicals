#Built-in Exception Program
try:
    l = [10, 20, 30]
    
    index = int(input("Enter index (0-2): "))
    print("Value:", l[index])

except IndexError:
    print("Error: Index out of range")

except ValueError:
    print("Error: Enter valid number")

finally:
    print("Program Ended")


#User-defined Exception Program
class NegativeError(Exception):
    pass

try:
    num = int(input("Enter a number: "))

    if num < 0:
        raise NegativeError

    print("You entered:", num)

except NegativeError:
    print("Error: Negative numbers are not allowed")

finally:
    print("Program Ended")