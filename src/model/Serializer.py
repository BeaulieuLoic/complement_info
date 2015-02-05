#!/usr/bin/env python3

import json
from Installations import Installations as In

class Serializer(object):
    """
    this class contains differents method of import/export for differents format 
    """

    def __init__(self):
        pass

    def unserialise_installations_json(self, pathName):
        """
        function for unserialise json file in object Installations
        return list of object
        """
        toReturn = []
        with open(pathName) as json_file:
            json_data = json.load(json_file)

            for installation in json_data["data"]:
                installation[""]                
                toReturn.append(Installations(installation["insNom"],installation["InsNumeroInstall"],installation["ComLib"],installation["ComInsee"],installation["InsCodePostal"],installation["InsLieuDit"],installation["InsNoVoie"],installation["InsLibelleVoie"],installation[""],installation[""],installation[""],installation[""],installation[""],installation[""],installation[""],installation[""],installation[""],installation[""],installation[""],installation[""],installation[""],installation[""],installation[""],installation[""],installation[""],installation[""],installation[""],installation[""],installation[""]))


            #print(json_data["data"][0])

if __name__ == "__main__":
    tmp = Serialisation()
    tmp.unSerialise_Installations_json("installations.json")
