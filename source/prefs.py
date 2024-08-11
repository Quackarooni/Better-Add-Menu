import bpy
from bpy.props import BoolProperty, EnumProperty, StringProperty
from .keymaps import keymap_layout


class BetterAddMenuPreferences(bpy.types.AddonPreferences):
    bl_idname = "Better Add Menu"

    show_keymaps: BoolProperty(
        name="Show Keymaps",
        default=False,
        description="When enabled, displays keymap list",
    )

    show_assets_menu: BoolProperty(
        name="Show \"Assets\" Menu",
        default=True,
        description="Toggle visibility of \"Assets\" menu, which contains nodegroup assets from the user's asset library",
    )

    if bpy.app.version >= (4, 1, 0):
        show_deprecated_menu: BoolProperty(
            name="Show \"Deprecated\" Menu",
            default=True,
            description="Toggle visibility of \"Deprecated\" menu, which contains nodes that are intended to be phased out of use",
        )

        def draw_properties(self, layout):
            layout.prop(self, "show_assets_menu")
            layout.prop(self, "show_deprecated_menu")
    else:
        def draw_properties(self, layout):
            layout.prop(self, "show_assets_menu")

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