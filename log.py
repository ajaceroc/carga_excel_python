# -*- coding: utf-8 -*-

import os
import time
import Leer_Archivo
import Creacion_Carpetas

#def error_datos():


def cambiar_nombre_archivo_fecha():
    fecha =time.strftime("%d/%m/%y")+" "+time.strftime("%H:%M:%S")
    fecha=list(fecha)
    for x in range(0,len(fecha)):
        if (fecha[x]=='/'):
            fecha[x]='_'
        if (fecha[x]==':'):
            fecha[x]='-'
    fecha =" ".join(fecha)
    return fecha

cargar='C:\\FCBFIRE\\CargarTickets\\'
log='C:\\FCBFIRE\\LogTickets\\'
no_cargados='C:\\FCBFIRE\\NoCarTickets\\'
cargados='C:\\FCBFIRE\\CargadosTickets\\'

cargarI='C:\\FCBFIRE\\CargarIVR\\'
logI='C:\\FCBFIRE\\LogIVR\\'
no_cargadosI='C:\\FCBFIRE\\NoCarIVR\\'
cargadosI='C:\\FCBFIRE\\CargadosIVR\\'

def verificacion(archivo):
    errores=[]
    if (Leer_Archivo.existencia_archivo(cargar+archivo)==True):
        fecha=cambiar_nombre_archivo_fecha()
        if(len(Leer_Archivo.verificacion_columnas_base_data(cargar+archivo))==0):
            Leer_Archivo.lectura_base_data(cargar+archivo)
            Leer_Archivo.mover_archivo(cargar+archivo,cargados)
            Leer_Archivo.cambiar_nombre_archivo(cargados+archivo,cargados+archivo.replace('.xlsx',' ')+fecha+'.xlsx')
        else:
            if(Leer_Archivo.verificacion_columnas_base_data(cargar+archivo)[0]==0):
                errores.append('El archivo de excel no tiene la hoja Base Tickets ')
            else:
                errores.append('Errores en las columnas:\n')
                errores=errores+Leer_Archivo.verificacion_columnas_base_data(cargar+archivo)
            Leer_Archivo.mover_archivo(cargar+archivo,no_cargados)
            Leer_Archivo.cambiar_nombre_archivo(no_cargados+archivo,no_cargados+archivo+fecha+'.xlsx')
    else:
        print ("No existe el archivo")
    if(len(errores)==0):
        errores.append('Archivo exitoso')
    errores=" ".join(errores)
    crear_log(errores,fecha,archivo)

def crear_log(escribir,fecha,archivo):
    file = open(log+"\\log "+archivo+" "+fecha+".txt", "w")
    file.write(escribir + os.linesep)
    file.close()

def ls():
    Creacion_Carpetas.crear_carpetas()
    lstFiles = []
    lstDir = os.walk(cargar)
    for root, dirs, files in lstDir:
        for fichero in files:
            (nombreFichero, extension) = os.path.splitext(fichero)
            if(extension == ".xlsx" or extension == ".xls" ):
                lstFiles.append(nombreFichero+extension)
    print(lstFiles)
    print ("longitud de la lista Tickets= ", len(lstFiles))
    if(len(lstFiles)!=0):
        for x in range(0,len(lstFiles)):
            verificacion(lstFiles[x])
            time.sleep(1)
