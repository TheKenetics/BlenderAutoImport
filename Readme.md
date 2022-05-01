# BlenderAutoImport

Tools to automatically open and import 3D models from OS file browsers.
Have you ever wanted to double click an FBX file and it will automatically open in Blender?
This makes that happen.

## Supports
Made for Blender 3.1, but any should work.  

Supported formats:  
.obj  
.fbx  
.stl  
.abc  
.dae  
.usd  
.ply  
.gltf  
.glb  

## Installing
### Windows
Change default program for supported formats to `blender_auto_import.bat`
### Linux
Change default program for supported formats to `blender_auto_import.sh`

## Using
Double click a 3D file in your OS's file browser and Blender will load an empty file and import the file.
If you don't see model show up, wait a few seconds. The script has to delay the import or else Blender will crash.

## How To
### Change Blender Version
In `blender_auto_import.bat` or `blender_auto_import.sh`  
On the line that sets `BLENDER_COMMAND`, set it to the path to executable for Blender.  
Do not have spaces next to the =  
For .bat it should look like:  
```
set BLENDER_COMMAND=F:\Apps\Blender\3.1.0\blender.exe
```

And for .sh it should look like:  
```
BLENDER_COMMAND=/home/ken/AppsFast/Blender/3.1.0/blender
```

## Change the Import Delay
In `blender_auto_import_script.py`  
Change IMPORT_DELAY_SECS to whatever

## Change Blank.blend file
Just overwrite it.


## TODO
Finish QA Tool  

