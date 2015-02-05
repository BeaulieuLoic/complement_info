#!/usr/bin/env python3


class Installations(object):
    """
    docstring for Installations
    this class Installations represent file installations
    """
    def __init__(self, nameInstall, numInstall, nameTown, INSEE, zipCode
        , placeCalled, numStreet, nameStreet, location, longitude, latitude
        , noAccesArrang, accesReducMobi, accesHandSensor, sizeInM2
        , caretakerAndHousing, multiTown, numberPlaceParking
        , numberPlaceParkingdHand, installParticular, servSubway, servBus
        , servTram, servTrain, servBoat, servOther, numberEquip
        , numberCardEquip, installUpd):
        
        """
        Constructor, with 29 parameters:
        - nameInstall: String 
        - numInstall: String
        - nameTown: String
        - INSEE: String
        - zipCode: String
        - placeCalled: String
        - numStreet: String
        - nameStreet: String
        - location: GEO_LOCATION
        - longitude: float
        - latitude: float
        - noAccesArrang: String
        - accesReducMobi: String
        - accesHandSensor: String
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
        - numberCardEquip: String
        - installUpd: String

        for parameter and atribute documentation, see this url:
        http://data.paysdelaloire.fr/donnees/detail/equipements-sportifs-espaces-et-sites-de-pratiques-en-pays-de-la-loire-fiches-installations/?visualization=3

        """
        self.nameInstall = nameInstall
        self.numInstall = numInstall
        self.nameTown = nameTown
        self.INSEE = INSEE
        self.zipCode = zipCode
        self.placeCalled = placeCalled
        self.numStreet = numStreet
        self.nameStreet = nameStreet
        self.location = location
        self.longitude = longitude
        self.latitude = latitude
        self.noAccesArrang = noAccesArrang
        self.accesReducMobi = accesReducMobi
        self.accesHandSensor = accesHandSensor
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
        self.numberCardEquip = numberCardEquip
        self.installUpd = installUpd





        