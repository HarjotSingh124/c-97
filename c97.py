import random
number = random.randint(1,9)
print("welcome to Number Guessing Game\n" + "choose a number between (1,9) " )
chances = 0
while (chances <5) :
  

  guess = input("Enter the Number: ")
  
    
  if(guess > str(number)):
    print("your guess was high: " + "guess a number lower than: " + guess)
    chances=chances+1

  if(guess < str(number)):
    print("your guess was low: " + "guess a number higher than: " + guess)
    chances=chances+1
  if(guess == str(number)):
    print("Congratulation You Won")
    chances=chances+1
    break
  if(chances >5):  
    print("you loose the game" + "the number is " + str(number))

  
 