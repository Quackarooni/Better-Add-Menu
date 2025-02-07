from . import node_add_menu_compositor, node_add_menu_geometry, node_add_menu_shader
from ..utils import NODE_MT_add_node_assets

classes = (
    *node_add_menu_compositor.classes,
    *node_add_menu_geometry.classes,
    *node_add_menu_shader.classes,
    NODE_MT_add_node_assets,
)