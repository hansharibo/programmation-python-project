# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def modifinfoex(file, infomadif, new): #fonction pour modifier un fichier
    fichierinmatrice=[]
    with open(file,"r",encoding ='utf-8') as save:
        fichierinmatrice = save.readlines(-1)
    for i in range(len(fichierinmatrice)):
        fichierinmatrice[i] = matricetomatriceint(fichierinmatrice[i])
    i = 0
    while i != len(fichierinmatrice):
        try:
            if fichierinmatrice[i][2] == infomadif:
                j = 2
                while fichierinmatrice[i][j] != "moy":
                    j+=1
                j+=2
                fichierinmatrice[i][j] = str(new)
                with open(file,'w', encoding="utf-8") as save1:
                    for h in fichierinmatrice:
                        save1.write(mattostring(h))
                return
            i+=1
        except:
            i+=1
    print("erreur info not found")
    return


def stringtonumber(string) : #fonciton pour transformer et trouver un nombre dans une chaine de caractère
    num = 0
    for i in string:
        try :
            num = num * 10 + int(i)
        except:
            return num
    return num


def mattostring(mat): # fonction qui transforme une string en liste
    string = ""
    j = 0
    while j != len(mat) :
        if mat[j] != '' and j != len(mat) -1:
            string += mat[j] + " "
        elif mat[j] != '' and j == len(mat) -1:
            string += mat[j]
        j += 1
    return string

def mattostringintern(mat): # fonction qui transforme une string en liste
    string = ""
    j = 0
    while j != len(mat) :
        if mat[j] != '' and j != len(mat) -1:
            string += mat[j] + "/"
        elif mat[j] != '' and j == len(mat) -1:
            string += mat[j]
        j += 1
    return string

def matricetomatrice(string): # fonction qui transforme une string en liste
    mat=[]
    word = ''
    for i in range(len(string)): # on itère jusqu'a la fin de la chaine en terminant les mots a chaque espace
        if string[i] != " " and string[i] != "’"  and string[i] != "1"  and string[i] != "2"  and string[i] != "3"  and string[i] != "4"  and string[i] != "5"  and string[i] != "6"  and string[i] != "7"  and string[i] != "8"  and string[i] != "9"  and string[i] != "0" and string[i] != "~" and string[i] != "«" and string[i] != "»" and string[i] != "?" and string[i] != "'" and string[i] != "," and string[i] != "." and string[i] != "!" and string[i] != "(" and string[i] != "+" and string[i] != "-" and string[i] != ":" and string[i] != ";" and string[i] != "[" and string[i] != ")" and string[i] != "]":
            word += string[i]
        else:
            if string[i] == "'" or string[i] == "’":
                word += "'"
            if word !=' ' and word != '':
                mat.append(word.replace("\n",""))
            word =''
    mat.append(word)
    return mat # on retourne la matrice nouvellement formé

def matricetomatricelecturespace(string): # fonction qui transforme une string en liste
    mat=[]
    word = ''
    for i in range(len(string)): # on itère jusqu'a la fin de la chaine en terminant les mots a chaque espace
        if string[i] != " " and string[i] != "/":
            word += string[i]
        elif string[i] == "/":
            word += " "
        else:
            if word != '':
                mat.append(word)
                word =''
    if word != '':            
        mat.append(word)
    return mat # on retourne la matrice nouvellement formé

def matricetomatriceint(string): # fonction qui transforme une string en liste
    mat=[]
    word = ''
    for i in range(len(string)): # on itère jusqu'a la fin de la chaine en terminant les mots a chaque espace
        if string[i] != " ":
            word += string[i]
        else:
            if word != '':
                mat.append(word)
                word =''
    if word != '':            
        mat.append(word)
    return mat # on retourne la matrice nouvellement formé

def modifinfo(file, infomadif, new):
    fichierinmatrice=[]
    with open(file,"r",encoding ='utf-8') as save:
        fichierinmatrice = save.readlines(-1)
    for i in range(len(fichierinmatrice)):
        fichierinmatrice[i] = matricetomatriceint(fichierinmatrice[i])
    for i in range(len(fichierinmatrice)):
        for j in fichierinmatrice[i]:
            if j == infomadif:
                fichierinmatrice[i] = [infomadif,":",new + "\n"]
                with open(file,'w', encoding="utf-8") as save1:
                    for h in fichierinmatrice:
                        save1.write(mattostring(h))
                return
    print("erreur info not found")
    return


def matricetoliste(matrice): # fonction qui transforme une matrice en liste 
    liste = []
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            liste.append(matrice[i][j])
    return liste

def fichiertodico(dicofile): # fonction qui a partir d'un fichier dico le transforme en dico
    dicofichier = {}
    fileopen=open(dicofile,'r', encoding='utf-8')
    for i in fileopen:
        intermediere = matricetomatriceint(i)
        dicofichier[intermediere[0]] = int(intermediere[-1])
    return dicofichier

def iswordexist(word, file): #fonction pour verifier l'existance d'un mot
    motatrouver = open(file, "r")
    for i in motatrouver:
        if word in i:
            return True # s'il existe
    return False # s'il n'existe pas

def chercherinfo(infoatrouver, user):#fonction pour trouver une info associé a un utilisateur
    filelecture = open(user, 'r', encoding='utf-8')
    matricebrut =[]
    reponse = []
    for i in filelecture:
        matricebrut.append(i.splitlines() + [" "])
    matricebrut = matricetomatriceint(mattostring(matricetomatriceint(matricetoliste(matricebrut))))
    i = 0
    while i != len(matricebrut) - 1:
        if matricebrut[i] == infoatrouver:
            matricenew = matricebrut[i+2:]
            for a in matricenew:
                if a == ':':
                    return reponse[:-1]
                reponse.append(a)
            return reponse
        else:
            i+=1
    return "information non enregistrée"

def classeur(file, dico): # fonction pour donner un classement global en fonction de la réccurence d'un mot, plus le score est élevé, plus le texte s'approche d'un thème prédéterminer
    classement = 0
    dicoomnipotent = fichiertodico(dico)
    fichiertotal = []
    fichieraanalyser = open(file, "r", encoding='utf-8')
    for i in fichieraanalyser:
        fichiertotal.append(matricetomatrice(i))
    fichiertotal = matricetoliste(fichiertotal)
    for i in dicoomnipotent.keys():
        for j in fichiertotal :
            if j == i:
                classement += dicoomnipotent[i]
    return classement