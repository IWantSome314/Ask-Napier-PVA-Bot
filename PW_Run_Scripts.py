#!/usr/bin/env python3
#Run the autopass script
#10/07/2023 - 11:03
import subprocess
#Add the file path below
Path = "C://Users40017612//Desktop/Scripts//Auto_PW//Auto_Password_Reset.ps1"
result = subprocess.run(["powershell", Path], capture_output=True, text=True)
result = subprocess.call(["powershell", Path])
print(result.stdout)
