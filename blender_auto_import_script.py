import bpy

from sys import argv
from pathlib import Path
import functools


## Globals
# On Windows, with some files, Blender would mysteriously crash with no error
# No problems with the same files on Linux Mint
# But after adding a delay to import the files, it seems to be fixed
# Guessing that this script is trying to use things that haven't loaded yet
# And if you have a bunch of addons enabled in your preferences, Blender takes longer to load the important stuff
# If you get crashes with no errors, try increasing the delay
IMPORT_DELAY_SECS = 2.0

SUPPORTED_FILE_TYPES = {
	".obj" : bpy.ops.import_scene.obj,
	".fbx" : bpy.ops.import_scene.fbx,
	".stl" : bpy.ops.import_mesh.stl,
	".abc" : bpy.ops.wm.alembic_import,
	".dae" : bpy.ops.wm.collada_import,
	".usd" : bpy.ops.wm.usd_import,
	".ply" : bpy.ops.import_mesh.ply,
	".gltf": bpy.ops.import_scene.gltf,
	".glb" : bpy.ops.import_scene.gltf
}


## Helper Functions
def check_if_supported(file_path):
	for key in SUPPORTED_FILE_TYPES.keys():
		if file_path.name.lower().endswith(key):
			return True
	
	return False

def get_import_command(file_path):
	for key in SUPPORTED_FILE_TYPES.keys():
		if file_path.name.lower().endswith(key):
			return SUPPORTED_FILE_TYPES[key]
	
	print("Error: can't support", file_path)
	return None


## Main
def main():
	print(argv)
	# get value after "--auto-import"
	file_path = Path( argv[argv.index("--auto-import")+1] )
	
	import_command = get_import_command(file_path)
	
	if import_command:
		#import_command(filepath=str(file_path))
		# Delay so that Blender can totally load
		bpy.app.timers.register(
			functools.partial( import_command, filepath=str(file_path) ),
			first_interval=IMPORT_DELAY_SECS
		)
	else:
		print("No command to run", file_path)


if __name__ == "__main__":
	main()
