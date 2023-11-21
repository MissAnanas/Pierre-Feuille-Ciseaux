import random

choice_nb = {1: "la Pierre", 2: "la Feuille", 3: "le Ciseaux"}
results = {
    (1, 1): "Égalité ! Vous avez tous les deux choisi la Pierre.",
    (2, 2): "Égalité ! Vous avez tous les deux choisi la Feuille.",
    (3, 3): "Égalité ! Vous avez tous les deux choisi le Ciseaux.",
    (1, 3): "Vous avez gagné ! La Pierre bat le Ciseaux.",
    (2, 1): "Vous avez gagné ! La Feuille bat la Pierre.",
    (3, 2): "Vous avez gagné ! Le Ciseaux bat la Feuille.",
    (3, 1): "Vous avez perdu ! Le Ciseaux bat la Pierre.",
    (1, 2): "Vous avez perdu ! La Pierre bat la Feuille.",
    (2, 3): "Vous avez perdu ! La Feuille bat le Ciseaux."
}

def ask_int(nb, min_val, max_val):
    while True:
        try:
            value = int(input(nb))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Veuillez choisir un nombre entre {min_val} et {max_val}.")
        except ValueError:
            print("Veuillez entrer un nombre entier.")

def get_pc_choice():
    return random.randint(1, 3)

def winner(player_choice, pc_choice):
    result_winner = (player_choice, pc_choice)
    return results.get(result_winner, "Choix invalides.")

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
    
    while True:
        print("---------------------☺---------------------")
        player_choice = ask_int("Choisissez entre Pierre (1), Feuille (2) ou Ciseaux (3) : ", 1, 3)
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
            print("Merci d'avoir joué ! A bientôt :)")
            print("---------------------☺---------------------")
            break

main()
