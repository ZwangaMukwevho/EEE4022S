# Automated Temperature Detection and Attendance Register System

.. image:: https://readthedocs.org/projects/smartFileDemo/badge/?version=latest
        :target: https://eee4022s.readthedocs.io/en/latest/index.html
        :alt: Documentation Status

This is the repository contains all the code that was used to create the Automated Temperature Detection and Attendance Register System. The system can be interfaced with using the hardware modules from the physical system itself, and the user interfacing system that makes use of a **Command Line Interface (CLI)** and **Google Sheets**

INSTALLING DEPENDENCIES
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
