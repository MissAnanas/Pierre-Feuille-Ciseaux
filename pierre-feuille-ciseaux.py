import random

choices_mapping = {1: "la Pierre", 2: "la Feuille", 3: "le Ciseaux"}

def get_user_choice():
    while True:
        try:
            choice = int(input("Choisissez entre Pierre (1), Feuille (2) ou Ciseaux (3) : "))
            if 1 <= choice <= 3:
                return choice
            else:
                print("Veuillez choisir un nombre entre 1 et 3.")
        except ValueError:
            print("Veuillez entrer un nombre entier.")

def get_computer_choice():
    return random.randint(1, 3)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return f"Égalité ! Vous avez tous les deux choisi {choices_mapping[user_choice]}."
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        return f"Vous avez gagné ! {choices_mapping[user_choice]} bat {choices_mapping[computer_choice]}."
    else:
        return f"L'ordinateur a gagné ! {choices_mapping[computer_choice]} bat {choices_mapping[user_choice]}."

def main():
    print("Bienvenue dans le jeu Pierre-Papier-Ciseaux !")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"Vous avez choisi {choices_mapping[user_choice]}")
        print(f"L'ordinateur a choisi {choices_mapping[computer_choice]}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("Voulez-vous jouer à nouveau ? (Y/N) : ")
        if play_again.lower() != "N":
            print("Merci d'avoir joué. Au revoir !")
            break

if __name__ == "__main__":
    main()