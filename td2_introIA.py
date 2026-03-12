import re
import random

def addition(rep_defaut, memoire, msg_user, match_regex): #fonction qui permet de calculer deux nombres
    print("Veuillez saisir votre calcul (ex : 5+9): ")
    a = int(input(""))
    print("+")
    b = int(input(""))
    print(f"{a}+{b}= {a+b}")

def nombre_mystere(rep_defaut, memoire, msg_user, match_regex):
    nb_alea = random.randint(0, 10)
    print(nb_alea)
    reponse = int(input("Essayez de trouver le nombre auquel je pense...(Indice : c'est entre 0 et 10) : "))
    if reponse == nb_alea:
        print("\nBravo! Vous avez gagnez!")
    else:
        print("\nPerdu ! HAhaaAHHA")

def prenom(rep_defaut, memoire, msg_user, match_regex):
    prenom = "Lys"
    memoire["nom"] = prenom #Il faudrai récupérer ici le mot juste après le match (donc le mot qui s'arrête au prochain espace)
    print(f"{rep_defaut} {prenom}")

    return memoire


regles_V1 = [ #Ensembles des règles pour le chatbot
    ["Règle Salutation", "bonjour|salut", "Bonjour humain comment t'appelles-tu?"],
    ["Règle Au revoir", "au revoir|bye", "Au revoir humain!"],
    ["regle capable", "capable", "Je peux vous parler des futurs JO, mais je sais aussi calculer"],
    ["Règle défaut", "", "Je ne sais pas quoi répondre..."]
]

regles_V2 = [ #Nom de la fonction, priorité, pattern, réponse, fonction
    ["Règle Salutation", 2, "bonjour|salut", "Bonjour humain, comment t'appelles-tu?", None],
    ["Règle Au revoir", 1, "au revoir|bye", "Au revoir humain!", None],
    ["regle capable", 6, "capable", "Je peux vous parler des futurs JO, mais je sais aussi calculer",None],
    ["regle  JO",5 , "JO", "Les prochains JO auront lieu à Paris en 2024.",None],
    ["Règle calcul", 4, "calcul*", "Vous voulez calculer, allons-y : ", addition],
    ["Règle jeu nombre aléatoire", 5, "jouer", "Très bien, jouons!", nombre_mystere],
    ["Règle prénom", 3, "je m'appelle", "Bienvenue", prenom],
    ["Règle défaut", 7, "", "Je ne sais pas quoi répondre...", None] #patterne vide donc toutes les entrées utilisateurs déclencheront cette regle
]

print(">>> Vous commencez votre conversation avec PAM. Pour quitter la conversation entrez 0.")
User_data = {}
Boucle=True
while Boucle:
    User_Input = str(input("> "))
    if User_Input == "0": 
        Boucle=False #on quitte la boucle si l'utilisateur rentre "0"
    else:

        for regle in regles_V2:
            pattern = re.compile(regle[2],re.IGNORECASE) #compile les patternes dans les regles en expressions regex (majuscules ignorées par re.IGNORECASE)
            if re.search(pattern, User_Input): #cherche le pattern dans l'entrée utilisateur
                print(f"\n{regle[3]}") #Si le pattern est trouvé alors on print la réponse appropriée

                if regle[-1] != None: #si la regle nécéssite l'utilisation d'une fonction tierce
                    regle[-1](regle[-2], User_data, User_Input, re.search(pattern, User_Input)) #alors on appelle la fonction
                break


print("\n>>> Fin de la conversation.")