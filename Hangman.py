import random
from Humanbodyparts import Human_parts
import string

def hangman():
    word = random.choice(Human_parts).upper()  # randomly chooses something from the list
    no_of_letterwords = set(word)
    upper_letter = set(string.ascii_uppercase)
    used_letters = set()
    
    lives = 7

    while len(no_of_letterwords) > 0 and lives > 0:
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
        join_word = [letter if letter in used_letters else '-' for letter in word]
        print('The current word:', ' '.join(join_word))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in upper_letter - used_letters:
            used_letters.add(user_letter)
            if user_letter in no_of_letterwords:
                no_of_letterwords.remove(user_letter)
                print('')
            else:
                lives -= 1
                print('\nYour letter,', user_letter, 'is not in the word.')
        elif user_letter in used_letters:
            print('The letter is already used.')
        else:
            print('Invalid letter.')

    if lives == 0:
        print('You died. The word was', word)
    else:
        print('You guessed the word', word, '!!')

if __name__ == '__main__':
    hangman()
