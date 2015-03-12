#!/usr/bin/env python3


from dataBase import DataBase
from serialiser import Serializer


path_installations_json = "../data/installations/installations.json"
path_activity_json = "../data/activités/activités.json"
path_equipment_json = "../data/equipements/equipements.json"

path_data_base = "dataBase.db"

installation_Array = []
activity_Array = []
equipmentArray = []


'''
creation of dataBase and table
'''
print("creation of data base and tables ...")
DataBase.init_data_base_installation(path_data_base)
DataBase.init_data_base_activity(path_data_base)
DataBase.init_data_base_equipment(path_data_base)

'''
unserialise json file
'''
print("unserialise json files ...")
installationArray = Serializer.unserialise_installations_json(path_installations_json)
activityArray = Serializer.unserialise_activity_json(path_activity_json)
equipmentArray = Serializer.unserialise_equipment_json(path_equipment_json)

'''
insert Array into dataBase
'''
print("insert json objects into data base ...")
Serializer.object_export_in_dataBase(installationArray,path_data_base)
Serializer.object_export_in_dataBase(activityArray,path_data_base)
Serializer.object_export_in_dataBase(equipmentArray,path_data_base)
