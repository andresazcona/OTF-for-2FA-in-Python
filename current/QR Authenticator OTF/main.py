import time
import pyotp
import qrcode

key = "CYMKHYS4P6NWFXKGRI2DEC3NFKSI6JMY"

# you need to generate your own key with pyotp.random_base32() #

uri = pyotp.totp.TOTP(key).provisioning_uri(name="LuisB777",
                                            issuer_name="TestApp")
#name is equal to the username the qr code will vary between users

print(uri)

qrcode.make(uri).save("totp.png")

