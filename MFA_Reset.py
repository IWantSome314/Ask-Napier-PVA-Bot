import subprocess



#-------------------------------------------------------
def get_user_input():
    email = input("Please enter your Email: ")
    return email

if __name__ == "__main__":
    email_input = get_user_input()
    script_path = r'C:\Users\40017612\Desktop\Scripts\Auto_PW\MFA_Reset.ps1'
    
    # Run the PowerShell script as a subprocess using the -Command parameter
    powershell_command = f'& "{script_path}" -email "{email_input}"'
    subprocess.run(["powershell.exe", "-ExecutionPolicy", "Unrestricted", "-Command", powershell_command])
#-------------------------------------------------------

