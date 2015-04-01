import cherrypy
import sqlite3
from dataBase import DataBase as db
import argparse
import os
import sys

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

        to_return = "<h1>data base</h1> <ul>"
        to_return = to_return + "<h2>display all elements in table:</h2>"
        nbrIns = c.execute('SELECT count(*) FROM Installations').fetchone()
        to_return = to_return + "<li>" 
        to_return = to_return + "<a href=\"afficherTable?table=Installations\">number of Installations object: </a>"
        to_return = to_return + str(nbrIns).replace(",","").replace("(","").replace(")","")
        to_return = to_return + "</li>" 

        nbrAct = c.execute('SELECT count(*) FROM Activity').fetchone()
        to_return = to_return + "<li>" 
        to_return = to_return + "<a href=\"afficherTable?table=Activity\">number of Activity object: </a>"
        to_return = to_return + str(nbrAct).replace(",","").replace("(","").replace(")","")
        to_return = to_return + "</li>" 
        
        nbrEqu = c.execute('SELECT count(*) FROM Equipment').fetchone()
        to_return = to_return + "<li>" 
        to_return = to_return + "<a href=\"afficherTable?table=Equipment\">number of Equipment: </a>"
        to_return = to_return + str(nbrEqu).replace(",","").replace("(","").replace(")","")
        to_return = to_return + "</li>" 
        to_return = to_return +"</ul>"

        conn.close()

        to_return = to_return + "<h2>search somethin in table:</h2>"
        to_return = to_return + "<a href=\"searchOption\">search something</a>"

        to_return = to_return + "<h2>other:</h2>"
        to_return = to_return + "<a href=\"SQL?query=init\">make query in sqLite data base</a>"


        return to_return+"</ul>"+"<a href=\"index\">return to index<a>"

    @cherrypy.expose
    def afficherTable(self, table):
        """
        display all elements of equipment
        """
        to_return = "table "+str(table)
        to_return = to_return + "<table border=\"1\"> "

        nbrColumns = 0
        to_return = to_return + "<tr>"
        for field in db.get_name_of_column_in_array(pathDataBase, str(table)):
            to_return = to_return + "<td>"+field+"</td>"
            nbrColumns = nbrColumns + 1
        to_return = to_return + "</tr>"

        tmp = 0
        for elem in db.get_all_element_of_table(pathDataBase, str(table)):
            if tmp==0:
                to_return = to_return + "<tr>" 
            
            to_return = to_return + "<td>"+str(elem)+"</td>"
            if tmp == nbrColumns-1:
                to_return = to_return + "<tr>"
                tmp =-1
            tmp = tmp + 1

        return to_return+"</table>"+"<a href=\"index\">return to index<a>"

    @cherrypy.expose
    def searchOption(self):
        """
        display form for search elements in data base
        """
        to_return = ""

        to_return = to_return +""" 
        <h1>Search something</h1>
        <h2>search in tables: </h2>
            <table border=\"10\">
                <form method="get" action="search">
                    <tr>
                        <td>
                            <p name="table" value="Equipment">Equipment</p>
                        </td>
                        <td>
                            <input type="text" name="toSearch">
                        </td>
                        <td>
                            <select name="field" id="searchEquipment">
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
                    <input style="display: none" name="table" value="Equipment">
                </form>
                <form method="get" action="search" >
                    <tr>
                        <td>
                            Activity
                        </td>
                        <td>
                            <input type="text" name="toSearch">
                        </td>
                        <td>
                            <select name="field" id="searchActivity">
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
                    <input style="display: none" name="table" value="Activity">
                </form>
                <form method="get" action="search">
                    <tr>
                        <td>
                            Installations
                        </td>
                        <td>
                            <input type="text" name="toSearch">
                        </td>
                        <td>
                            <select name="field" id="searchInstallation">
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
                    <input style="display: none" name="table" value="Installations">
                </form>
            </table>
        """
        to_return = to_return +"""
        <h2>join tables 1 with table 2:</h2>
            <script>
                function actualiserField1(){
                    var table1 = document.getElementById("table1");
                    tableSelected = table1.options[table1.selectedIndex].value;

                    if(tableSelected == "Equipment")
                        document.getElementById("field1").innerHTML = document.getElementById("searchEquipment").innerHTML;
                    if(tableSelected == "Activity")
                        document.getElementById("field1").innerHTML = document.getElementById("searchActivity").innerHTML;
                    if(tableSelected == "Installations")
                        document.getElementById("field1").innerHTML = document.getElementById("searchInstallation").innerHTML;      
                }

                function actualiserField2(){
                    var table1 = document.getElementById("table2");
                    tableSelected = table1.options[table1.selectedIndex].value;

                    if(tableSelected == "Equipment")
                        document.getElementById("field2").innerHTML = document.getElementById("searchEquipment").innerHTML;
                    if(tableSelected == "Activity")
                        document.getElementById("field2").innerHTML = document.getElementById("searchActivity").innerHTML;
                    if(tableSelected == "Installations")
                        document.getElementById("field2").innerHTML = document.getElementById("searchInstallation").innerHTML;      
                }
            </script>
            <form method="get" action="join">
                <table border=\"10\">
                    <tr>
                        <td>num tab</td>
                        <td>table</td>
                        <td>field</td>
                        <td>elements to search</td>
                    </tr>
                    <tr>
                        <td>1</td>
                        <td>
                            <select name="table1" id="table1">
                                <option value=\"Activity\" selected onclick="actualiserField1()">Activity</option>
                                <option value=\"Equipment\" onclick="actualiserField1()">Equipment</option>
                                <option value=\"Installations\" onclick="actualiserField1()">Installations</option>
                            </select>
                        </td>
                        <td>
                            <select name="field1" id="field1">
                                <option selected onclick="actualiserField1()">click to refresh</option>
                            </select>
                        </td>
                        <td>
                            <input type=\"text\" name="search1"/>
                        </td>
                    </tr>
                    <tr>
                        <td>2</td>
                        <td>
                            <select name="table2" id="table2">
                                <option value=\"Activity\" selected onclick="actualiserField2()">Activity</option>
                                <option value=\"Equipment\" onclick="actualiserField2()">Equipment</option>
                                <option value=\"Installations\" onclick="actualiserField2()">Installations</option>
                            </select>
                        </td>
                        <td>
                            <select name="field2" id="field2">
                                <option selected onload="actualiserField2()">click to refresh</option>
                            </select>
                        </td>
                        <td>
                            <input type=\"text\" name="search2"/>
                        </td>
                    </tr>
                </table>
                <input type=\"submit\" />
            </form>

            e.g with
            <table border="10">
                <tr>
                    <td>Installations</td>
                    <td>nameTown</td>
                    <td>Nantes</td>
                </tr>
                <tr>
                    <td>Activity</td>
                    <td>actLib</td>
                    <td>Football</td>
                </tr>
            </table>a
            <script>actualiserField1();actualiserField2();</script>
        """
            
        return to_return+"</br><a href=\"index\">return to index<a>"
    
    @cherrypy.expose
    def search(self, table, toSearch, field):
        """
        display elements in table where field in data base contain toSearch
        """
        to_return = ""
        to_return = to_return + "<table border=\"1\"> "

        to_return = to_return + "<tr>"
        for element in db.get_name_of_column_in_array(pathDataBase, str(table)):
            to_return = to_return + "<td>"+element+"</td>"
        to_return = to_return + "</tr>"

        to_return = to_return + db.search_element_of_table(pathDataBase, str(table), field, str(toSearch))
        to_return = to_return + "</table>"
        return to_return+"<a href=\"index\">return to index<a>"

    @cherrypy.expose
    def join(self, table1, table2, field1, field2, search1, search2):
        to_return=""
        for row in db.jointure_table(pathDataBase, table1, table2, field1, field2, search1, search2):
            to_return = to_return +"</br>"+ str(row)
        if to_return!="":
            return to_return+"</br><a href=\"index\">return to index<a>"
        else:
            return "nothing found"+"</br><a href=\"index\">return to index<a>"

    @cherrypy.expose
    def SQL(self,query):
        """
        display interface for make query and display the result 
        """

        to_return = """
        <form method="get" action="SQL">
            make query: </br> <TEXTAREA name="query"></TEXTAREA>
            </br>
            <input type="submit">
        </form>
        """
        if (str(query)!="init"):
            to_return = to_return + "result of the query: </br><div style=\"background: #AAAAAA\">"
            result = ""

            for elem in db.make_query(pathDataBase,query):
                result = result + str(elem)
                result = result + "</br>"
            to_return = to_return + result + "</div>"


        return to_return+"<a href=\"index\">return to index<a>"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='web service.')
    parser.add_argument('path_data_base', metavar='path_data_base', type=str, help='set the data base path')

    args = parser.parse_args()

    pathDataBase = args.path_data_base
    if not os.path.isfile(args.path_data_base):
        print("Error: file don't exists !")
        sys.exit()

    cherrypy.quickstart(WebManager())
