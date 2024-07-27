@echo off
setlocal

REM Path to Python executable
set PYTHON_EXE=C:\Users\Ratch\AppData\Local\Programs\Python\Python312\python.exe

REM List of libraries to check and install
set libraries=pyautogui

REM Check and install libraries
echo Checking and installing libraries...
for %%i in (%libraries%) do (
    echo Checking for %%i...
    "%PYTHON_EXE%" -c "import %%i" 2>nul
    if errorlevel 1 (
        echo Library "%%i" is not installed. Installing now...
        pip install %%i
    ) else (
        echo Library "%%i" is already installed.
    )
)
echo Library check and install complete.

REM Run the main Python script
echo Attempting to run the script with 'py'...
"%PYTHON_EXE%" main.py > output.log 2>&1
if errorlevel 1 (
    echo 'py' failed. Attempting to run the script with 'python3'...
    "%PYTHON_EXE%" main.py >> output.log 2>&1
    if errorlevel 1 (
        echo Both 'py' and 'python3' commands failed. Please check your Python installation. >> output.log
        echo Both 'py' and 'python3' failed. See output.log for details.
    
        exit /b 1
    )
)
echo Script executed successfully.

REM Open the log file
echo Opening log file...
if exist output.log (
    notepad output.log
) else (
    echo No log file created. Check script execution.
)
