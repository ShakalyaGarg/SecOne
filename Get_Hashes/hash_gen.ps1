# Set input and output file paths
$inputFilePath = "C:\Users\Nishchhal\Desktop\KAVACH\Get_locations\All_aps.txt"
$outputFilePath = "C:\Users\Nishchhal\Desktop\KAVACH\Get_hash\Hashes.txt"

# Read input file and loop through each line
Get-Content $inputFilePath | ForEach-Object {
    # Remove any leading or trailing whitespace
    $location = $_.Trim()

    # Generate SHA256 hash for application file
    $hash = Get-FileHash -Algorithm SHA256 $location | Select-Object -ExpandProperty Hash

    # Write hash to output file
    echo $hash
    Add-Content -Path $outputFilePath -Value $hash
}
