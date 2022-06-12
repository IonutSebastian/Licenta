import json
from random import random
import mysql.connector
from time import sleep

server = 'localhost'
database = 'AllBooksInOnePlace'
username = 'root'
port = '3306'

mydb = mysql.connector.connect(host=server, user=username, port=port, database=database)

mycursor = mydb.cursor()



def databaseLibris():
    with open("./data/libris.json", 'r+', encoding="utf-8") as file:
        json_file = json.load(file)

    for key, value in json_file.items():
        mycursor.execute("""SELECT id FROM resource WHERE id_library=4 AND identifier = %s """, (key, ))
        exista = mycursor.fetchone()
        # varificam daca cartea exista in baza de date
        if exista is None:
            # adaugam titlul carii si biblioteca in tabelul carte
            mycursor.execute("""INSERT INTO resource(id_library, identifier) VALUES (4, %s)""", (key, ))
            mydb.commit()

            mycursor.execute("""SELECT id FROM resource WHERE id_library=4 AND identifier = %s """, (key, ))
            id = mycursor.fetchone()
            for i in value:
                # adaugam fiecare field in tabelul fields
                mycursor.execute("""INSERT INTO field (id_resource, value, field) VALUES (%s, %s, %s)""",
                                 (id[0], i['fld']['val'], i['fld']['fld_name']))
                mydb.commit()
        else:
            for i in value:
                # actualizam fiecare field in tabelul fields
                mycursor.execute("""UPDATE field SET value = %s WHERE id_resource = %s AND field = %s""",
                                 (i['fld']['val'], exista[0], i['fld']['fld_name']))
                mydb.commit()


def databasetinread(id:int,dict:dict):
    sleep(random()*5)
    if(len(dict['1'])>0):
        identif = dict['1'][1]['fld']['val']
        mycursor.execute("INSERT INTO  resource (id_library,identifier) VALUES (%s,%s)",(id,identif))
        mydb.commit()
        sleep(0.2)
        mycursor.execute("SELECT id FROM resource WHERE id_library=%s AND identifier=%s",(id,identif))
        sleep(0.2)
        id_resource = mycursor.fetchall()
        if len(id_resource)>=0 :
            id_resource=id_resource[0][0]
            for j in range(len(dict['1'])):
                nume = str(dict['1'][j]['fld']['fld_name'])
                valore = str(dict['1'][j]['fld']['val'])
                index_1 = dict['1'][j]['fld']['ind_1']
                index_2 = dict['1'][j]['fld']['ind_2']

                if (valore == ""):
                    valore = " "
                if (index_1 == ""):
                    comment="INSERT INTO field (field.id_resource,field.value ,field.field) VALUES ({}, {}, {})".format(id_resource,valore,nume)
                elif (index_2 == ""):
                    comment="INSERT INTO field (field.id_resource,field.value ,field.field, field.index_1) VALUES ({},{},{},{})".format(id_resource,valore,nume,index_1)
                else:
                    comment="INSERT INTO field (field.id_resource,field.value ,field.index_1,field.index_2,field.field) VALUES ({},{},{},{},{})".format(id_resource,valore,index_1,index_2,nume)
                try:
                    mycursor.execute(comment)
                except:
                    print(dict)

                mydb.commit()

                mycursor.execute("SELECT id FROM field WHERE field.id_resource= %s and field.value = %s and field.field= %s;",(id_resource,valore,nume))
                id_field = mycursor.fetchall()
                if(id_field):
                    id_field=id_field[0][0]
                    for k in range(len(dict['1'][j]['fld']['subflds'])):
                        nume = dict['1'][j]['fld']['subflds'][k]['subfld']['name']
                        val = dict['1'][j]['fld']['subflds'][k]['subfld']['val']
                        mycursor.execute(
                            "INSERT INTO subfield (subfield.id_field ,subfield.name , subfield.value) VALUES ( %s , %s, %s);",(id_field,nume,val))
                        mydb.commit()


def databaseelefant(id: str, dict: dict):
    sleep(random() * 5)
    mycursor.execute(f"INSERT INTO  resource (id_library,identifier) VALUES (3,{id})")
    mydb.commit()
    mycursor.execute(f"SELECT id FROM resource WHERE id_library = 3 AND identifier='{id}'")
    id_resource = mycursor.fetchall()
    id_resource = id_resource[0][0]
    for j in range(len(dict['1'])):
        nume = dict['1'][j]['fld']['fld_name']
        valore = dict['1'][j]['fld']['val']
        comment = f"INSERT INTO field (field.id_resource,field.value ,field.field) VALUES ({id_resource},'{valore}','{nume}')"
        mycursor.execute(comment)
        mydb.commit()

    # jsonfile[i][str(i+1)][index]['fld']['fld_name']



