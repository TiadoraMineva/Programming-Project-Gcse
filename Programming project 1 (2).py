import random
p1point = 0
p2point = 0
number11= 0
number12=0
number21=0
number22=0
counter =0
total1=0
total2=0
authentication2=False
authentication1= False
game= False
people=["Megha","Casper","Emil","Hugo","Lyce", "Tia", "q", "w","Mum","Grandad"]


while authentication1== False:
    P1name = input("Player 1, please enter a name ")
    if P1name in people:
        authentication1= True

while authentication2 == False:
        P2name = input("Player 2, please enter a name ")
        if P2name in people:
            authentication2 = True


if authentication1== True:
        while authentication2== True:
            while counter < 5:
                number11 = random.randint(1, 6)
                number12 = random.randint(1, 6)
                number21 = random.randint(1, 6)
                number22 = random.randint(1, 6)
                # adds the points
                p1point = p1point + number11 + number12
                p2point = p2point + number21 + number22
                # adds or takes away point if it is even or odd
                total1 = number11 + number12
                total2 = number21 + number22
                if total1 % 2 == 0:
                    p1point = p1point + 10
                else:
                    p1point = p1point - 5
                if total2 % 2 == 0:
                    p2point = p2point + 10
                else:
                                p2point = p2point - 5
                if number11==number12:
                    number1d=random.randint(1,6)
                    p1point=p1point+number1d

                if number21 == number22:
                    number2d = random.randint(1, 6)
                    p2point = p2point + number2d

                enter= input ("Press enter key to continue")
                counter = counter+ 1

                print(" Player 1,your score on round " + str(counter) ,"is " + str(total1), "and your total score is "+ str(p1point))
                print(" Player 2, your score on round " + str(counter) ,"is " + str(total2), "and your total score is "+ str(p2point))
                print("                                              ")
                print("                                              ")
                print("                                              ")
                print("                                              ")



            if p1point < p2point:
                print("Congratulations "+ P2name, "You have won!!")
                authentication1= False
            else :
                print("Congratulations " + P1name, "You have won!!")
                authentication1= False
            break

print("yes, we are here")
file=open("leaderboard.txt", "w")
file.write("LeaderBoard")
file.close()




