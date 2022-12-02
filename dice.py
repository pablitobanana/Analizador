import re
from csv import reader
from nltk.tokenize import word_tokenize #exportar la funcion para tokenizar
from nltk.corpus import stopwords #libreria de las stopwords
from collections import Counter #libreria para contar las palabras y cuantas veces se repiten
from collections import OrderedDict # libreria para ordenar las palabras
import palabras_vacias as pv

lista_d = ''

with open('datasets\dice_com-job_us_sample.csv', encoding='utf-8') as archivo_en_memoria:
    csv = reader(archivo_en_memoria)
    lista_d = list(csv)
    lista_d.pop(0)

#  print(len(lista_d))
lista_dice=''
for titulo in lista_d:
    lista_dice += titulo[6] + ", "

#  print(lista_dice,"\n \n")
x = 0
n_lista_dice = ""
while x< len( lista_dice ):
    if lista_dice[x] == "(":
        if lista_dice[x-1] != " ":
            n_lista_dice += " ,"
    elif lista_dice[x] == "-" or lista_dice[x] == "/":
        if lista_dice[x-1] == " " or lista_dice[x+1] == " ":
            n_lista_dice += ","
        else:
            n_lista_dice += lista_dice[x]
    elif lista_dice[x] == ")":
        n_lista_dice += ""
    else:
        n_lista_dice += lista_dice[x]
    x+=1

#  print(n_lista_dice)


lista_dice = []
lista_dice.append(n_lista_dice)
lista_dice = lista_dice[0].split(",")
#  print(lista_dice)


x = 0
while x < len(lista_dice):
    if lista_dice[x][:1] == ' ':
        lista_dice[x] = lista_dice[x][1:]

    if lista_dice[x][-1:] == ' ':
        lista_dice[x] = lista_dice[x][:-1]

    x+= 1

while("" in lista_dice):
    lista_dice.remove("")
#  print(lista_dice)




palabras_vacias = set(stopwords.words('english')) #llamamos las stopwords en español

lista_final_d = [] #hacemos una lista donde vamos a guardar las palabras con valor

for palabra in lista_dice: # recorremos cada palabra de los tokens
    if palabra not in  palabras_vacias: # si la palabra NO ES una stopword se guardara en la lista
       lista_final_d.append(palabra)

y = 0
for cadena in lista_final_d:
    if "devops" in cadena.lower():
        y+=1
        print(cadena)

print(y)
#  n_lista_dice = ''
#  for lista_dice[x] in lista_dice:
#      cambiar = '-/)'
#      eliminar = '('






