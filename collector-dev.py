   import RPi.GPIO as GPIO
 2 import time
 3 from time import sleep
 4 from datetime import datetime
 5 GPIO.setmode(GPIO.BCM)
 6 import mysql.connector
 7
 8
 9 db = mysql.connector.connect(
10     host = "192.168.70.1",
11     user = "rpi_user",
12     passwd = "Alap1234_",
13     database="smart_home"
14 )
15 print("Mysql connect success!")
16
17 mycursor = db.cursor()
18
19 GPIO.setup(4, GPIO.IN)
20 GPIO.setup(17, GPIO.IN)
21
22 try:
23     while True:
24         if GPIO.input(4):
25             now = datetime.now()
26             formatted_date = now.strftime('%Y-%m-%d %H:%M:%S.%f')
27             mycursor.execute("INSERT INTO proba (datum) VALUES (%s)", (now.strftime('%Y-%m-%d %H:%M:%S.%f'),))
28             db.commit()
29             GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
30             print(now)
31         sleep(0.1)
32
33 #        if GPIO.input(17):
34 #            #f.write(str(datetime.now()))
35 #            #f.write('\n')
36 #            print(datetime.now())
37 #            mycursor.execute("INSERT INTO TVOF11_2 (Datetime) VALUES (localtime)")
38 #            db.commit()
39 #            GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
40 #        sleep(0.1)
41
42
43
44
45
46
47 except KeyboardInterrupt:
48     GPIO.cleanup()
49
