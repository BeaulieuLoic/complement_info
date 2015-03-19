import sqlite3

"""
this file contains differents method for create table in a SQLite3 file 
"""



def init_data_base_installation(path):

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

def init_data_base_activity(path):
    """
    Create table Activity in file path
    """

    conn = sqlite3.connect(path)
    c = conn.cursor()

    c.execute("DROP TABLE IF EXISTS Activity")
    c.execute('''CREATE TABLE Activity
                (
                    inseeNb TEXT, comLib TEXT, equipementId TEXT,
                    equNbEquIdentique TEXT, actCode TEXT,actLib TEXT,
                    equActivitePraticable TEXT, equActivitePratique TEXT,
                    equActiviteSalleSpe TEXT, actNivLib TEXT
                )'''
    )

    conn.commit()
    conn.close()

def init_data_base_equipment(path):
    """
    Create table Equipment in file path
    """

    conn = sqlite3.connect(path)
    c = conn.cursor()

    c.execute("DROP TABLE IF EXISTS Equipment")
    c.execute('''CREATE TABLE Equipment
        (
            comInsee text, comLib text,equipmentFile text,
            equAnneeService text, equNom text , equNomBatiment text
            )'''
    )
    conn.commit()
    conn.close()