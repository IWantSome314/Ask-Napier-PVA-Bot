#Run the autopass script
#10/07/2023 - 10:44
import subprocess
#Add the file path below
Path = "C:/Users/Hamish/Desktop/PVAAuto/Auto_Password_Reset.ps1"
result = subprocess.run(["powershell", Path], capture_output=True, text=True)
print(result.stdout)
