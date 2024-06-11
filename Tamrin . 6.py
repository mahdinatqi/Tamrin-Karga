

element = input("Enter your information: ")

if element.startswith("[") and element.endswith("]"):
    print(f"your Entered a list which is {element}")
elif element.startswith("(") and element.endswith(")"):
    print(f"You entered a Tuple which is {element}")
elif element.startswith("{") and element.endswith("}"):
    print(f"you enetered a Dictionary which is {element}")
elif len(element)== 1 and ord(element)>= 32 and ord(element)<= 47:
    print(f"you entered a character whcich is {element}")
elif len(element) == 1 and ord(element)>=57 and ord(element)<=126:
    print(f"you enetered a character which is {element}")
elif len(element) > 0:
    t = 0
    acci = [48,49,50,51,52,53,54,55,56,57]
    for i in element:
        if ord(i) not in acci:
            t += 1
    if t==0:
        print(f"your entered a number which is {element}")
    elif t > 0 and element[0] != "." and i == "." :
        print(f"you eneted a float number which is {element}")
    else:
        print(f"you enetered a string which is {element}")
    
else:
    print(f"you entered a string  which is {element}")
''' 
'''   
# THE SECOND PRACTICe----> A simple bank system to get cach
# ,transfer money, and show balance

exist = 32424354478
def Get():
    amount = int(input("Amount: "))
    remain = exist-amount
    print("The Operation  was successfully done!")
    return remain
    
def Transfer ():
    card_num = int(input("Target Card_number: "))
    for i in range(3):
        if len(card_num) > 16:
            print("Invalid Card_number!")
            continue
    amount = int(input("Amount: "))
    remain = exist - amount
    return remain
    
def Balance():
    print("Your blance is: ", exist)



print("Enter your Card!")
input(
    
)
password = int(input("Password: "))

for i in range(4):
    print("Please Enter The number of Your Service: ")
    print("1. Get Cash      2. Transfer     3. Show Balance ")
    option = int(input())
    
    if option == 1:
        exist = Get()
    elif option == 2:
        exist = Transfer
    elif option == 3:
        Balance()
    else:
        print("Invalid Option!")
    
    answer = input("Any Other Operation? y/n ")
    if answer.upper() =="Y":
        continue
    elif answer.upper() == "N":
        break
    
'''

'''
# The program must print the result of the selected operation by its name!
# The third practice

print("please Enter your operand by its name, sum, difference, multiple, or devide! ")
num_1 = int(input("No_1: "))
op = input("Operand: ") 
num_2 = int(input("No_2: "))

if op.upper() == "SUM":
    z = num_1 + num_2
elif op.upper() == "DIFFERENCE":
    z = num_1 - num_2
elif op.upper() == "MULTIPLE":
    z = num_1 * num_2
elif op.upper() == "DEVIDE":
    z = num_1 / num_2
else:
    print("Sorry the operation is not suppored!")
print(f"The result is : {z}.")
'''

'''
# The fourth practice
# to change the temperature from C to F and vice versa, the user selects C to F or ... 
type = input("for F to C enter FC and for C to F enter CF: ")
temp = int(input("Temperature: "))

if type.upper()=="FC":
    C = 5/9*(temp-32)
    print(f"your temprature in celisuce is {C}")
elif type.upper()=="CF":
    F = 9/5 * temp +32
    print(f"your temperature in farenhite is {F}")
    
'''
'''
# The fifthe one 
color = []
size = []
for i in range(4):
    c = input("Colors: ")
    color.append(c)
    s = int(input("size: "))
    size.append(s)
    

import turtle
Square = turtle.Turtle()
turtle.pensize(4)
for c,s in zip(color,size):
    Square.color(c)
    Square.forward(s)
    Square.right(90)
turtle.done()
'''