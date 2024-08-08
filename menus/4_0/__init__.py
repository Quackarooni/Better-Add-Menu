from . import node_add_menu_compositor, node_add_menu_geometry, node_add_menu_shader

classes = (
    *node_add_menu_compositor.classes,
    *node_add_menu_geometry.classes,
    *node_add_menu_shader.classes,
)