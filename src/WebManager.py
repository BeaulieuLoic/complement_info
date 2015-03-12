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

        return to_return+"</ul>"

    @cherrypy.expose
    def equipment(self):
        conn = sqlite3.connect(pathDataBase)
        c = conn.cursor()

        to_return = "table Equipment"
        to_return = to_return + "<table border=\"1\"> "

        to_return = to_return +"<tr>"
            
        to_return = to_return +"<td>comInsee</td>"
        to_return = to_return +"<td>comLib</td>"
        to_return = to_return +"<td>equipmentFile</td>"
        to_return = to_return +"<td>equAnneeService</td>"
        to_return = to_return +"<td>equNom</td>"
        to_return = to_return +"<td>equNomBatiment</td>"

        to_return = to_return +"</tr>"

        for row in c.execute('SELECT * FROM Equipment').fetchall():
            to_return = to_return + "<tr>"
            to_return = to_return + "<td>"+ row[0]+ "</td>"
            to_return = to_return + "<td>"+ row[1]+ "</td>"
            to_return = to_return + "<td>"+ row[2]+ "</td>"
            to_return = to_return + "<td>"+ row[3]+ "</td>"
            to_return = to_return + "<td>"+ row[4]+ "</td>"
            to_return = to_return + "<td>"+ row[5]+ "</td>"
            to_return = to_return + "</tr>"

        return to_return+"</table>"


    @cherrypy.expose
    def activity(self):
        conn = sqlite3.connect(pathDataBase)
        c = conn.cursor()

        to_return = "table activity </br>"
        to_return = to_return + "<table border=\"1\"> "

        to_return = to_return +"<tr>"
            
        to_return = to_return +"<td>inseeNb</td>"
        to_return = to_return +"<td>comLib</td>"
        to_return = to_return +"<td>equipementId</td>"
        to_return = to_return +"<td>equNbEquIdentique</td>"
        to_return = to_return +"<td>actCode</td>"
        to_return = to_return +"<td>actLib</td>"
        to_return = to_return +"<td>equActivitePraticable</td>"
        to_return = to_return +"<td>equActivitePratique</td>"
        to_return = to_return +"<td>equActiviteSalleSpe</td>"
        to_return = to_return +"<td>actNivLib</td>"

        to_return = to_return +"</tr>"

        for row in c.execute('SELECT * FROM Activity').fetchall():
            to_return = to_return + "<tr>"
            to_return = to_return + "<td>"+ row[0]+ "</td>"
            to_return = to_return + "<td>"+ row[1]+ "</td>"
            to_return = to_return + "<td>"+ row[2]+ "</td>"
            to_return = to_return + "<td>"+ row[3]+ "</td>"
            to_return = to_return + "<td>"+ row[4]+ "</td>"
            to_return = to_return + "<td>"+ row[5]+ "</td>"
            to_return = to_return + "<td>"+ row[6]+ "</td>"
            to_return = to_return + "<td>"+ row[7]+ "</td>"
            to_return = to_return + "<td>"+ row[8]+ "</td>"
            to_return = to_return + "<td>"+ row[9]+ "</td>"
            to_return = to_return + "</tr>"

        return to_return+"</table>"

    @cherrypy.expose
    def installations(self):
        to_return = "table Installations </br>"
        to_return = to_return +"trop long a faire"

        return to_return

cherrypy.quickstart(WebManager())