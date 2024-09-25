import bpy
from bpy.props import BoolProperty, EnumProperty
from .keymaps import keymap_layout


class BetterAddMenuPreferences(bpy.types.AddonPreferences):
    bl_idname = "Better Add Menu"

    show_asset_nodegroups: EnumProperty(
        name="Show Asset Nodegroups",
        items=(
            ("TOP_LEVEL", "In Main Menu", "Put nodegroup assets under the main \"Add\" menu"),
            ("SUBMENU", "In Dedicated Submenu", "Put nodegroup assets under a dedicated \"Assets\" submenu"),
            ("HIDDEN", "Hidden", "Nodegroup assets are not included in the \"Add\" menu")
        ),
        default='SUBMENU',
        description="Specifies how nodegroup assets from the user's asset library will be displayed")
        
    show_header_icons: BoolProperty(
        name="Show Header Icons",
        default=True,
        description="Toggle icons for header labels of submenus",
    )

    if bpy.app.version >= (4, 1, 0):
        show_deprecated_menu: BoolProperty(
            name="Show \"Deprecated\" Menu",
            default=True,
            description="Toggle visibility of \"Deprecated\" menu, which contains nodes that are intended to be phased out of use",
        )

        def draw_properties(self, layout):
            layout.prop(self, "show_deprecated_menu")
            layout.prop(self, "show_header_icons")
            layout.separator()
            self.draw_enum_prop(layout, "show_asset_nodegroups")
    else:
        def draw_properties(self, layout):
            layout.prop(self, "show_header_icons")
            layout.separator()
            self.draw_enum_prop(layout, "show_asset_nodegroups")


    def draw_enum_prop(self, layout, prop_id):
        prop_label = self.__annotations__[prop_id].keywords["name"]
        
        layout.label(text=f"{prop_label}:")
        layout.prop(self, prop_id, text="")


    def draw(self, context):
        layout = self.layout

        col = layout.column(align=True)
        self.draw_properties(col)

        keymap_layout.draw_keyboard_shorcuts(self, layout, context)


keymap_layout.register_properties(preferences=BetterAddMenuPreferences)


classes = (
    BetterAddMenuPreferences,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)