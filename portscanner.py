import nmap
import os
import pyfiglet
from pyfiglet import Figlet
os.system('cls')
ascii = pyfiglet.figlet_format("EASYMAP")
print(ascii)

ip = input("INSERT IP:")
nm = nmap.PortScanner()
x = nm.scan(ip, arguments="-sT")

print('----------------------------------------------------')
print('Host : %s' % ip)
print('State : %s' % nm[ip].state())

for proto in nm[ip].all_protocols():
    print('----------')
    print('Protocol : %s' % proto)
    lport = nm[ip][proto].keys()
    lport.sort()
    for port in lport:
        print ('port : %s\tstate : %s' % (port, nm[ip][proto][port]['state']))