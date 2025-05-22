#Guess my fav fruit
import random
fav = ["Apple", "Banana", "Mango", "Goava", "Pine apple", "Grapes", "Papaya"]
fav1 = random.choice(fav)
print(fav)
guess = input("Guess my favouriate fruit from the list and win a game: ")
#for i in range(len(fav)):
if(guess == fav1):
    print("My favouriate fruit is ", fav1)
    print("Your guess is ",guess)
    print("Yay......!! You got it")
else:
    print("My favouriate fruit is ", fav1)
    print("Your guess is ",guess)
    print("Aww...........!! better luck next time")