import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root"
  database="python"
)

mycursor = mydb.cursor()

def insertUser(nom, prenom, login, password):
    sql = "INSERT INTO user (nom, prenom, login, password) VALUES (%s, %s, %s, %s)"
    val = (nom, prenom, login, password)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

def selectUser(login):
    sql = "SELECT * FROM user WHERE login = %s"
    val = (login)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchAll()
    return myresult[0]