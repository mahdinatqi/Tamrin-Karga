import turtle
import random
import time
import turtle

def unlock_vault(x,solved_puzzle,magic_nums,test_num, userName):
    word = ''
    word = word +x[1][0]
    w = str(solved_puzzle[1])  
    word = word + w[0]
    word = word+magic_nums[1][0]
    word = word + userName[0]    
    
    print("The Password is: ", word)
        
    
# first mission
def decrypt_clue(text):
    key_words =["and", "as","assert","break","class","continue","def","if","else","exec",
    "finally","for","while","from","global","elif","import","import","in","is","lamda","nonlocal",
    "not","or","pass","raise","return","try","with","yeild","True","False","None"]
    
    found_Keys = []
    for j in range(len(key_words)):
        for i in range(len(text)):
            keyword = ""
            if text[i:i+len(key_words[j])] == key_words[j]:
                keyword = key_words[j]
                found_Keys.append(keyword)
                         
    return found_Keys
            


#second mission
def solve_puzzles(puzzle):
    print(puzzle)
    T_F_list = []
    for pz in puzzle:
        if pz == "0" or pz=="''" or pz=='""' or pz=="()" or pz=="[]" or pz=="{}"or pz=="False" or pz=="None":
            TF = False
            T_F_list.append(TF)
        else:
            TF  = True
            T_F_list.append(TF)
         
    return T_F_list       
        
        
#Third mission
def calculate_magic_numbers(start, end):
        
    Bi_list = []
    for i in range(start,end):
        Bi_list.append(format(i,'04b'))
    return Bi_list


def exam_numbers(magic_nums):
    duration = 20  
    s = 0
    while True:
        ran = random.choice(magic_nums)
        print("\nYou have 20 seconds to answer each question...\n")
        print("Binary number:", ran)
        
        start_time = time.time()
        decimal = None
        i=0
        while True:
            time_up = time.time() - start_time
            if time_up > duration:
                print("\nTime's up!")
                s+=1
                break
            
            decimal = int(input("Enter the dicimal: "))
            #intDecimal = int(decimal)
            bi_decimal = bin(decimal)
            nbi = len(bi_decimal)
                
            if nbi==3:
                    c = bi_decimal[2:]
                    cp =  "000"+str(c)
                    if cp == ran:
                        print("Nice job! >O   O<")
                        print("             O    ")
                        s+=1
                        break
                    else:
                        print("Wrong Decimal!  >-   -<")
                        print("                   O")
                        
                    
            elif nbi == 4:
                    c = bi_decimal[2:]
                    cp =  "00"+str(c)
                    if cp == ran:
                        print("Nice job! >O   O<")
                        print("             O    ")
                        s+=1
                        break
                    else:
                        print("Wrong Decimal!  >-   -<")
                        print("                   O")
                        
                        

            elif nbi == 5:
                    c = bi_decimal[2:]
                    cp =  "0"+str(c)
                    if cp ==ran:
                        print("Nice job! >O   O<")
                        print("             O    ")
                        s+=1
                        break
                    else:
                        print("Wrong Decimal!  >-   -<")
                        print("                   O")
                        
                    
                        
            elif nbi == 6:
                    c = bi_decimal[2:]
                    if c == ran:
                        print("Nice job! >O   O<")
                        print("             O    ")
                        s+=1
                        break
                    else:
                        print("Wrong Decimal!  >-   -<")
                        print("                   O")
                        
            else:
                    print("OUT of RANGE!")
                    break
        if s>3:
            break
            




#The third mission    
def check_pass(info_list):
    chars = ['@','!','$','%','^','*','&','(',')','.','_','-',',','|','/']
    small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                     'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O'
                       , 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i in range(len(info_list)):
        s = 0
        c = 0
        l = 0
        L = len(info_list[i][1])            
        if L>=8:
                    l +=1
                    for sl in small_letters :
                        if sl in info_list[i][1]:
                            s +=1
                    for cl in capital_letters:
                        if cl in info_list[i][1]:
                            c +=1
        if l>0 and s>0 and c>0:
            return info_list[i][0]                        

file_text = open("C:\\Users\\TOSHIBA\\Desktop\\Decoding The Puzzle\mysterious.txt","r")
rd_file = file_text.read()
x = decrypt_clue(rd_file)

file = open("C:\\Users\\TOSHIBA\\Desktop\\Decoding The Puzzle\puzzles.txt","r+")
rd_file = file.readlines()
line = [line.rstrip('\n') for line in rd_file]
solved_puzzle = solve_puzzles(line)
   
start = 0
end = 16
magic_nums = calculate_magic_numbers(start,end)
test_num = exam_numbers(magic_nums)


employee_info = [("@ahmad","12345Sav#@"),("#ali","234t")]
userName = check_pass(employee_info)
if userName:
    print(f"{userName} has the strongest password!")
else:
    print("No one has striong password!")

unlock_vault(x,solved_puzzle,magic_nums,test_num, userName)


def draw_word():

    s = turtle.Screen()
    s.title("MAGIC")
    s.bgcolor("black")
    turtle.shape("turtle")
    turtle.speed("slow")
    turtle.pensize(4)
    turtle.pencolor("green")
    turtle.fillcolor("green")
    turtle.ht()
    
    turtle.penup()
    turtle.goto(140,50)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(50)
    turtle.right(30)
    turtle.forward(30)
    turtle.left(120)
    turtle.forward(30)
    turtle.left(125)
    turtle.forward(100)
        
    turtle.penup()
    turtle.goto(80,0)
    turtle.pendown()
    turtle.circle(-5,360)
    turtle.penup()
    turtle.goto(60,0)
    turtle.pendown()
    turtle.circle(-5,360)
    turtle.penup()
    turtle.goto(100,-20)
    turtle.pendown()
    turtle.left(150)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(45)
    turtle.forward(50)
        
    turtle.penup()
    turtle.goto(-30,-20)
    turtle.pendown()
    turtle.right(180)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(140)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(90)
    turtle.right(90)
    turtle.forward(50)
    turtle.penup()
    turtle.goto(-10,-60)
    turtle.pendown()
    turtle.circle(-5,360)
     

turtle.done() 
draw_word() 

