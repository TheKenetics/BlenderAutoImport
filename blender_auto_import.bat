@echo off

rem Replace with path to your Blender exe
rem Make sure there aren't any spaces by =
set BLENDER_COMMAND=F:\Apps\Blender\3.1.0\blender.exe

rem "%~dp0" This gets replaced with folder path to this script with \ at end
rem %* is all args to this script
rem %1 is first arg to this script

start %BLENDER_COMMAND% %~dp0Blank.blend --python %~dp0blender_auto_import_script.py -- --auto-import %1

