#!/usr/bin/env python3

import json
import sqlite3
from modele.Installations import Installations

"""
this file contains differents method of import/export for differents format 
"""

def unserialise_installations_json(pathName):
    """
    function for unserialise json file in object installs
    return list of object
    """
    toReturn = []
    with open(pathName) as json_file:
        json_data = json.load(json_file)

        for install in json_data["data"]:                
            toReturn.append(Installations(
                install["InsNumeroInstall"],install["ComLib"],
                install["ComInsee"],install["InsCodePostal"],
                install["InsLieuDit"],install["InsNoVoie"],
                install["InsLibelleVoie"],install["Longitude"],
                install["Latitude"],install["InsAccessibiliteAucun"],
                install["InsAccessibiliteHandiMoteur"],
                install["InsAccessibiliteHandiSens"],
                install["InsEmpriseFonciere"],install["InsGardiennee"],
                install["InsMultiCommune"],install["InsNbPlaceParking"],
                install["InsNbPlaceParkingHandi"],install["InsPartLibelle"],
                install["InsTransportMetro"],install["InsTransportBus"],
                install["InsTransportTram"],install["InsTransportTrain"],
                install["InsTransportBateau"],install["InsTransportAutre"],
                install["Nb_Equipements"],
                install["InsDateMaj"]))
    return toReturn

def installations_export_in_dataBase(installationsArray, pathFile):
    """
    unserialise a json's file and export in dataBase SQLite
    installationsArray: array of Installations's object
    pathFile: path of SQLite's file
    """
    i = 0
    conn = sqlite3.connect(pathFile)

    for install in installationsArray:

        install.exportToDataBase(conn)
        i = i + 1
        print(i)