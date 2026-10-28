import numpy as np
import pandas as pd
# Jaquez Andres NC 0074
## datos matriz 4 x 3
datos_alumno = [
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]
]
# poner nombre a las columnas
# y almacenar la tabla  en la variable df dataframe
print("----Datos a partir de una matriz 4 x 3----") 
df = pd.DataFrame(datos_alumno,columns=['ci', 'marcas', 'paquete'])
print(df)

#Datos a partir del diccionario
print("----Datos a partir de un diccionario -----") 
alumno_diccionario = {
    "Nombre": ["Eliseo","Joel","Pedro","Nicole","Dilan","Jesse"],
    "Califa" : [60,90,100,80,70,80],
    "edad" : [64,15,16,16,18,14]
}

estudiante = pd.DataFrame(alumno_diccionario)
print(estudiante)

print("Jaquez Andres 0074")