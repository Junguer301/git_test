from calendar import c
from this import d
from pyrsistent import b



num1=int(input("numero1:"))
num2=int(input("numero2:"))

def division(num1, num2):
    c=num1/num2
    return(c)
    try:
        c=num1/num2
    except Exception as e:
        c=eval(input("Error {}, intente de nuevo:".format(e)))
        print(c) 
    else:
        print("C=",c)
    return(c)
print(c)  