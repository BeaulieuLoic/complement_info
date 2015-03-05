#!/usr/bin/env python3

from dataBase import DataBase
from serialiser import Serializer

from modele.Installations import Installations
from modele.Activity import Activity


pathInstallationsJson = "../data/installations/installations.json"
pathActivityJson = "../data/activités/activités.json"

pathDataBase = "dataBase.db"

installationArray = []
activityArray = []

'''
creation of dataBase and table
'''
#DataBase.initDataBaseInstallation(pathDataBase)
DataBase.initDataBaseActivity(pathDataBase)

'''
unserialise json file
'''
#installationArray = Serializer.unserialise_installations_json(pathInstallationsJson)
activityArray = Serializer.unserialise_activity_json(pathActivityJson)

'''
insert Array into dataBase
'''
#Serializer.object_export_in_dataBase(installationArray,pathDataBase)
Serializer.object_export_in_dataBase(activityArray,pathDataBase)
