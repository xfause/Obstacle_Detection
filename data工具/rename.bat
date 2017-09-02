@echo off&setlocal EnableDelayedExpansion 
set a=1 
for /f "delims=" %%i in ('dir /b *.jpg') do ( 
if not "%%~ni"=="%~n0" ( 
if !a! LSS 10 (ren "%%i" "positive_0!a!.jpg") else ren "%%i" "positive_!a!.jpg" 
set/a a+=1 
) 
)