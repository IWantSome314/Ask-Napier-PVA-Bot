#Run the autopass script
#24/07/2023 - 9:40
import subprocess
#Add the file path below
Path = "/home/GitHub/AutoPW/AutoPass/Auto_Password_Reset.ps1"
#result = (subprocess.run(["powershell", Path], capture_output=True, text=True))
result = subprocess.call([Path])
print(result.stdout)
