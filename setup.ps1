# PowerShell Script to Set Up AirQualityBackend Outside OneDrive

# Step 1: Define paths
$currentPath = "c:/Users/jayde/OneDrive/Desktop/AirQualityBackend"
$targetPath = "C:\Projects\AirQualityBackend"

# Step 2: Create the target directory if it doesn't exist
if (-not (Test-Path $targetPath)) {
    New-Item -ItemType Directory -Path $targetPath -Force
    Write-Host "Created directory: $targetPath"
} else {
    Write-Host "Directory already exists: $targetPath"
}

# Step 3: Copy all files from current directory to target
Write-Host "Copying files from $currentPath to $targetPath..."
Copy-Item -Path "$currentPath\*" -Destination $targetPath -Recurse -Force
Write-Host "Files copied successfully."

# Step 4: Change to the new directory
Set-Location $targetPath
Write-Host "Changed directory to: $targetPath"

# Step 5: Create virtual environment
Write-Host "Creating virtual environment..."
python -m venv venv
Write-Host "Virtual environment created."

# Step 6: Activate venv and install dependencies
Write-Host "Activating virtual environment and installing dependencies..."
& ".\venv\Scripts\Activate.ps1"
pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic python-dotenv
Write-Host "Dependencies installed."

# Step 7: Run the FastAPI app
Write-Host "Starting FastAPI app on port 8001..."
uvicorn src.main:app --host 0.0.0.0 --port 8001 --reload
