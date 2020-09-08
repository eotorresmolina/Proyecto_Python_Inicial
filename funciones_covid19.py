"""
Módulo que Permite calcular diversos paramétros, tales
como cantidad de casos según la fecha, provincia con mayor
cantidad, pico de casos en el mes, etc.
Sirve únicamente para un registro de la Pandemia producida
por el Covid-19.
Archivo: registro_covid19.csv
"""

import myfunctions as myf
import math as mth
from datetime import date



def total_contagiados ( ):
    """
    Función que Devuelve la Cantidad Total
    de Casos Positivos en la República Argentina.
    """
    return myf.cantidad_lineas()


def contagios_provincia (provincia ):
    """
    Función que Calcula la Cantidad de Contagios
    que Hubo en una Determinada Provincia de la 
    República Argentina:
    Recibe como parametro un str: provincia
    Retorna la Cantidad de Contagios en esa Provincia.
    """

    caso_positivo = 0
    data = myf.leer_registro(nombre_archivo='registro_covid19.csv')
    for row in range(len(data)):
        if data[row].get('provincia_residencia') == provincia:
            caso_positivo += 1

    return caso_positivo


def obtener_provincia( ):
    """
    Función que Calcula la Provincia con
    Mayor Cantidad de Casos.
    Retorna la Provincia y la Cantidad de Casos.
    """
    # Genero una lista con Todas las Provincias de Argentina.
    provincias = ['Buenos Aires', 'Catamarca', 'Chaco', 'Chubut', 'Córdoba', 'Corrientes', 
    'Entre Ríos', 'Formosa', 'Jujuy' ,'La Pampa', 'La Rioja', 'Mendoza', 'Misiones' ,'Neuquén', 
    'Río Negro', 'Salta', 'San Juan', 'San Luis', 'Santa Cruz', 'Santa Fe', 'Santiago del Estero', 
    'Tierra del Fuego, Antártida e Isla del Atlántico Sur', 'Tucumán']
    provincias.sort() 
    casos = [0] * len(provincias)  # Genero una lista de ceros del mismo tamaño que 'provincias'.
    for i in range(len(provincias)):
        casos[i] = contagios_provincia(provincias[i])
    
    max_contagiados = max(casos) # Calculo el Máximo.
    index = casos.index(max_contagiados) # Obtengo el índice del Máximo
    provincia = provincias[index]

    return provincia, max_contagiados


def promedio ( ):
    """
    Función que Calcula el Promedio de
    Contagios, Personas Internadas y
    Personas Fallecidas.
    Retorna promedio de contagios, internación, fallecimiento.
    """
    suma_edades_contagiados = 0
    suma_edades_internados = 0
    suma_edades_fallecidos = 0

    personas_internadas = 0
    personas_fallecidas = 0

    data = myf.leer_registro(nombre_archivo='registro_covid19.csv')
    for row in range(len(data)):
        suma_edades_contagiados += int(data[row].get('edad'))

        if ((data[row].get('indicacion_internacion') == 'SI') or ((data[row].get('indicacion_internacion') == 'si'))):
            personas_internadas += 1
            suma_edades_internados += int(data[row].get('edad'))

        if ((data[row].get('fallecido') == 'SI') or ((data[row].get('fallecido') == 'si'))):
            personas_fallecidas += 1
            suma_edades_fallecidos += int(data[row].get('edad'))

    if ((personas_internadas != 0) or (personas_fallecidas != 0)):
        promedio_internados = mth.ceil(suma_edades_internados / personas_internadas)
        promedio_fallecidos = mth.ceil(suma_edades_fallecidos / personas_fallecidas)
    else:
        promedio_internados = 0
        promedio_fallecidos = 0

    promedio_contagiados = mth.ceil(suma_edades_contagiados / len(data)) # Redondeo el Promedio.

    return promedio_contagiados, promedio_internados, promedio_fallecidos


def casos_fecha(dia, mes, anio):
    """
    Función que Calcula la Cantidad
    de Contagios en una determinada
    fecha.
    Recibe como parámetros el día, el
    mes y el año.
    Retorna la Cant. de Contagiados.
    """
    contagios_positivos = 0
    data = myf.leer_registro(nombre_archivo='registro_covid19.csv')
    for row in range(len(data)):
        date = data[row].get('fecha_inicio_sintomas').split('-')
        dd, mm, aa = int(date[0]), int(date[1]), int(date[2])
        if aa == anio:
            if mm == mes:
                if dd == dia: 
                    contagios_positivos += 1
        
    return contagios_positivos


def obtener_anio (anio):
    """
    Función que Calcula la Cantidad de
    Casos de un determinado Año.
    Recibe el año
    Retorna la Cant. de Contagiados.
    """
    contagios_positivos = 0
    data = myf.leer_registro(nombre_archivo='registro_covid19.csv')
    for row in range(len(data)):
        date = data[row].get('fecha_inicio_sintomas').split('-')
        aa = int(date[2])
        if aa == anio:
            contagios_positivos += 1

    return contagios_positivos


def contagios_mes(mes, anio):
    """
    Función que Calcula la Cant. de
    Contagios de un determinado mes y 
    Año.
    Recibe: mes, anio
    Retorna: cant_contagios
    """
    contagios_positivos = 0
    data = myf.leer_registro(nombre_archivo='registro_covid19.csv')
    for row in range(len(data)):
        date = data[row].get('fecha_inicio_sintomas').split('-')
        dd, mm, aa = int(date[0]), int(date[1]), int(date[2])
        if aa == anio:
            if mm == mes:
                contagios_positivos += 1
        
    return contagios_positivos

        
def obtener_mes ( ):
    """
    Función que Calcula el Mes con más cantidad de
    Casos Registrados.
    Return: mes, max_contagios
    """
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio',
    'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    meses_numeros = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    contagios = [0] * len(meses) 

    for i in range(len(meses_numeros)):
        contagios[i] = contagios_mes(int(meses_numeros[i]), anio=2020)

    max_contagios = max(contagios)
    index = contagios.index(max_contagios)
    mes = meses[index]

    return mes, max_contagios
        

def fecha_uactualizacion( ):
    """
    Función que Calcula la Fecha de la
    Última Actualización que se Hizo para
    la Carga de Registro o Casos.
    Return: fecha de última actualización.
    """
    data = myf.leer_registro(nombre_archivo='registro_covid19.csv')
    fecha = str(data[-1].get('ultima_actualizacion')).split('-')
    dd, mm, aa = fecha[2], fecha[1], fecha[0]
    ult_actualiz = str(dd) + '-' + str(mm) + '-' + str(aa)
    
    return ult_actualiz


def asistencia_respiratoria ( ):
    """
    Función que Calcula la Cantidad
    de Contagios que Requirieron Asistencia
    Respiratoria Mecánica.
    Return: cantidad
    """
    cantidad = 0
    data = myf.leer_registro(nombre_archivo='registro_covid19.csv')
    for row in range(len(data)):
        if ((data[row].get('asist_resp_mecanica') == 'SI') or (data[row].get('asist_resp_mecanica') == 'si')):
            cantidad += 1

    return cantidad