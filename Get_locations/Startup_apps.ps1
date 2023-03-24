$outputFile = "C:\users\tester\Desktop\output_basic_run_key.txt"
#output file where the startup app locations are stored

# Check the HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run key for startup programs
$runKeyPath = "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run"
$runKeyValues = Get-ItemProperty -Path $runKeyPath
Write-Output "Programs set to run automatically at startup (HKLM):"
foreach ($value in $runKeyValues.PSObject.Properties) {
    try
    {
        Write-Output $value.Name
        Write-Output $value.Value
        if ($value.Value -like "*.exe"){
            Add-Content -Path $outputFile -Value $value.value
            }
    }catch
    {
        Write-Warning "Error checking key "
    }
}
# Check the HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Runonce key for startup programs
$runonceKeyPath = "HKLM:\Software\Microsoft\Windows\CurrentVersion\RunOnce"
$runonceKeyValues = Get-ItemProperty -Path $runKeyPath
#Write-Output "Programs set to run automatically at startup (HKLM):"
foreach ($value in $runonceKeyValues.PSObject.Properties) {
    try
    {
        Write-Output $value.Name
        Write-Output $value.Value
        if ($value.Value -like "*.exe"){
            Add-Content -Path $outputFile -Value $value.value
            }
    }catch
    {
        Write-Warning "Error checking key "
    }
}


# Check the HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run key for user-specific startup programs
$currentUserRunKeyPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run"
$currentUserRunKeyValues = Get-ItemProperty -Path $currentUserRunKeyPath
Write-Output "Programs set to run automatically at user logon (HKCU):"
foreach ($value in $currentUserRunKeyValues.PSObject.Properties) {
    try
    {
        Write-Output $value.Name
        Write-Output $value.Value
        if ($value.Value -like "*.exe"){
            Add-Content -Path $outputFile -Value $value.value
            }
    }catch
    {
        Write-Warning "Error checking key "
    }
}
# Check the HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run key for startup programs
$currentuserrunonceKeyPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Runonce"
$currentuserrunonceKeyValues = Get-ItemProperty -Path $currentuserrunonceKeyPath
#Write-Output "Programs set to run automatically at startup (HKCU):"
foreach ($value in $currentuserrunonceKeyValues.PSObject.Properties) {
    try
    {
        Write-Output $value.Name
        Write-Output $value.Value
        if ($value.Value -like "*.exe"){
            Add-Content -Path $outputFile -Value $value.value
            }
    }catch
    {
        Write-Warning "Error checking key "
    }
}

#Try to generate the above using a for loop, iterating through the run registry entries
