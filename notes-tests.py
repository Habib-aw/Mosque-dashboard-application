
# need to change so that after proposed salah message changes from this salah will be changing :|
# need to fix up salah in 2 :)
# need to change suhoor after suhoor and iftaar after iftaar link to req 2 where change after salah

# In masjid only
# need to increase size of circle and canvas
# need to install chromedriver on raspberry pi

# METHOD 1  no gui
# Open the terminal and type the following command to open the rc.local file: 
# sudo nano /etc/rc.local.
# In the rc.local file, enter the following line of code before the "exit 0" line: 
# python3 /home/pi/Mosque-dashboard-application/RUN.py &
# Here, replace PiCounter/display.py with your program/script name. Also, make sure that you use the absolute path to your program and not its relative path.

# method 2 -- gui
# mkdir /home/pi/.config/autostart
# nano /home/pi/.config/autostart/Dashboard.desktop
# in file ----
# [Desktop Entry]
# Type=Application
# Name=Dashboard
# Exec=/usr/bin/python3 /home/pi/Mosque-dashboard-application/RUN.py
# or 
# Exec=@/usr/bin/python3 /home/pi/Mosque-dashboard-application/RUN.py

# method 3 -- gui
# sudo nano /lib/systemd/system/dashboard.service

# [Unit]
# Description=Start Dashboard

# [Service]
# Environment=DISPLAY=:0
# Environment=XAUTHORITY=/home/pi/.Xauthority
# ExecStart=/usr/bin/python3 /home/pi/Mosque-dashboard-application/RUN.py
# Restart=always
# RestartSec=10s
# KillMode=process
# TimeoutSec=infinity

# [Install]
# WantedBy=graphical.target


#sudo systemctl daemon-reload
#sudo systemctl enable clock.service

# debug
# journalctl -u clock.log

# Method 4---
# Create a directory ‘autostart’ in .config if it’s not created before.
# pi@raspberrypi:~ $ mkdir /home/pi/.config/autostart/
# move into this directory
# pi@raspberrypi:~ $ cd /home/pi/.config/autostart/
# Now create a file MyApp.desktop in the above directory with the following content.
# [Desktop Entry]
# Name=Your Application Name
# Type=Application
# Comment=Some Comments about your program
# Exec=/usr/bin/python {replace with file path}.py
# Allow File to be executable.
# pi@raspberrypi:~ $ chmod +x /home/pi/.config/autostart/MyApp.desktop
# Now restart your pi and it will run your app After desktop is ready.



