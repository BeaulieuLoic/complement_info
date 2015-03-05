#!/usr/bin/env python3

from dataBase import DataBase
#from modele.Installations import Installations
from serialiser import Serializer

pathDataBase = "dataBase.db"
installationArray = []

'''
creation of dataBase and table Installations
'''
DataBase.initDataBaseInstallation(pathDataBase)


'''
unserialise json file installations
'''
installationArray = Serializer.unserialise_installations_json("../data/installations/installations.json")


'''
insert Array installations into dataBase
'''
Serializer.installations_export_in_dataBase(installationArray,pathDataBase)