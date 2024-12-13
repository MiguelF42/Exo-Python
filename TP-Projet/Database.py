import mysql.connector

mydb = mysql.connector.connect(
  host="localhost", 
  user="root",
  password="root",
  database="python"
)

mycursor = mydb.cursor()

def insertUser(nom, prenom, nbEtud, specialite, login, password):
    sql = "INSERT INTO users_etudiant (lname, fname, nb_etudiant, specialite, login, password) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (nom, prenom, nbEtud, specialite, login, password)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

def selectUser(login):
    sql = "SELECT * FROM users_etudiant WHERE login = %s"
    val = [login]
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    print(myresult)
    return myresult[0]