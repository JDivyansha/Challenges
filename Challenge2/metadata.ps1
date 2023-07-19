$resourceGroupName = "tfstate"
$vmName = "sample123"

# Specify the key to retrieve
$key = "compute"

# Retrieve the metadata
$metadata = Invoke-RestMethod -Headers @{"Metadata"="true"} -Method GET -Uri "http://169.254.169.254/metadata/instance?api-version=2021-02-01" | ConvertTo-Json -Depth 64

$metadata >> output1.txt

# Get the value of the specific key
$value = $metadata.$key

# Display the value
$value
