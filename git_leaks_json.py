from git import Repo
import re
import signal
import sys
import time
import json


def handler_signal(signal,frame):

    # Salida controlada del programa en caso de pulsar 
    # control C

    print("\n\n [!] out .......\ n")

    sys.exit(1)

signal.signal(signal.SIGINT,handler_signal)



def extract(url):

    # Se extrae la información del repositorio clonado y se
    # genera una lista con los commits realizados en dicho repo

    repo = Repo(url)
    lista = list(repo.iter_commits())   # Devuelve una lista de objetos
    return lista


def transform(lista, palabras):

    # Se buscan las palabras clave en cada uno de los commits
    # En caso de que se encuentren se almacena en un diccionario
    # el código del commit y el mensaje

    leaks = {}

    for commit in lista:
        for buscar in KEY_WORDS:
            if re.search(buscar, commit.message, re.I):
                leaks[commit.hexsha] = commit.message

    time.sleep(1)
    return leaks


def load(leaks):

    # Se crea el fichero json y se almacena en él todos los leaks
    # Posteriormente también se muestran los leaks encontrados por
    # pantalla

    with open('leak.json', 'w') as json_file:
        json.dump(leaks, json_file, indent=4)

    for key in leaks:
        print(f'Commit: {key}\n Mensaje: {leaks[key]}')

    time.sleep(1)


if __name__ == "__main__":

    REPO_DIR = './skale/skale-manager'
    KEY_WORDS = ['credentials', 'password','key']
    lista = extract(REPO_DIR)
    leaks = transform(lista, KEY_WORDS)
    load(leaks)
