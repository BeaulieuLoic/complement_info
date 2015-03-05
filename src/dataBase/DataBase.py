import sqlite3

"""
this file contains differents method for create table in a SQLite3 file 
"""



def initDataBaseInstallation(path):

    """
    Create table installations in file path
    """

    conn = sqlite3.connect(path)
    c = conn.cursor()

    c.execute("DROP TABLE IF EXISTS Installations")
    c.execute('''CREATE TABLE Installations
                (
                    numInstall TEXT, nameTown TEXT,
                    INSEE TEXT,zipCode TEXT,placeCalled TEXT,
                    numStreet TEXT,nameStreet TEXT,
                    latitude REAL,longitude REAL,noAccessArrang TEXT,
                    accesReducMobi TEXT,accessSensHand TEXT,
                    sizeInM2 TEXT,caretakerAndHousing TEXT,
                    multiTown TEXT,numberPlaceParking TEXT,
                    numberPlaceParkingdHand TEXT,installParticular TEXT,
                    servSubway TEXT,servBus TEXT,servTram TEXT,
                    servTrain TEXT,servBoat TEXT,servOther TEXT,
                    numberEquip TEXT,installUpd TEXT
                )''')

    conn.commit()
    conn.close()