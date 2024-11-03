# todo_list.py

def afficher_taches(taches):
    print("Liste de Tâches :")
    for i, tache in enumerate(taches, start=1):
        print(f"{i}. {tache}")

def ajouter_tache(taches, tache):
    taches.append(tache)
    print(f"Tâche ajoutée : {tache}")

def supprimer_tache(taches, index):
    if 0 <= index < len(taches):
        removed = taches.pop(index)
        print(f"Tâche supprimée : {removed}")
    else:
        print("Index invalide.")

def main():
    taches = []
    
    while True:
        print("\nOptions :")
        print("1. Afficher les tâches")
        print("2. Ajouter une tâche")
        print("3. Supprimer une tâche")
        print("4. Quitter")
        
        choix = input("Choisissez une option : ")

        if choix == '1':
            afficher_taches(taches)
        elif choix == '2':
            tache = input("Entrez la nouvelle tâche : ")
            ajouter_tache(taches, tache)
        elif choix == '3':
            index = int(input("Entrez le numéro de la tâche à supprimer : ")) - 1
            supprimer_tache(taches, index)
        elif choix == '4':
            print("Au revoir !")
            break
        else:
            print("Option invalide, essayez à nouveau.")

if __name__ == "__main__":
    main()
# todo_list.py

def afficher_taches(taches):
    print("Liste de Tâches :")
    for i, tache in enumerate(taches, start=1):
        print(f"{i}. {tache}")

def ajouter_tache(taches, tache):
    taches.append(tache)
    print(f"Tâche ajoutée : {tache}")

def supprimer_tache(taches, index):
    if 0 <= index < len(taches):
        removed = taches.pop(index)
        print(f"Tâche supprimée : {removed}")
    else:
        print("Index invalide.")

def main():
    taches = []
    
    while True:
        print("\nOptions :")
        print("1. Afficher les tâches")
        print("2. Ajouter une tâche")
        print("3. Supprimer une tâche")
        print("4. Quitter")
        
        choix = input("Choisissez une option : ")

        if choix == '1':
            afficher_taches(taches)
        elif choix == '2':
            tache = input("Entrez la nouvelle tâche : ")
            ajouter_tache(taches, tache)
        elif choix == '3':
            index = int(input("Entrez le numéro de la tâche à supprimer : ")) - 1
            supprimer_tache(taches, index)
        elif choix == '4':
            print("Au revoir !")
            break
        else:
            print("Option invalide, essayez à nouveau.")

if __name__ == "__main__":
    main()
