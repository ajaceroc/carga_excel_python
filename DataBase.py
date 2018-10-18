# -*- coding: utf-8 -*-
# -*- coding: 850-*-
import MySQLdb

try:
    db = MySQLdb.connect(host="127.0.0.1",
                     user="root",
                     db="dbFire")
    db.set_character_set('utf8')
except:
    print("Servidor no encontrado")
else:
    print ("Conexión satisfactoria")

def insertar_registros(registro):
    cur = db.cursor()
    cur.execute('SET NAMES utf8;')
    cur.execute('SET CHARACTER SET utf8;')
    cur.execute('SET character_set_connection=utf8;')
    valores = "'" +"','".join(unicode(v) for v in registro)+"'"
    SQL = "INSERT INTO `dbFire`.`dbAcumulacion` (`crmId`,`Pincode`,`Fin`,`sabor`) VALUES (" + valores + ")"
    try:
        cur.execute(SQL)

    except:
        print ("Error al insertar datos")
    else:
        db.commit()
        cur.close()

def ejecutarSPCarga():
    cur = db.cursor()
    cur.execute('SET NAMES utf8;')
    cur.execute('SET CHARACTER SET utf8;')
    cur.execute('SET character_set_connection=utf8;')
    sp_cargaDatos = "CALL SP_CARGA_BASE;"
    cur.execute(sp_cargaDatos)
    cur.close()

def truncate_base_tickets_stage():
    cur.execute('SET NAMES utf8;')
    cur.execute('SET CHARACTER SET utf8;')
    cur.execute('SET character_set_connection=utf8;')
    sp_truncateDatos = "CALL SP_truncate_base_tickets_stage;"
    cur.execute(sp_truncateDatos)
    cur.close()

