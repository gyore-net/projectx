#Szukseges ahhoz, hogy pi GPIO portjait pythonnal lehessen hasznalni.



import time
#sleep csak azert van benne, mert sima nyomogombbal tesztelem tuzkodos panelon a dolgot es lusta vagyok osszerakni egy impulzus jeladot... - igy jelen esetben elofordul, hogy tobbszor kontaktal "egy adott pillanatban"
#tobbszor is ad jelet a nyomogomb es az sql hibara fut, hogy 2 vagy tobb adat van 1 idopillanatban.
from time import sleep
from datetime import datetime

#Szukseges ahhoz, hogy a python tudja kezelni a mysql-t.
import mysql.connector
import random
#A helyi idot kerdezem le vele(a raspberry levo idot kerdezi le). Az rpi es a mysql server egy azon ntp server-t hasznal, es elvben minden nap 0:00-kor szinkrinizalnak.
localtime = datetime.now()

a = random.randint(1, 3)
eon_mero = float(input("Add meg a szamot"))


#Kapcsolodas az adatbazishoz:
db = mysql.connector.connect(
    host = "192.168.70.1",
    user = "rpi_user",
    passwd = "Alap1234_",
    database = "smart_home"
)

print("Mysql connect success!")

mycursor = db.cursor()

try:
    while True:
         if a == 1:
            now = datetime.now()
            a = random.randint(1, 3)
            formatted_date = now.strftime('%Y-%m-%d %H:%M:%S.%f')
            print("L1-->", formatted_date)
            mycursor.execute("INSERT INTO L1_be (L1_be_datum) VALUES (%s)", (now.strftime('%Y-%m-%d %H:%M:%S.%f'),))
            db.commit()
            eon_mero = eon_mero + 0.0005
            print("EON mero allasa:", round(eon_mero, 4))
            sleep((random.random()*10)+0.1)

         if a == 2:
            now = datetime.now()
            a = random.randint(1, 3)
            formatted_date = now.strftime('%Y-%m-%d %H:%M:%S.%f')
            print("L2-->", formatted_date)
            mycursor.execute("INSERT INTO L2_be (L2_be_datum) VALUES (%s)", (now.strftime('%Y-%m-%d %H:%M:%S.%f'),))
            db.commit()
            eon_mero = eon_mero + 0.0005
            print("EON mero allasa:", round(eon_mero, 4))
            sleep((random.random() * 10) + 0.1)

         if a == 3:
            now = datetime.now()
            a = random.randint(1, 3)
            formatted_date = now.strftime('%Y-%m-%d %H:%M:%S.%f')
            print("L3-->", formatted_date)
            mycursor.execute("INSERT INTO L3_be (L3_be_datum) VALUES (%s)", (now.strftime('%Y-%m-%d %H:%M:%S.%f'),))
            db.commit()
            eon_mero = eon_mero + 0.0005
            print("EON mero allasa:", round(eon_mero, 4))
            sleep((random.random() * 10) + 0.1)


except KeyboardInterrupt:
    exit()
