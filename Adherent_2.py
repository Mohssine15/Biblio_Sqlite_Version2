# Classe Adhérent permet d'ajouter un adhérent, d'afficher la liste des adhérents et supprimer un adhérent
import sqlite3
class Adherent:
    def __init__(self, p_adhID="", p_nom="", p_prenom="", p_adhNum=""):
        self.adhID = p_adhID
        self.nom = p_nom
        self.prenom = p_prenom
        self.adhNum = p_adhNum
    def connectionDB(self):
        self.con = sqlite3.connect("Biblio.db")
        self.cur = self.con.cursor()
        req1 = "CREATE TABLE IF NOT EXISTS adherent(adhID INTEGER PRIMARY KEY AUTOINCREMENT, nom TEXT, prenom TEXT, adhNum INTEGER )"
        self.cur.execute(req1)
        self.con.commit()
    def ajouterAdherent(self):
        self.a = input("Nom >> ")
        self.b = input("Prénom >> ")
        self.c = input("Num >> ")
        req2 = "INSERT INTO adherent VALUES(NULL, '"+self.a+"', '"+self.b+"', '"+self.c+"')"
        self.cur.execute(req2)
        self.con.commit()
        print("=========================================================")
        print("======= L'adhérent suivant est ajouté avec succés  ======")
        print("=========================================================")
        print("Nom: ", self.a)
        print("Prénom: ", self.b)
        print("Numéro: ", self.c)
        print("=========================================================")
        print("")
    def afficherListeAdherents(self):
        req3 = "SELECT * FROM adherent"
        self.cur.execute(req3)
        self.con.commit()
        resultat = self.cur.fetchall()
        print("===== AdhID  ,  Nom  ,  Prénom  ,  Numéro ===============")
        for i in range(0, len(resultat)):
            print(resultat[i][0]," , ", resultat[i][1]," , ", resultat[i][2]," , ", resultat[i][3])
        print("=========================================================")
        print("nbr total d'adhérents : ", len(resultat))
        print("=========================================================")
        print("")
    def supprimerAdherent(self):
        self.d = input("Saisir numéro d'adhérent à supprimer >> ")
        req4 = "SELECT * FROM adherent WHERE(adhID == '"+self.d+"')"
        self.cur.execute(req4)
        self.con.commit()
        resultat2 = self.cur.fetchall()
        print("=========================================================")
        print("=========== L'adhérent suivant sera supprimé ============")
        print("=========================================================")
        for i in range(0, len(resultat2)):
            print(resultat2[i][0], " , ", resultat2[i][1], " , ", resultat2[i][2], " , ", resultat2[i][3])
        print("")
        confirm = input("ÊTES-VOUS SÛR DE VOULOIR LE SUPPRIMER ?  O/N  >> ")
        print("=========================================================")
        if confirm == "o" or confirm == "O":
            req5 = "DELETE FROM adherent WHERE(adhID == '"+self.d+"')"
            self.cur.execute(req5)
            self.con.commit()
            print("=========================================================")
            print("========== L'adhérent numéro ", self.d, " est supprimé ===========")
            print("==================== avec succés ========================")
            print("=========================================================")
        else:
            print("=========================================================")
            print("================ Suppression annulée ====================")
            print("=========================================================")
    def close(self):
        self.cur.close()
        self.con.close()
# ad1 = Adherent()
# ad1.connectionDB()
# ad1.ajouterAdherent()
# ad1.afficherListeAdherents()
# ad1.supprimerAdherent()
# ad1.close()
