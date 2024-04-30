import random

ChoosenNumber=random.randint(1,100)
difficulty=input("Choose Difficulty: Hard or Easy: ").lower()

if difficulty == "hard":
    LIVES = 5
    while LIVES > 0:
        userInput = int(input("guess a number: "))
        if userInput > ChoosenNumber:
            print(f"bigger than the guess number!!\ntry again: {LIVES-1} lives remaining")
        elif userInput < ChoosenNumber:
            print(f"smaller than the guess number!!\ntry again: {LIVES-1} lives remaining")
        elif userInput == ChoosenNumber:
            print("yeaa your guess is correct!!", ChoosenNumber)
            break
        else:
            print("game over! Monster will eat you now ")
        LIVES -= 1

elif difficulty=="easy":
    LIVES=10
    while LIVES>0:
        userInput=int(input("guess a number: "))
        if userInput>ChoosenNumber:
            print(f"bigger than the guess number!!\ntry again: {LIVES-1} lives remaining")
        elif userInput<ChoosenNumber:
            print(f"smaller than the guess number!!\ntry again: {LIVES-1} lives remaining")
        elif userInput==ChoosenNumber:
            print("yeaa your guess is correct!!",ChoosenNumber)
            break
        else : print("game over! Monster will eat you now")
        LIVES -= 1

else : print("choose korte bhul korsos bainchod")