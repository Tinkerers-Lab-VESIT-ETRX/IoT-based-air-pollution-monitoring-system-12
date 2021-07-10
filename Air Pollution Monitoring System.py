import serial
from firebase import firebase
from time import sleep
from datetime import datetime
import serial.tools.list_ports


ports = serial.tools.list_ports.comports()
for port, desc, hwid in sorted(ports):
        print("{}: {} [{}]".format(port, desc, hwid))


ser = serial.Serial("COM2", 9600)
print(ser.readline())
res =1
i=0
time=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
print(time)

while res:
     firebase1 = firebase.FirebaseApplication('https://air-pollution-monitoring-9687d-default-rtdb.asia-southeast1.firebasedatabase.app/', None)
     
     for i in range(0,9):
             string1=str(ser.readline())
             string1=string1[14:][:8]
             data =  { 'date': datetime.now().strftime("%Y-%m-%d"),
               'reading':string1,
               'time': datetime.now().strftime("%H:%M")               
          }
             result = firebase1.patch('https://air-pollution-monitoring-9687d-default-rtdb.asia-southeast1.firebasedatabase.app/'+ '/AQ_Level_in_ppm/'+ str(i), data)
             print(result)
             
             string1=str(ser.readline())
             string1=string1[24:][:13]
             data =  { 'date': datetime.now().strftime("%Y-%m-%d"),
               'reading':string1,
               'time': datetime.now().strftime("%H:%M")               
          }
             result = firebase1.patch('https://air-pollution-monitoring-9687d-default-rtdb.asia-southeast1.firebasedatabase.app/'+ '/AQ_Level/'+ str(i), data)
             print(result)
             
             
     res=0
     
