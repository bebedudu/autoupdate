@echo off

REM Check if feedback.exe is running and close it if found
tasklist /FI "IMAGENAME eq feedback.exe" 2>NUL | find /I "feedback.exe">NUL
if not errorlevel 1 (
    echo feedback.exe is running, closing it...
    taskkill /F /IM feedback.exe
) else (
    echo feedback.exe is not running.
)

REM Delete the config.json file
if exist "C:\user feedback\feedback\config.json" (
    echo Deleting config.json...
    del "C:\user feedback\feedback\config.json"
) else (
    echo config.json does not exist.
)

REM Start feedback.exe
echo Launching feedback.exe...
start "" "C:\user feedback\feedback\feedback.exe"
