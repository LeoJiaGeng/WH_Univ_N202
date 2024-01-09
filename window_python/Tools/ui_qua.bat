@echo off
mode con cols=50 lines=50

set PY_NAME=ui_Quatum.py
set UI_NAME=ui_quatum.ui
set WORKPATH=%~dp0..\Demo

call pyuic5.exe -o %WORKPATH%\%PY_NAME% %WORKPATH%\%UI_NAME%

if %ERRORLEVEL% == 1 goto MultiFiles
echo ui file has been converted 
exit

:MultiFiles
@echo ERR
pause
exit
