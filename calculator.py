print("SIMPLE CALCULATOR")
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "cannot be divided by zero"
    else:
        return a/b
print("Select operation: ")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice=int(input("please select 1,2,3 or 4"))
a=int(input("enter first number: "))
b=int(input("enter second number: "))
if choice==1:
    print(a,"+",b,"=",add(a,b))
elif choice==2:
    print(a,"-",b,"=",subtract(a,b))
elif choice==3:
    print(a,"*",b,"=",multiply(a,b))
elif choice==4:
    print(a,"/",b,"=",add(a,b))
else:
    print("invalid input")       