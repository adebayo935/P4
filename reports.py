import json
from operator import itemgetter

def list_players():
    print("--- Liste des joueurs ---\n")

    print("1. Par classement\n")
    print("2. Par ordre alphabétique\n")
    choice = input("Votre choix : ")

    file = json.load(open("db_players.json"))

    if choice == 1:
        i = 1
        while file['players']:
            items = list((file['players'][str(i)].items()))
            print(items)
            newfile = sorted(items, key=itemgetter(0))
            print(newfile)
            i += 1
            break
    else:
         i = 1
         while file['players']:
            items = list((file['players'][str(i)].items()))
            new_items = tuple(items)
            print(items)
            print(new_items)
            newfile = sorted(items, key=itemgetter(1)(0))
            print(newfile)
            i += 1
            continue