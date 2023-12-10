import sqlite3

class Livre:
    def __init__(self, p_livreID="", p_titre="", p_auteur="", p_nbrPages="", p_ISBN=""):
        self.livreID = p_livreID
        self.titre = p_titre
        self.auteur = p_auteur
        self.nbrPages = p_nbrPages
        self.ISBN = p_ISBN
    def connectionDB(self):
        self.con = sqlite3.connect("Biblio.db")
        self.cur = self.con.cursor()
        req1 = "CREATE TABLE IF NOT EXISTS livre (livreID INTEGER PRIMARY KEY AUTOINCREMENT, titre TEXT, auteur TEXT, nbrPages INTERGER, ISBN INTEGER)"
        self.cur.execute(req1)
        self.con.commit()
    def ajouterLivre(self):
        self.a = input("Titre >> ")
        self.b = input("Auteur >> ")
        self.c = input("Nombre de pages >> ")
        self.d = input("ISBN >> ")
        req2 = "INSERT INTO livre VALUES(NULL, '"+self.a+"', '"+self.b+"', '"+self.c+"', '"+self.d+"')"
        self.cur.execute(req2)
        self.con.commit()
    def afficherListeLivres(self):
        req3 = "SELECT * FROM livre"
        self.cur.execute(req3)
        self.con.commit()
        resultat = self.cur.fetchall()
        print("====== LivreID , Titre , Auteur , Nbr pages , ISBN ======")
        for i in range(0, len(resultat)):
            print(resultat[i][0], " , ", resultat[i][1], " , ", resultat[i][2], " , ", resultat[i][3], " , ", resultat[i][4])
        print("=========================================================")
        print("nbr total de livres: ", len(resultat))
        print("=========================================================")
        print("")
    def supprimerLivre(self):
        self.e = input("Saisir le numéro de livre à supprimer >> ")
        req4 = "SELECT * FROM livre WHERE(livreID = '"+self.e+"')"
        self.cur.execute(req4)
        self.con.commit()
        resultat2 = self.cur.fetchall()
        print("=========================================================")
        print("=========== Le livre suivant sera supprimé ==============")
        print("=========================================================")
        for i in range(0, len(resultat2)):
            print(resultat2[i][0], " , ", resultat2[i][1], " , ", resultat2[i][2], " , ", resultat2[i][3])
        print("=========================================================")
        print("")
        confirm = input("ÊTES-VOUS SÛR DE VOULOIR LE SUPPRIMER ?  O/N  >> ")
        if confirm == "o" or confirm == "O":
            req5 = "DELETE FROM livre WHERE(livreID == '"+self.e+"')"
            self.cur.execute(req5)
            self.con.commit()
            print("=========================================================")
            print("========== Le livre numéro ", self.e, " est supprimé =============")
            print("==================== avec succés ========================")
            print("=========================================================")
        else:
            print("=========================================================")
            print("================ Suppression annulée ====================")
            print("=========================================================")
    def close(self):
        self.cur.close()
        self.con.close()
# liv1 = Livre()
# liv1.connectionDB()
# liv1.ajouterLivre()
# liv1.afficherListeLivres()
# liv1.supprimerLivre()
# liv1.close()