
import random
import hangman_art
import hangman_words
from replit import clear

#Escoge una palabra de la lista hangman_words
chosen_word = random.choice(hangman_words.word_list)

word_length = len(chosen_word)

end_of_game = False
lives = 6

#Imprime el logo de Hangman

print(hangman_art.logo)

#Codigo de prueba
#print(f'Pssst, la solucion es {chosen_word}.')

#Crea espacios
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()

    #Si el usuario ya habia introducido la letra que adivinó, imprime la letra y se le hace saber.

    if guess in display:
      print(f"You've already guessed {guess}")

    #Verifica la letra adivinada
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Verifica si el usuario se equivocó.
    if guess not in chosen_word:
        #Si la letra no está en la palabra escogida, imprime la letra y le hace saber que no esta en la palabra.
        print (f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose :(.")

    #Une todos los elementos de la lista y lo convierte en un string.
    print(f"{' '.join(display)}")

    #Verifica si el jugador tiene todas las letras.
    if "_" not in display:
        end_of_game = True
        print("You win!!.")

    #Importa los escenarios del colgado.
    print(hangman_art.stages[lives])
