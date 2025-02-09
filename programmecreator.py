import lecturefichier as lf
import analyseur as an

def tutoriel():
    print ('bonjour, bienvenu dans le Z.E.U.S sport manager')
    print ('je serai votre guide pendant le peu de temps que j\'ai')
    print ('comme vous le savez, le but de ce programme est de permettre de simplement vous proposer un programme d\'entrainement')
    print ('chaque programme est généré suivant vos retour.')
    print ('vous poouvez a tout moment accéder a ce dernier en tabulant E')
    print('une fois votre semaine terminer, tabuler R et écrivait un rapport concernant votre semaine')
    print('enfin en tabulant Q, vous quittez le programme')
    return
def newprogrammedemarrage(user):
    print("étant donné que votre niveau est ", lf.mattostring(lf.chercherinfo("niveau",user)))
    print("nous vous avons concocté le programme suivant pour la semaine:")
    print("nous allons commencé par :", lf.mattostring(lf.chercherinfo("entrainement", user)))
    print("ensuite, vous allez faire :", lf.mattostring(lf.chercherinfo("exercice", user)))
    print("enfin, vous terminerez par:", lf.mattostring(lf.chercherinfo("final", user)))
    return

def programmelecture(file):
    matricebrut = open(file, "r", encoding='utf-8')
    matriceaanalysee = []
    listeentrainement = []
    listeexercice = []
    listefindeseance = []
    for i in matricebrut:
        matriceaanalysee.append(i.replace("\n"," "))
    matricebrut.close()
    matriceaanalysee = lf.matricetomatriceint(lf.matricetoliste(matriceaanalysee))
    i = 1
    while matriceaanalysee[i] != "exercice" :
        listeentrainement.append(matriceaanalysee[i])
        i+= 1
    i += 1
    while matriceaanalysee[i] != "findeseance" :
        listeexercice.append(matriceaanalysee[i])
        i += 1
    while i != len(matriceaanalysee) - 1 :
        i+= 1
        listefindeseance.append(matriceaanalysee[i])
    return listeentrainement,listeexercice,listefindeseance

def séancecreatornew(niveau, user):
    save = open(user,"a",encoding="utf-8")
    temps = 0
    unit = 0
    exercice = 0
    listeentrainement,listeexercice,listefindeseance = programmelecture(niveau)
    if "(3)" not in listeentrainement :
        valeuretalon = "(1)"
    else :
        valeuretalon = "(2)"
    i = 0
    while listeentrainement[i] != valeuretalon :
        i += 1
    i += 2
    exercice = listeentrainement[i]
    while listeentrainement[i] != "moy":
        i += 1
    i += 2
    temps = listeentrainement[i]
    while listeentrainement[i] != "unit":
        i += 1
    i += 2
    unit = listeentrainement[i]
    save.write("niveauentrainement : " + lf.mattostring(lf.chercherinfo("niveau", user)) + "\n")
    save.write("entrainement : " + exercice + " " + temps + unit + "\n")
    if "(3)" not in listeexercice :
        valeuretalon = "(1)"
    else :
        valeuretalon = "(2)"
    i = 0
    while listeexercice[i] != valeuretalon :
        i += 1
    i += 2
    exercice = listeexercice[i]
    while listeexercice[i] != "moy":
        i += 1
    i += 2
    temps = listeexercice[i]
    while listeexercice[i] != "unit":
        i += 1
    i += 2
    unit = listeexercice[i]
    save.write("niveauexercice : " + lf.mattostring(lf.chercherinfo("niveau", user)) + "\n")
    save.write("exercice : " + exercice + " " + temps + unit + "\n")
    if "(3)" not in listefindeseance :
        valeuretalon = "(1)"
    else :
        valeuretalon = "(2)"
    i = 0
    while listefindeseance[i] != valeuretalon :
        i += 1
    i += 2
    exercice = listefindeseance[i]
    while listefindeseance[i] != "moy":
        i += 1
    i += 2
    temps = listefindeseance[i]
    while listefindeseance[i] != "unit":
        i += 1
    i += 2
    unit = listefindeseance[i]
    save.write("niveaufinal : " + lf.mattostring(lf.chercherinfo("niveau", user)) + "\n")
    save.write("final : " + exercice + " " + temps + unit + "\n")
    save.close()
    newprogrammedemarrage(user)
    return

def improvedico(user): #fonction utiliser si le programme n'a pas réussi a comprendre le niveau de l'utilisateur
    save = open(user,"a",encoding="utf-8")
    print("il se peut que notre programme ait ses limites, veuiller choisir votre niveau (D)ébutant, (I)ntermédiaire ou (A)vancé")
    reponse = input(":")
    reponseutilisateur = open("buffer/reponseutilisateur.rp", "r")
    if reponse == "D" or reponse == "d" :
        print ("vous êtes donc un débutant...")
        save.write("niveau : debutant\n")
        save.close()
        séancecreatornew("exercicepossible/niveaudebutant.txt", user)
        dossierdbutant = open("dossierteste/dossiertestniveudebutant.txt", "a", encoding='utf-8')
        for i in reponseutilisateur:
            dossierdbutant.write(i)
    elif reponse == "I" or reponse == "i" :
        print ("vous êtes donc un intermédiaire...")
        save.write("niveau : intermédiaire\n")
        save.close()
        séancecreatornew("exercicepossible/niveauintermédiaire.txt", user)
        dossierdbutant = open("dossierteste/dossiertestniveauintermédiaire.txt", "a",encoding='utf-8')
        for i in reponseutilisateur:
            dossierdbutant.write(i)
    elif reponse == "a" or reponse == "A" :
        print ("vous êtes donc un avancé...")
        save.write("niveau : avancé\n")
        save.close()
        séancecreatornew("exercicepossible/niveauavancé.txt", user)
        dossierdbutant = open("dossierteste/dossiertesteniveauavancé.txt", "a", encoding='utf-8')
        for i in reponseutilisateur:
            dossierdbutant.write(i)
    else:
        print("nous ne comprenons pas votre réponse veuiller retaper votre réponse avec une seul lettre")
        save.close()
        improvedico(user)
        return
        
def programmecreatorfornewuser(user):
    programmelevel = open("buffer/reponseutilisateur.rp", "w", encoding='utf-8')
    text = input("comment qualifiez-vous votre niveau ? :")
    programmelevel.write(text)
    save = open(user,"a",encoding="utf-8")
    if 1.5 * lf.classeur("buffer/reponseutilisateur.rp", "dico/dicotestIAAvancé.dico") > lf.classeur("buffer/reponseutilisateur.rp", "dico/dicotestIAIntermediaire.dico") and 1.5 * lf.classeur("buffer/reponseutilisateur.rp", "dico/dicotestIAAvancé.dico") > lf.classeur("buffer/reponseutilisateur.rp", "dico/dicotestniveaudebutant.dico"):
        print("nous avons déterminé que vous aviez un niveau avancé")
        reponse = input("cela vous convient-il ?(y/n)")
        if reponse == "y" or reponse == "Y" :
            print("nous allons ajouter les niveaux de bases associés au niveau avancé...")
            save.write("niveau : avancé\n")
            save.close()
            séancecreatornew("exercicepossible/niveauavancé.txt", user)
            return
        else : 
            improvedico(user)
            return
    elif 1.5 * lf.classeur("buffer/reponseutilisateur.rp", "dico/dicotestIAIntermediaire.dico") > lf.classeur("buffer/reponseutilisateur.rp", "dico/dicotestIAAvancé.dico") and 1.5 * lf.classeur("buffer/reponseutilisateur.rp", "dico/dicotestIAIntermediaire.dico") > lf.classeur("buffer/reponseutilisateur.rp", "dico/dicotestniveaudebutant.dico"):
        print("nous avons déterminé que vous aviez un niveau intermediaire")
        reponse = input("cela vous convient-il ?(y/n)")
        if reponse == "y" or reponse == "Y" :
            print("nous allons ajouter les niveaux de bases associés au niveau intermedière...")
            save.write("niveau : intermédiaire\n")
            save.close()
            séancecreatornew("exercicepossible/niveauintermédiaire.txt", user)
            return
        else : 
            improvedico(user)
            return
    else:
        print("nous avons déterminé que vous aviez un niveau débutant")
        reponse = input("cela vous convient-il ?(y/n)")
        if reponse == "y" or reponse == "Y" :
            print("nous allons ajouter les niveaux de bases associés au niveau débutant...")
            save.write("niveau : debutant\n")
            save.close()
            séancecreatornew("exercicepossible/niveaudebutant.txt", user)
            return
        else : 
            save.close()
            improvedico(user)
            return
