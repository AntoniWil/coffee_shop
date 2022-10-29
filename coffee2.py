print('''                                                            
                         ad88    ad88                       
                        d8"     d8"                         
                        88      88                          
 ,adPPYba,  ,adPPYba, MM88MMM MM88MMM ,adPPYba,  ,adPPYba,  
a8"     "" a8"     "8a  88      88   a8P_____88 a8P_____88  
8b         8b       d8  88      88   8PP""""""" 8PP"""""""  
"8a,   ,aa "8a,   ,a8"  88      88   "8b,   ,aa "8b,   ,aa  
 `"Ybbd8"'  `"YbbdP"'   88      88    `"Ybbd8"'  `"Ybbd8"'  
                                                            
         88                                             
          88                                             
          88                                             
,adPPYba, 88,dPPYba,   ,adPPYba,  8b,dPPYba,    
I8[    "" 88P'    "8a a8"     "8a 88P'    "8a   
 `"Y8ba,  88       88 8b       d8 88       d8    
aa    ]8I 88       88 "8a,   ,a8" 88b,   ,a8"  
`"YbbdP"' 88       88  `"YbbdP"'  88`YbbdP"'    
                                  88                     
                                  88         
              ________
             / ______ \
             || _  _ ||
             ||| || |||
             |||_||_|||
             || _  _o|| (o)
             ||| || |||
             |||_||_|||      ^~^  ,
             ||______||     ('Y') )
            /__________\    /   \/
    ________|__________|__ (\|||/) _________
    ____________________\
   `       |____________|\n\n''')

                                                            
print("Welcome to my coffe shop!!")



name = input("Hello what is your name?\n")

menu = "Ice caramel.\nIce mocha.\nBlack coffe.\nLatte.\nCappucino.\nEspresso.\nSpecial menu\n\n"



print("hello " + name + ", thank you so much for coming to my coffe shop today\n")


drink = input(name + ", what would you like from our menu today? Here is what we are serving.\n" + menu)


if(drink == "Special menu"): 
  drink = input("Special menu ($7)!!\nHot coco\nHot coffe\nHot matcha\nSoda coffe\nGo back\n")
  if(drink == "Go back"):
    drink = input(name + ", what would you like from our menu today? Here is what we are serving.\n" + menu)



if drink == "Ice caramel":
  price = 5
elif drink == "Ice mocha":
  price = 6
elif drink == "Black coffe":
  price = 4
elif drink == "Latte":
  price = 5
elif drink == "Capuchino":
  price = 6
elif drink == "Espresso":
  price = 5
elif drink == "Hot coco":
  price = 7
elif drink == "Hot coffe":
  price = 4
elif drink == "Hot matcha":
  price = 7
elif drink == "Soda coffe":
  price = 7
  


print("That drink costs $" + str(price))

quantity = input("how many " + drink + ", would you like?\n")

total = price * int(quantity)


print("thenk you. Your total is: $" + str(total))


print("sounds good " + name + ", we'll have your " + quantity + " " + drink + " redy for you in a moment.\n")



print('''

                             ______________________
                            (___________           |
                              [XXXXX]   |          |
                         __  /~~~~~~~\  |          |
       CT               /  \|@@@@@@@@@\ |          |
         )              \   |@@@@@@@@@@||          |
        (                   \@@@@@@@@@@||  ______  |
       __)__                 \@@@@@@@@/ | |on|off| |
    C\|     \               __\@@@@@@/__|  ~~~~~~  |
      \     /              (____________|__________|
       \___/               |_______________________|
                      

''')

