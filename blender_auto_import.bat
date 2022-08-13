@echo off

rem "%~dp0" This gets replaced with folder path to this script with \ at end
rem %* is all args to this script
rem %1 is first arg to this script

start %BLENDER% %~dp0Blank.blend --python %~dp0blender_auto_import_script.py -- --auto-import %1

