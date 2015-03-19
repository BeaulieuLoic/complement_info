import cherrypy
import sqlite3
from dataBase import DataBase

pathDataBase = "dataBase.db"



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
        return the name of all column of a table
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


        toReturn = """ 
        <h1>Search something in table</h1>
            <h3>search by INSEE number</h3>

            <table border=\"1\">
                <form method="get" action="search_equipment_INSEE">
                    <tr>
                        <td>
                            Equipment
                        </td>
                        <td>
                            <input type="text" name="searchEquipment">
                        </td>
                        <td>
                            <input type="submit">
                        </td>
                    </tr>
                </form>
                <form method="get" action="search_activity_INSEE">
                    <tr>
                        <td>
                            Activity
                        </td>
                        <td>
                            <input type="text" name="searchActivity">
                        </td>
                        <td>
                            <input type="submit">
                        </td>
                    </tr>
                </form>
                <form method="get" action="search_installation_INSEE">
                    <tr>
                        <td>
                            Installations
                        </td>
                        <td>
                            <input type="text" name="searchInstallation">
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
    def search_equipment_INSEE(self, searchEquipment):
        """
        display elements in Equipment where insee contain searchEquipment
        """
        toReturn = ""
        toReturn = toReturn + "<table border=\"1\"> "
        toReturn = toReturn + self.get_name_of_column("Equipment")
        toReturn = toReturn + self.search_element_of_table("Equipment", "comInsee", str(searchEquipment))
        toReturn = toReturn + "</table>"
        return toReturn

    @cherrypy.expose
    def search_activity_INSEE(self, searchActivity):
        """
        display elements in Equipment where insee contain searchActivity
        """
        toReturn = ""
        toReturn = toReturn + "<table border=\"1\"> "
        toReturn = toReturn + self.get_name_of_column("Activity")
        toReturn = toReturn + self.search_element_of_table("Activity", "inseeNb", str(searchActivity))
        toReturn = toReturn + "</table>"
        return toReturn

    @cherrypy.expose
    def search_installation_INSEE(self, searchInstallation):
        """
        display elements in Installations where insee contain searchInstallation
        """
        toReturn = ""
        toReturn = toReturn + "<table border=\"1\"> "
        toReturn = toReturn + self.get_name_of_column("Installations")
        toReturn = toReturn + self.search_element_of_table("Installations", "INSEE", str(searchInstallation))
        toReturn = toReturn + "</table>"
        return toReturn


cherrypy.quickstart(WebManager())