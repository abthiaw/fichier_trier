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
            # elif line_list == "fname":
            #       pass        
            else:
                value = line_list[i+1]
                # print(value)
        # nom = ["fname", "wfname"]
        # if r is not None:
        #     line_list = line[r.span()[0]:].split()
        #     a = line_list
        #     print(a)
            

    return value

    # return value


if __name__ == "__main__":
    # liste_element_s = get_data_blocks(r"C:\Users\U17IL35\Documents\doc cft_v2\send.csv", step=119, start_mark="Transfer attributes")
    liste_element_r = get_data_blocks(r"C:\Users\U17IL35\Documents\doc cft_v2\recv.csv", step=103, start_mark="Transfer attributes")

    list_a_recup = ["FNAME", "FTYPE", "FCODE", "wfname"]
    for block in liste_element_r:
        for name in list_a_recup:
            print(fetch_value(name, block))