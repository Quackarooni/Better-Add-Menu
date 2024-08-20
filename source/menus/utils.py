from bpy.types import Menu
from bl_ui.node_add_menu import add_node_type

from ..utils import fetch_user_preferences

spacing = 0.65

def draw_asset_menu(layout):
    mode = fetch_user_preferences("show_asset_nodegroups") 
    layout.separator()

    if mode == "TOP_LEVEL":
        layout.menu_contents("NODE_MT_add_node_assets")
    elif mode == "SUBMENU":
        layout.menu("NODE_MT_add_node_assets", text="Assets", icon='ASSET_MANAGER')

def add_separator(layout):
    layout.separator(factor=spacing)

def draw_node_group_add_menu(context, layout):
    """Add items to the layout used for interacting with node groups."""
    space_node = context.space_data
    node_tree = space_node.edit_tree
    all_node_groups = context.blend_data.node_groups

    if node_tree in all_node_groups.values():
        layout.separator()
        add_node_type(layout, "NodeGroupInput")
        add_node_type(layout, "NodeGroupOutput")

    if not node_tree:
        return
    
    from nodeitems_builtins import node_tree_group_type

    groups = [
        group for group in context.blend_data.node_groups
        if (group.bl_idname == node_tree.bl_idname and
            not group.contains_tree(node_tree) and
            not group.name.startswith('.'))
    ]
    
    if len(groups) <= 0:
        layout.separator()
        layout.label(text="No nodegroups available.")
    else:
        layout.separator()
        for group in groups:
            props = add_node_type(layout, node_tree_group_type[group.bl_idname], label=group.name)
            ops = props.settings.add()
            ops.name = "node_tree"
            ops.value = "bpy.data.node_groups[%r]" % group.name

class ColumnMenu:
    @staticmethod
    def draw_column(layout, menus):
        col = layout.column()

        for i, menu in enumerate(menus):
            if i > 0:
                col.separator(factor=spacing)

            icon = getattr(menu, "header_icon", "NONE")
            col.label(text=menu.bl_label, icon=icon)
            col.separator(factor=spacing + 0.15)
            col.menu_contents(menu.bl_idname)
    
        return col

class NODE_MT_add_node_assets(Menu):
    bl_idname = __qualname__
    bl_label = "Add Asset"
    bl_space_type = 'NODE_EDITOR'
    bl_options = {'SEARCH_ON_KEY_PRESS'}

    @classmethod
    def poll(cls, context):
        space = context.space_data

        is_existing = space.node_tree is not None
        is_node_editor = space.type == "NODE_EDITOR"

        return all((is_existing, is_node_editor))

    def draw(self, context):
        layout = self.layout

        if layout.operator_context == 'EXEC_REGION_WIN':
            layout.operator_context = 'INVOKE_REGION_WIN'
            layout.operator("WM_OT_search_single_menu", text="Search...", icon='VIEWZOOM').menu_idname = "NODE_MT_node_add_root_catalogs"
            layout.separator()

        layout.operator_context = 'INVOKE_REGION_WIN'
        layout.menu_contents("NODE_MT_node_add_root_catalogs")