"""ROCK PAPER SCISOR GAME WAOOOOOOOOOOOOOO"""
import random
computer = (random.randint(0, 2))
def check(computer, user):
     
     if computer == user:
          return 0 #draw

     if (computer == 0 and user == 1):
           return -1 #loss

     if (computer == 1 and user == 2):
          return -2 #loss
     
     if (computer == 0 and user == 2):
          return -3 #win

     if (computer == 2 and user == 0):
          return -4 #win
user = int(input("0 is for ROCK and 1 for scisor and 2 for paper\n"))
score = check(computer, user)
print("you:", user)
print("computer:", computer)

if(score == 0):
      print("its draw")

elif(score == -3):
 print("you win")

else:
 print("you loss")