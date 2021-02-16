Ubuntu-val kapcsolatos segedletek, amik szamomra szuksegesek:

## GUI letiltasa/engedelyezese 
Ezzel azt lehet elerni, hogy esetlegesen csak akkor induljon el a GUI ha szukseg van ra. 

https://askubuntu.com/questions/1056363/how-to-disable-gui-on-boot-in-18-04-bionic-beaver

I. 
To disable GUI on boot, run:
sudo systemctl set-default multi-user.target

II.
To enable GUI again issue the command:
sudo systemctl set-default graphical.target

III.
To start Gnome session on a system without a current GUI just execute:
sudo systemctl start gdm3.service

## Szolgaltatas indulasanak kesleltetese
Azok az alkalmazasok amik szolgaltataskent vannak engedelyezve azoknak az indulasa kesleltetheto. 
Ez akkor jon jol, ha vpn mogul akarunk valamit futattni. 

A *.service file-ban kell felvenni +1 sort. A sleep parancsot kell hazsnalni.
A service fajlok helye: /lib/systemd/system/

A file-ba az alábbi sort kell beiirni:
ExecStartPre=/bin/sleep 30

A 30 a kesletetes, ebben az esetben a 30 az 30 masodperces kesleltetest jelent startup-tol!



