# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 21:30:20 2023

@author: nljfe
"""
import lecturefichier as lf
import os

def newmoy(): #fonction qui reattribut les moyennes en fonction des utilisateurs
    buffer = 0
    listeutdébutant = []
    entrainementdebutant = []
    niveau = ['debutant','intermédiaire','avancé']
    ordre = ['entrainement','exercice','final']
    file = os.listdir("utilisateur")
    print(file)
    for n in niveau:
        for o in ordre :
            listeutdébutant = []
            for i in file:
                liste = lf.chercherinfo( "niveau", "utilisateur/" + i)
                if liste[0] == n :
                    listeutdébutant.append("utilisateur/" + i)
                    print("pint")
            entrainementdebutant = []
            for u in listeutdébutant:
                entrainementwait = ''
                entrainement = lf.chercherinfo( o, u)
                if len(entrainement) > 2 :
                    for i in range(len(entrainement)-2):
                        entrainementwait += entrainement[i] + "/"
                    entrainementwait += entrainement[-2]
                    entrainement = [entrainementwait, entrainement[-1]]
                if  entrainement[0] not in entrainementdebutant:
                    entrainementdebutant.append(entrainement[0])
                    entrainementdebutant.append([lf.stringtonumber(entrainement[-1])])
                else:
                    i = 0
                    while entrainementdebutant[i] != entrainement[0]:
                        i += 1
                    else:
                        i += 1
                    entrainementdebutant[i].append(lf.stringtonumber(entrainement[-1]))
            print(entrainementdebutant)
            for z in range(len(entrainementdebutant)):
                if z % 2 == 1:
                    print(entrainementdebutant[z])
                    for j in range(len(entrainementdebutant[z])):
                        print("pong")
                        buffer += entrainementdebutant[z][j]
                    buffer = buffer / len(entrainementdebutant[z])
                    entrainementdebutant[z] = buffer
            for b in range(len(entrainementdebutant)):
                if b % 2 == 0:
                    try :
                        lf.modifinfoex("exercicepossible/niveau"+ n +".txt", entrainementdebutant[i],entrainementdebutant[i+1])
                    except :
                        print(entrainementdebutant[b])
    return      
    




def dicocreate(filetoanalyse, namedico): # fonction qui a partir d'un fichier brut classe, tri et donne une valeur au mot en focntion de leur importance
    analyse = open(filetoanalyse,"r",encoding='utf-8')
    nonanalyseur = ["le","la", "l'", "les","ou","en","dans", "au", "aux", "du" ,"des", "mon" ,"ma", "mes", "ton" ,"ta" ,"tes" ,"son", 'sa', "ses", "notre", "nos", "votre", "vos"," leur", "leurs", "ce", "cet", "cette", "ceci", "ceux-ci", "cela", "ces", "un" ,"une", "des", "d'", "du","de","à","et","qu'","qui","que","quoi","pour"]
    liste_mot = []
    liste_mot_trie =[]
    recurrenceinliste = []
    for i in analyse:
        liste_mot.append(i)
    analyse.close()
    liste_mot = lf.matricetomatrice(lf.matricetoliste(liste_mot))
    for i in liste_mot:
        reccurrence = 0
        for j in liste_mot:
            if i == j and j not in nonanalyseur:
                reccurrence += 1
        if reccurrence >= 10 and i.lower() not in nonanalyseur: #nombre d'occurence min pour q'un mot soit accepté
            recurrenceinliste.append(reccurrence)
            liste_mot_trie.append(i.replace("\n","").lower())
    if liste_mot_trie != []:
        liste_mot_trie.sort()
        i=0
        while i != len(liste_mot_trie)-1:
            if liste_mot_trie[i] == liste_mot_trie[i +1]:
                liste_mot_trie.remove(liste_mot_trie[i])
                i = 0
            else :
                i+=1
        ecrituredico = open("dico/" + namedico + ".dico", "w", encoding="utf-8")
        for i in liste_mot_trie :
            if i !='' and i not in nonanalyseur:
                ecrituredico.write(i + " : " + str(recurrenceinliste[liste_mot_trie.index(i)]) +"\n")
        print("fichier modifié avec vos préférences")
    else :
        print("aucune préference n'a été ajouté")
    ecrituredico.close()
    return

def comparateurdedico(diconom1, diconom2,nom):#fonction qui permet de supprimer les mots qui existe déja dans un dico, ce qui a pour but d'amplifier l'importance des mots propre a un dico
    dico1_listify = []
    dico2_listify = []
    listeintermediaire = []
    liseurdico1 = open(diconom1,"r",encoding='utf-8')
    for i in liseurdico1:
        dico1_listify.append(lf.matricetomatriceint(i.replace("\n","")))
    liseurdico1.close()
    liseurdico2 = open(diconom2, "r",encoding='utf-8')
    for i in liseurdico2:
        dico2_listify.append(lf.matricetomatriceint(i.replace("\n","")))
    liseurdico2.close()
    for i in dico1_listify:
        if i != []:
            listeintermediaire.append(i[0])
    ecrituredico = open("dico/"+nom+"new.dico", "w",encoding='utf-8')
    for i in dico2_listify:
        #print (i)
        if i != []:
            if i[0] not in listeintermediaire:
                ecrituredico.write(i[0] + " : " + i[-1]+"\n")
    print("vos listes ont été comparé")
    return

def améliorerfichier(file1, file2):#fonction qui permet de fine tune un fichier non utiliser, dans le programme finale...
    raison = 0
    fileuser ="utilisateur.ut"
    dicomal ="dico/dicotestmal.dico"
    dicosupmal ="dico/dicomalnew.dico"
    dicobien = "dico/dicotestbien.dico"
    dicosupbien = "dico/dicobiennew.dico"
    print("comment allez vous ?")
    text = input("réponse :")
    fichier = open("reponseutilisateur.rp", "w", encoding='utf-8')
    fichier.write(text)
    fichier.close()
    print(lf.classeur("reponseutilisateur.rp", dicomal))
    print(lf.classeur("reponseutilisateur.rp", dicobien))
    if lf.classeur("reponseutilisateur.rp", dicomal) + lf.classeur("reponseutilisateur.rp", dicosupmal)> lf.classeur("reponseutilisateur.rp", dicobien) :
        print("ah merde !")
        raison = 1
    else:
        print("coolll!!")
        raison = 0
    a = input("réponse correcte ?(y/n)")
    if a == 'n':
        print("la réponse aurait du être :")
        if raison == 1 :
            print("cool")
        if raison == 0 :
            print("ah merde")
        print("nous ajoutons votre réponse")
        if raison == 1 :
            for i in range(1000):
                changement = open(file2,"a", encoding='utf-8')
                changement.write("\n" + text)
                changement.close()
            dicocreate(file2, "dicotestbien")
        if raison == 0 :
            for i in range(1000):
                changement = open(file1,"a", encoding='utf-8')
                changement.write("\n" + text)
                changement.close()
            dicocreate(file1, "dicotestmal")     
    return