import random
from RandomWord import random_word
numOfUsernames=0
while numOfUsernames==0:
    try:
        numOfUsernames = int(input("How many usernames do you want to generate? "))
    except ValueError:
        print("You need to enter a number.")
    


adjective = random_word('english-adjectives.txt',1000)
noun = random_word('english-nouns.txt',1000)
for usernames in range(numOfUsernames):
    adjective = random_word('english-adjectives.txt',1000)
    noun = random_word('english-nouns.txt',1000)    
    username = f"{adjective.title()}{noun.title()}{random.randint(1,9999):04d}"
    print(username)

    file = open('usernames.txt','a')
    file.write(f'{username}\n')