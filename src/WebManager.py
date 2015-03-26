import cherrypy
import sqlite3
from dataBase import DataBase as db
import argparse
import os
import sys

pathDataBase = "dataBase.db"





if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='web service.')
    parser.add_argument('path_data_base', metavar='path_data_base', type=str, help='set the data base path')

    args = parser.parse_args()

    pathDataBase = args.path_data_base
    if not os.path.isfile(args.path_data_base):
        print("Error: file don't exists !")
        sys.exit()


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

        to_return = "structure of the database: <ul>"

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

        to_return = to_return + "<a href=\"searchOption\">search something</a>"

        return to_return+"</ul>"


    @cherrypy.expose
    def equipment(self):
        """
        display all elements of equipment
        """

        to_return = "table Equipment"
        to_return = to_return + "<table border=\"1\"> "

        to_return = to_return + "<tr>"
        for field in db.get_name_of_column_in_array(pathDataBase, "Equipment"):
            to_return = to_return + "<td>"+field+"</td>"
        to_return = to_return + "</tr>"


        to_return = to_return + db.get_all_element_of_table(pathDataBase, "Equipment")

        return to_return+"</table>"


    @cherrypy.expose
    def activity(self):
        """
        display all elements of activity
        """

        to_return = "table activity </br>"
        to_return = to_return + "<table border=\"1\"> "

        to_return = to_return + "<tr>"
        for field in db.get_name_of_column_in_array(pathDataBase, "Activity"):
            to_return = to_return + "<td>"+field+"</td>"
        to_return = to_return + "</tr>"

        to_return = to_return + db.get_all_element_of_table(pathDataBase, "Activity")

        return to_return+"</table>"

    @cherrypy.expose
    def installations(self):
        """
        display all elements of installations
        """

        to_return = "table Installations </br>"
        
        to_return = to_return + "<table border=\"1\"> "

        to_return = to_return + "<tr>"
        for field in db.get_name_of_column_in_array(pathDataBase, "Installations"):
            to_return = to_return + "<td>"+field+"</td>"
        to_return = to_return + "</tr>"

        to_return = to_return + db.get_all_element_of_table(pathDataBase, "Installations")

        to_return = to_return + "</table>"

        return to_return

    @cherrypy.expose
    def searchOption(self):
        """
        display form for search elements in data base
        """
        to_return = ""

        to_return = to_return +""" 
        <h1>Search something in table</h1>
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

        for field in db.get_name_of_column_in_array(pathDataBase, "Equipment"):
            to_return = to_return + "<option value="+str(field)+">"+str(field)+"</option>"
        to_return = to_return +"""

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

        for field in db.get_name_of_column_in_array(pathDataBase, "Activity"):
            to_return = to_return + "<option value="+str(field)+">"+str(field)+"</option>"

        to_return = to_return +"""
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

        for field in db.get_name_of_column_in_array(pathDataBase, "Installations"):
            to_return = to_return + "<option value="+str(field)+">"+str(field)+"</option>"
        
        to_return = to_return +"""
                            </select>
                        </td>
                        <td>
                            <input type="submit">
                        </td>
                    </tr>
                </form>
            </table>
        """
        return to_return


    @cherrypy.expose
    def search_equipment(self, searchEquipment, field):
        """
        display elements in Equipment where insee contain searchEquipment
        """
        to_return = ""
        to_return = to_return + "<table border=\"1\"> "

        to_return = to_return + "<tr>"
        for element in db.get_name_of_column_in_array(pathDataBase, "Equipment"):
            to_return = to_return + "<td>"+element+"</td>"
        to_return = to_return + "</tr>"

        to_return = to_return + db.search_element_of_table(pathDataBase, "Equipment", field, str(searchEquipment))
        to_return = to_return + "</table>"
        return to_return

    @cherrypy.expose
    def search_activity(self, searchActivity, field):
        """
        display elements in Equipment where insee contain searchActivity
        """
        to_return = ""
        to_return = to_return + "<table border=\"1\"> "

        to_return = to_return + "<tr>"
        for element in db.get_name_of_column_in_array(pathDataBase, "Activity"):
            to_return = to_return + "<td>"+element+"</td>"
        to_return = to_return + "</tr>"

        to_return = to_return + db.search_element_of_table(pathDataBase, "Activity", field, str(searchActivity))
        to_return = to_return + "</table>"
        return to_return

    @cherrypy.expose
    def search_installation(self, searchInstallation, field):
        """
        display elements in Installations where insee contain searchInstallation
        """
        to_return = ""
        to_return = to_return + "<table border=\"1\"> "

        to_return = to_return + "<tr>"
        for element in db.get_name_of_column_in_array(pathDataBase, "Installations"):
            to_return = to_return + "<td>"+element+"</td>"
        to_return = to_return + "</tr>"

        to_return = to_return + db.search_element_of_table(pathDataBase, "Installations", field, str(searchInstallation))
        to_return = to_return + "</table>"
        return to_return


cherrypy.quickstart(WebManager())