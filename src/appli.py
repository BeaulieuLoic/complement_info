#!/usr/bin/env python3

from dataBase import DataBase
from serialiser import Serializer
import argparse
import os
import sys
'''
set default value for test appli
'''
path_installations_json = "../data/installations/installations.json"
path_activity_json = "../data/activités/activités.json"
path_equipment_json = "../data/equipements/equipements.json"

path_data_base = "dataBase.db"

installation_Array = []
activity_Array = []
equipmentArray = []

def set_path_data_base(path):
	path_data_base = path
	if args.init:
		print("creation of data base and tables ...")
		DataBase.init_data_base_installation(path_data_base)
		DataBase.init_data_base_activity(path_data_base)
		DataBase.init_data_base_equipment(path_data_base)
	else:
		if not os.path.isfile(path):
			print("file don't exists, use --init for create data base")
			sys.exit()

def set_path_json_installation():
	path_installations_json=input('Enter the path of json file installations:')

def set_path_json_activity():
	path_activity_json=input('Enter the path of json file activity:')

def set_path_json_equipment():
	path_equipment_json=input('Enter the path of json file equipment:')


if __name__ == "__main__":

	parser = argparse.ArgumentParser(description='insert object from json a files in data base.')

	'''
	args for set the path of data base 
	'''
	parser.add_argument('-i','--init', action='store_true', help='initialisation of data base')
	parser.add_argument('path_data_base', metavar='path_data_base', type=str, help='set the data base path (if it isn\'t exists use --init )')

	'''
	args for set the path of json file for installations, activity, equipments
	'''
	parser.add_argument('-insJson','--installationsJson', action='store_true', help='set optional json file ')
	parser.add_argument('-actJson','--activityJson', action='store_true', help='set optional json file ')
	parser.add_argument('-equJson','--equipmentsJson', action='store_true', help='set optional json file ')


	args = parser.parse_args()


	set_path_data_base(args.path_data_base)


	if args.installationsJson:
		set_path_json_installation()
		print("unserialise json installations and import to data base ...")
		installationArray = Serializer.unserialise_installations_json(path_installations_json)
		Serializer.object_export_in_dataBase(installationArray,path_data_base)

	if args.activityJson:
		set_path_json_activity()
		print("unserialise json activity and import to data base ...")
		activityArray = Serializer.unserialise_activity_json(path_activity_json)
		Serializer.object_export_in_dataBase(activityArray,path_data_base)

	if args.equipmentsJson:
		set_path_json_equipment()
		print("unserialise json equipments and import to data base ...")
		equipmentArray = Serializer.unserialise_equipment_json(path_equipment_json)
		Serializer.object_export_in_dataBase(equipmentArray,path_data_base)

	"""
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
	print("insert array objects into data base ...")
	Serializer.object_export_in_dataBase(installationArray,path_data_base)
	Serializer.object_export_in_dataBase(activityArray,path_data_base)
	Serializer.object_export_in_dataBase(equipmentArray,path_data_base)
	"""
