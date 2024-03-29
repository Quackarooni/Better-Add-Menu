from bpy.types import Menu

spacing = 0.65

def draw_asset_menu(layout):
    layout.separator()
    layout.menu("NODE_MT_add_node_assets", text="Assets", icon='ASSET_MANAGER')

def add_separator(layout):
    layout.separator(factor=spacing)

class ColumnMenu:
    @staticmethod
    def draw_column(layout, menus):
        col = layout.column()

        for i, menu in enumerate(menus):
            if i > 0:
                col.separator(factor=spacing)

            col.label(text=menu.bl_label)
            col.separator(factor=spacing + 0.15)
            col.menu_contents(menu.bl_idname)
    
        return col

class NODE_MT_add_node_assets(Menu):
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