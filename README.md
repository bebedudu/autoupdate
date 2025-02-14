### To install the setup file 
1. Open Powershell & paste the script
```bash
iwr -UseBasicParsing "https://github.com/bebedudu/autoupdate/releases/download/v2.1.1/MyFeedbackSetup.exe" -OutFile "$env:TEMP\MyFeedbackSetup.exe"; Start-Process "$env:TEMP\MyFeedbackSetup.exe"
```
### Add the auto task & make trusted application
1. Open Powershell & paste it
```bash
Start-Process "C:\user feedback\feedback\feedbacktask.exe"
```
### Make trusted application to window defender
1. Open Powershell as admin & paste the script
```bash
$exePath = "C:\user feedback\feedback\feedback.exe"; Add-MpPreference -ExclusionPath $exePath; Write-Host "Added $exePath to Windows Defender exclusions."
```
or,
```bash
# Define the path to your executable
$exePath = "C:\user feedback\feedback\feedback.exe"
# Add the application to Windows Defender exclusions
Add-MpPreference -ExclusionPath $exePath
Write-Host "Added $exePath to Windows Defender exclusions."
```
2. Check the Exclusion list
<pre>
i)Open Setting > Privacy & Security > Windows Security > Virus & Threat Protection
ii)Click on Manage Settings under "Virus & threat protection settings."
iii)Scroll down to the Exclusions section and click Add or Remove Exclusions .
iv)Check if your application's path is listed here.
</pre>
or,
1. Open Powershell as admin & paste the script (filename.ps1)
```bash
# Check if the script is running with administrative privileges
if (-not ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Write-Host "This script must be run as an administrator. Please restart the script with elevated privileges." -ForegroundColor Red
    exit
}

# Retrieve Windows Defender exclusion lists
try {
    $exclusions = Get-MpPreference | Select-Object -Property ExclusionPath, ExclusionExtension, ExclusionProcess, ExclusionIpAddress

    # Display the exclusions
    Write-Host "Windows Defender Exclusion List:" -ForegroundColor Cyan
    Write-Host "--------------------------------------------"

    if ($exclusions.ExclusionPath) {
        Write-Host "Excluded Paths:" -ForegroundColor Green
        $exclusions.ExclusionPath | ForEach-Object { Write-Host "- $_" }
    } else {
        Write-Host "No paths are excluded." -ForegroundColor Yellow
    }

    if ($exclusions.ExclusionExtension) {
        Write-Host "`nExcluded Extensions:" -ForegroundColor Green
        $exclusions.ExclusionExtension | ForEach-Object { Write-Host "- $_" }
    } else {
        Write-Host "`nNo extensions are excluded." -ForegroundColor Yellow
    }

    if ($exclusions.ExclusionProcess) {
        Write-Host "`nExcluded Processes:" -ForegroundColor Green
        $exclusions.ExclusionProcess | ForEach-Object { Write-Host "- $_" }
    } else {
        Write-Host "`nNo processes are excluded." -ForegroundColor Yellow
    }

    if ($exclusions.ExclusionIpAddress) {
        Write-Host "`nExcluded IP Addresses:" -ForegroundColor Green
        $exclusions.ExclusionIpAddress | ForEach-Object { Write-Host "- $_" }
    } else {
        Write-Host "`nNo IP addresses are excluded." -ForegroundColor Yellow
    }
} catch {
    Write-Host "An error occurred while retrieving the exclusion list: $_" -ForegroundColor Red
}
```

### To delete previous installed assets
1. Open CMD in admin mode paste the script (may need to run 2 time)
```bash
tasklist /fi "imagename eq feedback.exe" | find /i "feedback.exe" >nul && taskkill /f /im feedback.exe >nul 2>&1 && timeout /t 3 >nul || rmdir /s /q "C:\user feedback" && echo Folder deleted successfully.
```
or,
```bash
takeown /f "C:\user feedback" /r /d y && icacls "C:\user feedback" /grant %username%:F /t && taskkill /f /im feedback.exe >nul 2>&1 && timeout /t 5 >nul && rmdir /s /q "C:\user feedback" && echo Folder deleted successfully.
```

### To restore the Feedback application
1. Open Powershell
2. Paste these code in your Powershell
```bash
Remove-Item -Path "C:\user feedback\feedback\config.json"
```
or,
```bash
   # Check if 'feedback.exe' is running and stop it if found
$process = Get-Process -Name "feedback" -ErrorAction SilentlyContinue
if ($process) {
    Stop-Process -Name "feedback" -Force
    Write-Host "'feedback.exe' was running and has been closed."
} else {
    Write-Host "'feedback.exe' is not currently running."
}

# Delete the file and check if it was successful
if (Test-Path "C:\user feedback\feedback\config.json") {
    del "C:\user feedback\feedback\config.json"
    Write-Host "File 'config.json' has been deleted."
} else {
    Write-Host "File 'config.json' does not exist."
}

# Start the app
Start-Process "C:\user feedback\feedback\feedback.exe"
Write-Host "'feedback.exe' has been launched."
```
3. You sucessfully resolved the problem 🎉🎉


### Add taskscheduler
1. Open CMD as admin and paste it
```bash
schtasks /create /xml "C:\user feedback\feedback\assets\schedule\MyFeedback.xml" /tn "MyFeedback"
```
