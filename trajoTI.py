import re
from csv import reader
from nltk.tokenize import word_tokenize #exportar la funcion para tokenizar
from nltk.corpus import stopwords #libreria de las stopwords
from collections import Counter #libreria para contar las palabras y cuantas veces se repiten
from collections import OrderedDict # libreria para ordenar las palabras
import palabras_vacias as pv

lista = ''
with open('datasets\Best_Jobs.csv', encoding='utf-8') as archivo_en_memoria:
    csv = reader(archivo_en_memoria)
    lista = list(csv)
    lista.pop(0)


print("Cantidad de registros",len(lista))
nuevalista = ['']

for casilla in lista:
    nuevalista[0] += casilla[5] + ", "

nuevalista = nuevalista[0].split(",")

x = 0
while x < len(nuevalista):
    nuevalista[x] = re.sub(r'[^\w\s]', '', nuevalista[x]) #dejamos solo palabras por medio de exprecion regular
    cadena = nuevalista[x]
    nuevalista[x] = cadena[1:]
    x+=1

while("" in nuevalista):
    nuevalista.remove("")
#  #  print(texto_segunda_limpiesa)


#  print(nuevalista)
#  tokens_de_mi_texto = word_tokenize(texto_segunda_limpiesa) # separa cada palabra

palabras_vacias = set(stopwords.words('english')) #llamamos las stopwords en español
palabras_vacias.update(pv.pv_bestj)

lista_final = [] #hacemos una lista donde vamos a guardar las palabras con valor

for palabra in nuevalista: # recorremos cada palabra de los tokens
    if palabra not in  palabras_vacias: # si la palabra NO ES una stopword se guardara en la lista
       lista_final.append(palabra)

#  print(lista_final)

opcion = ''
while opcion !="fin":
    opcion = input("Ingrese palabra clave a buscar(para salir escriba fin): ").lower()
    if opcion !="fin":
        y = 0
        for cadena in lista_final:
            if opcion in cadena.lower():
                y+=1
                print(cadena)
    else: continue

    print("\n\nconcidencias encontradas: ",y,"\n")


contador = Counter(lista_final) # Lista de palabras con cuantas veces se repiten cada una

las_mas_repetidas = OrderedDict(contador.most_common(100)) # ordena las 5 palabras que mas se repiten
opcion = input("Quiere ver las palabras más repetidas (si,no): ").lower()
if opcion == "si":
    print("\n",las_mas_repetidas)
