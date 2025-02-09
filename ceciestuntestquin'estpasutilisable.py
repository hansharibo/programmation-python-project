def modifséancegen(user,isexercicehard,num):
    newentrainement = []
    type = ["entrainement","exercice","final"]
    listeentrainement,listeseance,listefinalex = pc.programmelecture("exercicepossible/niveau"+lf.mattostring(lf.chercherinfo("niveau", user))+".txt")
    entrainement = lf.chercherinfo(type[num - 1], user)
    inc =0
    unit =''
    valeur = 0
    min = 0
    max = 0
    if len(entrainement) > 2 :
        newentrainement.append(lf.mattostringintern(entrainement[:-1]))
        newentrainement.append(lf.mattostringintern(entrainement[:-2]))
    for i in entrainement[1]:
        try:
            valeur = valeur * 10 + int(i)
        except:
            break
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
    if valeur + inc > max:
        i = 0
        while listefinal[i] != entrainement[0]:
            i+=1
        i -= 2
        nieveausup = "(" + str(int(listefinal[i][1]) + 1 ) + ")"
        if nieveausup not in listefinal:
            print("ils semblerait qu'il vous faille changer de niveau")
            niveauutilisateur = lf.mattostring(lf.chercherinfo(user, "niveau"))
            listeniveau = ['debutant', 'intermédiaire', 'avancé']
            for i in range(len(listeniveau)):
                if listeniveau[i] == niveauutilisateur:
                    try:
                        lf.modifinfo(user,"niveau", listeniveau[i+1])
                        listeentrainement,listeseance,listefinalex = pc.programmelecture("exercicepossible/niveau"+lf.mattostring(lf.chercherinfo("niveau", user))+".txt")
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
            niveauutilisateur = lf.mattostring(lf.chercherinfo(user, "niveau"))
            listeniveau = ['debutant', 'intermédiaire', 'avancé']
            for i in range(len(listeniveau)):
                if listeniveau[i] == niveauutilisateur:
                    try:
                        lf.modifinfo(user,"niveau", listeniveau[i - 1])
                        listeentrainement,listeseance,listefinalex = pc.programmelecture("exercicepossible/niveau"+lf.mattostring(lf.chercherinfo("niveau", user))+".txt")
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