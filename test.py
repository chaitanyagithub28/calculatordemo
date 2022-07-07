from app import Calculator

a = eval(input("Enter first number:"))    
b = eval(input("Enter second number:"))
c = eval(input("Enter third number:"))  
cal = Calculator(a,b,c)   
print("Addition of {first},{second},{third} :".format(first=a,second=b,third=c),cal.sum())
print("Subtraction of {first},{second},{third} :".format(first=a,second=b,third=c),cal.diff())
print("Multiplication of {first},{second},{third} :".format(first=a,second=b,third=c),cal.mul())
print("Division of {first},{second},{third} :".format(first=a,second=b,third=c),cal.div())
print("Reminder of {first},{second},{third} :".format(first=a,second=b,third=c),cal.rem())