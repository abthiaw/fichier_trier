# Créer un script d'extration de block de fichier

####################
# connaitre le debut du block et la fin

# enregistrer dans une variables
# rechercher chaque champs qu'on veut enregister
# Enregistrer les champs dans la base de données
import sys
from pprint import pprint
import re


def get_data_blocks(filename: str, step: int, start_mark: str) -> list:

    #file_1, file_2, file_3 = open(args[1]), open(args[3]), open(args[3])
    f = open(filename)
    object_read = f.readlines()

    debut, fin, list_data_blocks = None, None, []
    for idx, line in enumerate(object_read):
        # debut de l'objet
        r = re.search(start_mark, line)
        if r is not None:
            debut = idx - 1
            fin = idx + step
            #print(object_read[idx - 1].strip())
            list_data_blocks.append(object_read[debut:fin])
    return list_data_blocks


def fetch_value(field_name: str, block: str):
    """
    Cette fonction recupere la valeur des données basé sur le nom en entré(field_name)
    dans un bloc de données (block)
    
    
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('sample.jpeg')
imgplot = plt.imshow(img)
plt.show()
    @params :
        field_name : le nom du champ a récuperer
        block : le bloc des données
    """
    value = None
    for line in block:
        r = re.search(field_name, line)
        if r is not None:
            line_list = line[r.span()[0]:].split()
            i = line_list.index("=")
            if len(line_list) <= 2:
                value = ""
            else:
                value = line_list[i+1]
    return value

    # return value


if __name__ == "__main__":
    liste_element = get_data_blocks(
        "/Users/gabinmberikongo/code/dev/test/recv.csv", step=103, start_mark="Transfer attributes")

    list_a_recup = ["FTYPE", "FCODE"]
    for block in liste_element:
        for name in list_a_recup:
            print(fetch_value(name, block))
            
            
            
Traceback (most recent call last):
  File "D:\Applis\automatisation\mail\bpc\send_mail_pj_bpc_ref_app.py", line 61, in <module>
    server.sendmail(sender_mail, toaddrs, msg.as_string())
  File "D:\Program Files\Python38\lib\smtplib.py", line 868, in sendmail
    msg = _fix_eols(msg).encode('ascii')
UnicodeEncodeError: 'ascii' codec can't encode characters in position 572-573: ordinal not in range(128)            
