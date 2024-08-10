import bpy
import importlib


version_tuple = tuple(map(str, bpy.app.version))
version = "." + "_".join(version_tuple[:2])

try:
    version_module = importlib.import_module(version, package=__package__)
except Exception:
    raise NotImplementedError(f"Blender version \"{'.'.join(version_tuple[:2])}\" is not supported.")

classes = (
    *version_module.classes,
    )