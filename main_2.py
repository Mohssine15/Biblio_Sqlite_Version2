#menu et programme principale qui gére la bibliothéque et fait appel aux classes: Adherent, Livre et Emprunt
from Adherent_2 import Adherent
from Livre_2 import Livre
from Emprunt_2 import Emprunt
menu ="""    *************************************************
    *      Bienvenue à votre bibliothèque           *
    *              Faites un choix :                *
    *************************************************
    *    1       Ajouter un adhérent                *
    *    2       Afficher tous les adhérents        *
    *    3       Supprimer un adhérent              *
    *    4       Ajouter un livre                   *
    *    5       Afficher tous les livre            *
    *    6       Supprimer un livre                 *
    *    7       Ajouter un Emprunt                 *
    *    8       Afficher tous les Emprunts         *
    *    9       Retour d’un Emprunt                *
    *    Q       Quitter                            *
    ************************************************* """
print(menu)
while True:
    print("""=========================================================
=================== Menu principal ======================
=========================================================""")
    choix = input("Saisir votre choix selon le menu >> ")
    print("")
    # Ajout d'adhérent
    if choix == "1":
        print("""=========================================================
=================== Ajout d'adhérent ====================
=========================================================""")
        ad1 = Adherent()
        ad1.connectionDB()
        ad1.ajouterAdherent()
        ad1.close()
    # Afficher la liste d'adhérents
    elif choix == "2":
        print("""=========================================================
================== Liste des adhérents ==================
=========================================================""")
        ad1 = Adherent()
        ad1.connectionDB()
        ad1.afficherListeAdherents()
        ad1.close()
    # Suppression d'adhérent
    elif choix == "3":
        print("""=========================================================
=============== Suppression d'adhérent ==================
=========================================================""")
        ad1 = Adherent()
        ad1.connectionDB()
        ad1.afficherListeAdherents()
        ad1.supprimerAdherent()
        ad1.close()
    # Ajout de livre
    elif choix == "4":
        print("""=========================================================
================== Ajout de livre =======================
=========================================================""")
        liv1 = Livre()
        liv1.connectionDB()
        liv1.ajouterLivre()
        liv1.close()
    # Afficher La liste des livres
    elif choix == "5":
        print("""=========================================================
==================== Liste des livres ===================
=========================================================""")
        liv1 = Livre()
        liv1.connectionDB()
        liv1.afficherListeLivres()
        liv1.close()
    # Suppression de livre
    elif choix == "6":
        print("""=========================================================
=============== Suppression de livre ====================
=========================================================""")
        liv1 = Livre()
        liv1.connectionDB()
        liv1.afficherListeLivres()
        liv1.supprimerLivre()
        liv1.close()
    # Ajout d'emprunt
    elif choix == "7":
        print("""=========================================================
================== Ajout d'emprunt ======================
=========================================================""")
        emp1 = Emprunt()
        emp1.connectionDB()
        emp1.ajouterEmprunt()
        emp1.close()
    # Afficher la liste des emprunts
    elif choix == "8":
        print("""=========================================================
================== Liste des emprunts  ==================
=========================================================""")
        emp1 = Emprunt()
        emp1.connectionDB()
        emp1.afficherListeEmprunts()
        emp1.close()
    # Retour d'un livre
    elif choix == "9":
        print("""=========================================================
=================== Retour d'un livre ===================
=========================================================""")
        emp1 = Emprunt()
        emp1.connectionDB()
        emp1.afficherListeEmprunts()
        emp1.retourLivre()
        emp1.close()
    # Quitter le menu
    elif choix == "Q" or choix == "q":
        print("""=========================================================
=========== Vous avez quitté l'application ! ============
=============== Merci d'avoire utiliser =================
================= notre bibliothèque ====================
=========================================================""")
        break
    else:
        print("!!! Choix erroné! Saisir à nouveaux !!!  ")
