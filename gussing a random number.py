import random
r=random.randint(1,50)

while(True):
    inp=int(input())
    if(inp<r):
        print("Wrong guess,Try a greater number")
    elif (inp > r):
         print("Wrong guess,Try a smaller number")
    else:
         print("Congrats,You have gussed a right number") 
    break;  
