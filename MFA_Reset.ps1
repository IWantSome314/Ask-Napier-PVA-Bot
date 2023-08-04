#param(
    #[string]$email
#)

#Write-Output "Received email: $email"
#Write-Output "Email variable: $email"

$userUPN = gradya@6bspgh.onmicrosoft.com #$email

$id = (az ad user list --upn $email | Select-String -Pattern "id" | ForEach-Object { $_ -replace '^.*?": "', '' -replace '".*$' }).Trim()
Write-Host $id

#Write-Output "Email: $email"
Write-Output "UserUPN: $userUPN"
Write-Output "Object ID: $id"

# Replace <user_object_id> with the Object ID obtained in the previous step.
# Replace <user_object_id> with the Object ID obtained earlier.
$user_object_id = $id

# Define the JSON payload for strongAuthenticationRequirements
$jsonPayload = @'
[
    {
        "@odata.type": "microsoft.graph.authenticationRequirement",
        "name": "mfa"
    }
]
'@

# Convert the JSON payload to a string and escape double quotes
$escapedJsonPayload = $jsonPayload -replace '"', '\"'

# Form the Azure CLI command using PowerShell variables
$command = "az ad user update --id "" $id "" --set ""strongAuthenticationRequirements=$escapedJsonPayload"""

# Execute the Azure CLI command
Invoke-Expression -Command $command


#az ad user update --id $id --add strongAuthenticationMethods mfa