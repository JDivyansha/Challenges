
 # Get Matadata of an Azure Instance

## Process 1: By Logging into the VM
### A). Get whole metadata details
#### Step1
Login the specific VM.
#### Step 2
Open Powershell.exe
#### Step 3
Run following commands: 

    a.	$resourceGroupName = "tfstate" 
    b.	$vmName = "sample123"
    c.	$metadata = Invoke-RestMethod -Headers @{"Metadata"="true"} -Method GET -Uri "http://169.254.169.254/metadata/instance?api-version=2021-02-01" | ConvertTo-Json -Depth 64
    d.	$metadata >> output1.txt (Store it in a output file)

#### Step 4
Open output1.txt. (It includes the whole metadata).

### B) Get Metadata based on specific key.

#### Step1
Login the specific VM.
#### Step 2
Open Powershell.exe
#### Step 3
Run following commands:  

    a.	$resourceGroupName = "tfstate"
    b.	$vmName = "sample123"
    c.	$key = "name"
    d.	$uri = "http://169.254.169.254/metadata/instance/compute/" + $key + "?api-version=2021-02-01&format=text"
    e.	$metadata = Invoke-RestMethod -Headers @{"Metadata"="true"} -Method GET -Uri $uri
    $metadata >> keymetadata.txt
#### Step 4
Open keymetadata.txt (It includes the specific metadata based on the key provided).

### Process 2: From Portal
#### Step 1. Open Azure portal -> Go to VM -> Left Panel -> Run Commands 
#### Step 2. Run the same commands mentioned above.
#### Step 3. Get Output file from VM

       Or


#### Step 1. Create a custom extensions for the VM

    a.	Open Azure Portal
    b.	Go the VM
    c.	Select Extensions and Application from Left Panel.
    d.	Add a new extension.
    e.	Select Custom Script Extension.
    f.	Click next and add the powershell script (with the same commands mentioned above).
    g.	Open Cloudshell 
        a.	Specify the resource group and virtual machine name
            i.	$resourceGroupName = "tfstate"
            ii.	$vmName = "sample123"

        b.	# Get the virtual machine
            i.	$vm = Get-AzVM -ResourceGroupName $resourceGroupName -Name $vmName -Status

        c.	# Retrieve the metadata
            i.	$metadata = $vm.Extensions | Where-Object {$_.Publisher -eq 'Microsoft.Compute' -and $_.Type -eq 'microsoft.compute/virtualmachines/extensions'}

        d.	# Display the metadata
            i.	$value = $metadata.PublicSettings | ConvertFrom-Json









