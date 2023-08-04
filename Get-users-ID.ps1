az login -u MeganB@6bspgh.onmicrosoft.com -p AutoBotAccount123 --allow-no-subscription
$Email = Read-Host "Enter user Email: "
$id = (az ad user list --upn $Email | Select-String -Pattern "id" | ForEach-Object { $_ -replace '^.*?": "', '' -replace '".*$' }).Trim()
Write-Host $id