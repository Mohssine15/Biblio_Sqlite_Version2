import sqlite3

class Emprunt:
    def __init__(self, p_empruntID="", p_titre="", p_nomAdh="", p_ISBN="", p_date=""):
        self.empruntID = p_empruntID
        self.titre = p_titre
        self.nomAdh = p_nomAdh
        self.ISBN = p_ISBN
        self.date = p_date
    def connectionDB(self):
        self.con = sqlite3.connect("Biblio.db")
        self.cur = self.con.cursor()
        req1 = "CREATE TABLE IF NOT EXISTS emprunt (empruntID INTEGER PRIMARY KEY AUTOINCREMENT, titre TEXT, nomAdh TEXT, ISBN INTERGER, date TEXT)"
        self.cur.execute(req1)
        self.con.commit()
    def ajouterEmprunt(self):
        self.a = input("Titre >> ")
        self.b = input("Nom Adhérent >> ")
        self.c = input("ISBN >> ")
        self.d = input("Date >> ")
        req2 = "INSERT INTO emprunt VALUES(NULL, '"+self.a+"', '"+self.b+"', '"+self.c+"', '"+self.d+"')"
        self.cur.execute(req2)
        self.con.commit()
    def afficherListeEmprunts(self):
        req3 = "SELECT * FROM emprunt"
        self.cur.execute(req3)
        self.con.commit()
        resultat = self.cur.fetchall()
        print("===== EmpruntID , Titre , Nom Adhérent , ISBN , Date =====")
        for i in range(0, len(resultat)):
            print(resultat[i][0], " , ", resultat[i][1], " , ", resultat[i][2], " , ", resultat[i][3], " , ", resultat[i][4])
        print("=========================================================")
        print("nbr total des emprunts: ", len(resultat))
        print("=========================================================")
        print("")
    def retourLivre(self):
        self.e = input("Saisir le titre de livre à retourner >> ")
        req4 = "SELECT * FROM emprunt WHERE(titre = '"+self.e+"')"
        self.cur.execute(req4)
        self.con.commit()
        resultat2 = self.cur.fetchall()
        print("=========================================================")
        print("============ Le livre suivant sera retourné =============")
        print("=========================================================")
        for i in range(0, len(resultat2)):
            print(resultat2[i][0], " , ", resultat2[i][1], " , ", resultat2[i][2], " , ", resultat2[i][3])
        print("=========================================================")
        print("")
        confirm = input("Confirmez SVP le retour de ce livre!  O/N  >> ")
        if confirm == "o" or confirm == "O":
            req5 = "DELETE FROM emprunt WHERE(titre == '"+self.e+"')"
            self.cur.execute(req5)
            self.con.commit()
            print("=========================================================")
            print("========== Le livre ", self.e, " est retourné ===========")
            print("==================== avec succés ========================")
            print("=========================================================")
        else:
            print("=========================================================")
            print("=================== Retour annulé =======================")
            print("=========================================================")
    def close(self):
        self.cur.close()
        self.con.close()
# emp1 = Emprunt()
# emp1.connectionDB()
# emp1.ajouterEmprunt()
# emp1.afficherListeEmprunts()
# emp1.retourLivre()
# emp1.close()