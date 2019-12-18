#!/usr/bin/env python

## This program parses the Serial port of the Raspberry Pi to
# isolate encoder readings at a rate of 200 Hz.
# These readings are then published to the /encoder_data topic.
# The messages are custom "enc_data"
__author__ = "Wanyue Xu, Victor Freire, Rebecca Roembke"
__email__ = "freiremelgiz@wisc.edu"

# Dependencies
import rospy
from latd.msg import enc_data
import serial

## Start serial port object
ser = serial.Serial('/dev/ttyS0')
ser.baudrate = 115200
ser.bytesize = 8
ser.parity = 'N'
ser.stopbits = 1
ser.timeout = 1
# Create custom message object
msg = enc_data()

# Read serial port for encoder data
def read_encoder():
    global ser
    a = [0,0,0,0,0,0,0,0,0,0]
    for i in range(0,9):
        a[i] = ser.readline().strip()
    data = [0,0]
    for p in range(0,9):
        a[p] = a[p].split(":")
        if a[p][0] == "E0":
            data[0] = int(a[p][1]) - initial_enc[0]
        if a[p][0] == "E1":
            data[1] = int(a[p][1]) - initial_enc[1]
    print(data)
    return data

# Offset encoders when starting from != 0
initial_enc = [0,0]
initial_enc = read_encoder()

# Initialize node
rospy.init_node('encoder', anonymous=False)
# Create publisher for encoder data
pub = rospy.Publisher('/encoder_data', enc_data, queue_size = 0)
# Create Rate object
f = 200      # Hz | Rate at which enc_data messages are published
rate = rospy.Rate(f)

# Publishes encoder data continously
def talker():
    while not rospy.is_shutdown():
        enc_arr = read_encoder()
        msg.encLeft = enc_arr[0]
        msg.encRight = -enc_arr[1]
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        # Cleanup serial port
        ser.close()
        pass

