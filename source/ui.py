import bpy

from bl_ui import node_add_menu_geometry, node_add_menu_shader, node_add_menu_compositor
from . import menus

built_in_menus = (
    *node_add_menu_compositor.classes, 
    *node_add_menu_geometry.classes, 
    *node_add_menu_shader.classes
    )


def register():
    for cls in built_in_menus:
        if hasattr(bpy.types, cls.__name__):
            bpy.utils.unregister_class(cls)

    for cls in menus.classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in menus.classes:
        if hasattr(bpy.types, cls.__name__):
            bpy.utils.unregister_class(cls)

    for cls in built_in_menus:
        bpy.utils.register_class(cls)