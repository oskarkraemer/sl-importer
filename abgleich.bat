@echo off
REM ### UPDATE SCRIPT ###
.\git\bin\git.exe pull

REM ### DB Code ###

REM "requests" package needed
.\runtime\python-3.11.5.amd64\python.exe .\upload.py

pause