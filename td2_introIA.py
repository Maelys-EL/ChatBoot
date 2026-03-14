import re
import random

def addition(rep_defaut, memoire, msg_user, match_regex): #fonction qui permet de calculer deux nombres
    print("Saisissez le premier nombre :")
    a = input("")
    try: a=int(a) #vérifie que l'entrée est un nombre
    except ValueError:
        print("ce n'est pas un nombre")
        return
    
    print("Saisissez le second nombre :")
    b = input("")
    try: b=int(b) #vérifie que l'entrée est un nombre
    except ValueError:
        print("ce n'est pas un nombre")
        return
    print(f"{a}+{b}= {a+b}")

def nombre_mystere(rep_defaut, memoire, msg_user, match_regex):
    nb_alea = random.randint(0, 10)
    reponse = input("Essayez de trouver le nombre auquel je pense...(Indice : c'est entre 0 et 10) : ")
    try: reponse=int(reponse) #vérifie que l'entrée est un nombre
    except ValueError:
        print("ce n'est pas un nombre")
        return
    
    if reponse == nb_alea:
        print("\nBravo! Vous avez gagnez!")
    else:
        print("\nPerdu !")

def prenom(rep_defaut, memoire, msg_user, match_regex):
    memoire["nom"] = msg_user.split()[-1]
    print("Bienvenue",memoire["nom"])

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
    ["regle  JO",5 , r"\bJO\b", "Les prochains JO auront lieu à Paris en 2024.",None], # \b = caracteres qui délimitent un mot soit espace virgule etc.. r devant pour que python ne prenne pas directement les antislash en compte
    ["Règle calcul", 4, "calcul*", "Vous voulez calculer, allons-y : ", addition],
    ["Règle jeu nombre aléatoire", 5, "jouer", "Très bien, jouons!", nombre_mystere],
    ["Règle prénom", 3, "je m'appelle|je suis", "", prenom],
    ["Règle défaut", 7, "", "Je ne sais pas quoi répondre...", None] #patterne vide donc toutes les entrées utilisateurs déclencheront cette regle
]

regles_V2.sort(key=lambda list: list[1])

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