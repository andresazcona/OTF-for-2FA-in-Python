#Counter Based OTF By: https://github.com/andresazcona

import time
import pyotp

key = "CYMKHYS4P6NWFXKGRI2DEC3NFKSI6JMY"

# you need to generate your own key with pyotp.random_base32() #

counter = 0

hotp = pyotp.HOTP(key)

print(hotp.at(1))
print(hotp.at(2))
print(hotp.at(3))
print(hotp.at(4))
print(hotp.at(5))

#counter based OTF will always be the same according to the counter number

for _ in range(5):
    print(hotp.verify(input("Enter Code:"), counter))
    counter += 1

#counter verification will increase wih the counter position