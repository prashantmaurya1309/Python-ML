import random

with open('random words','r') as f:
    words= f.readlines()

word = random.choice(words)[:-1]

allowed_error = int(len(word))
done =False
guesses = []

while not done:
    for letters in word:
        if letters.lower() in guesses:
            print(letters, end=" ")
        else:
            print('_',end=' ')
    print('')

    guess = input(f'allowed error left {allowed_error} , next guess: ')
    guesses.append(guess.lower())
    if guess.lower() not in word:
        allowed_error -= 1
        if allowed_error == 0:
            break

    done =True
    for letter in word:
        if letter.lower() not in guesses:
            done = False

if done:
    print(f'you found the word {word}')
else:
    print(f'game over!! \n word was {word}')
