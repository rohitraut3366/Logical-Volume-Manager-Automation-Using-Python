import getpass
import subprocess

from LVM_features import authTypeKey, authTypePass

password = getpass.getpass()
if password != "1":
    exit()

# Installing sshpasss software


# Getting Operating System Information
ipAddress = input("Enter IP of target System :")
username = input("UserName: ")
auth_type = input("Enter Authentication type-->  [key/password] : ")

if auth_type.lower() == "key":
    key_path = input("Enter key path from base directory: ")
    authTypeKey(username, key_path, ipAddress)
elif auth_type.lower() == "password" or auth_type.lower() == "pass":
    print("Setting Up environment please wait")
    subprocess.getoutput("yum install sshpass -y")
    password = input("Enter password: ")
    authTypePass(username, password, ipAddress)
else:
    print("Not Valid")
    exit()

