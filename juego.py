import os
import random

content = []

def phrase():
    with open("./archivos/data.txt", "r") as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        return content[random.randint(0, len(content))]

def clean_console():
    os.system("clear")

def get_input():
    while True:
        value = input("Ingresa una letra: ")
        if len(value) > 1:
            raise ValueError("No se admite mas de una letra")
        elif len(value) == 0:
            raise ValueError("Por Favor ingresar una letra, no se admiten textos vacios")
        
        return value.lower()

def progress(actual_words, list_words):
    print("¡Adivina la palabra!")

    status = ""
    ESPACIO = " _ "

    for i in range(0, len(list_words) ):
        if i >= len(actual_words):
            status += ESPACIO
            continue
        elif actual_words[i] == list_words[i]:
            status += f" {actual_words[i].upper()} "
        else:
            status += ESPACIO
    
    print(status + "\n")

actual_words = []

def validate_character(new_character, objetive):
    e_listWords = enumerate(objetive)

    for position, character in e_listWords:
        if character.lower() == new_character:
            actual_words[position] = new_character

def game(objetive):
    myList_words = []
    for character in objetive:
        myList_words.append(character)
        actual_words.append("")

    while actual_words != myList_words:
        progress(actual_words, myList_words)
        get_actual = get_input()
        validate_character(get_actual, myList_words)
        clean_console()

    print("=====================================")
    print(f"=== ¡Ganaste! La palabra era {objetive} ===")
    print("=====================================")

def run():
    print("")
    # game("papá")

if __name__ == '__main__':
    run()