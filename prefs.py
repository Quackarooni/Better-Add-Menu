import bpy
from bpy.props import BoolProperty, EnumProperty, StringProperty
from .keymaps import keymap_layout


class BetterAddMenuPreferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    show_keymaps: BoolProperty(
        name="Show Keymaps",
        default=False,
        description="When enabled, displays keymap list",
    )

    show_assets: BoolProperty(
        name="Show Assets Menu",
        default=True,
        description="Toggles whether the menu for applying asset modifiers is displayed in the Modifier Tab",
    )

    display_as: EnumProperty(
        name="Display As",
        items=(
            ("DROPDOWN", "Dropdowns", "Display menus as dropdowns, similar to the pre-4.0 style", "DOWNARROW_HLT", 0),
            ("BUTTON", "Buttons", "Display menus as dropdowns, similar to the current 4.0 style", "ADD", 1),
        ),
        default='BUTTON',
        description="Specifies how the menus are going to be displayed in the Modifier Panel"
    )

    stacking: EnumProperty(
        name="Arrangement",
        items=(
            ("HORIZONTAL", "Horizontal", "Arrange the menus in a row, left-to-right", "NONE", 0),
            ("VERTICAL", "Vertical", "Arrange the menus in a column, top-to-bottom", "NONE", 1),
        ),
        default='HORIZONTAL',
        description="Specifies how the menus are going to be arranged in the Modifier Panel"
    )

    modifier_menu_label: StringProperty(
        name="Label",
        description="Specifies the text that will display on the modifier menu",
        default="Add Modifier",
    )

    asset_menu_label: StringProperty(
        name="Label",
        description="Specifies the text that will display on the asset menu",
        default="Add Asset",
    )

    modifier_headers: EnumProperty(
        name="Category Headers",
        items=(
            ("HIDE", "Hide Headers", "Don't show the headers per category column"),
            ("SHOW", "Show Headers", "Display a label per column indicating the category of modifiers in that column",),
            ("WITH_ICONS", "Show Headers (w/ Icons)", "Same as 'Show Headers' but with icons"),
        ),
        default='WITH_ICONS',
        description="Specifies how the labels on the top of each category are going to be displayed"
    )

    built_in_asset_categories: EnumProperty(
        name="Built-in Categories",
        items=(
            ("HIDE", "Hide Assets", "Don't display built-in category assets in asset menu"),
            ("SHOW", "Show Assets", "Display built-in category assets in asset menu",),
            ("APPEND", "Append to Modifiers", "Display built-in category assets in modifier menu"),
            ("SHOW_AND_APPEND", "Show and Append to Modifiers", "Display built-in category assets in both the modifier and asset menu"),
        ),
        default='SHOW',
        description="Specifies how assets in catalogs named after built-in categories (Edit, Generate, Deform, Physics), are displayed"
    )

    def draw_prop_newline(self, layout, prop_name):
        prop_label = self.__annotations__[prop_name].keywords["name"]
        layout.label(text=f"{prop_label}:")
        layout.prop(self, prop_name, text="")

    def draw(self, context):
        layout = self.layout
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