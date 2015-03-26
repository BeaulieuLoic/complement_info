import cherrypy
import sqlite3
from dataBase import DataBase
import argparse
import os

pathDataBase = "dataBase.db"


def set_path_data_base(path):
    path_data_base = path
    if not os.path.isfile(path):
        print("Error: file don't exists !")
        sys.exit()



parser = argparse.ArgumentParser(description='web service.')
parser.add_argument('path_data_base', metavar='path_data_base', type=str, help='set the data base path')

args = parser.parse_args()
set_path_data_base(args.path_data_base)

class WebManager(object):

    @cherrypy.expose
    def index(self):
        """
        default page, display all table in data base and the number of 
        elements in every table. you can click on the name of table for 
        display all elements of table, or use search function
        """

        conn = sqlite3.connect(pathDataBase)
        c = conn.cursor()

        toReturn = "structure de la base de donnée: <ul>"

        for row in c.execute('SELECT count(*) FROM Installations'):
            toReturn = toReturn + "<li>" 
            toReturn = toReturn + "<a href=\"installations\">Installations:</a>"
            toReturn = toReturn + str(row).replace(",","").replace("(","").replace(")","")
            toReturn = toReturn + "</li>" 
        for row in c.execute('SELECT count(*) FROM Activity'):
            toReturn = toReturn + "<li>" 
            toReturn = toReturn + "<a href=\"activity\">Activity:</a>"
            toReturn = toReturn + str(row).replace(",","").replace("(","").replace(")","")
            toReturn = toReturn + "</li>" 
        for row in c.execute('SELECT count(*) FROM Equipment'):
            toReturn = toReturn + "<li>" 
            toReturn = toReturn + "<a href=\"equipment\">Equipment:</a>"
            toReturn = toReturn + str(row).replace(",","").replace("(","").replace(")","")
            toReturn = toReturn + "</li>" 

        conn.close()

        toReturn = toReturn + "<a href=\"searchOption\">search something</a>"

        return toReturn+"</ul>"



    def get_name_of_column(self, table):
        """
        return the name of all column in a table html
        """
        conn = sqlite3.connect(pathDataBase)
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

    def get_name_of_column_in_array(self, table):
        """
        return the name of all column in a array
        """
        conn = sqlite3.connect(pathDataBase)
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


    def get_all_element_of_table(self, table):
        """
        return all element of table
        """
        conn = sqlite3.connect(pathDataBase)
        c = conn.cursor()
        toReturn = "<tr>"
        for row in c.execute('SELECT * FROM '+table).fetchall():
            for x in row:
                toReturn = toReturn + "<td>"+ str(x) + "</td>"
            toReturn = toReturn + "</tr>"
        conn.close()
        return toReturn

    def search_element_of_table(self, table, nameColumn, data):
        """
        search a element in table where nameColumn contain data
        """
        conn = sqlite3.connect(pathDataBase)
        c = conn.cursor()
        toReturn = "<tr>"
        for row in c.execute('SELECT * FROM '+table +' where '+nameColumn+" like '%"+data+"%'").fetchall():
            for x in row:
                toReturn = toReturn + "<td>"+ str(x) + "</td>"
            toReturn = toReturn + "</tr>"

        conn.close()
        return toReturn


    @cherrypy.expose
    def equipment(self):
        """
        display all elements of equipment
        """

        toReturn = "table Equipment"
        toReturn = toReturn + "<table border=\"1\"> "

        toReturn = toReturn + self.get_name_of_column("Equipment")
        toReturn = toReturn + self.get_all_element_of_table("Equipment")

        return toReturn+"</table>"


    @cherrypy.expose
    def activity(self):
        """
        display all elements of activity
        """

        toReturn = "table activity </br>"
        toReturn = toReturn + "<table border=\"1\"> "

        toReturn = toReturn + self.get_name_of_column("Activity")
        toReturn = toReturn + self.get_all_element_of_table("Activity")

        return toReturn+"</table>"

    @cherrypy.expose
    def installations(self):
        """
        display all elements of installations
        """


        toReturn = "table Installations </br>"
        
        toReturn = toReturn + "<table border=\"1\"> "

        toReturn = toReturn + self.get_name_of_column("Installations")
        toReturn = toReturn + self.get_all_element_of_table("Installations")

        toReturn = toReturn + "</table>"

        return toReturn

    @cherrypy.expose
    def searchOption(self):
        """
        display form for search elements in data base
        """
        toReturn = ""

        toReturn = toReturn +""" 
        <h1>Search something in table</h1>
            <h3>search by INSEE number</h3>

            <table border=\"1\">
                <form method="get" action="search_equipment">
                    <tr>
                        <td>
                            Equipment
                        </td>
                        <td>
                            <input type="text" name="searchEquipment">
                        </td>
                        <td>
                            <select name="field">
        """

        for field in self.get_name_of_column_in_array("Equipment"):
            toReturn = toReturn + "<option value="+str(field)+">"+str(field)+"</option>"
        toReturn = toReturn +"""

                            </select>
                        </td>
                        <td>
                            <input type="submit">
                        </td>
                    </tr>
                </form>
                <form method="get" action="search_activity">
                    <tr>
                        <td>
                            Activity
                        </td>
                        <td>
                            <input type="text" name="searchActivity">
                        </td>
                        <td>
                            <select name="field">
        """

        for field in self.get_name_of_column_in_array("Activity"):
            toReturn = toReturn + "<option value="+str(field)+">"+str(field)+"</option>"

        toReturn = toReturn +"""
                            </select>
                        </td>
                        <td>
                            <input type="submit">
                        </td>
                    </tr>
                </form>
                <form method="get" action="search_installation">
                    <tr>
                        <td>
                            Installations
                        </td>
                        <td>
                            <input type="text" name="searchInstallation">
                        </td>
                        <td>
                            <select name="field">
        """

        for field in self.get_name_of_column_in_array("Installations"):
            toReturn = toReturn + "<option value="+str(field)+">"+str(field)+"</option>"
        
        toReturn = toReturn +"""
                            </select>
                        </td>
                        <td>
                            <input type="submit">
                        </td>
                    </tr>
                </form>
            </table>
        """
        return toReturn


    @cherrypy.expose
    def search_equipment(self, searchEquipment, field):
        """
        display elements in Equipment where insee contain searchEquipment
        """
        toReturn = ""
        toReturn = toReturn + "<table border=\"1\"> "
        toReturn = toReturn + self.get_name_of_column("Equipment")
        toReturn = toReturn + self.search_element_of_table("Equipment", field, str(searchEquipment))
        toReturn = toReturn + "</table>"
        return toReturn

    @cherrypy.expose
    def search_activity(self, searchActivity, field):
        """
        display elements in Equipment where insee contain searchActivity
        """
        toReturn = ""
        toReturn = toReturn + "<table border=\"1\"> "
        toReturn = toReturn + self.get_name_of_column("Activity")
        toReturn = toReturn + self.search_element_of_table("Activity", field, str(searchActivity))
        toReturn = toReturn + "</table>"
        return toReturn

    @cherrypy.expose
    def search_installation(self, searchInstallation, field):
        """
        display elements in Installations where insee contain searchInstallation
        """
        toReturn = ""
        toReturn = toReturn + "<table border=\"1\"> "
        toReturn = toReturn + self.get_name_of_column("Installations")
        toReturn = toReturn + self.search_element_of_table("Installations", field, str(searchInstallation))
        toReturn = toReturn + "</table>"
        return toReturn


cherrypy.quickstart(WebManager())