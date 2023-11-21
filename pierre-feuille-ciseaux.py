import random

choice_nb = {1: "la Pierre", 2: "la Feuille", 3: "le Ciseaux"}

def get_player_choice():
    while True:
        try:
            choice = int(input("Choisissez entre Pierre (1), Feuille (2) ou Ciseaux (3) : "))
            if 1 <= choice <= 3:
                return choice
            else:
                print("Veuillez choisir un nombre entre 1 et 3.")
        except ValueError:
            print("Veuillez entrer un nombre entier.")

def get_pc_choice():
    return random.randint(1, 3)

def winner(player_choice, pc_choice):
    if player_choice == pc_choice:
        return f"Égalité ! Vous avez tous les deux choisi {choice_nb[player_choice]}."
    elif (player_choice == 1 and pc_choice == 3) or \
         (player_choice == 2 and pc_choice == 1) or \
         (player_choice == 3 and pc_choice == 2):
        return f"Vous avez gagné ! {choice_nb[player_choice]} bat {choice_nb[pc_choice]}."
    else:
        return f"L'ordinateur a gagné ! {choice_nb[pc_choice]} bat {choice_nb[player_choice]}."

def main():
    print("---------------------☺---------------------")
    print("Bienvenue sur ce jeu de Pierre, Feuille, Ciseaux !")
    
    reponse = input("Souhaitez-vous consulter les règles (Y/N) ? ")
    if reponse.upper() == "Y":
        print("---------------------☺---------------------")
        print("Règles :")
        print("- Le but du jeu est de vaincre l'ordinateur. - ")
        print("------> - La partie se joue en 1 manche !")
        print("------> - Vous avez le choix entre Pierre, Feuille, Ciseaux,")
        print("------> - Une fois votre choix fait, l'ordinateur fait son choix aléatoirement,")
        print("------> - Ensuite, l'affrontement : La Pierre bat le Ciseaux, le Ciseaux bat la Feuille, et la Feuille bat la Pierre.")
        print("---------------------☺---------------------")
    
    while True:
        player_choice = get_player_choice()
        pc_choice = get_pc_choice()
        
        print("---------------------☺---------------------")
        print(f"Vous avez choisi {choice_nb[player_choice]}")
        print(f"L'ordinateur a choisi {choice_nb[pc_choice]}")

        result = winner(player_choice, pc_choice)
        print("---------------------☺---------------------")
        print(result)
        print("---------------------☺---------------------")

        play_again = input("Voulez-vous jouer à nouveau ? (Y/N) : ")
        if play_again.upper() != "Y":
            print ("Merci d'avoir joué ! A bientôt :)")
            print("---------------------☺---------------------")
            break

main()