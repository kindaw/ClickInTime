@echo on

REM List of libraries to check and install
set libraries=pyautogui

REM Check and install libraries
for %%i in (%libraries%) do (
    REM Check if the library is installed
    py -c "import %%i" 2>nul
    if errorlevel 1 (
        echo Library "%%i" is not installed. Installing now...
        pip install %%i
    )
)

REM Run the main Python script and log output
py main.py > output.log 2>&1

REM Open the log file
notepad output.log
