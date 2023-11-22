import random

# Dictionnaire pour les choix possibles et leur numéro associé
choice_nb = {1: "la Pierre", 2: "la Feuille", 3: "le Ciseaux"}

# Dictionnaire pour les résultats possibles du jeu
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

# Fonction pour vérifier si un nombre est entier dans une plage donnée
def ask_int(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Veuillez choisir un nombre entre {min_val} et {max_val}.")
        except ValueError:
            print("Veuillez entrer un nombre entier.")

# Fonction pour obtenir le choix de l'ordinateur (aléatoire)
def get_pc_choice():
    return random.randint(1, 3)

# Fonction pour déterminer le gagnant
def winner(player_choice, pc_choice):
    result_winner = (player_choice, pc_choice)
    return results.get(result_winner, "Choix invalides.")

# Fonction principale du jeu
def main():
    print("---------------------☺---------------------")
    print("Bienvenue sur ce jeu de Pierre, Feuille, Ciseaux !")
    
    reponse = input("Souhaitez-vous consulter les règles (Y/N) ? ")
    if reponse.upper() == "Y":
        # Affichage les règles du jeu
        print("---------------------☺---------------------")
        print("Règles :")
        print("- Le but du jeu est de vaincre l'ordinateur. - ")
        print("------> - La partie se joue en 1 manche !")
        print("------> - Vous avez le choix entre Pierre, Feuille, Ciseaux,")
        print("------> - Une fois votre choix fait, l'ordinateur fait son choix aléatoirement,")
        print("------> - Ensuite, l'affrontement : La Pierre bat le Ciseaux, le Ciseaux bat la Feuille, et la Feuille bat la Pierre.")
    
    while True:
        print("---------------------☺---------------------")
        # Demande du choix du joueur
        player_choice = ask_int("Choisissez entre Pierre (1), Feuille (2) ou Ciseaux (3) : ", 1, 3)
        pc_choice = get_pc_choice()  # Obtenir le choix de l'ordinateur
        
        print("---------------------☺---------------------")
        print(f"Vous avez choisi {choice_nb[player_choice]}")
        print(f"L'ordinateur a choisi {choice_nb[pc_choice]}")

        result = winner(player_choice, pc_choice)  # Détermination du résultat
        print("---------------------☺---------------------")
        print(result)  # Affichage du résultat de la manche
        print("---------------------☺---------------------")

        play_again = input("Voulez-vous jouer à nouveau ? (Y/N) : ")
        if play_again.upper() != "Y":
            print("Merci d'avoir joué ! A bientôt :)")
            print("---------------------☺---------------------")
            break

# Appeler la fonction principale pour lancer le jeu
main()
