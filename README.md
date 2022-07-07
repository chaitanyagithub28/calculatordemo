# This ia a basic Calculator Program using Class
<!-- It contains:
            addition
            subtraction
            multiplication
            division
            reminder methods. -->

```py
   from app import Calculator
   a = eval(input("Enter first number:"))    
   b = eval(input("Enter second number:")) 
   cal = Calculator(a,b)   
   print("Addition of {first} & {second} :".format(first=a,second=b),cal.sum())
   print("Subtraction of {first} & {second} :".format(first=a,second=b),cal.diff())
   print("Multiplication of {first} & {second} :".format(first=a,second=b),cal.mul())
   print("Division of {first} & {second} :".format(first=a,second=b),cal.div())
   print("Reminder of {first} & {second} :".format(first=a,second=b),cal.rem())
```
