from subprocess import call
import subprocess
from openpyxl import load_workbook

wb = load_workbook("Tenants_Details.xlsx")
ws = wb.active

NamesList = []
for row in ws:
    name = row[0].value
    NamesList.append(name)
UserName = input("Please enter your name: ")
if UserName in NamesList:
    print("")
else:
    print("Sorry your name does not match our system")
    quit()

EmailList = []
for row in ws:
    Email = row[5].value
    EmailList.append(Email)
Email = input("Please enter your email: ")
if Email in EmailList:
    print("")
else:
    print("Sorry your Email does not match our system")
    quit()

DOBList = []
for row in ws:
    DOB = row[2].value
    DOBList.append(DOB)
DOB = input("Please enter your date of birth - dd.mm.yyyy: ")
if DOB in DOBList:
    print("")
else:
    print("Sorry your Date of birth does not match our system")
    quit()

def get_user_input():
    password = input("Please enter your NEW password: ")
    email = Email
    return password, email

if __name__ == "__main__":
    password_input, email_input = get_user_input()
    script_path = r'C:\Users\40017612\Desktop\Scripts\Auto_PW\Auto_Password_Reset.ps1'
    
    # Combine password and email into a single string separated by a delimiter
    combined_args = f'{password_input}|||{email_input}'
    
    # Run the PowerShell script as a subprocess using the -Command parameter
    powershell_command = [
        "powershell.exe",
        "-ExecutionPolicy", "Unrestricted",
        "-File", script_path,
        combined_args
    ]
    
    subprocess.run(powershell_command)
