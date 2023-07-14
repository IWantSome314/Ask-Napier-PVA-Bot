#Run the autopass script
#14/07/2023 - 16:00
import subprocess
#Add the file path below
Path = "/home/GitHub/AutoPW/AutoPass/Auto_Password_Reset.ps1"
result = (subprocess.run(["powershell", Path], capture_output=True, text=True))
print(result.stdout)
