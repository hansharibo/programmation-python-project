# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 21:33:42 2024

@author: nljfe
"""

import random as rd
def programme(pNiveau):
    #définition des listes d'exercices avec leurs niveaux
    listeechauffement = ["étirement","marche/active","footing","accélération/progressive"] #4 éléments
    #                   poids = 0       1               1               2
    listetempsechauffement = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40] #39 éléments
    listeexercice = ["alternance/course/marche","course/(distance)","course/(temps)","alternance/effort/marche","pyramide/de/VMA"] #5 éléments
    listealternance = ["5 fois 30s/30s", "5 fois 45s/45s", "8 fois 30s/30s", "8 fois 45s/45s", "5 fois 1min/45s", "10 fois 30s/30s", "10 fois 45s/45s", "8 fois 1min/45s", "10 fois 1min/45s", "5 fois 3min/ 1min", "8 fois 3min/1min", "5 fois 4min/1min", "8 fois 4min/1min"] #13 éléments
    listedistance = [20,25,3,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125,130,135,140,145,150] #27 éléments
    listeduree = [15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120] #22 éléments
    listepyramide = [1,2] #2 éléments
    listefinseance = ["étirement","marche","trottiner"] #3 éléments
    listetempsfinseance = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] #16 éléments
    #création du programme en fonction du niveau
    difficultemax = 0
    difficulte=99
    entrainement =[]
    programme =[]
    if pNiveau == "debutant":
        programme = []
        difficulte = 0
        difficultetemps = rd.randint(0,2)
        programme.append(listeechauffement[difficultetemps])
        difficulte += difficultetemps
        difficultetemps = rd.randint(0,2)
        programme.append(listeexercice[difficultetemps])
        difficulte += difficultetemps
        difficultetemps = rd.randint(0,1)
        programme.append(listefinseance[difficultetemps])
        difficulte += difficultetemps
        programmetemps = []
        difficultetemps = difficulte
        programmetemps = []
        difficulte = difficultetemps
        difficultetemps1 = rd.randint(0,8)
        programmetemps.append(listetempsechauffement[difficultetemps1])
        difficulte += difficultetemps1
        if programme[1] == "course (distance)":
            difficultetemps1 = rd.randint(0,6)
            programmetemps.append(listedistance[difficultetemps1])
        elif programme[1] == "course (durée)":
            difficultetemps1 = rd.randint(0,6)
            programmetemps.append(listeduree[difficultetemps1])
        elif programme[1] == "alternance course/marche" or programme[1] == "alternance effort/marche":
            difficultetemps1 = rd.randint(0,3)
            programmetemps.append(listealternance[difficultetemps1])
        else:
            difficultetemps1 = rd.randint(0,1)
            programmetemps.append(listepyramide[difficultetemps1])
        difficulte += difficultetemps1
        difficultetemps1 = rd.randint(0,5)
        programmetemps.append(listetempsfinseance[difficultetemps1])
        difficulte += difficultetemps1
            
    elif pNiveau == "intermédiaire":
        difficultemax = 6
        programme = []
        difficulte = 0
        difficultetemps = rd.randint(0,3)
        programme.append(listeechauffement[difficultetemps])
        difficulte += difficultetemps
        difficultetemps = rd.randint(0,3)
        programme.append(listeexercice[difficultetemps])
        difficulte += difficultetemps
        difficultetemps = rd.randint(0,2)
        programme.append(listefinseance[difficultetemps])
        difficulte += difficultetemps
        programmetemps = []
        difficultetemps = difficulte
        difficulte = 99
        programmetemps = []
        difficulte = difficultetemps
        difficultetemps1 = rd.randint(0,13)
        programmetemps.append(listetempsechauffement[difficultetemps1])
        difficulte += difficultetemps1
        if programme[1] == "course (distance)":
            difficultetemps1 = rd.randint(2,16)
            programmetemps.append(listedistance[difficultetemps1])
        elif programme[1] == "course (durée)":
            difficultetemps1 = rd.randint(3,15)
            programmetemps.append(listeduree[difficultetemps1])
        elif programme[1] == "alternance course/marche" or programme[1] == "alternance effort/marche":
            difficultetemps1 = rd.randint(4,8)
            programmetemps.append(listealternance[difficultetemps1])
        else:
            difficultetemps1 = rd.randint(0,1)
            programmetemps.append(listepyramide[difficultetemps1])
        difficulte += difficultetemps1
        difficultetemps1 = rd.randint(0,5)
        programmetemps.append(listetempsfinseance[difficultetemps1])
        difficulte += difficultetemps1   
    else:
        programme = []
        difficulte = 0
        difficultetemps = rd.randint(0,3)
        programme.append(listeechauffement[difficultetemps])
        difficulte += difficultetemps
        difficultetemps = rd.randint(0,4)
        programme.append(listeexercice[difficultetemps])
        difficulte += difficultetemps
        difficultetemps = rd.randint(0,2)
        programme.append(listefinseance[difficultetemps])
        difficulte += difficultetemps
        programmetemps = []
        difficultetemps = difficulte
        difficulte = 99
        programmetemps = []
        difficulte = difficultetemps
        difficultetemps1 = rd.randint(0,38)
        programmetemps.append(listetempsechauffement[difficultetemps1])
        difficulte += difficultetemps1
        if programme[1] == "course (distance)":
            difficultetemps1 = rd.randint(6,26)
            programmetemps.append(listedistance[difficultetemps1])
        elif programme[1] == "course (durée)":
            difficultetemps1 = rd.randint(6,21)
            programmetemps.append(listeduree[difficultetemps1])
        elif programme[1] == "alternance course/marche" or programme[1] == "alternance effort/marche":
            difficultetemps1 = rd.randint(9,12)
            programmetemps.append(listealternance[difficultetemps1])
        else:
            difficultetemps1 = rd.randint(0,1)
            programmetemps.append(listepyramide[difficultetemps1])
        difficulte += difficultetemps1
        difficultetemps1 = rd.randint(0,5)
        programmetemps.append(listetempsfinseance[difficultetemps1])
        difficulte += difficultetemps1
    for i in range(len(programme)):
        entrainement.append(programme[i])
        entrainement.append(programmetemps[i])
    return entrainement