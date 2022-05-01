import blender_auto_import_script
import subprocess

from pathlib import Path
from sys import argv, exit

DEBUG = True
BLENDER_COMMAND = r"F:\Apps\Blender\3.1.0\blender.exe"
EMPTY_BLEND_FILE = Path(__file__).parent / Path("Blank.blend")
IMPORT_SCRIPT = Path(__file__).parent / Path("blender_auto_import_script.py")

## Helper functions
def dprint(to_print:str):
	"""Print debug string
	Args:
		 to_print (str): Message to print
	"""
	
	if DEBUG:
		print(f"DEBUG | {__file__} | {to_print}")


## Main
def main():
	## Init
	is_recursive = False
	if "-r" in argv or "--recursive" in argv:
		is_recursive = True
	
	# Get folder to act on
	#folders = []
	#if argv[-1]:
	#	folders.append()
	# else:
	#	folders.append(Path.cwd())
	
	files = []
	folders = [Path.cwd()]
	
	## Search folders
	while(folders):
		current_folder = folders.pop()
		for item in current_folder.iterdir():
			if item.is_file() and blender_auto_import_script.check_if_supported(str(item)):
				files.append(item)
			# if recursive, add folder to folders to search
			elif is_recursive and item.is_dir():
				folders.append(item)
			else:
				pass
	
	for file in files:
		#blender_auto_import.open_3d_file(file)
		command_array = [BLENDER_COMMAND, EMPTY_BLEND_FILE, "--python", IMPORT_SCRIPT, "--", "--auto-import", str(file)]
		# run detached process, dont wait for it to finish
		subprocess.Popen(command_array, shell=True, stdin=None, stdout=None, stderr=None, close_fds=True, creationflags=subprocess.DETACHED_PROCESS)

if __name__ == "__main__":
	main()
	