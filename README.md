# Automated Temperature Detection and Attendance Register System

.. image:: https://readthedocs.org/projects/smartFileDemo/badge/?version=latest
        :target: https://eee4022s.readthedocs.io/en/latest/index.html
        :alt: Documentation Status

This is the repository contains all the code that was used to create the Automated Temperature Detection and Attendance Register System. The system can be interfaced with using the hardware modules from the physical system itself, and the user interfacing system that makes use of a **Command Line Interface (CLI)** and **Google Sheets**

Installing Dependencies
===========================

 1. Installing dependencies for RC522 module
```
apt-get instaall python3-dev python3-pip
pip3 install spidev
pip3 install mfrc522
```
2. Installing dependencies for MLX90614 module
```
sudo pip3 install adafruit-blinka
sudp pip3 install adafruit-circuitpython-mlx90614
sudo pip3 install pyrebase
```
3. Additional dependencies
```
  pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
  pip install asyncio
```

## Running the main system 
 1.  Run the driver.py file in the backround
 ```
python3 driver.py &
```
**Note**: Keep note of the PID that is outputted on the file was run, will be used to kill the process.
 2. Killing the process
 ```
kill [PID]
```
**Where**: [PID] is the process ID given as output when **1.** was ran.

Alternatively run `ps aux` to get the process ID and run **2.** to kill the script

## Running the User Interfaces
1. On the remote server/local admin.py script.
 ```python
python3 admin.py
```
2. Scheduling activity in database and creating register for activity.

2.1.  Access spreadsheet and add the scheduled activity
https://docs.google.com/spreadsheets/d/1J3cPjzjKt7C20qA6SKbMP4uiy95oTLgCJEqW0fD4BLI/edit?usp=sharing

2.2. After adding activity to database.
	Run: `python3 admin.py`and follow the promts for adding schedule to the database
