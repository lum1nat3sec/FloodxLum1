@echo off
echo Installing required Python modules...

:: Downloading Modules
pip install colorama==0.4.4
pip install requests==2.26.0
pip install termcolor==1.1.0
pip install pyfiglet==0.8.post1

echo Installation complete. 
echo Now Run a Python Script
pause
