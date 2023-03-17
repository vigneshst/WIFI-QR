import pyqrcode
from pyqrcode import QRCode
from PIL import Image
import os
import subprocess
# network profile list
y=int(input('1.Linux\n2.windows \nChoose OS:'))
if y==1:
    os.system(" sudo ls /etc/NetworkManager/system-connections/ ")
    # Getting user input
    x = input('choose network:')
    # Create QR code
    url = pyqrcode.create(f'{str(subprocess.check_output(f"sudo cat /etc/NetworkManager/system-connections/{x}| grep ssid= ",shell=True))[2:-3]}\n{str(subprocess.check_output(f"sudo cat /etc/NetworkManager/system-connections/{x}| grep psk=",shell=True))[2:-3]}')
    # Create and save the svg file naming "myqr.svg"
    url.svg("myqr.svg", scale = 8)
    # Create and save the png file naming "myqr.png"
    a = url.png('myqr.png', scale = 6)
    img = Image.open("myqr.png")
    img.show()
elif y==2:
    os.system("Netsh wlan show profile")
    ssid=input("Enter newtorks:")
    key = str((str(subprocess.check_output(f'Netsh wlan show profile name={ssid} key=clear | find "SSID name"',shell=True))[2:-5].replace(' ',''),str(subprocess.check_output(f'Netsh wlan show profile name={ssid} key=clear | find "Key Content"',shell=True))[2:-5].replace(' ','')))
    
    url = pyqrcode.create(key)
    url.svg("myqr.svg", scale = 8)
    # Create and save the png file naming "myqr.png"
    a = url.png('myqr.png', scale = 6)
    img = Image.open("myqr.png")
    img.show()

else:
    print('choose correctly')
