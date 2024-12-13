import mysql.connector

mydb = mysql.connector.connect(
  host="localhost", 
  user="root",
  password="root",
  database="python"
)

mycursor = mydb.cursor()

def insertUser(nom, prenom, nbEtud, specialite, login, password, isAdmin = False):
    sql = "INSERT INTO users_etudiant (lname, fname, nb_etudiant, specialite, login, password, is_admin) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (nom, prenom, nbEtud, specialite, login, password, isAdmin)
    mycursor.execute(sql, val)
    mydb.commit()

def selectUser(login):
    sql = "SELECT * FROM users_etudiant WHERE login = %s"
    val = [login]
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    return myresult[0]

def selectAllUsers():
    sql = "SELECT * FROM users_etudiant"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult

def updateUser(nom, prenom, nbEtud, specialite, login, password, isAdmin, id):
    sql = "UPDATE users_etudiant SET lname = %s, fname = %s, nb_etudiant = %s, specialite = %s, password = %s, login = %s, is_admin = %s  WHERE id = %s"
    val = (nom, prenom, nbEtud, specialite, password, login, isAdmin, id)
    mycursor.execute(sql, val)
    mydb.commit()

def deleteUser(id):
    sql = "DELETE FROM users_etudiant WHERE id = %s"
    val = [id]
    mycursor.execute(sql, val)
    mydb.commit()

def banUser(id):
    sql = "UPDATE users_etudiant SET ban_date = NOW() WHERE id = %s"
    val = [id]
    mycursor.execute(sql, val)
    mydb.commit()
