import serial

ser = serial.Serial('/dev/ttyS0')
ser.baudrate = 115200
ser.bytesize = 8
ser.parity = 'N'
ser.stopbits = 1
ser.timeout = 1


#ser.flushInput()

a = [0,0,0,0,0,0,0,0,0,0]
for i in range(0,9):
    a[i] = ser.readline().strip()

print(a)
data = [0,0]

for p in range(0,9):
    a[p] = a[p].split(":")
    if a[p][0] == "E0":
        data[0] = int(a[p][1])
    if a[p][0] == "E1":
        data[1] = int(a[p][1])
print (data)
ser.close()
