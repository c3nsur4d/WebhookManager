import requests
import os
from termcolor import colored

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Effacer l'écran avant d'afficher les premières instructions
clear_console()
print(colored("""
                     ▄     ▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄   ▄    ▄▄   ▄▄ ▄▄▄▄▄▄ ▄▄    ▄ ▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   
                    █ █ ▄ █ █       █  ▄    █  █ █  █       █       █   █ █ █  █  █▄█  █      █  █  █ █      █       █       █   ▄  █  
                    █ ██ ██ █    ▄▄▄█ █▄█   █  █▄█  █   ▄   █   ▄   █   █▄█ █  █       █  ▄   █   █▄█ █  ▄   █   ▄▄▄▄█    ▄▄▄█  █ █ █  
                    █       █   █▄▄▄█       █       █  █ █  █  █ █  █      ▄█  █       █ █▄█  █       █ █▄█  █  █  ▄▄█   █▄▄▄█   █▄▄█▄ 
                    █       █    ▄▄▄█  ▄   ██   ▄   █  █▄█  █  █▄█  █     █▄   █       █      █  ▄    █      █  █ █  █    ▄▄▄█    ▄▄  █
                    █   ▄   █   █▄▄▄█ █▄█   █  █ █  █       █       █    ▄  █  █ ██▄██ █  ▄   █ █ █   █  ▄   █  █▄▄█ █   █▄▄▄█   █  █ █
                    █▄▄█ █▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄█ █▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄█ █▄█  █▄█   █▄█▄█ █▄▄█▄█  █▄▄█▄█ █▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄█  █▄█


""", 'cyan'))
webhook = input(colored("Bienvenue dans la console du gestionnaire de webhook ! Veuillez entrer votre webhook : ", "cyan"))
print(" ")

print(colored("Merci ! Maintenant, veuillez choisir 1 si vous voulez envoyer des messages dans le webhook ou 2 si vous voulez le supprimer : ", "cyan"), end="")

choice = input()

if choice == "1":
    clear_console()
    print(colored("""
    
                    ▄     ▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄   ▄       ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   
                    █ █ ▄ █ █       █  ▄    █  █ █  █       █       █   █ █ █     █       █       █       █  █▄█  █  █▄█  █       █   ▄  █  
                    █ ██ ██ █    ▄▄▄█ █▄█   █  █▄█  █   ▄   █   ▄   █   █▄█ █     █  ▄▄▄▄▄█    ▄  █   ▄   █       █       █    ▄▄▄█  █ █ █  
                    █       █   █▄▄▄█       █       █  █ █  █  █ █  █      ▄█     █ █▄▄▄▄▄█   █▄█ █  █▄█  █       █       █   █▄▄▄█   █▄▄█▄ 
                    █       █    ▄▄▄█  ▄   ██   ▄   █  █▄█  █  █▄█  █     █▄      █▄▄▄▄▄  █    ▄▄▄█       █       █       █    ▄▄▄█    ▄▄  █
                    █   ▄   █   █▄▄▄█ █▄█   █  █ █  █       █       █    ▄  █      ▄▄▄▄▄█ █   █   █   ▄   █ ██▄██ █ ██▄██ █   █▄▄▄█   █  █ █
                    █▄▄█ █▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄█ █▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄█ █▄█     █▄▄▄▄▄▄▄█▄▄▄█   █▄▄█ █▄▄█▄█   █▄█▄█   █▄█▄▄▄▄▄▄▄█▄▄▄█  █▄█

""", 'red'))
    print(colored("Bienvenue dans le WebhookSpammer ! Veuillez entrer le nombre de messages : ", "red"), end="")
    num_messages = int(input())
    print(" ")
    print(colored("Veuillez envoyer le message que vous souhaitez : ", "red"), end="")
    message = input()
    
    clear_console()
    for _ in range(num_messages):
        payload = {
            "content": message
        }
        response = requests.post(webhook, json=payload)
        if response.status_code == 204:

            print(colored("Message envoyé avec succès ! ", "green"), )
        else:
            print(colored("Webhook invalid!", "red"), end="")

            print(" ")
    
    print(colored("Si vous voulez supprimer le webhook, tapez 'delete'. ", "green"), end="")
    action = input()
    
    if action.lower() == "delete":
        requests.delete(webhook)
        clear_console()
        print("Webhook supprimé avec succès !")
    else:
        print("Opération terminée.")
    
elif choice == "2":
    clear_console()
    print(colored("""
                        ▄     ▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄   ▄       ▄▄▄▄▄▄  ▄▄▄▄▄▄▄ ▄▄▄     ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   
                        █ █ ▄ █ █       █  ▄    █  █ █  █       █       █   █ █ █     █      ██       █   █   █       █       █       █   ▄  █  
                        █ ██ ██ █    ▄▄▄█ █▄█   █  █▄█  █   ▄   █   ▄   █   █▄█ █     █  ▄    █    ▄▄▄█   █   █    ▄▄▄█▄     ▄█    ▄▄▄█  █ █ █  
                        █       █   █▄▄▄█       █       █  █ █  █  █ █  █      ▄█     █ █ █   █   █▄▄▄█   █   █   █▄▄▄  █   █ █   █▄▄▄█   █▄▄█▄ 
                        █       █    ▄▄▄█  ▄   ██   ▄   █  █▄█  █  █▄█  █     █▄      █ █▄█   █    ▄▄▄█   █▄▄▄█    ▄▄▄█ █   █ █    ▄▄▄█    ▄▄  █
                        █   ▄   █   █▄▄▄█ █▄█   █  █ █  █       █       █    ▄  █     █       █   █▄▄▄█       █   █▄▄▄  █   █ █   █▄▄▄█   █  █ █
                        █▄▄█ █▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄█ █▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄█ █▄█     █▄▄▄▄▄▄██▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█ █▄▄▄█ █▄▄▄▄▄▄▄█▄▄▄█  █▄█

    
    """, 'magenta'))
    print(" ")
    print(colored("Voulez-vous vraiment supprimer le webhook ? Tapez 'yes' pour oui et 'no' pour non : ", "magenta"), end="")
    confirmation = input()
    
    if confirmation.lower() == "yes":
        requests.delete(webhook)
        clear_console()
        print("Webhook supprimé avec succès !")
    elif confirmation.lower() == "no":
        print("Fermeture de la console.")
    else:
        print("Option invalide. Fermeture de la console.")
else:
    print("Choix invalide. Fermeture de la console.")