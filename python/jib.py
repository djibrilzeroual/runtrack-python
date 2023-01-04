def My_print_hello():
    print("hello world")

My_print_hello()

def My_print_name(name):
    print(name)

My_print_name("djibri")

def add(num1,num2):
    print(num1+num2)

add(2,2) 


def Gethello():
    return("hello la plateforem")

print(Gethello())

    
def calcule(num1, operator, num2):
    return eval(str(num1) + operator + str(num2))

print(calcule(18, "+", 34)) 

def nmbsi(nombre):
    if nombre > 0:
        print("positif")

    elif nombre < 0:
        print("negatif")

nmbsi(3)
nmbsi(-6)