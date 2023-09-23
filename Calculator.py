def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
def floorDiv(a,b):
    return a//b

a = '''
1)- Addition
2)- Subtraction
3)- Multiplication
4)- Division
5)- Modulus
6)- Floor Division
7)- Exit 
'''

print("***** Welcome to CODSOFT calci *****")

while True:
    print(a)
    b = input("Enter choice: ")
    if b not in ["1","2","3","4","5","6","7"]:
        print("Wrong choice!!!")
        p = input("<--Press Enter-->")
        continue
    
    if b == "7":
        break
    while True:
        try:
            n1 = eval(input("Enter 1st number: "))
            n2 = eval(input("Enter 2nd number: "))
            break
        except NameError:
            print("Invalid input! Enter numeric value")
            p = input("<--Press Enter-->")
            continue
    if b == "1":
        print("Addition of", n1, "and", n2, "is:\n", add(n1,n2))
    elif b == "2":
        print("Subtraction of", n2, "from", n1, "is:\n", sub(n1,n2))
    elif b == "3":
        print("Multiplication of", n1, "and", n2, "is:\n", mul(n1,n2))
    elif b == "4":
        print("Division of", n1, "by", n2, "is:\n", div(n1,n2))
    elif b == "5":
        print("Modulus of", n1, "and", n2, "is:\n", mod(n1,n2))
    elif b == "6":
        print("Floor Division of", n1, "and", n2, "is:\n", floorDiv(n1,n2))
    p = input("<--Press Enter-->") 