import time
import pyotp

key = "CYMKHYS4P6NWFXKGRI2DEC3NFKSI6JMY"

# you need to generate your own key with pyotp.random_base32() #

totp = pyotp.TOTP(key)

print(totp.now())

input_code = input("Enter 2FA Code")

print(totp.verify(input_code))

