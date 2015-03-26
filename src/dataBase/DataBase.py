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


def get_name_of_column(path,table):
    """
    return the name of all column in a table html
    """
    conn = sqlite3.connect(path)
    c = conn.cursor()
    toReturn = "<tr>"
    for row in c.execute("PRAGMA table_info('"+table+"')").fetchall():
        tmp = 0
        for x in row:
            if (x.__class__.__name__ == "str") and (tmp%2 == 1):
                toReturn = toReturn +"<td>"+str(x)+"</td>"
            tmp  = tmp + 1
    toReturn = toReturn +"</tr>"
    conn.close()
    return toReturn

def get_name_of_column_in_array(path, table):
    """
    return the name of all column in a array
    """
    conn = sqlite3.connect(path)
    c = conn.cursor()
    toReturn = []
    for row in c.execute("PRAGMA table_info('"+table+"')").fetchall():
        tmp = 0
        for x in row:
            if (x.__class__.__name__ == "str") and (tmp%2 == 1):
                toReturn.append(x)
            tmp  = tmp + 1
    conn.close()
    return toReturn


def get_all_element_of_table(path, table):
    """
    return all element of table
    """
    conn = sqlite3.connect(path)
    c = conn.cursor()
    toReturn = "<tr>"
    for row in c.execute('SELECT * FROM '+table).fetchall():
        for x in row:
            toReturn = toReturn + "<td>"+ str(x) + "</td>"
        toReturn = toReturn + "</tr>"
    conn.close()
    return toReturn

def search_element_of_table(path, table, nameColumn, data):
    """
    search a element in table where nameColumn contain data
    """
    conn = sqlite3.connect(path)
    c = conn.cursor()
    toReturn = "<tr>"
    for row in c.execute('SELECT * FROM '+table +' where '+nameColumn+" like '%"+data+"%'").fetchall():
        for x in row:
            toReturn = toReturn + "<td>"+ str(x) + "</td>"
        toReturn = toReturn + "</tr>"

    conn.close()
    return toReturn