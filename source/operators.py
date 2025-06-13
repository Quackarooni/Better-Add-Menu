import bpy
from bpy.types import Operator
from bl_operators.node import NodeAddOperator


class InvokeMenuBaseClass:
    @classmethod
    def poll(cls, context):
        space = context.space_data
        return space and space.type == 'NODE_EDITOR'

    def invoke(self, context, event):
        return bpy.ops.wm.call_menu(name=self.menu_id)


class INVOKE_OT_ADD_NODE_ASSET_MENU(InvokeMenuBaseClass, Operator):
    bl_idname = "node.invoke_add_node_asset_menu"
    bl_label = "Add Asset Nodegroup"
    menu_id = "NODE_MT_add_node_assets"


class NODE_OT_bt_add_empty_group(NodeAddOperator, bpy.types.Operator):
    bl_idname = "node.bt_add_empty_group"
    bl_label = "New Group"
    bl_description = "Add a group node with an empty group"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        from nodeitems_builtins import node_tree_group_type
        tree = context.space_data.edit_tree
        group = self.create_empty_group(tree.bl_idname)
        self.deselect_nodes(context)
        node = self.create_node(context, node_tree_group_type[tree.bl_idname])
        node.node_tree = group
        return {"FINISHED"}

    @staticmethod
    def create_empty_group(idname):
        group = bpy.data.node_groups.new(name="NodeGroup", type=idname)
        input_node = group.nodes.new('NodeGroupInput')
        input_node.select = False
        input_node.location.x = -200 - input_node.width

        output_node = group.nodes.new('NodeGroupOutput')
        output_node.is_active_output = True
        output_node.select = False
        output_node.location.x = 200
        return group


classes = (
    INVOKE_OT_ADD_NODE_ASSET_MENU,
    NODE_OT_bt_add_empty_group,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
