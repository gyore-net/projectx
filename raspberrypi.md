Raspberryvel kapcsolatos segedletek, amik szamomra szuksegesek:

## wireguard 
Siman apt-vel fel lehet telepiteni ha a wg0 interface felcsatolasanal nem tud kiepulni a kapcsolat, akkor a DNS serverrel valo problemajara megoldas:
Fel kell telepiteni az opendns-t es mar mukodik is. 

## Adatgyujto
Az adatgyujtohoz az alabbi csomagokat is telepiteni kell kulonben nem mukodik.

1. apt-get install pip
2. pip3 install mysql-connector
3. pip3 install mysql-connector-python
4. apt-get install rpi.gpio

1. --> python csomagkezeloje
2. --> szukseges ahhoz hogy a python script tudjon connectelni mysql adatbazishoz
3. --> ugyan az mint a 2-es
4. --> telepiti a gpio-hoz szukseges csomagokat
