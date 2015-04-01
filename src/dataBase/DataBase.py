import sqlite3
import modele.Activity


"""
this file contains differents method for create table in a SQLite3 file 
"""

def make_query(path, query):
    conn = sqlite3.connect(path)
    c = conn.cursor()

    result = c.execute(query).fetchall()

    conn.commit()
    conn.close()
    return result

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


def get_name_of_column_in_array(path, table):
    """
    return the name of all column in a array
    path: path of data base
    table: name of table
    """
    conn = sqlite3.connect(path)
    c = conn.cursor()
    to_return = []
    for row in c.execute("PRAGMA table_info('"+table+"')").fetchall():
        tmp = 0
        for x in row:
            if (x.__class__.__name__ == "str") and (tmp%2 == 1):
                to_return.append(x)
            tmp  = tmp + 1
    conn.close()
    return to_return


def get_all_element_of_table(path, table):
    """
    return all element of table
    path: path of data base
    table: name of table
    """
    conn = sqlite3.connect(path)
    c = conn.cursor()
    to_return = []
    for row in c.execute('SELECT * FROM '+table).fetchall():
        for x in row:
            to_return.append(x)
    conn.close()
    return to_return

def search_element_of_table(path, table, nameColumn, data):
    """
    search a element in table where nameColumn contain data
    path: path of data base
    table: name of table
    """
    conn = sqlite3.connect(path)
    c = conn.cursor()
    to_return = "<tr>"
    for row in c.execute('SELECT * FROM '+table +' where '+nameColumn+" like '%"+data+"%'").fetchall():
        for x in row:
            to_return = to_return + "<td>"+ str(x) + "</td>"
        to_return = to_return + "</tr>"

    conn.close()
    return to_return


def import_equipment_object_in_array(path):
    """
    import all equipment object and insert into an array
    path: the path of data base where are situate object
    """
    conn = sqlite3.connect(path)
    c = conn.cursor()
    to_return = []
    for row in c.execute('SELECT * FROM '+"Equipment").fetchall():
        to_return.append(Equipment(row[0],row[1],row[2],row[3],row[4],row[5]))
    conn.close()
    return to_return

def import_activity_object_in_array(path):
    """
    import all activity object and insert into an array
    path: the path of data base where are situate object
    """
    conn = sqlite3.connect(path)
    c = conn.cursor()
    to_return = []
    for row in c.execute('SELECT * FROM '+"Activity").fetchall():
        to_return.append(Activity(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))
    conn.close()
    return to_return
    
def import_installations_object_in_array(path):
    """
    import all installations object and insert into an array
    path: the path of data base where are situate object
    """
    return "todo"

def jointure_table(path, table1, table2, field1, field2, search1, search2):
    """
    make join between table1 and table2 where field1=search1 and field2 = search2
    and return the result in array
    """
    conn = sqlite3.connect(path)
    c = conn.cursor()
    rows = c.execute('SELECT * FROM '+table1 +' as t1 JOIN '+table2+" as t2 where t1."+field1+" like '%"+search1+"%' and t2."+field2+" like '%"+search2+"%'").fetchall()
    conn.close()
    return rows
