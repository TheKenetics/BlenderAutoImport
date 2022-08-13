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
Create an environment variable called BLENDER pointing to your favorite Blender.exe  
Change default program for supported formats to `blender_auto_import.bat`  

### Mac
Create an environment variable for Blender  
Add something similar to your `~/.bash_profile`  
```
export BLENDER="open -b org.blenderfoundation.blender --args"
```
Change default program for supported formats to `blender_auto_import.sh`  

### Linux  
Create an environment variable for Blender  
Add something similar to your `~/.bashrc` or `~/.bash_profile`  
```
export BLENDER="/home/ken/AppsFast/Blender/3.1.0/blender"
```
Change default program for supported formats to `blender_auto_import.sh`  

## Using
Double click a 3D file in your OS's file browser and Blender will load an empty file and import the file.  
If you don't see model show up, wait a few seconds. The script has to delay the import or else Blender will crash.  

## How To
### Change Blender Version  
Change the BLENDER environment variable  

### Change the Import Delay
In `blender_auto_import_script.py`  
Change IMPORT_DELAY_SECS to whatever  

### Change Blank.blend file  
Just overwrite it.  


## TODO  
Finish QA Tool  

