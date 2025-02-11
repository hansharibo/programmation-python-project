# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 18:15:03 2023

@author: jean troussier
"""
import lecturefichier as lf
import programmecreator as pc
dicomal ="dico/dicotestmal.dico"
dicosupmal =dicomal
dicobien = "dico/dicotestbien.dico"

def modifséancegen(user,isexercicehard,num):
    newentrainement = []
    type = ["entrainement","exercice","final"]
    listeentrainement,listeseance,listefinalex = pc.programmelecture("exercicepossible/niveau"+lf.mattostring(lf.chercherinfo("niveau"+ type[num -1], user))+".txt")
    entrainement = lf.chercherinfo(type[num - 1], user)
    inc =0
    unit =''
    valeur = 0
    min = 0
    max = 0
    if len(entrainement) > 2 :
        newentrainement.append(lf.mattostringintern(entrainement[:-1]))
        newentrainement.append(lf.mattostringintern(entrainement[:-2]))
    print(entrainement[1])
    valeur = lf.stringtonumber(entrainement[1])
    if num == 1:
        listefinal = listeentrainement[:]
    elif num == 2:
        listefinal = listeseance[:]
    elif num == 3:
        listefinal = listefinalex[:]
    i = 0
    while listefinal[i] != entrainement[0]:
        i+=1
    while listefinal[i] != 'min' :
        i+=1
    i+=2
    min = lf.stringtonumber(listefinal[i])
    while listefinal[i] != 'max' :
        i+=1
    i+=2
    max = lf.stringtonumber(listefinal[i])
    while listefinal[i] != 'inc' :
        i+=1
    i+=2
    if isexercicehard == True:    
        inc = -int(listefinal[i])
    else:
        inc = int(listefinal[i])
    while listefinal[i] != 'unit' : 
        i+=1
    i+=2
    unit = listefinal[i]
    print(valeur)
    print(inc)
    print(entrainement)
    if (valeur + inc) > max:
        i = 0
        while listefinal[i] != entrainement[0]:
            i+=1
        i -= 2
        nieveausup = "(" + str(int(listefinal[i][1]) + 1 ) + ")"
        if nieveausup not in listefinal:
            print("ils semblerait qu'il vous faille changer de niveau")
            niveauutilisateur = lf.mattostring(lf.chercherinfo( "niveau"+ type[num -1],user))
            listeniveau = ['debutant', 'intermédiaire', 'avancé']
            for i in range(len(listeniveau)):
                if listeniveau[i] == niveauutilisateur:
                    try:
                        lf.modifinfo(user,"niveau" + type[num -1], listeniveau[i+1])
                        listeentrainement,listeseance,listefinalex = pc.programmelecture("exercicepossible/niveau"+lf.mattostring(lf.chercherinfo("niveau"+ type[num -1], user))+".txt")
                        if num == 1:
                            listefinal = listeentrainement[:]
                        elif num == 2:
                            listefinal = listeseance[:]
                        elif num == 3:
                            listefinal = listefinalex[:]
                        i = 0
                        while '(1)' != listefinal[i]:
                            i+=1
                        i+=2
                        entrainement = []
                        entrainement.append(listefinal[i])
                        while 'min' != listefinal[i]:
                            i+=1
                        i+=2
                        entrainement.append(" ")
                        entrainement.append(listefinal[i])
                        while 'unit' != listefinal[i]:
                            i+=1
                        i+=2
                        entrainement.append(listefinal[i])
                        lf.modifinfo(user, type[num - 1], entrainement[0] + entrainement[1] + entrainement[2] +entrainement[3])
                    except:
                        print("nous ne pouvons pas améliorer votre séance, veuiller appeler un technicien si cela reviens...")
                        input("appuyer sur entrée pour continuer...")
        else:
            i = 0
            while nieveausup != listefinal[i]:
                i+=1
            i+=2
            entrainement = []
            entrainement.append(listefinal[i])
            while 'min' != listefinal[i]:
                i+=1
            i+=2
            entrainement.append(" ")
            entrainement.append(listefinal[i])
            while 'unit' != listefinal[i]:
                i+=1
            i+=2
            entrainement.append(listefinal[i])
            lf.modifinfo(user, type[num - 1], entrainement[0] + entrainement[1] + entrainement[2] +entrainement[3])
    elif valeur + inc < min:
        i = 0
        while listefinal[i] != entrainement[0]:
            i+=1
        i -= 2
        nieveausup = "(" + str(int(listefinal[i][1]) - 1) + ")"
        if nieveausup not in listefinal:
            print("ils semblerait qu'il vous faille changer de niveau")
            niveauutilisateur = lf.mattostring(lf.chercherinfo( "niveau"+ type[num -1], user))
            listeniveau = ['debutant', 'intermédiaire', 'avancé']
            for i in range(len(listeniveau)):
                if listeniveau[i] == niveauutilisateur:
                    try:
                        lf.modifinfo(user,"niveau"+ type[num -1], listeniveau[i - 1])
                        listeentrainement,listeseance,listefinalex = pc.programmelecture("exercicepossible/niveau"+lf.mattostring(lf.chercherinfo("niveau"+ type[num -1], user))+".txt")
                        if num == 1:
                            listefinal = listeentrainement[:]
                        elif num == 2:
                            listefinal = listeseance[:]
                        elif num == 3:
                            listefinal = listefinalex[:]
                        i = 0
                        while '(2)' != listefinal[i]:
                            i+=1
                        i+=2
                        entrainement = []
                        entrainement.append(listefinal[i])
                        while 'max' != listefinal[i]:
                            i+=1
                        i+=2
                        entrainement.append(" ")
                        entrainement.append(listefinal[i])
                        while 'unit' != listefinal[i]:
                            i+=1
                        i+=2
                        entrainement.append(listefinal[i])
                        lf.modifinfo(user, type[num - 1], entrainement[0] + entrainement[1] + entrainement[2] +entrainement[3])
                    except:
                        print("nous ne pouvons pas améliorer votre séance, veuiller appeler un technicien si cela reviens...")
                        input("appuyer sur entrée pour continuer...")
        else:
            i = 0
            while nieveausup != listefinal[i]:
                i+=1
            i+=2
            entrainement = []
            entrainement.append(listefinal[i])
            while 'min' != listefinal[i]:
                i+=1
            i+=2
            entrainement.append(" ")
            entrainement.append(listefinal[i])
            while 'unit' != listefinal[i]:
                i+=1
            i+=2
            entrainement.append(listefinal[i])
            lf.modifinfo(user, type[num - 1], entrainement[0] + entrainement[1] + entrainement[2] +entrainement[3]) 
    else:     
        lf.modifinfo(user, type[num - 1], entrainement[0] + " " + str(valeur + inc) + unit)
    print("votre ",type[num - 1], " a été mis a jour...")
    

def createnewuser(): #fonction pour retenir les informations des nouveaux utilisateurs
    utilisateur = input("votre nom ?:")
    save = open("utilisateur/" + utilisateur +".ut","w",encoding="utf-8")
    user = input("votre age :")
    save.write("age : " + user + '\n')
    user = input("votre sexe(h/f):")
    save.write("sexe : " +  user + '\n')
    user = input("estimation de votre poids :")
    save.write("poid : " +  user + '\n')
    save.close()
    pc.programmecreatorfornewuser("utilisateur/" + utilisateur +".ut")
    return

    
def lookingforexistinguser(fichier):#programme qui cherche si l'utilisateur existe
    try :
        userexist = open("utilisateur/" + fichier +".ut", "r", encoding='utf-8')
        return True
    except:
        return False

def entrainementraté(user): #programme qui permet de voir ce qui n'allait pas dans l'entrainement
    print("comment vous sentiez vous pendant l'entrainement ?")
    avisentrainement = input(":>")
    with open("buffer/reponseutilisateur.rp", "w", encoding='utf-8') as avis:
        avis.write(avisentrainement)
    if lf.classeur("buffer/reponseutilisateur.rp", dicomal) + lf.classeur("buffer/reponseutilisateur.rp", dicosupmal)> lf.classeur("buffer/reponseutilisateur.rp", dicobien) :
        choix =''
        while choix != 'y' and choix != 'Y' and  choix != 'N' and choix != 'n' :
            print("il semblerait que votre entrainement ne soit pas adapté(y/n)")
            choix = input(':>')
        if choix == 'y' or choix == 'Y':
            with open('dossierteste/dossier pas bien.txt', 'a', encoding='utf-8') as save:
                with open("buffer/reponseutilisateur.rp",'r', encoding='utf-8') as reponse:
                    for i in reponse:
                        save.write(i)
                        save.write(" ")
            choix = ''
            while choix != 'y' and choix != 'Y' and  choix != 'N' and choix != 'n' :
                print("votre entrainement était il trop dur ?(y/n)")
                choix = input(':>')
            if choix == 'y' or choix == 'Y':
                modifséancegen(user , True,1)
            else: 
                modifséancegen(user, False,1)
        else:
            with open('dossierteste/dossier bien.txt', 'a', encoding='utf-8') as save:
                with open("buffer/reponseutilisateur.rp",'r', encoding='utf-8') as reponse:
                    for i in reponse:
                        save.write(i)
                        save.write(" ")
    else :
        choix =''
        while choix != 'y' and choix != 'Y' and  choix != 'N' and choix != 'n' :
            print("je suis content de voir que la session d'entrainement vous convienne...(y/n)")
            choix = input(':>')
        if choix == 'n' or choix == 'N':
            with open('dossierteste/dossier pas bien.txt', 'a',encoding='utf-8') as save:
                with open("buffer/reponseutilisateur.rp",'r', encoding='utf-8') as reponse:
                    for i in reponse:
                        save.write(i)
                        save.write(" ")
            choix = ''
            while choix != 'y' and choix != 'Y' and  choix != 'N' and choix != 'n' :
                print("votre entrainement était il trop dur ?(y/n)")
                choix = input(':>')
            if choix == 'y' or choix == 'Y':
                modifséancegen(user , True,1)
            else: 
                modifséancegen(user, False,1)
        else:
            with open('dossierteste/dossier bien.txt', 'a', encoding='utf-8') as save:
                with open("buffer/reponseutilisateur.rp",'r', encoding='utf-8') as reponse:
                    for i in reponse:
                        save.write(i)
                        save.write(" ")
    print("comment vous sentez pendant l'exercice ?")
    avisentrainement = input(":>")
    with open("buffer/reponseutilisateur.rp", "w", encoding='utf-8') as avis:
        avis.write(avisentrainement)
    if lf.classeur("buffer/reponseutilisateur.rp", dicomal) + lf.classeur("buffer/reponseutilisateur.rp", dicosupmal)> lf.classeur("buffer/reponseutilisateur.rp", dicobien) :
        choix =''
        while choix != 'y' and choix != 'Y' and  choix != 'N' and choix != 'n' :
            print("il semblerait que votre exercice ne soit pas adapté(y/n)")
            choix = input(':>')
        if choix == 'y' or choix == 'Y':
            with open('dossierteste/dossier pas bien.txt', 'a',encoding='utf-8') as save:
                with open("buffer/reponseutilisateur.rp",'r',encoding='utf-8') as reponse:
                    for i in reponse:
                        save.write(i)
                        save.write(" ")
            choix = ''
            while choix != 'y' and choix != 'Y' and  choix != 'N' and choix != 'n' :
                print("votre exercice était il trop dur ?(y/n)")
                choix = input(':>')
            if choix == 'y' or choix == 'Y':
                modifséancegen(user , True,2)
            else: 
                modifséancegen(user, False,2)
        else:
            with open('dossierteste/dossier bien.txt', 'a', encoding='utf-8') as save:
                with open("buffer/reponseutilisateur.rp",'r', encoding='utf-8') as reponse:
                    for i in reponse:
                        save.write(i)
                        save.write(" ")
    else :
        choix =''
        while choix != 'y' and choix != 'Y' and  choix != 'N' and choix != 'n' :
            print("je suis content de voir que la session d'exercice vous conviennes...(y/n)")
            choix = input(':>')
        if choix == 'n' or choix == 'N':
            with open('dossierteste/dossier pas bien.txt', 'a', encoding='utf-8') as save:
                with open("buffer/reponseutilisateur.rp",'r', encoding='utf-8') as reponse:
                    for i in reponse:
                        save.write(i)
                        save.write(" ")
            choix = ''
            while choix != 'y' and choix != 'Y' and  choix != 'N' and choix != 'n' :
                print("votre exercice était il trop dur ?(y/n)")
                choix = input(':>')
            if choix == 'y' or choix == 'Y':
                modifséancegen(user , True,2)
            else: 
                modifséancegen(user , False,2)
        else:
            with open('dossierteste/dossier bien.txt', 'a',encoding='utf-8') as save:
                with open("buffer/reponseutilisateur.rp",'r', encoding='utf-8') as reponse:
                    for i in reponse:
                        save.write(i)
                        save.write(" ")
    print("comment vous sentez vous pendant la fin de séance ?")
    avisentrainement = input(":>")
    with open("buffer/reponseutilisateur.rp", "w", encoding='utf-8') as avis:
        avis.write(avisentrainement)
    if lf.classeur("buffer/reponseutilisateur.rp", dicomal) + lf.classeur("buffer/reponseutilisateur.rp", dicosupmal)> lf.classeur("buffer/reponseutilisateur.rp", dicobien) :
        choix =''
        while choix != 'y' and choix != 'Y' and  choix != 'N' and choix != 'n' :
            print("il semblerait que votre fin de séance ne soit pas adapté(y/n)")
            choix = input(':>')
        if choix == 'y' or choix == 'Y':
            with open('dossierteste/dossier pas bien.txt', 'a', encoding='utf-8') as save:
                with open("buffer/reponseutilisateur.rp",'r', encoding='utf-8') as reponse:
                    for i in reponse:
                        save.write(i)
                        save.write(" ")
            choix = ''
            while choix != 'y' and choix != 'Y' and  choix != 'N' and choix != 'n' :
                print("votre fin de séance était elle trop dur ?(y/n)")
                choix = input(':>')
            if choix == 'y' or choix == 'Y':
                modifséancegen(user , True,3)
            else: 
                modifséancegen(user , False,3)
        else:
            with open('dossierteste/dossier bien.txt', 'a', encoding='utf-8') as save:
                with open("buffer/reponseutilisateur.rp",'r', encoding='utf-8') as reponse:
                    for i in reponse:
                        save.write(i)
                        save.write(" ")
    else :
        choix =''
        while choix != 'y' and choix != 'Y' and  choix != 'N' and choix != 'n' :
            print("je suis content de voir que la session de fin de séance vous convienne...(y/n)")
            choix = input(':>')
        if choix == 'n' or choix == 'N':
            with open('dossierteste/dossier pas bien.txt', 'a', encoding='utf-8') as save:
                with open("buffer/reponseutilisateur.rp",'r', encoding='utf-8') as reponse:
                    for i in reponse:
                        save.write(i)
                        save.write(" ")
            choix = ''
            while choix != 'y' and choix != 'Y' and  choix != 'N' and choix != 'n' :
                print("votre fin de séance était elle trop dur ?(y/n)")
                choix = input(':>')
            if choix == 'y' or choix == 'Y':
                modifséancegen(user , True,3)
            else: 
                modifséancegen(user , False,3)
        else:
            with open('dossierteste/dossier bien.txt', 'a', encoding='utf-8') as save:
                with open("buffer/reponseutilisateur.rp",'r', encoding='utf-8') as reponse:
                    for i in reponse:
                        save.write(i)
                        save.write(" ")
    print("merci pour votre retour de fin de séance en espérant que cette dernière vous convienne pour cette semaine")
    return
    
def avisutilisateur(user):# programme qui permet de connaitre l'avis de l'utilisateur, s'il est bon on garde l'entrainement, sinon il renvoie vers entrainementraté
    print("comment était votre séance ?")
    with open("buffer/reponseutilisateur.rp", "w", encoding='utf-8') as avis:
        avis.write(input(":>"))
    if lf.classeur("buffer/reponseutilisateur.rp", dicomal) + lf.classeur("buffer/reponseutilisateur.rp", dicosupmal)> lf.classeur("buffer/reponseutilisateur.rp", dicobien) :
        choix =''
        while choix != 'n' and choix != 'N' and choix != 'Y' and choix != 'y':
            print("il semblerait que votre programme ne soit pas adapté (y/n)")
            choix = input(":>")
        if choix == 'y' or choix == 'Y':
            with open('dossierteste/dossier pas bien.txt', 'a', encoding='utf-8') as save:
                with open("buffer/reponseutilisateur.rp",'r', encoding='utf-8') as reponse:
                    for i in reponse:
                        save.write(i)
                        save.write(" ")
            print("essayons de comprendre ce qu'il n'allait pas...")
            entrainementraté(user)
        else:
            with open('dossierteste/dossier bien.txt', 'a', encoding='utf-8') as save:
                with open("buffer/reponseutilisateur.rp",'r', encoding='utf-8') as reponse:
                    for i in reponse:
                        save.write(i)
                        save.write(" ")
            print("nous sommes désolé pour la gène occasionnée")
    else :
        choix =''
        while choix != 'n' and choix != 'N' and choix != 'Y' and choix != 'y':
            print("il semblerait que votre programme soit adapté (y/n)")
            choix = input(":>")
        if choix == 'n' or choix == 'N':
            print("nous sommes désolé pour la gène occasionnée")
            with open('dossierteste/dossier pas bien.txt', 'a', encoding='utf-8') as save:
                with open("buffer/reponseutilisateur.rp",'r', encoding='utf-8') as reponse:
                    for i in reponse:
                        save.write(i)
                        save.write(" ")
            print("essayons de comprendre ce qu'il n'allait pas...")
            entrainementraté(user)
        else:
            with open('dossierteste/dossier bien.txt', 'a',encoding='utf-8') as save:
                with open("buffer/reponseutilisateur.rp",'r', encoding='utf-8') as reponse:
                    for i in reponse:
                        save.write(i)
                        save.write(" ")
            print("je suis content que la séance vous ait plus...")
    print("nous allons nous retrouver la semaine prochaine alors...")
    return        