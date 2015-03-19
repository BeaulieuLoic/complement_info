#!/usr/bin/env python3
class Equipment :
	''' class representing an equipment
	has too many characteristics, 6 have been selected
	all of thems are Strings.
	'''
	def __init__(self,comInsee,comLib,equipmentFile,equAnneeService,equNom,equNomBatiment):
		self.comInsee = comInsee
		self.comLib = comLib
		self.equipmentFile = equipmentFile
		self.equAnneeService = equAnneeService
		self.equNom = equNom
		self.equNomBatiment = equNomBatiment

	def __str__(self):
		return "EQUIPMENT [nom : "+self.equNom+", comLib : " + self.comLib + " , num INSEE : " + self.comInsee+" ]"

	def export_to_data_base(self,conn):
		c = conn.cursor()

		value ="\"{0}\",\"{1}\",\"{2}\",\"{3}\",\"{4}\",\"{5}\"".format(
		self.comInsee,self.comLib,self.equipmentFile,
		self.equAnneeService,self.equNom.replace('"',"'"),self.equNomBatiment)

		c.execute("INSERT INTO equipment VALUES ("+value+")")