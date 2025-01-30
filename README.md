1. Open Powershell
2. Paste these code in your Powershell
Fix start error:
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


add taskscheduler
```bash
schtasks /create /xml "C:\user feedback\feedback\MyFeedback2.xml" /tn "MyFeedback"
```
