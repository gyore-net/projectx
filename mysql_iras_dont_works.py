import mysql.connector
import time


localtime = time.localtime(time.time())


db = mysql.connector.connect(
    host = "192.168.70.1",
    user="rpi_user",
    passwd="Alap1234_",
    database="smart_home"
)

mycursor= db.cursor()

#mycursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")
mycursor.execute("INSERT INTO REAL_TIME(Time) VALUES (%s)",("6:30"))
db.commit()

print("smart_home")
