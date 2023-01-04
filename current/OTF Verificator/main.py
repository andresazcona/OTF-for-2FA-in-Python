#OTF Verificator By: https://github.com/andresazcona

import time
import pyotp
import qrcode

key = "CYMKHYS4P6NWFXKGRI2DEC3NFKSI6JMY"

totp = pyotp.TOTP(key)

while True:
    print(totp.verify(input("Enter Code:")))

