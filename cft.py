# Import
import os
import sys
import paramiko
import re
import time
from datetime import date
import mysql.connector
from mysql.connector import errorcode
from datetime import datetime

# Définition des variables
port = 22
user = "mid"
password = "*1PdWc2/"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Tableau
log_f5 = []
date = datetime.now()
time_now = date.strftime("%d/%m/%Y %HH:%MM")
log_f5.append(time_now)
date_now = log_f5[0]

# Définition des fonctions
def def_sql_fetchall(commande):
    try:
        check_cft = {
            'user': 'root',
            'password': 'password',
            'database': 'check_cft'
        }
        check_cft = mysql.connector.connect(**check_cft)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Erreur avec votre compte ou mot de passe")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La database n\'existe pas")
        else:
            print(err)
    else:
        cursor = check_cft.cursor()
        cursor.execute(commande)
        result_fetchall = cursor.fetchall()
        check_cft.close()
        cursor.close()
        check_cft.close()
        return result_fetchall
def def_sql_truncate():
    try:
        check_cft = {
            'user': 'root',
            'password': 'password',
            'database': 'check_cft'
        }
        check_cft = mysql.connector.connect(**check_cft)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Erreur avec votre compte ou mot de passe")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La database n\'existe pas")
        else:
            print(err)
    else:
        cursor = check_cft.cursor()
        sql = ("""select concat('truncate table ', TABLE_NAME) from information_schema.tables where table_schema = 'check_cft' and table_name not in ('list_hostname');""")
        cursor.execute(sql)
        result = cursor.fetchall()
        sql_foreign_key = ("""set foreign_key_checks = 0;""")
        cursor.execute(sql_foreign_key)
        for row in result:
            sql_truncate = (row[0])
            cursor.execute(sql_truncate)
        sql_foreign_key = ("""set foreign_key_checks = 1;""")
        cursor.execute(sql_foreign_key)
                                                                                                                                                                                                                                                                                                                             
def def_sql_multiple(commande):
    try:
        check_cft = {
            'user': 'root',
            'password': 'password',
            'database': 'check_cft'
        }
        check_cft = mysql.connector.connect(**check_cft)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Erreur avec votre compte ou mot de passe")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La database n\'existe pas")
        else:
            print(err)
    else:
        cursor = check_cft.cursor()
        cursor.execute(*commande)
        check_cft.commit()
        cursor.close()
        check_cft.close()
def def_sql(commande):
    try:
        check_cft = {
            'user': 'root',
            'password': 'password',
            'database': 'check_cft'
        }
        check_cft = mysql.connector.connect(**check_cft)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Erreur avec votre compte ou mot de passe")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La database n\'existe pas")
        else:
            print(err)
    else:
        cursor = check_cft.cursor()
        if commande == 'erreur':
            if sujet == 'connexion':
                message_error = "Erreur de connexion ssh"
                insert_error = ("""insert into error (date, hostname, action, message) values (%s, %s, %s, %s)""", (date_now, hostname, sujet, message_error,))
                cursor.execute(*insert_error)
                check_cft.commit()
                check_cft.close()
                cursor.close()
                check_cft.close()
            else:
                message_error = ("Perte de la connexion ssh")
                insert_error = ("""insert into error (date, hostname, action, message) values (%s, %s, %s, %s)""", (date_now, hostname, sujet, message_error,))
                cursor.execute(*insert_error)
                check_cft.commit()
                check_cft.close()
                cursor.close()
                check_cft.close()
                print()
                print("Un probleme a ete recontre lors de la recuperation de l'information:", sujet)
                print("Le script va etre re execute")
                print()
                script_name = sys.argv[0]
                #os.system("python " + script_name)
def ssh_result(commande):
    stdin,stdout,stderr = ssh.exec_command(commande)
    result = str(stdout.read().strip())
    try:
        m = re.search("b'(.+?)'", result)
        m = re.search("b'(.+?)'", result)
        result_fin = m.group(1)
        return result_fin
    except:
        server = serveur.strip()
        result_fin = server
        return result_fin    
    lines = stdout.readlines()
def ssh_result_multiple(commande):
    stdin,stdout,stderr = ssh.exec_command(commande)
    if sujet == '2_cft':
        lines = stdout.readlines()
        liste_ligne = []
        liste_mot = []
        resultant_liste_mot = []
        for line in lines:
            liste_ligne.append(line)            
        nbre_ligne = len(liste_ligne)
        nbre_ligne -= 1
        i = 0
        while i <= nbre_ligne:
            line = liste_ligne[i].split()
            idf_type = re.sub(",","",line[0])
            test_idf = re.sub(",","",line[2])
            nbre_test_idf = len(test_idf)
            if nbre_test_idf > 1:
                idf_name = re.sub(",","",line[2])
            else:
                idf_name = re.sub(",","",line[3])
            liste_mot.append(idf_name)
            insert_cft_cfg = ("""INSERT INTO cfg (hostname, hostname_fqdn, idf_type, idf_name) VALUES (%s, %s, %s, %s)""", (hostname, hostname_fqdn, idf_type, idf_name,))
            sql = (def_sql_multiple(insert_cft_cfg))
            i += 1
        for element in liste_mot:
            if element not in resultant_liste_mot:
                resultant_liste_mot.append(element)
        nbre_resultant_liste_mot = len(resultant_liste_mot)
        nbre_resultant_liste_mot -= 1
        x =0
        if hostname == 'lp002cft8500':
            while x <= nbre_resultant_liste_mot:
                mot = resultant_liste_mot[x].split()
                idf_name_2 = re.sub(",","",mot[0])
                insert_cft_idf = ("""INSERT INTO idf_prd (idf_name) VALUES (%s)""", (idf_name_2,))
                sql = (def_sql_multiple(insert_cft_idf))
                x += 1
        if hostname == 'lr002cft8500':
            while x <= nbre_resultant_liste_mot:
                mot = resultant_liste_mot[x].split()
                idf_name_2 = re.sub(",","",mot[0])
                insert_cft_idf = ("""INSERT INTO idf_rct (idf_name) VALUES (%s)""", (idf_name_2,))
                sql = (def_sql_multiple(insert_cft_idf))
                x += 1
        liste_ligne.clear()
        resultant_liste_mot.clear()

    else:
        lines = stdout.readlines()
        for line_ssh in lines:
            print(line_ssh.strip())
        i = 0
def_sql_truncate()
print("*******************")
print("")
print("Début du check cft")
print("")
print("*******************")
recup_server = ("""select * from list_hostname""")
sql_serveur = (def_sql_fetchall(recup_server))
nbre_sql_serveur = len(sql_serveur)
nbre_sql_serveur -= 1
nl = 0
while nl <= nbre_sql_serveur:
    serveur = sql_serveur[nl]
    serveur = serveur[0].strip()
    nl += 1
    if serveur != "":
        sujet = 'connexion'
        try:
            ssh.connect(serveur.strip(),port,user,password,timeout = 10)
            sujet = ''
        except Exception:
            hostname = serveur.strip()
            sql = (def_sql("erreur"))
            sujet = ''
        else:
            try:
                # hostname de la VM
                sujet = '0_hostname'
                hostname = (ssh_result("hostname"))
                hostname_fqdn = (ssh_result("hostname --fqdn"))
                if hostname_fqdn == 'localhost':
                    hostname_fqdn = (ssh_result("hostname"))
                sujet = ''
                #print("**********")
                # IDF
                #print("2_idf")
                sujet = '2_cft'
                id_name = ' id '
                nbre_ram = (ssh_result_multiple("cat /tools/list/cft/user/conf/config_cft.idf|grep ' id '"))
                sujet = ''
                #print("**********")
                ssh.close()
            except Exception:
                sql = (def_sql("erreur"))
                print("Ko")
print("*******************")
print("")
print("Fin du check system")
print("")
print("*******************")
