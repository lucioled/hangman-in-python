from ntpath import join
import os
import random

if __name__ == "__main__":
    """ creat a list with words """
    words = []
    with open("./files/data.txt", "r", encoding="utf-8") as datafile:
        for line in datafile:
            words.append(line)
    """ Quit accents """
    for i, word in enumerate(words):
        whitout_accents = word.maketrans("áéíóú", "aeiou")
        new_word = word.translate(whitout_accents)
        words[i] = new_word
    """ Get a random word """
    HANGMAN_PICS = ['''  +---+
  |   |
      |
      |
      |
      |
=========''', '''  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

    def getRandomWord():
        ran_number = random.randint(0, len(words) - 1)
        return words[ran_number]

    def updateScreen(word):
        introd_letter = input("Elige una letra: ")
        if introd_letter in word:
            return introd_letter

    def drawHangman(attempts):
        if attempts == 6:
            print(HANGMAN_PICS[0])
        elif attempts == 5:
            print(HANGMAN_PICS[1])
        elif attempts == 4:
            print(HANGMAN_PICS[2])
        elif attempts == 3:
            print(HANGMAN_PICS[3])
        elif attempts == 2:
            print(HANGMAN_PICS[4])
        elif attempts == 1:
            print(HANGMAN_PICS[5])
        elif attempts == 0:
            print(HANGMAN_PICS[6])

    """ Present the game """
    def playHangman():

        print(""" █████   █████                                                                   
░░███   ░░███                                                                    
 ░███    ░███   ██████   ████████    ███████ █████████████    ██████   ████████  
 ░███████████  ░░░░░███ ░░███░░███  ███░░███░░███░░███░░███  ░░░░░███ ░░███░░███ 
 ░███░░░░░███   ███████  ░███ ░███ ░███ ░███ ░███ ░███ ░███   ███████  ░███ ░███ 
 ░███    ░███  ███░░███  ░███ ░███ ░███ ░███ ░███ ░███ ░███  ███░░███  ░███ ░███ 
 █████   █████░░████████ ████ █████░░███████ █████░███ █████░░████████ ████ █████
░░░░░   ░░░░░  ░░░░░░░░ ░░░░ ░░░░░  ░░░░░███░░░░░ ░░░ ░░░░░  ░░░░░░░░ ░░░░ ░░░░░ 
                                    ███ ░███                                     
                                   ░░██████                                      
                                    ░░░░░░                                       
-----------------------------------------------------------------------------------""")

        word = getRandomWord()
        word_length = len(word)-1
        word_socket = []
        attempts = 6
        for i in range(int(word_length)):
            word_socket.append(" _")
        while " _" in word_socket and attempts != 0:
            print("=-=-=-= Adivina la palabra =-=-=-=")
            print("Intentos: " + str(attempts))
            drawHangman(attempts)
            print("".join(word_socket) + "\n")

            letter = input("Elige una letra:  ")
            """ Check if letter has coincidences """
            for i, item in enumerate(word):
                if item == letter:
                    word_socket[i] = letter
            if letter in word_socket:
                pass
            else:
                attempts -= 1

            os.system("clear")

        if " _" in word_socket:
            print("¡Perdiste!")
            drawHangman(0)
            print("La palabra es:  " + word.upper())
            playAgain()

        else:
            print("¡Ganaste!")
            print("La palabra es:  " + word.upper())
            playAgain()
    """ Play again? """
    def playAgain():
        play_again = input("1. Jugar de nuevo"+"\n" +
                           "2. Salir del juego"+"\n"+"¿Que deseas hacer?  ")
        print("\n\n\n\n")
        if play_again == "1":
            playHangman()

    playHangman()
