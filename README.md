# break-reminder

We all know sitting too long is bad for our health, and doctors suggest we should at least leave the desk for a short break every 50 minutes or an hour.

Working as a software engineer, the norm is sitting at a desk all day and coding. I have checked some break reminders readily available, and most of them are in the form of mobile apps, which require manually starting the timer every time.

This project aims to solve this issue by running the tracking service on Raspberry Pi, which requires no manual input once the initial setup is completed.

## steps for setup hardware

- by default, this program use gpio pin 17 to control the indicator led
- please connect your led, along with 100Ω resistor to pin 17 and ground
- to check which pins are 17 and ground, [please refer to this file](https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering)
- connect the camera module to Raspberry Pi
- position the camera so it can detect front of your face

## steps for setup Python3 on Raspberry Pi

- Raspberry PI 4 came with python3 pre-installed
- Open terminal and run *pip3 install opencv-python*
- Install dependent library by running *sudo apt-get install -y libatlas-base-dev libhdf5-dev libhdf5-serial-dev libatlas-base-dev libjasper-dev  libqtgui4  libqt4-test*
- Press windows key on keyboard to open Raspberry pi menu, click preference -> Raspberry PI configuration -> interfaces -> enable camera (need to reboot)
- Run *wget https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml*
- The xml file is the pretrained face detection model for opencv, please move it to */home/pi* folder
- Download main.py and detector.py in this github, and move them to */home/pi* folder

## run the program

- open terminal
- run command *python3 main.py*

## hardware shopping list for this project
- [Raspberry pi](https://www.pishop.us/product/raspberry-pi-4-model-b-2gb/)
- [camera module](https://www.pishop.us/product/raspberry-pi-camera-module-v2/)
- [camera mount](https://www.pishop.us/product/adjustable-raspberry-pi-camera-mount-protector/)
- [electronics kit](https://www.pishop.us/product/electronic-starter-kit-for-raspberry-pi/)

## limitation of version 0.1 of the project

- The camera is only able to detect front of the face, we will add support for other detection models soon
