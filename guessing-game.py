import random
ChoosenNumber=random.randint(1,100)
difficulty=input("choose difficulty: h or e: ").lower()
print(ChoosenNumber)
if difficulty == "h":
    lives = 5
    while lives > 0:
        userInput = int(input("guess a number: "))
        if userInput > ChoosenNumber:
            print(f"bigger than the guess number!!\ntry again: {lives-1} lives remaining")
        elif userInput < ChoosenNumber:
            print(f"smaller than the guess number!!\ntry again: {lives-1} lives remaining")
        elif userInput == ChoosenNumber:
            print(f"yeaa your guess is correct!!", ChoosenNumber)
            break
        else:
            print("game over! Monster will eat you now ")
        lives -= 1

elif difficulty=="e":
    lives=10
    while lives>0:
        userInput=int(input("guess a number: "))
        if userInput>ChoosenNumber:
            print(f"bigger than the guess number!!\ntry again: {lives-1} lives remaining")
        elif userInput<ChoosenNumber:
            print(f"smaller than the guess number!!\ntry again: {lives-1} lives remaining")
        elif userInput==ChoosenNumber:
            print(f"yeaa your guess is correct!!",ChoosenNumber)
            break
        else : print("game over! Monster will eat you now")
        lives-=1  
else : print("choose korte bhul korsos bainchod")
