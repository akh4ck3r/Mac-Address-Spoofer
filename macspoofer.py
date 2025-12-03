import subprocess
import re

subprocess.run(["ifconfig"])

networkInterfacname = input("Enter Network InterFace Name: ")
print("\n")

#-------MAC Validation-------
def validate_mac(user_input):
    # Regex: 6 groups of 2 alphanumeric chars separated by 5 colons
    pattern = r'^[A-Za-z0-9]{2}(:[A-Za-z0-9]{2}){5}$'

    if re.match(pattern, user_input):
        return True
    else:
        return False

# ----- Main Program -----
mac = input("Enter new MAC Address: ")

if validate_mac(mac):
    print("MAC Address string format is Valid!\n")
else:
    print("MAC Address string format is Invalid!")

subprocess.run(["macchanger", "-m", mac, networkInterfacname])
print("\n")
subprocess.run(["macchanger", "-m", mac, networkInterfacname])

print("\n")
print('* * * * * * * * * * * * * * * * *')
print('* MAC address has been changed! *')
print('* * * * * * * * * * * * * * * * *')



