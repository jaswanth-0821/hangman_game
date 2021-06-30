import random
import json

# you will understand this code later
def fill(random_word, user_word, output_word):
    output_word = output_word.split()
    user_word = list(user_word)  # changing a string into a list
    random_word = list(random_word)
    if(len(user_word) >= len(random_word)):
        for i in range(len(random_word)):
            if(user_word[i] == random_word[i]):
                output_word[i] = random_word[i]
    else:
        for i in range(len(user_word)):
            if(user_word[i] == random_word[i]):
                output_word[i] = random_word[i]
    output_word = " ".join(output_word)  # changning of list into a string
    return output_word


# we should open a file before we give it to a vairable
f = open("dictionary.json")
data = json.load(f)  # loading a json file into a variable

# taking a random variable and giving key and value to respective variables
random_word, word_meaning = random.choice(list(data.items()))
output_word = list(random_word)
for i in range(len(random_word)):
    if((i != 0) and (i != (len(random_word) - 1))):
        output_word[i] = " _ "

output_word = "".join(output_word)
print(output_word)
for i in range(3):
    print(f'you have {3-i} chances only')
    print("")
    user_word = input("enter your guess: ",)
    if user_word == random_word:
        print("congrats your guess is right")
        print("")
        break
    else:
        if(i == 2):

            print("sorry your guess is wrong")
            print("")
            print("you last all your chances. The majic word is ")

            print(f'{random_word}')
            print(f'{random_word} means : {word_meaning}')
        else:
            output_word = fill(random_word, user_word, output_word)
            print(output_word)
            print("sorry your guess is wrong")
            print("")

print(f'if you want to try again please press "PLAY AGAIN"')
f.close()
