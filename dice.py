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

print(len(lista_d))
lista_dice=''
for titulo in lista_d:
    lista_dice += titulo[6] + ", "

print(lista_dice)








