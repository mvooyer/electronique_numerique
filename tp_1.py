import numpy as np
import csv


# Nombre d entrees (permet aussi definir le nombre d entree qui seront crees et remplies dans le fichier csv
N = 4
# genere un tableau avec N entrees et 2**N lignes
noms = []
entrees = np.zeros((2**N, N))

# genere les entrees du tableau
for i in range(N):
    noms.append('Entree' + str(i+1) + '\t')
    for j in range(2**N):
        if (j*2**(i+1)//(2**N))%2 == 0:
            entrees[j, i] = 0
        else:
            entrees[j, i] = 1


def table_and(entr):
    sortie = np.zeros(len(entr))
    for i in range(len(entr)):
        if sum(entr[i]) == len(entr[i]):
            sortie[i] = 1
    return sortie


def table_or(entr):
    sortie = np.zeros(len(entr))
    for i in range(len(entr)):
        if sum(entr[i]) >=1:
            sortie[i] = 1
    return sortie


def table_or_exclu(entr):
    sortie = np.zeros(len(entr))
    for i in range(len(entr)):
        x = 0
        for elem in entr[i]:
            x = x^int(elem)
        sortie[i] = x
    return sortie


# print(table_and(entrees))
# print(table_or(entrees))
# print(table_or_exclu(entrees))


# ouvre/cree un fichier csv et ecrit les entrees et sorties
file_name = 'sortie_' + str(N) + '_entrees.csv'
with open(file_name, 'w', newline='') as csvfile:
    noms.append('Sortie AND \t')
    noms.append('Sortie OR \t')
    noms.append('Sortie OR_EXCLU \t')
    filewriter = csv.DictWriter(csvfile, fieldnames=noms, delimiter=';')

    # cree l entete du tableau dans le csv
    filewriter.writeheader()

    # calcule les differentes sorties pour le ET / OU / OU EXCLUSIF
    sortie_1 = table_and(entrees)
    sortie_2 = table_or(entrees)
    sortie_3 = table_or_exclu(entrees)
    for i in range(len(entrees)):
        ligne = {}
        n = 0
        for e in entrees[i]:
            # ajoute les entrees dans la ligne
            ligne[noms[n]] = str(e)
            n += 1
        # ajoute les sorties dans le fichier
        ligne[noms[n]] = str(sortie_1[i])
        ligne[noms[n+1]] = str(sortie_2[i])
        ligne[noms[n+2]] = str(sortie_3[i])
        # ecrit la ligne dans le fichier CSV
        filewriter.writerow(ligne)
csvfile.close()

