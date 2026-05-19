#if statement

a=10
if a>=5:
 print("Number is greater than 5")

#if else

a= int(input("Enter a number"))

if a>=0:
 print("Number is positive")
else:
 print("Number is negative")

#  #if elif

marks= int(input("Enter your marks"))

if marks>=75:
  print("Distinction")
elif marks>=60:
  print("First class")
elif marks>=50:
  print("Second class")
else:
  print("Fail")


# #switch case

day= int(input("Enter a number"))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Select proper number")