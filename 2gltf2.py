import sys
import bpy
import os

# Update the path for Blender 3.0.1
sys.path.append('/usr/bin/blender')

# Ensure bpy is available
try:
    import bpy
except ImportError as e:
    print("Error importing bpy:", e)
    sys.exit(1)

#   
# Globals
#

#
# Functions
#

current_directory = os.getcwd()

force_continue = True

for current_argument in sys.argv:

    if force_continue:
        if current_argument == '--':
            force_continue = False
        continue

    #

    root, current_extension = os.path.splitext(current_argument)
    current_basename = os.path.basename(root)

    if current_extension != ".abc" and current_extension != ".blend" and current_extension != ".dae" and current_extension != ".fbx" and current_extension != ".obj" and current_extension != ".ply" and current_extension != ".stl" and current_extension != ".usd" and current_extension != ".usda" and current_extension != ".usdc" and current_extension != ".wrl" and current_extension != ".x3d":
        continue

    bpy.ops.wm.read_factory_settings(use_empty=True)
    print("Converting: '" + current_argument + "'")

    #

    if current_extension == ".abc":
        bpy.ops.wm.alembic_import(filepath=current_argument)    

    if current_extension == ".blend":
        bpy.ops.wm.open_mainfile(filepath=current_argument)

    if current_extension == ".dae":
        bpy.ops.wm.collada_import(filepath=current_argument)    

    if current_extension == ".fbx":
        bpy.ops.import_scene.fbx(filepath=current_argument)    

    if current_extension == ".obj":
        bpy.ops.import_scene.obj(filepath=current_argument)    

    if current_extension == ".ply":
        bpy.ops.import_mesh.ply(filepath=current_argument)    

    if current_extension == ".stl":
        bpy.ops.import_mesh.stl(filepath=current_argument)

    if current_extension == ".usd" or current_extension == ".usda" or current_extension == ".usdc":
        bpy.ops.wm.usd_import(filepath=current_argument)

    if current_extension == ".wrl" or current_extension == ".x3d":
        bpy.ops.import_scene.x3d(filepath=current_argument)

    #

    export_file = current_directory + "/" + current_basename + ".gltf"
    print("Writing: '" + export_file + "'")
    bpy.ops.export_scene.gltf(filepath=export_file)
