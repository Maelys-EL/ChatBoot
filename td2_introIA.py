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
    ["Règle Salutation", "[bB]onjour|[sS]alut", "Bonjour humain, je suis PAM, comment t'appelles-tu?"],
    ["Règle Au revoir", "[aA]u revoir|[bB]ye", "Bye bye humain!"],
    ["Règle ILM", "I love myself", "I love me!"], 
    ["Règle DUNNO", "", "I don't know what to say..."]
]

regles_V2 = [ #Nom de la fonction, priorité, pattern, réponse, fonction
    ["Règle Salutation", 2, "[bB]onjour|[sS]alut", "Bonjour humain, je suis PAM, comment t'appelles-tu?", None],
    ["Règle Au revoir", 1, "[aA]u revoir|[bB]ye", "Bye bye humain!", None],
    ["Règle ILM", 6, "I love myself", "I love me!", None], 
    ["Règle calcul", 4, "[cC]alcul*", "Vous voulez calculer, allons-y : ", addition],
    ["Règle jeu nombre aléatoire", 5, "[jJ]ouer", "Très bien, jouons!", nombre_mystere],
    ["Règle prénom", 3, "[jJ]e m'appelle", "Bienvenu", prenom],
    ["Règle DUNNO", 7, "", "I don't know what to say...", None]
]

print(">>> Vous commencez votre conversation avec PAM. Pour quitter la conversation entrez 0.")
User_data = {}

while True:
    User_Input = str(input("> "))
    if User_Input == "0":
        break
    else:
        trouve = False

        for regle in regles_V2:
            pattern = re.compile(regle[2])
            if re.search(pattern, User_Input):
                print(f"\n{regle[3]}") #Pour les réponse avec fonction, ça fait doublon ici !
                trouve = True
                if regle[-1] != None:
                    regle[-1](regle[-2], User_data, User_Input, re.search(pattern, User_Input))
                break

        if not trouve:
            print(f"\n{regles_V2[-1][3]}")

print("\n>>> Fin de la conversation.")