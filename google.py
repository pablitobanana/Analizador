from csv import reader
from nltk.corpus import stopwords #libreria de las stopwords
from collections import Counter #libreria para contar las palabras y cuantas veces se repiten
from collections import OrderedDict # libreria para ordenar las palabras
import palabras_vacias as pv


lista_g = ''

with open('datasets\job_skills.csv', encoding='utf-8') as archivo_en_memoria:
    csv = reader(archivo_en_memoria)
    lista_g = list(csv)
    lista_g.pop(0)

print("Cantidad de registros",len(lista_g))
lista_google=''
for titulo in lista_g:
    lista_google += titulo[1] + ", "

#  print(lista_google + "\n \n")

n_lista_google = ''
for caracter in lista_google:
    cambiar = '('
    eliminar = '-)]アエンジニア、ソフトウェビデオ'
    if caracter in cambiar:
        n_lista_google += ","
    elif caracter in eliminar:
        continue
    else:
        n_lista_google += caracter


#  print(n_lista_google)

lista_google = []
lista_google.append(n_lista_google)
lista_google = lista_google[0].split(",")

x = 0
while x < len(lista_google):
    if lista_google[x][0] == ' ':
        lista_google[x] = lista_google[x][1:]

    if lista_google[x][-1:] == ' ':
        lista_google[x] = lista_google[x][:-1]

    x+= 1

while("" in lista_google):
    lista_google.remove("")

#  print(lista_google)


palabras_vacias = set(stopwords.words('english')) #llamamos las stopwords en español
palabras_vacias.update(pv.pv_google)



lista_final_g = [] #hacemos una lista donde vamos a guardar las palabras con valor

for palabra in lista_google: # recorremos cada palabra de los tokens
    if palabra not in palabras_vacias: # si la palabra NO ES una stopword se guardara en la lista
       lista_final_g.append(palabra)

#  print(lista_final_g)

opcion = ''
while opcion !="fin":
    opcion = input("Ingrese palabra clave a buscar(para salir escriba fin): ").lower()
    if opcion !="fin":
        y = 0
        for cadena in lista_final_g:
            if opcion in cadena.lower():
                y+=1
                print(cadena)
    else: continue

    print("\n\nconcidencias encontradas: ",y,"\n")

contador_g = Counter(lista_final_g) # Lista de palabras con cuantas veces se repiten cada una
las_mas_repetidas_g = OrderedDict(contador_g.most_common(340)) # ordena las 5 palabras que mas se repiten
opcion = input("Quiere ver las palabras más repetidas (si,no): ").lower()
if opcion == "si":
    print("\n",las_mas_repetidas_g)
