#!/usr/bin/env python3
import sqlite3

class Installations(object):
    """
    docstring for Installations.
    this class Installations represent file installations
    url:
    http://data.paysdelaloire.fr/donnees/detail/equipements-sportifs-espaces-et-sites-de-pratiques-en-pays-de-la-loire-fiches-installations/
    """
    def __init__(self, numInstall, nameTown, INSEE, zipCode
        , placeCalled, numStreet, nameStreet, longitude, latitude
        , noAccessArrang, accesReducMobi, accessSensHand, sizeInM2
        , caretakerAndHousing, multiTown, numberPlaceParking
        , numberPlaceParkingdHand, installParticular, servSubway, servBus
        , servTram, servTrain, servBoat, servOther, numberEquip
        , installUpd):
        
        """
        Constructor, with 26 parameters:
        #- nameInstall: String 
        - numInstall: String
        - nameTown: String
        - INSEE: String
        - zipCode: String
        - placeCalled: String
        - numStreet: String
        - nameStreet: String
        #- location : GEO_LOCATION
        - longitude: float
        - latitude: float
        - noAccessArrang: String
        - accesReducMobi: String
        - accessSensHand: String
        - sizeInM2: String
        - caretakerAndHousing: String
        - multiTown: String
        - numberPlaceParking: String
        - numberPlaceParkingdHand: String
        - installParticular: String
        - servSubway: String
        - servBus: String
        - servTram: String
        - servTrain: String
        - servBoat: String
        - servOther: String
        - numberEquip: String
        #- numberCardEquip: String
        - installUpd: String

        for parameter and atribute documentation, see this url:
        http://data.paysdelaloire.fr/donnees/detail/equipements-sportifs-espaces-et-sites-de-pratiques-en-pays-de-la-loire-fiches-installations/?visualization=3

        """
        #self.nameInstall = nameInstall
        self.numInstall = numInstall
        self.nameTown = nameTown
        self.INSEE = INSEE
        self.zipCode = zipCode
        self.placeCalled = placeCalled
        self.numStreet = numStreet
        self.nameStreet = nameStreet
        #self.location = location
        self.longitude = longitude
        self.latitude = latitude
        self.noAccessArrang = noAccessArrang
        self.accesReducMobi = accesReducMobi
        self.accessSensHand = accessSensHand
        self.sizeInM2 = sizeInM2
        self.caretakerAndHousing = caretakerAndHousing
        self.multiTown = multiTown
        self.numberPlaceParking = numberPlaceParking
        self.numberPlaceParkingdHand = numberPlaceParkingdHand
        self.installParticular = installParticular
        self.servSubway = servSubway
        self.servBus = servBus
        self.servTram = servTram
        self.servTrain = servTrain
        self.servBoat = servBoat
        self.servOther = servOther
        self.numberEquip = numberEquip
        #self.numberCardEquip = numberCardEquip
        self.installUpd = installUpd

        """
        function for display Installations object
        """
    def __str__(self):
        return ("["+str(self.numInstall)+","+str(self.nameTown)+","+str(self.INSEE)+
        ","+str(self.zipCode)+","+str(self.placeCalled)+","+str(self.numStreet)+
        ","+str(self.nameStreet)+","+str(self.longitude)+","+str(self.latitude)+
        ","+str(self.noAccessArrang)+","+str(self.accesReducMobi)+","+
        str(self.accessSensHand)+","+str(self.sizeInM2)+","+
        str(self.caretakerAndHousing)+
        ","+str(self.multiTown)+","+str(self.numberPlaceParking)+","+
        str(self.numberPlaceParkingdHand)+","+str(self.installParticular)+
        ","+str(self.servSubway)+","+str(self.servBus)+
        ","+str(self.servTram)+","+str(self.servTrain)+","+
        str(self.servBoat)+","+str(self.servOther)+","+
        str(self.numberEquip)+","+str(self.installUpd)+
        "]")

        """
        export Installations object in data file SQLite3
        filePath: path of SQLite3's file
        """
    def export_to_data_base(self, conn):
        c = conn.cursor()

        value = "\"{0}\",\"{1}\",\"{2}\",\"{3}\",\"{4}\",\"{5}\",\"{6}\",{7},{8},\"{9}\",\"{10}\",\"{11}\",\"{12}\",\"{13}\",\"{14}\",\"{15}\",\"{16}\",\"{17}\",\"{18}\",\"{19}\",\"{20}\",\"{21}\",\"{22}\",\"{23}\",\"{24}\",\"{25}\"".format(
                self.numInstall, self.nameTown , self.INSEE , self.zipCode,
                self.placeCalled , self.numStreet , self.nameStreet,
                self.latitude , self.longitude , self.noAccessArrang,
                self.accesReducMobi , self.accessSensHand , self.sizeInM2,
                self.caretakerAndHousing , self.multiTown,
                self.numberPlaceParking , self.numberPlaceParkingdHand,
                self.installParticular , self.servSubway , self.servBus,
                self.servTram , self.servTrain , self.servBoat,
                self.servOther , self.numberEquip , self.installUpd)

        c.execute("INSERT INTO Installations VALUES ("+value+")")


    """
    get and set of all atribute
    """

    def getNameInstall(self, nameInstall):
        return self.nameInstall

    def setNameInstall(self, nameInstall):
        self.nameInstall = nameInstall


    def getNumInstall(self):
        return self.numInstall

    def setNumInstall(self, numInstall):
        self.numInstall = numInstall


    def getNameTown(self):
        return self.nameTown

    def setNameTown(self, nameTown):
        self.nameTown = nameTown


    def getINSEE(self):
        return self.INSEE

    def setINSEECode(self, INSEE):
        self.INSEE = INSEE


    def getZipCode(self):
        return self.zipCode

    def setZipCode(self, zipCode):
        self.zipCode = zipCode


    def getPlaceCalled(self):
        return self.placeCalled

    def setPlaceCalled(self, placeCalled):
        self.placeCalled = placeCalled


    def getNumStreet(self):
        return self.numStreet

    def setStreetNum(self, numStreet):
        self.numStreet = numStreet


    def getNameStreet(self):
        return self.nameStreet

    def setNameStreet(self, nameStreet):
        self.nameStreet = nameStreet


    def getLongitude(self):
        return self.longitude

    def setLongitude(self, longitude):
        self.longitude = logitude


    def getLatitude(self):
        return self.latitude

    def setLatitude(self, latitude):
        self.latitude = latitude


    def getNoAccessArrang(self):
        return self.noAccessArrang

    def setNoAccessArrang(self, noAccessArrang):
        self.noAccessArrang = noAccessArrang


    def getAccesReducMobi(self):
        return self.accesReducMobi

    def setAccesReducMobi(self, accesReducMobi):
        self.accesReducMobi = accesReducMobi


    def getAccessSensHand(self):
        return self.accessSensHand

    def setAccessSensHand(self, accessSensHand):
        self.accessSensHand = accessSensHand


    def getSizeInM2(self):
        return self.sizeInM2

    def setSizeInM2(self, sizeInM2):
        self.sizeInM2 = sizeInM2


    def getCareTakerAndHousing(self):
        return self.caretakerAndHousing

    def setCareTakerAndHousing(self, caretakerAndHousing):
        self.careTakerAndHousing = caretakerAndHousing


    def getMultiTown(self):
        return self.multiTown

    def setMultiTown(self, multiTown):
        self.multiTown = multiTown


    def getNumberPlaceParking(self):
        return self.numberPlaceParking

    def setNumberPlaceParking(self, numberPlaceParking):
        self.numberPlaceParking = numberPlaceParking


    def getNumberPlaceParkingdHand(self):
        return self.numberPlaceParkingdHand

    def setNumberPlaceParkingdHand(self, numberPlaceParkingdHand):
        self.numberPlaceParkingdHand = numberPlaceParkingdHand


    def getInstallParticular(self):
        return self.installParticular

    def setInstallParticular(self, installParticular):
        self.installParticular = installParticular


    def getSubwServc(self):
        return self.subwServc

    def setservSubway(self, servSubway):
        self.servSubway = servSubway


    def getServBus(self):
        return self.servBus

    def setServBus(self, servBus):
        self.servBus = servBus


    def getServTram(self):
        return self.servTram

    def setServTram(self, servTram):
        self.servTram = servTram


    def getServTrain(self):
        return self.servTrain

    def setServTrain(self, servTrain):
        self.servTrain = servTrain


    def getBoatServic(self):
        return self.servBoat

    def setServBoat(self, servBoat):
        self.servBoat = servBoat


    def getServOther(self):
        return self.servOther

    def setServOther(self, servOther):
        self.servOther = servOther


    def getNumberEquip(self):
        return self.numberEquip

    def setNumberEquip(self, numberEquip):
        self.numberEquip = numberEquip


    def getNumberCardEquip(self):
        return self.numberCardEquip

    def setNumberCardEquip(self, numberCardEquip):
        self.numberCardEquip = numberCardEquip


    def getInstallUpd(self):
        return self.installUpd
        
    def setInstallUpd(self, installUpd):
        self.installUpd = installUpd