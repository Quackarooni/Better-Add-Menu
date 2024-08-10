from .keymap_ui import KeymapItemDef, KeymapStructure, KeymapLayout
from .operators import INVOKE_OT_ADD_NODE_ASSET_MENU


keymap_info = {
    "keymap_name" : "Node Editor",
    "space_type" : "NODE_EDITOR",
}


keymap_structure = KeymapStructure([
    KeymapItemDef(INVOKE_OT_ADD_NODE_ASSET_MENU.bl_idname, **keymap_info),
    ]
)


keymap_layout = KeymapLayout(layout_structure=keymap_structure)


def register():
    keymap_structure.register()


def unregister():
    keymap_structure.unregister()
