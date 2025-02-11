import random as rd
import lecturefichier as lf

def moy(dico):
    entrainement =[]
    trueentrainement =''
    entrainementtemps = []
    truetempsentrainement = 0
    exercice =[]
    trueexercice = ''
    exercicetemps= []
    truetempsexercice = 0
    fin = []
    truefin =''
    fintemps = []
    truetempsfin = 0
    for i in dico.values():

        if i[0] not in entrainement:
            entrainement.append(i[0])
            entrainement.append(1)
        else :
            j = 0
            while entrainement[j] != i[0]:
                j += 1
            j+=1
            entrainement[j] +=1
        if i[2] not in exercice:
            exercice.append(i[2])
            exercice.append(1)
        else :
            j = 0
            while exercice[j] != i[2]:
                j += 1
            j+=1
            exercice[j] +=1
        if i[4] not in fin:
            fin.append(i[4])
            fin.append(1)
        else :
            j = 0
            while fin[j] != i[4]:
                j += 1
            j+=1
            fin[j] +=1
    max = 0
    i = 0 
    indice = 0
    for i in range(len(entrainement)):
        if i%2 == 1:
            if max < entrainement[i]:
                indice = i -1
                max = entrainement[i]
    trueentrainement = entrainement[indice]
    for training in dico.values() :
        if training[0] == trueentrainement:
            entrainementtemps.append(training[1])
    for i in entrainementtemps :
        truetempsentrainement += i
    truetempsentrainement = int(truetempsentrainement/len(entrainementtemps))
    max = 0
    i = 0 
    indice = 0
    for i in range(len(exercice)):
        if i%2 == 1:
            if max < exercice[i]:
                indice = i -1
                max = exercice[i]
    trueexercice = exercice[indice]
    for training in dico.values() :
        if training[2] == trueexercice:
            exercicetemps.append(training[3])
    for i in exercicetemps :
        truetempsexercice += i
    truetempsexercice = int(truetempsexercice/len(exercicetemps))
    max = 0
    i = 0 
    indice = 0
    for i in range(len(fin)):
        if i%2 == 1:
            if max < fin[i]:
                indice = i -1
                max = fin[i]
    truefin = fin[indice]
    for training in dico.values() :
        if training[4] == truefin:
            fintemps.append(training[5])
    for i in fintemps :
        truetempsfin += i
    truetempsfin = int(truetempsfin/len(fintemps))
    return[trueentrainement,truetempsentrainement,trueexercice,truetempsexercice,truefin,truetempsfin]





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

def experience2(nbsujet, niveau):
    dicoutilisateur = {}
    compteur =0
    resultat =  ["nbsujet act10 act100 act1000\n"]
    niveaur = "exercicepossible/niveau"+ niveau[:] + '.txt'
    nbouverturerell10 = 0
    nbouverturerell100 = 0
    nbouverturerell1000 = 0
    listeentrainement,listeexercice,listefindeseance = programmelecture(niveaur)
    séancemoy = séancecreatornew(niveau)
    listemoy10 = séancemoy[:]
    listemoy100 = séancemoy[:]
    listemoy1000 = séancemoy[:]
    for compteur in range(nbsujet):
        if int(compteur *100 /nbsujet) == compteur *100 /nbsujet:
            print("vous en ête a ", compteur *100 /nbsujet,"%")
        if compteur not in dicoutilisateur.keys():
            valeurséanceintercompt = []
            varcompteur = [listemoy10, listemoy100, listemoy1000]
            programmeutilisateurideal = programmeideal(niveau)[:]
            for i in varcompteur :
                programmeutilisateur = i[:]
                n = 0
                o = 0
                valeurnbséance = 0
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
                            valeurséanceinter1 = programmeutilisateur[n + 1] - int(listeentrainement[o]) 
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
                            valeurséanceinter2 = int(listeentrainement[o])
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
                            valeurséanceinter1 = programmeutilisateurideal[n + 1] - int(listeentrainement[o]) 
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
                            valeurséanceinter1 = programmeutilisateur[n + 1] - int(listeexercice[o]) 
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
                            valeurséanceinter1 = programmeutilisateurideal[n + 1] - int(listeexercice[o]) 
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
                            valeurséanceinter1 = programmeutilisateur[n + 1] - int(listefindeseance[o]) 
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
                            valeurséanceinter1 = programmeutilisateurideal[n + 1] - int(listefindeseance[o]) 
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
                valeurséanceintercompt.append(valeurnbséance)
            dicoutilisateur[compteur] = programmeutilisateurideal[:]
        for test in dicoutilisateur.keys():
            nbouverturerell10 += 1
            if nbouverturerell10== 10:
                nbouverturerell10 = 0
                listemoy10 = moy(dicoutilisateur)
        for test in dicoutilisateur.keys():
            nbouverturerell100 += 1
            if nbouverturerell100== 100:
                nbouverturerell100 = 0
                listemoy100 = moy(dicoutilisateur)
        for test in dicoutilisateur.keys():
            nbouverturerell1000 += 1
            if nbouverturerell1000== 1000:
                nbouverturerell1000 = 0
                listemoy100 = moy(dicoutilisateur)
        
        resultat.append(str(compteur)+ " "+ str(valeurséanceintercompt[0]) + " " + str(valeurséanceintercompt[1]) + " "+ str(valeurséanceintercompt[2]) + "\n")
    with open("resultat/resultat" + niveau  +str(nbsujet)+".txt","w",encoding='utf-8') as saveresulatat:
        for i in resultat:
            saveresulatat.write(i)
    return

for i in ['debutant','intermédiaire','avancé']:
    experience2(1000, i)
print("fin")

