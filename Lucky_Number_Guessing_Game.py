import random
secret_number = random.randint(1, 15)
guesse_count = 0
guesse_limit = 3
while guesse_count < guesse_limit:
    guess = int(input("guess(from 1 to 15):"))
    guesse_count += 1
    if guess == secret_number:
        print("you won!")
        break
else:
    print('sorry you failed')
    print(secret_number)
exit = input("press enter to exit")





