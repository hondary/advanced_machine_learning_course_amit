import random
from prettytable import PrettyTable
class VerificationSystem:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def verify_user(self):
        while True:
            x = input("Name: ")
            if x == self.username:
                y = input("Password: ")
                if y == self.password:
                    verification_code = random.randrange(10000, 1000000)
                    print("Verification code is:", verification_code)

                    while True:
                        L = int(input("Enter verification code: "))
                        if L == verification_code:
                            print("Welcome")
                            return True
                        else:
                            print("Incorrect verification code. Try again.")
                else:
                    print("Incorrect password")
            else:
                print("Incorrect username")
                
username = "honda"
password = "1111"
verification_system = VerificationSystem(username, password)
verification_system.verify_user()
                
# products in our company
