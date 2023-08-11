import random
import time

from RandomWord import random_word
numOfUsernames=0
while numOfUsernames <= 0:
    try:
        numOfUsernames = int(input("How many usernames do you want to generate? "))
        if numOfUsernames <= 0:
            print("Please enter a number higher than 0.")
    except ValueError:
        print("You need to enter a number.")

start = time.time()

adjective = random_word('english-adjectives.txt',1000)
noun = random_word('english-nouns.txt',1000)

generatedAmount = 0
for usernames in range(numOfUsernames):

    generatedAmount += 1

    adjective = random_word('english-adjectives.txt',1000)
    noun = random_word('english-nouns.txt',1000)    

    username = f"{adjective.title()}{noun.title()}{random.randint(1,9999):04d}"

    print(f"Usernames generated: {generatedAmount}")

    file = open('usernames.txt','a')
    file.write(f'{username}\n')
end = time.time()
print(f"\n You generated {numOfUsernames} usernames in {round((end-start),5)} seconds")