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
import datetime
from datetime import date



def total_contagiados ( ):
    """
    Función que Devuelve la Cantidad Total
    de Casos Positivos en la República Argentina.
    """
    return myf.cantidad_lineas()


def total_internados ( ):
    """    
    Función que Devuelve la Cantidad Total
    de Contagiados Internados en la República Argentina.
    """
    cant_total_int = 0
    data = myf.leer_registro(nombre_archivo='registro_covid19.csv')
    for row in range(len(data)):
        if data[row].get('indicacion_internacion').upper( ) == 'SI':
            cant_total_int += 1

    return cant_total_int


def total_fallecidos ( ):
    """    
    Función que Devuelve la Cantidad Total
    de Contagiados Fallecidos en la República Argentina.
    """
    cant_total_fallec = 0
    data = myf.leer_registro(nombre_archivo='registro_covid19.csv')
    for row in range(len(data)):
        if data[row].get('fallecido').upper( ) == 'SI':
            cant_total_fallec += 1

    return cant_total_fallec


def contagios_provincia (provincia ):
    """
    Función que Calcula la Cantidad de Contagios
    que Hubo en una Determinada Provincia de la 
    República Argentina:
    Recibe como parametro un str: provincia
    Retorna la Cantidad de Contagios en esa Provincia.
    """

    caso_positivo = 0
    provincia = provincia.upper( )
    data = myf.leer_registro(nombre_archivo='registro_covid19.csv')
    for row in range(len(data)):
        if (data[row].get('provincia_residencia').upper( ) in provincia):
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
        provincias[i] = str(provincias[i]).upper( )
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
        suma_edades_contagiados += int(data[row].get('edad')) # Realizo la Suma de Todas las Edades.

        if (data[row].get('indicacion_internacion').upper( ) == 'SI'):
            personas_internadas += 1
            suma_edades_internados += int(data[row].get('edad'))

        if (data[row].get('fallecido').upper( ) == 'SI'):
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


def promedio_dsf ( ):
    """
    Función que Calcula el Promedio de Días
    que Hay Entre que Una Persona Tuvo los Síntomas
    y Falleció.
    """
    promedio = 0
    dias = 0
    cant_fallecidos = 0
    fecha_sintomas = 0
    fecha_fallecimiento = 0
    data = myf.leer_registro(nombre_archivo='registro_covid19.csv')
    for row in range(len(data)):
        if data[row].get('fallecido').upper( ) == 'SI':
            cant_fallecidos +=1
            fecha_sintomas = data[row].get('fecha_inicio_sintomas').split('-')
            dds, mms, aas = int(fecha_sintomas[0]), int(fecha_sintomas[1]), int(fecha_sintomas[2])
            fecha_fallecimiento = data[row].get('fecha_fallecimiento').split('-')
            ddf, mmf, aaf = int(fecha_fallecimiento[0]), int(fecha_fallecimiento[1]), int(fecha_fallecimiento[2])
            if mms != mmf:
                if ((mms == 1) or (mms == 3) or (mms == 5) or (mms == 7) or (mms == 8) or (mms == 10) or (mms == 12)):
                    dias += (31 - dds) + ddf

                elif ((mms == 4) or (mms == 6) or (mms == 9) or (mms == 11)):
                    dias += (30 - dds) + ddf

                elif mms == 2:
                    dias += (28 - dds) + ddf


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

        
def obtener_max_mes ( ):
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


def obtener_min_mes ( ):
    """
    Función que Calcula el Mes con menos cantidad de
    Casos Registrados.
    Return: mes, max_contagios
    """
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio',
    'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    meses_numeros = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    contagios = [0] * len(meses) 

    for i in range(len(meses_numeros)):
        contagios[i] = contagios_mes(int(meses_numeros[i]), anio=2020)

    min_contagios = min(contagios)
    index = contagios.index(min_contagios)
    mes = meses[index]

    return mes, min_contagios
        

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
        if (data[row].get('asist_resp_mecanica').upper( ) == 'SI'):
            cantidad += 1

    return cantidad


def mostrar_info ( ):
    """
    Función que Muestra en Pantalla
    Toda la Información Disponible
    acerca del Covid-19
    """
    today = date.today( )
    print('Fecha Actual: {}\n'.format(today))
    cant_total_contagiados = myf.cantidad_lineas( )
    cant_total_intern = total_internados()
    cant_total_fallec = total_fallecidos( )
    print('La Cantidad Total de Contagiados en la República Argentina es de: {}.'.format(cant_total_contagiados))
    print('La Cantidad Total de Internados en la República Argentina es de: {}.'.format(cant_total_intern))
    print('La Cantidad Total de Fallecidos en la República Argentina es de: {}.\n\n'.format(cant_total_fallec))
    provincia_max, cant = obtener_provincia( )
    print('{} con un Total de {} Personas Contagiadas es la Provincia con Mayor Cantidad de Casos Registrados.'.format(provincia_max, cant))
    promedios = [0] * 3
    promedios[0], promedios[1], promedios[2] = promedio( )
    print('El Promedio de Edad de Personas Contagiadas es de {} años.'.format(promedios[0]))
    print('El Promedio de Edad de Personas Internadas es de {} años.'.format(promedios[1]))
    print('El Promedio de Edad de Personas Fallecidas es de {} años.'.format(promedios[2]))
    cant_asist_resp = asistencia_respiratoria( )
    print('La Cantidad de Contagiados que Requirieron Asistencia Respiratoria Mecánica es: {}.'.format(cant_asist_resp))
    mm, cant_contag = obtener_max_mes( )
    print('{} con un Total de {} Personas Contagiadas es el Mes con Mayor Cantidad de Casos Registrados.'.format(mm, cant_contag))
    mm, cant_contag = obtener_min_mes( )
    print('{} con un Total de {} Personas Contagiadas es el Mes con Menor Cantidad de Casos Registrados.\n\n'.format(mm, cant_contag))
    fecha_u_actualizacion = fecha_uactualizacion( )
    print('Toda la Información hasta el Momento fue Cargada en la Fecha: {}\n\n'.format(fecha_u_actualizacion))


def escribir_informe ( ):
    """
    Función que Crea un Informe con Toda la Información
    Disponible acerca del COVID-19. La Información
    se Almacena en "informe_covid19.txt"
    """
    nombre_archivo = 'informe_covid19.txt'
    now = datetime.datetime.now( ) # Obtengo la Fecha Actual
    with open(nombre_archivo, 'w') as txt:
        row = 'Fecha y Hora del Informe: ' + str(now) + '\n\n'
        txt.writelines(row)

        cant_total_contagiados = myf.cantidad_lineas( )
        row = 'La Cantidad Total de Contagiados en la República Argentina es de: ' + str(cant_total_contagiados) + '\n'
        txt.writelines(row)

        cant_total_intern = total_internados()
        row = 'La Cantidad Total de Internados en la República Argentina es de: ' + str(cant_total_intern) + '\n'
        txt.writelines(row)

        cant_total_fallec = total_fallecidos( )
        row = 'La Cantidad Total de Fallecidos en la República Argentina es de: ' + str(cant_total_fallec) + '\n'
        txt.writelines(row)
        
        provincia_max, cant = obtener_provincia( )
        row = provincia_max + ' con un Total de ' + str(cant) + ' Personas Contagiadas es la Provincia con Mayor Cantidad de Casos Registrados.\n'
        txt.writelines(row)
    
        promedios = [0] * 3
        promedios[0], promedios[1], promedios[2] = promedio( )
        txt.writelines('El Promedio de Edad de Personas Contagiadas es de ' + str(promedios[0]) + ' años.\n')
        txt.writelines('El Promedio de Edad de Personas Internadas es de ' + str(promedios[1]) + ' años.\n')
        txt.writelines('El Promedio de Edad de Personas Fallecidas es de ' + str(promedios[2]) + ' años.\n')
    
        cant_asist_resp = asistencia_respiratoria( )
        row ='La Cantidad de Contagiados que Requirieron Asistencia Respiratoria Mecánica es de ' + str(cant_asist_resp) + '.\n'
        txt.writelines(row)

        mm, cant_contag = obtener_max_mes( )
        row = mm + ' con un Total de ' + str(cant_contag) + ' Personas Contagiadas es el Mes con Mayor Cantidad de Casos Registrados.\n'
        txt.writelines(row)

        mm, cant_contag = obtener_min_mes( )
        row = mm + ' con un Total de ' + str(cant_contag) + ' Personas Contagiadas es el Mes con Menor Cantidad de Casos Registrados.\n'
        txt.writelines(row)

        fecha_u_actualizacion = fecha_uactualizacion( )
        row = 'Última Actualización del Registro ==> Toda la Información hasta el Momento fue Cargada en la Fecha: ' + fecha_u_actualizacion + '.\n'
        txt.writelines(row)      