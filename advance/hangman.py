import random

words = ["screen", "random", "acronym", "platitude", "sober", "historic", "altitude"]
print("Enter your name: ")
name = input()
print("Welcome to Hangman", name, ", You will get 6 chances to guess a word")
word = random.choice(words)

def hangman(word):
    stages = ["",
              "_________        ",
              "         |       ",
              "         0       ",
              "        /|\      ",
              "        / \      ",
              "                 "]
    remaining_letters = list(word) # to convert the word in char
    wrong = 0
    board = ['__'] * len(word) # to show how many char are input right
    win = False

    while wrong < len(stages)-1:
        msg = "Guess a letter"
        char = input("Enter a char")
        if len(char) > 1:
            print("Illegal input enter only one char at a time.")
            char = input("Enter a char")
        if char in remaining_letters: # match the input and show the letter in output
            ind = remaining_letters.index(char)
            board[ind] = char
            remaining_letters[ind] = '$'
        else:
            wrong += 1
        print("".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if '__' not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("".join(stages[0:wrong]))
        print("You lose! it was {}.".format(word))


hangman(word)