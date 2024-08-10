import bpy
from bpy.types import Operator


class InvokeMenuBaseClass:
    @classmethod
    def poll(cls, context):
        space = context.space_data
        return space and space.type == 'NODE_EDITOR'

    def invoke(self, context, event):
        return bpy.ops.wm.call_menu(name=self.menu_id)


class INVOKE_OT_ADD_NODE_ASSET_MENU(InvokeMenuBaseClass, Operator):
    bl_idname = "node.invoke_add_node_asset_menu"
    bl_label = "Add Asset Modifier"
    menu_id = "NODE_MT_add_node_assets"


classes = (
    INVOKE_OT_ADD_NODE_ASSET_MENU,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
