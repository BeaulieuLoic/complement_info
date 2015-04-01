#!/usr/bin/env python3

import json
import sqlite3
from modele.Installations import Installations
from modele.Activity import Activity
from modele.Equipment import Equipment

"""
this file contains differents method of import/export for differents format 
"""

def unserialise_installations_json(pathName):
    """
    function for unserialise json file in object installation
    return list of Installation object


    """
    to_return = []

    try:
        with open(pathName) as json_file:
            json_data = json.load(json_file)

            for install in json_data["data"]:
                to_return.append(Installations(
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
    except FileNotFoundError:
        print("bad path of activity json file")
    except KeyError:
        print("bad json file, see documentation of activity for see how is construct this object")
        
    return to_return

def unserialise_activity_json(pathName):
    """
    function for unserialise json file in object installs
    return list of Activity object.
    """
    to_return = []

    try:
        with open(pathName) as json_file:
            json_data = json.load(json_file)

            for activity in json_data["data"]:
                to_return.append(
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
    except FileNotFoundError:
        print("bad path of activity json file")
    except KeyError:
        print("bad json file, see documentation of activity for see how is construct this object")

    return to_return

def unserialise_equipment_json(pathName):
    """
    function for unserialise json file in object equipment
    return list of Equipement object
    """
    to_return = []
    try:
        with open(pathName) as json_file:
            json_data = json.load(json_file)

            for equipment in json_data["data"]:
                to_return.append(
                    Equipment(
                        equipment["ComInsee"],equipment["ComLib"],
                        equipment["EquipementFiche"],equipment["EquAnneeService"],
                        equipment["EquNom"],equipment["EquNomBatiment"]
                    )
                )
    except FileNotFoundError:
        print("bad path of equipment json file")
    except KeyError:
        print("bad json file, see documentation of equipment for see how is construct this object")



    return to_return



def object_export_in_dataBase(object_array, pathFile):
    """
    unserialise a json's file and export in dataBase SQLite
    object_array: array of object
    pathFile: path of SQLite's file
    object in array need to implement exportToDataBase fucntion.
    """
    conn = sqlite3.connect(pathFile)

    for obj in object_array:
        try:
            obj.export_to_data_base(conn)
        except AttributeError:
            print("object need to implement the function: \'export_to_data_base\'")

    conn.commit()
    conn.close()