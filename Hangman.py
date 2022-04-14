import random
import os


def clear():
  os.system("cls") if os.name=="nt" else os.system("clear")


gameover = False

words = "ape cat dog baboon elephant giraffe apple coconut " \
        "monkey rubik mice mouse pineapple android apple house fence python grail " \
        "zerg protoss terran llama fire policeman zebra lion luffy " \
        " universidad".split()

wordIndex = random.randint(0, len(words)-1)
word = words[wordIndex]

list_of_letters = list(word)
list_of_found = list()
list_of_picked = list()
fails = 0
word_length = len(word)
letters_in_word = list(word)

list_of_hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

list_of_correct_guesses = list()
for i in range(word_length):
    list_of_correct_guesses.append("_")


while not gameover:

    # INTERFACE
    print("\nplease pick a letter \n", list_of_hangman[fails], "\nPrevious letters picked:\n", list_of_picked,
          "\nCorrect Guesses: \n")

    blank = "_"
    list_of_blanks = list()
    print(list_of_correct_guesses)

    letter = input()


    # IF MORE THEN ONE LETTER IS ENTERED OR IF SOMETHING OTHER THEN AN ENGLISH LETTER IS ENTERED
    if len(letter) > 1 or letter.isalpha() == False:
        if letter.isalpha() == False:
            print("you must pick an english letter!")
        elif len(letter) > 1:
            print("you can only pick one letter at a time!")

    # IF LETTER IS ALREADY PICKED
    elif letter in list_of_found or letter in list_of_picked:
        print("you already picked that letter!")

    # IF LETTER IS CORRECT
    elif letter in list_of_letters:
        list_of_found.append(letter)

        for i in range(word_length):
            if letter == list_of_letters[i]:
                list_of_correct_guesses[i] = list_of_letters[i]

        if "_" not in list_of_correct_guesses:
            print(list_of_hangman[fails], list_of_picked, "\nCorrect Guesses: \n", list_of_correct_guesses)
            print ("\nGood Job You Win!")
            gameover = True

    # IF LETTER IS INCORRECT
    elif letter not in list_of_letters:
        print("\nnope!")
        list_of_picked.append(letter)
        fails += 1
        if fails == 6:
            print(list_of_hangman[fails])
            gameover = True
    clear()