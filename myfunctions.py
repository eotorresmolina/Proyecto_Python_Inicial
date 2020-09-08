"""
Módulo que Permite Trabajar con archivo .csv
y contiene distintas funciones que permiten la
escritura/lectura del mismo.
"""

import os
import csv


def write_header_csv (nombre_archivo, header ):
    """
    Función que Escribe el header/encabezado de un archivo
    .csv en función si él mismo existe o no.
    Recibe: nombre_archivo, header
    """
    file_exists = os.path.isfile(nombre_archivo)    # Pregunto si existe el archivo
    if not file_exists:     # Si no Existe el Archivo==> Lo Creo y escribo el Header del mismo.
        with open(nombre_archivo, 'w', newline='') as csvfile:  # Abro el archivo para escritura
            writer = csv.DictWriter(csvfile, fieldnames=header)
            writer.writeheader()    # Escribo el Encabezado del Archivo
    else:
        pass


def leer_registro (nombre_archivo):
    """
    Función que Lee las líneas de un
    Archivo .csv y las almacena en una
    lista.
    Recibe: nombre_archivo
    Return: data ===> lista que contiene cada fila del .csv
    """
    with open(nombre_archivo, 'r') as csvfile:
        data = list(csv.DictReader(csvfile)) 
    return data


def cantidad_lineas( ):
    """
    Función que Lee un archivo .csv
    y obtiene la Cantidad de Líneas del
    Archivo.
    Return: cant_lineas
    """
    rows = leer_registro (nombre_archivo='registro_covid19.csv')
    return len(rows)


def escribir_registro(header, contagiados):
    """
    Función que Escribe en un archivo .csv
    una línea.
    Recibe: header, contagiados
    """
    file_name = 'registro_covid19.csv'
    fila = {}
    with open(file_name, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        
        for i in range(len(header)):
            fila[header[i]] = contagiados[i]

        writer.writerow(fila)


def mostrar_registro_completo(nombre_archivo):
    """
    Función que Muestra en Pantalla la lista con todas
    las líneas que contiene un archivo .csv
    Recibe: nombre_archivo
    """
    with open(nombre_archivo, 'r') as csvfile:
        data = list(csv.DictReader(csvfile))

        for row in range(len(data)):
            print('Fila {}: {}'.format(row+1, data[row]))

    print('\n\n')

