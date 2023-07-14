#Run the autopass script
#10/07/2023 - 10:44
import subprocess
#Add the file path below
Path = "/usr/bin/bash --noprofile --norc /home/vsts/work/_temp/"
result = subprocess.run(["powershell", Path], capture_output=True, text=True)
print(result.stdout)
