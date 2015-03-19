import cherrypy
import sqlite3
from dataBase import DataBase

pathDataBase = "dataBase.db"



class WebManager(object):

    @cherrypy.expose
    def index(self):
        conn = sqlite3.connect(pathDataBase)
        c = conn.cursor()

        to_return = "structure de la base de donnée: <ul>"

        for row in c.execute('SELECT count(*) FROM Installations'):
            to_return = to_return + "<li>" 
            to_return = to_return + "<a href=\"installations\">Installations:</a>"
            to_return = to_return + str(row).replace(",","").replace("(","").replace(")","")
            to_return = to_return + "</li>" 

        for row in c.execute('SELECT count(*) FROM Activity'):
            to_return = to_return + "<li>" 
            to_return = to_return + "<a href=\"activity\">Activity:</a>"
            to_return = to_return + str(row).replace(",","").replace("(","").replace(")","")
            to_return = to_return + "</li>" 

        for row in c.execute('SELECT count(*) FROM Equipment'):
            to_return = to_return + "<li>" 
            to_return = to_return + "<a href=\"equipment\">Equipment:</a>"
            to_return = to_return + str(row).replace(",","").replace("(","").replace(")","")
            to_return = to_return + "</li>" 

        conn.close()
        return to_return+"</ul>"



    def get_name_of_column(self, table):
        conn = sqlite3.connect(pathDataBase)
        c = conn.cursor()
        
        to_return = ""
        to_return = to_return +"<tr>"

        for row in c.execute("PRAGMA table_info('"+table+"')").fetchall():
            tmp = 0
            for x in row:
                if (x.__class__.__name__ == "str") and (tmp%2 == 1):
                    to_return = to_return +"<td>"+str(x)+"</td>"
                tmp  = tmp + 1

        to_return = to_return +"</tr>"

        conn.close()
        return to_return

    def get_all_element_of_table(self, table):
        conn = sqlite3.connect(pathDataBase)
        c = conn.cursor()

        to_return = ""

        for row in c.execute('SELECT * FROM '+table).fetchall():
            to_return = to_return + "<tr>"
            for x in row:
                to_return = to_return + "<td>"+ str(x) + "</td>"
            to_return = to_return + "</tr>"

        conn.close()
        return to_return

    def get_element_of_table(self, table, nameColumn, data):
        conn = sqlite3.connect(pathDataBase)
        c = conn.cursor()

        to_return = ""

        for row in c.execute('SELECT * FROM '+table +'where '+nameColumn+" = '"+data+"'").fetchall():
            to_return = to_return + "<tr>"
            for x in row:
                to_return = to_return + "<td>"+ str(x) + "</td>"
            to_return = to_return + "</tr>"

        conn.close()
        return to_return


    @cherrypy.expose
    def equipment(self):
        to_return = "table Equipment"
        to_return = to_return + "<table border=\"1\"> "

        to_return = to_return + self.get_name_of_column("Equipment")
        to_return = to_return + self.get_all_element_of_table("Equipment")

        return to_return+"</table>"


    @cherrypy.expose
    def activity(self):

        to_return = "table activity </br>"
        to_return = to_return + "<table border=\"1\"> "

        to_return = to_return + self.get_name_of_column("Activity")
        to_return = to_return + self.get_all_element_of_table("Activity")

        return to_return+"</table>"

    @cherrypy.expose
    def installations(self):

        to_return = "table Installations </br>"
        
        to_return = to_return + "<table border=\"1\"> "

        to_return = to_return + self.get_name_of_column("Installations")
        to_return = to_return + self.get_all_element_of_table("Installations")

        to_return = to_return + "</table>"

        return to_return

    @cherrypy.expose
    def searchOption(self):
        to_return = """ 
        <h1>Search something in table</h1>
            <h3>search INSEE number</h3>

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
                <form method="get" action"search_activity_INSEE">
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
            </table>
        """
        return to_return

    def search_equipment_INSEE(self, searchEquipment):
        toReturn = ""

        to_return = to_return + "<table border=\"1\"> "
        to_return = to_return + self.get_name_of_column("Equipment")
        toReturn = toReturn + get_element_of_table(self, "Equipment", "comInsee", str(searchEquipment)):
        to_return = to_return + "</table>"
        return toReturn

    def search_activity_INSEE(self, searchActivity):
        pritn("a")



cherrypy.quickstart(WebManager())