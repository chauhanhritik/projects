import random
def choice(p1,c1):         #	to display comp and user choice
	if p1.lower()=='r':
		p1 = 'rock'
	elif p1.lower()=='s':
		p1 = "scissor"
	else:
		p1 = 'paper'
	if c1.lower() == 'r':
		c1 = 'rock'
	elif c1.lower() == 's':
		c1 = 'scissor'
	else:
		c1 = 'paper'
	print(f"You chose : {p1}. Comp chose : {c1} ")  	
def decision(p1,c1):    #checking who won
    if (p1==c1):
        print("it's a draw")
    elif c1.lower()=="s":
        if p1.lower()=="r":
            print('YOU WIN!!!')
        else:
            print("YOU LOSE")
    elif c1.lower()=='r':
        if p1.lower()==p:
            print("YOU WIN")
        else:
            print('YOU LOSE')
    elif c1.lower()=='p':
        if p1.lower() =='r':
            print('YOU LOOSE')
        else:
            print("YOU WIN")
		
x = 1
while(x!=0):
    p = input("Enter your choice: rock(r), paper(p), or scissor(s) : ") #inputting the user choice
    c = random.randint(1,3)   #taking the computer choice
    if c==1:
        c= 'r'
    elif c==2:
        c='p'
    else:
    	c='s'
    if p=='r' or p== 'R' or p=='S' or p=='s' or p=='p' or p=='P':   #checking if user entered a valid choice or not
        choice(p,c)
        decision(p,c)   #if true then check who wins
    else:
        print('WRONG CHOICE')
