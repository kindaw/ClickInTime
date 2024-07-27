@echo off
setlocal

REM Change to the directory where the batch file is located
cd /d "%~dp0"

REM Attempt to use 'py' first
set PYTHON_CMD=py

REM If 'py' is not available, try 'python' or 'python3'
where %PYTHON_CMD% >nul 2>nul
if errorlevel 1 (
    set PYTHON_CMD=python
    where %PYTHON_CMD% >nul 2>nul
    if errorlevel 1 (
        set PYTHON_CMD=python3
        where %PYTHON_CMD% >nul 2>nul
        if errorlevel 1 (
            echo Python executable not found. Please install Python or check your PATH.
        
            exit /b 1
        )
    )
)

REM Path to Python script (relative path)
set SCRIPT_PATH=main.py

REM List of libraries to check and install
set libraries=pyautogui

REM Check and install libraries
echo Checking and installing libraries...
for %%i in (%libraries%) do (
    echo Checking for %%i...
    "%PYTHON_CMD%" -c "import %%i" 2>nul
    if errorlevel 1 (
        echo Library "%%i" is not installed. Installing now...
        pip install %%i
    ) else (
        echo Library "%%i" is already installed.
    )
)
echo Library check and install complete.

REM Run the main Python script
echo Attempting to run the script with '%PYTHON_CMD%'...
"%PYTHON_CMD%" "%SCRIPT_PATH%" > output.log 2>&1
if errorlevel 1 (
    echo Failed to run the script. Check output.log for details.

    exit /b 1
)
echo Script executed successfully.

REM Open the log file
echo Opening log file...
if exist output.log (
    notepad output.log
) else (
    echo No log file created. Check script execution.
)
