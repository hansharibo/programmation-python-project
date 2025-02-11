import random as rd
import lecturefichier as lf
import ProgrammeCoach as pc

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



def programmeideal(use):
    niveau = "exercicepossible/niveau"+ use[:] + '.txt'
    séanceparfaite = []
    listeentrainement,listeexercice,listefindeseance = programmelecture(niveau)
    choix ="("+ str(rd.randint(1,3)) + ")"
    while choix not in listeentrainement :
        choix ="("+ str(rd.randint(1,3)) + ")"
    i = 0
    while listeentrainement[i] != choix :
        i += 1
    i += 2
    séanceparfaite.append(listeentrainement[i])
    while listeentrainement[i] != "min":
        i += 1
    i += 2
    min = int(listeentrainement[i])
    while listeentrainement[i] != "max":
        i += 1
    i += 2
    max = int(listeentrainement[i])
    temps = rd.randint(min,max)
    séanceparfaite.append(temps)
    choix ="("+ str(rd.randint(1,3)) + ")"
    while choix not in listeexercice :
        choix ="("+ str(rd.randint(1,3)) + ")"
    i = 0
    while listeexercice[i] != choix :
        i += 1
    i += 2
    séanceparfaite.append(listeexercice[i])
    while listeexercice[i] != "min":
        i += 1
    i += 2
    min = int(listeexercice[i])
    while listeexercice[i] != "max":
        i += 1
    i += 2
    max = int(listeexercice[i])
    temps = rd.randint(min,max)
    séanceparfaite.append(temps)
    choix ="("+ str(rd.randint(1,3)) + ")"
    while choix not in listefindeseance :
        choix ="("+ str(rd.randint(1,3)) + ")"
    i = 0
    while listefindeseance[i] != choix :
        i += 1
    i += 2
    séanceparfaite.append(listefindeseance[i])
    while listefindeseance[i] != "min":
        i += 1
    i += 2
    min = int(listefindeseance[i])
    while listefindeseance[i] != "max":
        i += 1
    i += 2
    max = int(listefindeseance[i])
    temps = rd.randint(min,max)
    séanceparfaite.append(temps)
    return séanceparfaite

def séancecreatornew(use):
    temps = 0
    exercice = 0
    niveau = "exercicepossible/niveau"+ use[:] + '.txt'
    séance= []
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
    séance.append(exercice)
    séance.append(int(temps))
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
    séance.append(exercice)
    séance.append(int(temps))
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
    séance.append(exercice)
    séance.append(int(temps))
    return séance

def experience1(nbsujet):
    resultat = ["nbsujet nbséanceia nbséanceprog\n"]
    for compteur in range(nbsujet):
        if int(compteur *100 /nbsujet) == compteur *100 /nbsujet:
            print("vous en ête a ", compteur *100 /nbsujet,"%")
        niveau = ['debutant','intermédiaire','avancé']
        ordre = ['entrainement','exercice','final']
        valeurnbséance = 0
        valeurnbséance2 = 0
        niveausujet = niveau[rd.randint(0,2)]
        niveaur = "exercicepossible/niveau"+ niveausujet[:] + '.txt'
        listeentrainement,listeexercice,listefindeseance = programmelecture(niveaur)
        programmeutilisateur = séancecreatornew(niveausujet)
        programmeutilisateurideal = programmeideal(niveausujet)
        programmeutilisateur2 = []
        n = 0
        o = 0
        valeurséanceinter = 0
        valeurséanceinter1 = 0
        valeurséanceinter2 = 0
        if programmeutilisateurideal[n] != programmeutilisateur[n]:
            i = 0
            j = 0
            while listeentrainement[i] != programmeutilisateurideal[n]:
                i+= 1
            while listeentrainement[j] != programmeutilisateur[n]:
                j+= 1 
            if j - i > 0:
                if abs(j - i) == 16:
                    while listeentrainement[o] != programmeutilisateurideal[n]:
                        o += 1
                    while listeentrainement[o] != 'max':
                        o+=1
                    o+=2
                    valeurséanceinter += programmeutilisateurideal[n +1] + int(listeentrainement[o])
                    while listeentrainement[o] != 'inc':
                        o+=1
                    o+=2
                    valeurséanceinter =int(valeurséanceinter / int(listeentrainement[o]))
                    while listeentrainement[o] != 'min':
                        o += 1
                    o += 2
                    valeurséanceinter1 = programmeutilisateur[n + 1] - int(listeentrainement[o]) 
                    while listeentrainement[o] != 'inc':
                        o += 1
                    o += 2
                    valeurséanceinter1 = int(valeurséanceinter1 / int(listeentrainement[o]))
                    valeurséanceinter += valeurséanceinter1
                else :
                    valeurséanceinter = 0
                    while listeentrainement[o] != programmeutilisateurideal[n]:
                        o += 1
                    while listeentrainement[o] != 'max':
                        o+=1
                    o+=2
                    valeurséanceinter += programmeutilisateurideal[n +1] + int(listeentrainement[o])
                    while listeentrainement[o] != 'inc':
                        o+=1
                    o+=2
                    valeurséanceinter =int(valeurséanceinter/ int(listeentrainement[o]))
                    while listeentrainement[o] != 'min':
                        o+=1
                    o += 2
                    valeurséanceinter2 += int(listeentrainement[o])
                    while listeentrainement[o] != 'max':
                        o+=1
                    o += 2
                    valeurséanceinter2 += int(listeentrainement[o])
                    while listeentrainement[o] != 'inc':
                        o+=1
                    o += 2
                    valeurséanceinter2  = int(valeurséanceinter2/ int(listeentrainement[o]))
                    while listeentrainement[o] != 'min':
                        o+=1
                    o += 2
                    valeurséanceinter1 = programmeutilisateur[n] - int(listeentrainement[o]) 
                    while listeentrainement[o] != 'inc':
                        o += 1
                    o += 2
                    valeurséanceinter1 = int(valeurséanceinter1 / int(listeentrainement[o]))
                    valeurséanceinter += valeurséanceinter1 + valeurséanceinter2
            else: 
                if abs(j - i) == 16:
                    o = 0
                    valeurséanceinter = 0
                    while listeentrainement[o] != programmeutilisateur[n]:
                        o += 1
                    while listeentrainement[o] != 'max':
                        o+=1
                    o+=2
                    valeurséanceinter += programmeutilisateur[n +1] + int(listeentrainement[o])
                    while listeentrainement[o] != 'inc':
                        o+=1
                    o+=2
                    valeurséanceinter =int(valeurséanceinter/ int(listeentrainement[o]))
                    while listeentrainement[o] != 'min':
                        o+=1
                    o += 2
                    valeurséanceinter1 = int(programmeutilisateurideal[n +1]) - int(listeentrainement[o]) 
                    while listeentrainement[o] != 'inc':
                        o += 1
                    o += 2
                    valeurséanceinter1 = int(valeurséanceinter1 / int(listeentrainement[o]))
                    valeurséanceinter += valeurséanceinter1
                else :
                    valeurséanceinter = 0
                    while listeentrainement[o] != programmeutilisateur[n]:
                        o += 1
                    while listeentrainement[o] != 'max':
                        o+=1
                    o+=2
                    valeurséanceinter += programmeutilisateur[n +1] + int(listeentrainement[o])
                    while listeentrainement[o] != 'inc':
                        o+=1
                    o+=2
                    valeurséanceinter =int(valeurséanceinter/ int(listeentrainement[o]))
                    while listeentrainement[o] != 'min':
                        o+=1
                    o += 2
                    valeurséanceinter2 += int(listeentrainement[o])
                    while listeentrainement[o] != 'max':
                        o+=1
                    o += 2
                    valeurséanceinter2 += int(listeentrainement[o])
                    while listeentrainement[o] != 'inc':
                        o+=1
                    o += 2
                    valeurséanceinter2  = int(valeurséanceinter2/ int(listeentrainement[o]))
                    while listeentrainement[o] != 'min':
                        o+=1
                    o += 2
                    valeurséanceinter1 = programmeutilisateurideal[n] - int(listeentrainement[o]) 
                    while listeentrainement[o] != 'inc':
                        o += 1
                    o += 2
                    valeurséanceinter1 = int(valeurséanceinter1 / int(listeentrainement[o]))
                    valeurséanceinter += valeurséanceinter1 + valeurséanceinter2
        else :
            valeurséanceinter = 0
            while listeentrainement[o] != programmeutilisateur[n]:
                o += 1
            while listeentrainement[o] != 'inc':
                o += 1
            o+=2
            valeurséanceinter = int(abs(programmeutilisateur[ n + 1 ]- programmeutilisateurideal[ n + 1 ]/ int(listeentrainement[o])))
        if valeurnbséance < valeurséanceinter:
            valeurnbséance = valeurséanceinter
        n = 2
        o = 0
        valeurséanceinter = 0
        valeurséanceinter1 = 0
        valeurséanceinter2 = 0
        if programmeutilisateurideal[n] != programmeutilisateur[n]:
            i = 0
            j = 0
            while listeexercice[i] != programmeutilisateurideal[n]:
                i+= 1
            while listeexercice[j] != programmeutilisateur[n]:
                j+= 1 
            if j - i > 0:
                if abs(j - i) == 16:
                    o = 0
                    valeurséanceinter = 0
                    while listeexercice[o] != programmeutilisateurideal[n]:
                        o += 1
                    while listeexercice[o] != 'max':
                        o+=1
                    o+=2
                    valeurséanceinter += programmeutilisateurideal[n +1] + int(listeexercice[o])
                    while listeexercice[o] != 'inc':
                        o+=1
                    o+=2
                    valeurséanceinter =int(valeurséanceinter/ int(listeexercice[o]))
                    while listeexercice[o] != 'min':
                        o+=1
                    o += 2
                    valeurséanceinter1 = programmeutilisateur[n + 1 ] - int(listeexercice[o]) 
                    while listeexercice[o] != 'inc':
                        o += 1
                    o += 2
                    valeurséanceinter1 = int(valeurséanceinter1 / int(listeexercice[o]))
                    valeurséanceinter += valeurséanceinter1
                else :
                    valeurséanceinter = 0
                    while listeexercice[o] != programmeutilisateurideal[n]:
                        o += 1
                    while listeexercice[o] != 'max':
                        o+=1
                    o+=2
                    valeurséanceinter += programmeutilisateurideal[n +1] + int(listeexercice[o])
                    while listeexercice[o] != 'inc':
                        o+=1
                    o+=2
                    valeurséanceinter =int(valeurséanceinter/ int(listeexercice[o]))
                    while listeexercice[o] != 'min':
                        o+=1
                    o += 2
                    valeurséanceinter2 += int(listeexercice[o])
                    while listeexercice[o] != 'max':
                        o+=1
                    o += 2
                    valeurséanceinter2 += int(listeexercice[o])
                    while listeexercice[o] != 'inc':
                        o+=1
                    o += 2
                    valeurséanceinter2  = int(valeurséanceinter2/ int(listeexercice[o]))
                    while listeexercice[o] != 'min':
                        o+=1
                    o += 2
                    valeurséanceinter1 = programmeutilisateur[n] - int(listeexercice[o]) 
                    while listeexercice[o] != 'inc':
                        o += 1
                    o += 2
                    valeurséanceinter1 = int(valeurséanceinter1 / int(listeexercice[o]))
                    valeurséanceinter += valeurséanceinter1 + valeurséanceinter2
            else: 
                if abs(j - i) == 16:
                    o = 0
                    valeurséanceinter = 0
                    while listeexercice[o] != programmeutilisateur[n]:
                        o += 1
                    while listeexercice[o] != 'max':
                        o+=1
                    o+=2
                    valeurséanceinter += programmeutilisateur[n +1] + int(listeexercice[o])
                    while listeexercice[o] != 'inc':
                        o+=1
                    o+=2
                    valeurséanceinter =int(valeurséanceinter/ int(listeexercice[o]))
                    while listeexercice[o] != 'min':
                        o+=1
                    o += 2
                    valeurséanceinter1 = programmeutilisateurideal[n + 1] - int(listeexercice[o]) 
                    while listeexercice[o] != 'inc':
                        o += 1
                    o += 2
                    valeurséanceinter1 = int(valeurséanceinter1 / int(listeexercice[o]))
                    valeurséanceinter += valeurséanceinter1
                else :
                    valeurséanceinter = 0
                    while listeexercice[o] != programmeutilisateur[n]:
                        o += 1
                    while listeexercice[o] != 'max':
                        o+=1
                    o+=2
                    valeurséanceinter += programmeutilisateur[n +1] + int(listeexercice[o])
                    while listeexercice[o] != 'inc':
                        o+=1
                    o+=2
                    valeurséanceinter =int(valeurséanceinter/ int(listeexercice[o]))
                    while listeexercice[o] != 'min':
                        o+=1
                    o += 2
                    valeurséanceinter2 = int(listeexercice[o])
                    while listeexercice[o] != 'max':
                        o+=1
                    o += 2
                    valeurséanceinter2 += int(listeexercice[o])
                    while listeexercice[o] != 'inc':
                        o+=1
                    o += 2
                    valeurséanceinter2  = int(valeurséanceinter2/ int(listeexercice[o]))
                    while listeexercice[o] != 'min':
                        o+=1
                    o += 2
                    valeurséanceinter1 = programmeutilisateurideal[n] - int(listeexercice[o]) 
                    while listeexercice[o] != 'inc':
                        o += 1
                    o += 2
                    valeurséanceinter1 = int(valeurséanceinter1 / int(listeexercice[o]))
                    valeurséanceinter += valeurséanceinter1 + valeurséanceinter2
        else :
            valeurséanceinter = 0
            while listeexercice[o] != programmeutilisateur[n]:
                o += 1
            while listeexercice[o] != 'inc':
                o += 1
            o+=2
            valeurséanceinter = int(abs(programmeutilisateur[ n + 1 ]- programmeutilisateurideal[ n + 1 ]/ int(listeexercice[o])))
        if valeurnbséance < valeurséanceinter:
            valeurnbséance = valeurséanceinter
        n = 4
        o = 0
        valeurséanceinter = 0
        valeurséanceinter1 = 0
        valeurséanceinter2 = 0
        if programmeutilisateurideal[n] != programmeutilisateur[n]:
            i = 0
            j = 0
            while listefindeseance[i] != programmeutilisateurideal[n]:
                i+= 1
            while listefindeseance[j] != programmeutilisateur[n]:
                j+= 1 
            if j - i > 0:
                if abs(j - i) == 16:
                    o = 0
                    valeurséanceinter = 0
                    while listefindeseance[o] != programmeutilisateurideal[n]:
                        o += 1
                    while listefindeseance[o] != 'max':
                        o+=1
                    o+=2
                    valeurséanceinter += programmeutilisateurideal[n +1] + int(listefindeseance[o])
                    while listefindeseance[o] != 'inc':
                        o+=1
                    o+=2
                    valeurséanceinter =int(valeurséanceinter/ int(listefindeseance[o]))
                    while listefindeseance[o] != 'min':
                        o+=1
                    o += 2
                    valeurséanceinter1 = programmeutilisateur[n + 1] - int(listefindeseance[o]) 
                    while listefindeseance[o] != 'inc':
                        o += 1
                    o += 2
                    valeurséanceinter1 = int(valeurséanceinter1 / int(listefindeseance[o]))
                    valeurséanceinter += valeurséanceinter1
                else :
                    valeurséanceinter = 0
                    while listefindeseance[o] != programmeutilisateurideal[n]:
                        o += 1
                    while listefindeseance[o] != 'max':
                        o+=1
                    o+=2
                    valeurséanceinter += programmeutilisateurideal[n +1] + int(listefindeseance[o])
                    while listefindeseance[o] != 'inc':
                        o+=1
                    o+=2
                    valeurséanceinter =int(valeurséanceinter/ int(listefindeseance[o]))
                    while listefindeseance[o] != 'min':
                        o+=1
                    o += 2
                    valeurséanceinter2 += int(listefindeseance[o])
                    while listefindeseance[o] != 'max':
                        o+=1
                    o += 2
                    valeurséanceinter2 += int(listefindeseance[o])
                    while listefindeseance[o] != 'inc':
                        o+=1
                    o += 2
                    valeurséanceinter2  = int(valeurséanceinter2/ int(listefindeseance[o]))
                    while listefindeseance[o] != 'min':
                        o+=1
                    o += 2
                    valeurséanceinter1 = programmeutilisateur[n] - int(listefindeseance[o]) 
                    while listefindeseance[o] != 'inc':
                        o += 1
                    o += 2
                    valeurséanceinter1 = int(valeurséanceinter1 / int(listefindeseance[o]))
                    valeurséanceinter += valeurséanceinter1 + valeurséanceinter2
            else: 
                if abs(j - i) == 16:
                    o = 0
                    valeurséanceinter = 0
                    while listefindeseance[o] != programmeutilisateur[n]:
                        o += 1
                    while listefindeseance[o] != 'max':
                        o+=1
                    o+=2
                    valeurséanceinter += programmeutilisateur[n +1] + int(listefindeseance[o])
                    while listefindeseance[o] != 'inc':
                        o+=1
                    o+=2
                    valeurséanceinter =int(valeurséanceinter/ int(listefindeseance[o]))
                    while listefindeseance[o] != 'min':
                        o+=1
                    o += 2
                    valeurséanceinter1 = programmeutilisateurideal[n + 1] - int(listefindeseance[o]) 
                    while listefindeseance[o] != 'inc':
                        o += 1
                    o += 2
                    valeurséanceinter1 = int(valeurséanceinter1 / int(listefindeseance[o]))
                    valeurséanceinter += valeurséanceinter1
                else :
                    valeurséanceinter = 0
                    while listefindeseance[o] != programmeutilisateur[n]:
                        o += 1
                    while listefindeseance[o] != 'max':
                        o+=1
                    o+=2
                    valeurséanceinter += programmeutilisateur[n +1] + int(listefindeseance[o])
                    while listefindeseance[o] != 'inc':
                        o+=1
                    o+=2
                    valeurséanceinter =int(valeurséanceinter/ int(listefindeseance[o]))
                    while listefindeseance[o] != 'min':
                        o+=1
                    o += 2
                    valeurséanceinter2 += int(listefindeseance[o])
                    while listefindeseance[o] != 'max':
                        o+=1
                    o += 2
                    valeurséanceinter2 += int(listefindeseance[o])
                    while listefindeseance[o] != 'inc':
                        o+=1
                    o += 2
                    valeurséanceinter2  = int(valeurséanceinter2/ int(listefindeseance[o]))
                    while listefindeseance[o] != 'min':
                        o+=1
                    o += 2
                    valeurséanceinter1 = programmeutilisateurideal[n] - int(listefindeseance[o]) 
                    while listefindeseance[o] != 'inc':
                        o += 1
                    o += 2
                    valeurséanceinter1 = int(valeurséanceinter1 / int(listefindeseance[o]))
                    valeurséanceinter += valeurséanceinter1 + valeurséanceinter2
        else :
            valeurséanceinter = 0
            while listefindeseance[o] != programmeutilisateur[n]:
                o += 1
            while listefindeseance[o] != 'inc':
                o += 1
            o+=2
            valeurséanceinter = int(abs(programmeutilisateur[ n + 1 ]- programmeutilisateurideal[ n + 1 ]/ int(listefindeseance[o])))
        if valeurnbséance < valeurséanceinter:
            valeurnbséance = valeurséanceinter
        programmeutilisateur2 = pc.programme(niveausujet)
        while programmeutilisateur2 != programmeutilisateurideal and valeurnbséance2 <= 4680:
            valeurnbséance2 += 1
            programmeutilisateur2 = pc.programme(niveausujet)
        resultat.append(str(compteur)+ " " + str(valeurnbséance) +" "+ str(valeurnbséance2)+"\n")
    with open("resultat/resultat"+str(nbsujet)+".txt","w", encoding="utf-8") as saveexp:
        for i in resultat:
            saveexp.write(i)

experience1(50000)