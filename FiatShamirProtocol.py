import random
from Crypto.Util.number import *


class FiatShamirProtocol:
    def __init__(self):
        self.p = getPrime(15)
        self.q = getPrime(15)
        self.n = self.p * self.q
        self.secret = bytes_to_long(b"Secret")

    def getPublicKey(self):
        return pow(self.secret, 2, self.n)

    def getCertification(self, iterations):
        for i in range(iterations):
            r = random.randint(1, self.n - 1)
            x = pow(r, 2, self.n)
            a = random.randint(0, 1)
            y = (r * (self.secret ** a)) % self.n
            print(f"y^2 mod n = {pow(y, 2, self.n)}")
            print(f"(x * (public_key ** a)) % n = {(x * (self.getPublicKey() ** a)) % self.n}")
            if pow(y, 2, self.n) == (x * (self.getPublicKey() ** a)) % self.n:
                print("Success")
            else:
                print("Failed")
                exit()
            print("------------------------")
        print("Proven")


FiatShamirProtocol().getCertification(3)
