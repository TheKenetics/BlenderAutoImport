#!/bin/bash
# Use this to read BLENDER environment var
source ~/.profile

# if blank, something isnt working
echo "$BLENDER"

# Thanks to Claudio Sabato
SCRIPT_DIR=$(cd $(dirname "${BASH_SOURCE[0]}") && pwd)

# $@ gets replaced with args to this bash script
# & at end will fork this command so this script isnt running all the time in the background
"$BLENDER" "$SCRIPT_DIR/Blank.blend" --python "$SCRIPT_DIR/blender_auto_import_script.py" -- --auto-import "$1" &

# for debugging
#sleep 10
