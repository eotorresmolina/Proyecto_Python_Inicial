'''
Proyecto [Python]

Proyecto Python Inicial

---------------------------
Autor: Torres Molina Emmnauel Oscar
Version: 1.1

Descripcion:
Programa creado como Proyecto del Curso de "Python Inicial" y Consiste
en los 'Casos Registrados en la República Argentina'.
'''

__author__ = "Torres Molina Emmanuel Oscar"
__email__ = "emmaotm@gmail.com"
__version__ = "1.1"


# Librerías Estándar del Sistema:
import os
from os import system

# Librerías de Terceros:
import csv
from datetime import date

# Librerías Propias:
import myfunctions as myf
from myfunctions import write_header_csv
import funciones_covid19 as fcovid19


# Desarrollo de las Funciones que Contiene el Programa:

def ingresar_usuario ( ):
    """
    Función que Realiza y Analiza el Logueo
    del Usuario y devuelve el estado si fue
    exitoso o no en base a 3 intentos como máximo.
    Return: estado del logueo (bool)
    """
    user = 'user1234'
    pwrd = 'jilguero124'
    max_cant_intentos = 3
    intentos = 0
    login = False

    while intentos < max_cant_intentos:     
        username = str(input('Usuario / Username: '))
        password = str(input('Clave / Password: '))
        intentos += 1   #  Ingremento 1 Intento
        intentos_restantes = max_cant_intentos - intentos
        if ((username == user) and (password == pwrd)):
            login = True
            intentos = 3
            system('cls')
        else:
            system('cls')
            if intentos_restantes == 0:
                print('Error al Ingresar el Nombre de Usuario o Contraseña.')
                print('Se Ha Quedado sin Intentos.\n\n')
            else:
                print('Error al Ingresar el Nombre de Usuario o Contraseña. Vuelva A Intentar:')
                print('Le quedan {} Intentos.\n\n'.format(intentos_restantes))
 
    return login


def menu_logueo (username):
    """
    Función que Muestra un Menú una vez
    que el usuario se ha logueado.
    """
    opcion_correcta = False
    opcion_logueo = None

    print('Usted se Ha Logueado Correctamente.')
    print('Bienvenido Usuario: {}'.format(username))
    print('Opciones que Puede Realizar:\n')

    while opcion_correcta == False:
        print('1 - Continuar con el Registro de Casos.')
        print('2 - Ver el Registro de Casos a la Fecha Actual.')
        print('3 - Desloguearse y Volver al Menú de Bienvenida.')

        try:
            opcion_logueo = int(input('Ingrese la Opción que Desee y luego Presione Enter: '))
            system('cls')
            if ((opcion_logueo != 1) and (opcion_logueo != 2) and (opcion_logueo != 3)):
                print('Error. Ha Ingresado una Opción Incorrecta.')
                print('Vuelva a Ingresar la Opción.\n')
            else:
                opcion_correcta = True
        except ValueError:
            system('cls')
            print('Error. Ha Ingresado una Opción No Válida. Puede que Haya Ingresado un Caracter.')
            print('Vuelva a Ingresar la Opción.\n')

    return opcion_logueo


def menu_campos ( ):
    """
    Función que Muestra en Pantalla
    el Menú Disponible con los Campos 
    que se deben Completar.
    """
    print('A Continuación se Detalla los Campos del Contagiado que Debe Completar:')
    print('1 - Género.')
    print('2 - Edad en Años.')
    print('3 - Provincia de Residencia.')
    print('4 - Fecha de Inicio de Síntomas.')
    print('5 - Indicación si Estuvo Internado.')
    print('6 - Fecha de Internación en Caso de Corresponder.')
    print('7 - Indicación si Estuvo en Cuidado Intensivo.')
    print('8 - Indicación si Requirió Asistencia Respiratoria Mecánica.')
    print('9 - Indicación de Fallecimiento.')
    print('10 - Fecha de Fallecimiento en Caso de Corresponder.')


def generar_campos (contagiados ):
    """
    Función que Carga los Campos del
    Registro de Casos en una lista.
    Recibe la lista contagiados.
    """
    contagiados.append(myf.cantidad_lineas( ) + 1)
    print('Completar con la Letra que Corresponda==> m:masculino, f:femenino, o:otros')
    contagiados.append(str(input('Ingrese Género: ')))
    contagiados.append(int(input('\nIngrese Edad en Años: ')))
    contagiados.append(str(input('\nIngrese Provincia de Residencia: ')))
    contagiados.append(str(input('\nFecha de Inicio de Síntomas. dd-mm-aaaa: ')))
    contagiados.append(str(input('\nIndicación de Internación. SI/NO: ')))
    print('\nFecha: dd-mm-aaaa. En Caso de No Haber Estado Internado Completar con: 00-00-0000')
    contagiados.append(str(input('Fecha de Internación: ')))
    contagiados.append(str(input('\nIndicación si Estuvo en Cuidado Intensivo. SI/NO: ')))
    contagiados.append(str(input('\nIndicación si Requirió Asistencia Respiratoria Mecánica. SI/NO: ')))
    contagiados.append(str(input('\nIndicación de Fallecimiento. SI/NO:  ')))
    print('\nFecha: dd-mm-aaaa. En Caso de No Haber Fallecido Completar con 00-00-0000')
    contagiados.append(str(input('Fecha de Fallecimiento: ')))
    contagiados.append(date.today())


def menu_invitado( ):
    """
    Función que Muestra en Pantalla el Menú
    para cuando Estamos en la opción Invitado.
    """
    print('Atención: Usted Ingresó como Invitado.')
    print('A Continuación se Detalla un Menú con las Opciones Disponibles:\n')
    print('1 - Obtener el Total de Contagiados, Internados y Fallecidos en la República Argentina.')
    print('2 - Provincia con Mayor y Menor Cantidad de Casos.')
    print('3 - Promedio de Edad de Personas Contagiadas, Internadas y Fallecidas.')
    print('4 - Cantidad de Personas que Necesitaron Asistencia Respiratoria Mecánica.')
    print('5 - Mes con Mayor y Menor Cantidad de Contagios y Fallecidos.')
    print('6 - Fecha de la Última Actualización del Registro.')
    print('7 - Ver Toda la Información Disponible y Generar un Informe.')
    print('8 - Salir y Volver al Menú de Bienvenida.')


def invitado ( ):
    flag = False
    while flag == False:
        menu_invitado( )
        try:
            opcion_menu = int(input('\nIngrese la Opción que Desee: '))
            if opcion_menu == 1:
                system('cls')
                cant_total_contagiados = fcovid19.total_contagiados( )
                cant_total_intern = fcovid19.total_internados()
                cant_total_fallec = fcovid19.total_fallecidos( ) 
                print('La Cantidad Total de Contagiados en la República Argentina es de: {}.'.format(cant_total_contagiados))
                print('La Cantidad Total de Internados en la República Argentina es de: {}.'.format(cant_total_intern))
                print('La Cantidad Total de Fallecidos en la República Argentina es de: {}.\n'.format(cant_total_fallec))                
            elif opcion_menu == 2:
                system('cls')
                provincia, cant_contagiados = fcovid19.obtener_max_provincia( )
                print('{} con un Total de {} Personas Contagiadas es la Provincia con Mayor Cantidad de Casos Registrados.'.format(provincia, cant_contagiados))
                provincia, cant_contagiados = fcovid19.obtener_min_provincia( )
                print('{} con un Total de {} Personas Contagiadas es la Provincia con Menor Cantidad de Casos Registrados.\n\n'.format(provincia, cant_contagiados))
                prov = str(input('Ingrese la Provincia que Desee para Obtener la Cantidad de Contagiados o "FIN" para Volver. Luego Presione la Tecla "Enter": '))
                print('\n\n')
                if prov.upper( ) != "FIN":
                    cant = fcovid19.contagios_provincia(prov)
                    print('\nLa Cantidad de Personas Contagiadas que Hay en la Provincia que Ingresó: "{}" es: {}\n\n'.format(prov, cant))
            elif opcion_menu == 3:
                system('cls')
                promedios = [0] * 3     # Genero una lista de ceros
                promedios[0], promedios[1], promedios[2] = fcovid19.promedio( )
                print('El Promedio de Edad de Personas Contagiadas es de {} años.'.format(promedios[0]))
                print('El Promedio de Edad de Personas Internadas es de {} años.'.format(promedios[1]))
                print('El Promedio de Edad de Personas Fallecidas es de {} años.\n\n'.format(promedios[2]))
            elif opcion_menu == 4:
                system('cls')
                cant_asist_resp = fcovid19.asistencia_respiratoria( )
                print('La Cantidad de Contagiados que Requirieron Asistencia Respiratoria Mecánica es: {}.\n\n'.format(cant_asist_resp))
            elif opcion_menu == 5:
                system('cls')
                mm, cant_contag = fcovid19.obtener_max_mes( )
                print('{} con un Total de {} Personas Contagiadas es el Mes con Mayor Cantidad de Casos Registrados.'.format(mm, cant_contag))
                mm, cant_contag = fcovid19.obtener_min_mes( )
                print('{} con un Total de {} Personas Contagiadas es el Mes con Menor Cantidad de Casos Registrados.\n\n'.format(mm, cant_contag))
            elif opcion_menu == 6:
                system('cls')
                fecha_u_actualizacion = fcovid19.fecha_uactualizacion( )
                print('Toda la Información hasta el Momento fue Cargada en la Fecha: {}\n\n'.format(fecha_u_actualizacion))
            elif opcion_menu == 7:
                system('cls')
                fcovid19.mostrar_info( )
                fcovid19.escribir_informe( )
                print('ATENCIÓN!!: Se Ha Generado y/o Actualizado el Siguiente Archivo: "informe_covid19.txt".\n\n')
            elif opcion_menu == 8:
                flag = True
                system('cls')
            else:
                print('\n\nERROR!! Ha Ingresado una Opción Inválida... Vuelva a Intentarlo:\n\n')

        except ValueError:
            print('\n\nError en el Valor Ingresado.')
            print('Puede que Haya Ingresado un Caracter.')
            print('Vuelva a Intentarlo:\n\n')


def menu_bienvenida ( ):
    """
    Función Principal del Programa.
    """
    # Inicialización de Variables:
    salir = False
    today = date.today()    # Obtengo la Fecha Actual
    file_name = 'registro_covid19.csv'
    contagiados = []

    # Detallo los nombres de las columnas ==> Header
    header = ['nro_caso', 'genero', 'edad', 'provincia_residencia', 'fecha_inicio_sintomas',
    'indicacion_internacion', 'fecha_internacion', 'cuidado_intensivo', 
    'asist_resp_mecanica', 'fallecido', 'fecha_fallecimiento', 'ultima_actualizacion']

    system('cls')   # Limpio la Pantalla de la Terminal

    while salir == False:
        print('Fecha: {}\n'.format(today))
        print('Bienvenido/a al Sistema de Registro del "COVID-19". Casos Registrados en la República Argentina:')
        print('1 - Loguearse.')
        print('2 - Ingresar como Invitado.')
        print('3 - Salir del Programa.\n')

        try:
            opcion = int(input('Ingrese la Opción que Desee y Luego Presione Enter: '))         
            if opcion == 1:     # Ingreso como Usuario.
                system('cls')
                login_ok = ingresar_usuario ( )     # Compruebo el Estado del Logueo.
                if login_ok == True:    # Si se Logueó Correctamente...
                    choice = None
                    while ((choice == None) or (choice == 'n')): 
                        #system('cls')
                        opcion_logueo = menu_logueo(username='user1234')
                        if opcion_logueo == 1: 
                            system('cls')
                            menu_campos( ) # Muestro los Campos que Posteriormente voy a Cargar.
                            print('\nA Continuación Escriba "y" para Continuar o "n" para Volver.')
                            print('Luego Presione Enter.')
                            choice = str(input('¿Desea Continuar? [y/n]: '))
                            if choice == 'y':
                                system('cls')
                                write_header_csv(file_name, header)
                                generar_campos(contagiados) # Genero los Campos y los cargo en la Lista Contagiados.
                                myf.escribir_registro(header, contagiados) # Escribo todo los campos como registro y fila en el archivo
                                choice = 'n'
                                system('cls')
                            elif choice == 'n':
                                system('cls')                       
                        elif opcion_logueo == 2:
                            system('cls')
                            myf.mostrar_registro_completo(file_name) # Muestro el Registro Completo.
                            choice = 'n'
                        elif opcion_logueo == 3:
                            system('cls')
                            choice = 'c'   
            elif opcion == 2:   # Ingreso Como Invitado.
                system('cls')
                invitado ( )
            elif opcion == 3: # Opción para Salir del Programa.
                salir = True
                system('cls')
                print('*************** Usted ha Salido del Programa. ***************')
                print('Muchas Gracias.\n\n')
            else:
                print('\n\nERROR!! Ha Ingresado una Opción Inválida... Vuelva a Intentarlo:\n')

        except ValueError:
            print('\n\nError en el Valor Ingresado.')
            print('Puede que Haya Ingresado un Caracter.')
            print('Vuelva a Intentarlo:\n')


if __name__ == "__main__":
    menu_bienvenida( )
