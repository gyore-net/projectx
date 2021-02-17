#Szukseges ahhoz, hogy pi GPIO portjait pythonnal lehessen hasznalni.
import RPi.GPIO as GPIO


import time
#sleep csak azert van benne, mert sima nyomogombbal tesztelem tuzkodos panelon a dolgot es lusta vagyok osszerakni egy impulzus jeladot... - igy jelen esetben elofordul, hogy tobbszor kontaktal "egy adott pillanatban"
#tobbszor is ad jelet a nyomogomb es az sql hibara fut, hogy 2 vagy tobb adat van 1 idopillanatban.
from time import sleep
from datetime import datetime

#Szukseges ahhoz, hogy a python tudja kezelni a mysql-t.
import mysql.connector

#A helyi idot kerdezem le vele(a raspberry levo idot kerdezi le). Az rpi es a mysql server egy azon ntp server-t hasznal, es elvben minden nap 0:00-kor szinkrinizalnak.
localtime = datetime.now()

#Beallitja, hogy a GPIO-t hogyan lehessen meghivni. Jelenleg a BCM-et hasznalom, ez a GPIO pin szamat hasznalja, nem pedig az rpi-n a pinek kiosztasat.
#pinout parancsra a GPIO-t kijelzi, es az alapjan a szamozas alapjan mukodik
GPIO.setmode(GPIO.BCM)

##INPUT bekeresek##
##Berekem a szukseges adatokat:
## - L1 mero melyik gpio-ra van csatlakoztatva
## - L2 mero melyik gpio-ra van csatlakoztatva
## - L2 mero melyik gpio-ra van csatlakoztatva
## - Bekerem az EON-os fogyasztasmeron szereplo erteket, es ahhoz kepest fogok szamolni

l1_gpio = int(input("Add meg, hogy az L1 fazis mero, melyik GPIO-ra van csatlakoztatva:"))
l2_gpio = int(input("Add meg, hogy az L2 fazis mero, melyik GPIO-ra van csatlakoztatva:"))
l3_gpio = int(input("Add meg, hogy az L3 fazis mero, melyik GPIO-ra van csatlakoztatva:"))
eon_mero = round(float(input("Add meg az EON meron szereplo aktualis fogyasztast:")), 2)

#Kapcsolodas az adatbazishoz:
db = mysql.connector.connect(
    host = "192.168.70.1",
    user = "rpi_user",
    passwd = "Alap1234_",
    database = "smart_home"
)

print("Mysql connect success!")

mycursor = db.cursor()

#A harom GPIO beallitasa, hogy input vagy output-kent lesz hasznalva
GPIO.setup(l1_gpio, GPIO.IN)
GPIO.setup(l2_gpio, GPIO.IN)
GPIO.setup(l3_gpio, GPIO.IN)
print("GPIO setup success!")

try:
    while True:
        if GPIO.input(l1_gpio):
            print("L1-->", datetime.now())
            mycursor.execute("INSERT INTO L1_be (L1_be_datum) VALUES (localtime)")
            db.commit()
            eon_mero = eon_mero + 0.0005
            print("EON:",round(eon_mero, 4))
            GPIO.setup(l1_gpio, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        sleep(0.1)

        if GPIO.input(l2_gpio):
            print("L2-->", datetime.now())
            mycursor.execute("INSERT INTO L2_be (L2_be_datum) VALUES (localtime)")
            db.commit()
            eon_mero = eon_mero + 0.0005
            print("EON:", round(eon_mero, 4))
            GPIO.setup(l2_gpio, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        sleep(0.1)

        if GPIO.input(l3_gpio):
            print("L3-->", datetime.now())
            mycursor.execute("INSERT INTO L3_be (L3_be_datum) VALUES (localtime)")
            db.commit()
            eon_mero = eon_mero + 0.0005
            print("EON:", round(eon_mero, 4))
            GPIO.setup(l3_gpio, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        sleep(0.1)
        
except KeyboardInterrupt:  
    GPIO.cleanup()
