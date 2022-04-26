# Créer un script d'extration de block de fichier

####################
# connaitre le debut du block et la fin

# enregistrer dans une variables
# rechercher chaque champs qu'on veut enregister
# Enregistrer les champs dans la base de données
import sys
from pprint import pprint


def read_file(filename: str):
    import re

    #file_1, file_2, file_3 = open(args[1]), open(args[3]), open(args[3])
    f = open(filename)
    object_read = f.readlines()

    debut, fin, data_block = None, None, None
    for idx, line in enumerate(object_read):
        # debut de l'objet
        r = re.search("Transfer attributes", line)
        if r is not None:
            debut = idx - 1
            fin = idx + 103
            #print(object_read[idx - 1].strip())
            data_block = object_read[debut:fin]
            pprint(data_block)


if __name__ == "__main__":
    read_file("/Users/gabinmberikongo/code/dev/test/recv.csv")
