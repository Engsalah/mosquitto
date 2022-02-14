# mosquitto
# README.md
# DESCRIPTION
** Version 1.0.0 **
A simple project of MQTT broker, to send a message from the publisher to the subscriber.

## INSTALLATION  
Open your terminal and write the following commands.
* firstly, you need to install mosquitto.
$sudo apt-get update
$sudo apt-get upgrade
$sudo apt-get install mosquitto

* Then you need to start the service.
$sudo systemctl enable --now mosquitto

* Last thing, install python pip and paho-mqtt.
$sudo apt-get install python3-pip
$sudo apt-get install paho-mqtt

Now you are ready to go

## INSTRUCTIONS

*To run the program, you need to open 2 Windows from your Terminal
*Make sure you are in the directory of the project
*In the first Terminal you will write "$./publisher.py" and in the second Terminal "$./subscriber.py"
*In case you get an error message "Permission denied" Then you have to write this command
"$sudo chmod +x publisher.py" && "$sudo chmod +x subscriber.py"
