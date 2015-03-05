#!/usr/bin/env python3

import json
import sqlite3
from modele.Installations import Installations
from modele.Activity import Activity

"""
this file contains differents method of import/export for differents format 
"""

def unserialise_installations_json(pathName):
    """
    function for unserialise json file in object installation
    return list of Installation object
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

def unserialise_activity_json(pathName):
    """
    function for unserialise json file in object installs
    return list of Activity object
    """
    toReturn = []
    with open(pathName) as json_file:
        json_data = json.load(json_file)

        for activity in json_data["data"]:
            toReturn.append(
                Activity(
                    activity["ComInsee"],activity["ComLib"],
                    activity["EquipementId"],activity["EquNbEquIdentique"],
                    activity["ActCode"],
                    activity["ActLib"],activity["EquActivitePraticable"],
                    activity["EquActivitePratique"],
                    activity["EquActiviteSalleSpe"],
                    activity["ActNivLib"]
                )
            )

    return toReturn


def object_export_in_dataBase(objectArray, pathFile):
    """
    unserialise a json's file and export in dataBase SQLite
    objectArray: array of object
    pathFile: path of SQLite's file
    object in array need to implement exportToDataBase fucntion
    """
    i = 0
    conn = sqlite3.connect(pathFile)

    for obj in objectArray:
        obj.exportToDataBase(conn)
        i = i + 1
        #print(i)
    conn.close()