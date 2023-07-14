$Email = Read-Host "Please enter your email"
$Password = Read-Host "Please enter your new Password"  -AsSecureString
$id = (az ad user list --upn $Email | Select-String -Pattern "id" | ForEach-Object { $_ -replace '^.*?": "', '' -replace '".*$' }).Trim()
az ad user update --id (Write-Host)$id --password (Write-Host) $Password
echo"Password has been updated"

