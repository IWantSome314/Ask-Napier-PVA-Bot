param (
    [string]$combinedArgs
)

# Parse the combined arguments to get password and email
$password, $email = $combinedArgs -split '\|\|\|'

# PowerShell code to use the password and email values
Write-Output "Received password: $password"
Write-Output "Received email: $email"
Write-Output "Email variable: $email"

# Login to Azure
az login -u $email -p $password --allow-no-subscription

# Get the user information using the az ad user show command
#$user = az ad user show --upn $email

if (-not $email) {
    Write-Output "Email argument is missing or empty."
}
    # Get the user ID from the user information
    #$id = $user | Select-Object -ExpandProperty id
$id = (az ad user list --upn $email | Select-String -Pattern "id" | ForEach-Object { $_ -replace '^.*?": "', '' -replace '".*$' }).Trim()

    # Check if the user ID is empty or not
    if ([string]::IsNullOrWhiteSpace($id)) {
        Write-Output "User with email $email not found. Please check the email address."
    }
    else {
        # Update the user's password using the retrieved ID
        az ad user update --id $id --password $password
        Write-Output "Your Password has been updated"
    }

