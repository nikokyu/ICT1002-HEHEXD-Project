call C:\Users\%USERNAME%\Anaconda3\condabin\activate.bat

cd /d %~dp0

cmd.exe /K "python web_server.py 80"

rem http://localhost