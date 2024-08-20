# SPDX-FileCopyrightText: 2022-2023 Blender Authors
#
# SPDX-License-Identifier: GPL-2.0-or-later

from bpy.types import Menu
from bl_ui import node_add_menu
from bpy.app.translations import (
    pgettext_iface as iface_,
    contexts as i18n_contexts,
)

from ..utils import (
    ColumnMenu, 
    add_separator, 
    draw_asset_menu, 
    draw_node_group_add_menu
    )

class NODE_MT_compositor_input(ColumnMenu, Menu):
    bl_idname = "NODE_MT_category_compositor_input"
    bl_label = "Input"

    def draw(self, context):
        snode = context.space_data
        #is_group = (len(snode.path) > 1)

        layout = self.layout.row()

        self.draw_column(layout, menus=(NODE_MT_compositor_input_constant, ))
        self.draw_column(layout, menus=(NODE_MT_compositor_input_data, ))
        self.draw_column(layout, menus=(NODE_MT_compositor_input_scene, ))

        #if is_group:
        #    add_separator(col)
        #    node_add_menu.add_node_type(layout, "NodeGroupInput")

        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_compositor_input_constant(Menu):
    bl_idname = "NODE_MT_category_compositor_input_constant"
    bl_label = "Constant"

    header_icon = "CON_TRANSFORM"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "CompositorNodeRGB")
        node_add_menu.add_node_type(layout, "CompositorNodeValue")

        #node_add_menu.draw_assets_for_catalog(layout, "Input/Constant")
        

class NODE_MT_compositor_input_data(Menu):
    bl_idname = "NODE_MT_compositor_input_data"
    bl_label = "Data"
        
    header_icon = "PRESET"

    def draw(self, _context):
        layout = self.layout
        
        node_add_menu.add_node_type(layout, "CompositorNodeBokehImage")
        node_add_menu.add_node_type(layout, "CompositorNodeImage")
        node_add_menu.add_node_type(layout, "CompositorNodeMask")
        node_add_menu.add_node_type(layout, "CompositorNodeMovieClip")
        node_add_menu.add_node_type(layout, "CompositorNodeTexture")

        #node_add_menu.draw_assets_for_catalog(layout, "Input/Data")


class NODE_MT_compositor_input_scene(Menu):
    bl_idname = "NODE_MT_category_compositor_input_scene"
    bl_label = "Scene"

    header_icon = "SCENE_DATA"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "CompositorNodeRLayers")
        node_add_menu.add_node_type(layout, "CompositorNodeSceneTime")
        node_add_menu.add_node_type(layout, "CompositorNodeTime")

        #node_add_menu.draw_assets_for_catalog(layout, "Input/Scene")


class NODE_MT_compositor_output(Menu):
    bl_idname = "NODE_MT_category_compositor_output"
    bl_label = "Output"

    def draw(self, context):
        snode = context.space_data
        #is_group = (len(snode.path) > 1)

        layout = self.layout
        node_add_menu.add_node_type(layout, "CompositorNodeComposite")
        node_add_menu.add_node_type(layout, "CompositorNodeOutputFile")
        node_add_menu.add_node_type(layout, "CompositorNodeViewer")

        #if is_group:
        #    add_separator(col)
        #    node_add_menu.add_node_type(layout, "NodeGroupOutput")

        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_compositor_color(ColumnMenu, Menu):
    bl_idname = "NODE_MT_category_compositor_color"
    bl_label = "Color"

    def draw(self, _context):
        layout = self.layout.row()

        self.draw_column(layout, menus=(NODE_MT_compositor_color_adjust,))
        self.draw_column(layout, menus=(NODE_MT_compositor_color_mix,))
        self.draw_column(layout, menus=(NODE_MT_compositor_color_misc,))

        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_compositor_color_adjust(Menu):
    bl_idname = "NODE_MT_category_compositor_color_adjust"
    bl_label = "Adjust"

    header_icon = "MOD_HUE_SATURATION"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "CompositorNodeBrightContrast")
        node_add_menu.add_node_type(layout, "CompositorNodeColorBalance")
        node_add_menu.add_node_type(layout, "CompositorNodeColorCorrection")
        node_add_menu.add_node_type(layout, "CompositorNodeExposure")
        node_add_menu.add_node_type(layout, "CompositorNodeGamma")
        node_add_menu.add_node_type(layout, "CompositorNodeHueCorrect")
        node_add_menu.add_node_type(layout, "CompositorNodeHueSat")
        node_add_menu.add_node_type(layout, "CompositorNodeCurveRGB")
        node_add_menu.add_node_type(layout, "CompositorNodeTonemap")

        #node_add_menu.draw_assets_for_catalog(layout, "Color/Adjust")


class NODE_MT_compositor_color_mix(Menu):
    bl_idname = "NODE_MT_category_compositor_color_mix"
    bl_label = "Mix"

    header_icon = "OVERLAY"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "CompositorNodeMixRGB", label=iface_("Mix Color"))
        node_add_menu.add_node_type(layout, "CompositorNodeCombineColor")
        node_add_menu.add_node_type(layout, "CompositorNodeSeparateColor")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "CompositorNodeAlphaOver")
        node_add_menu.add_node_type(layout, "CompositorNodeZcombine")
        #node_add_menu.draw_assets_for_catalog(layout, "Color/Mix")


class NODE_MT_compositor_color_misc(Menu):
    bl_idname = "NODE_MT_compositor_color_misc"
    bl_label = "Miscellaneous"

    header_icon = "COLLAPSEMENU"

    def draw(self, _context):
        layout = self.layout

        add_separator(layout)
        node_add_menu.add_node_type(layout, "CompositorNodePremulKey")
        node_add_menu.add_node_type(layout, "CompositorNodeValToRGB")
        node_add_menu.add_node_type(layout, "CompositorNodeConvertColorSpace")
        node_add_menu.add_node_type(layout, "CompositorNodeSetAlpha")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "CompositorNodeInvert")
        node_add_menu.add_node_type(layout, "CompositorNodeRGBToBW")

        #node_add_menu.draw_assets_for_catalog(layout, "Color/Miscellaneous")


class NODE_MT_compositor_filter(ColumnMenu, Menu):
    bl_idname = "NODE_MT_category_compositor_filter"
    bl_label = "Filter"

    def draw(self, _context):
        layout = self.layout.row()

        self.draw_column(layout, menus=(NODE_MT_compositor_filter_blur,))
        self.draw_column(layout, menus=(NODE_MT_compositor_filter_effect,))
        self.draw_column(layout, menus=(NODE_MT_compositor_filter_utilities,))

        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_compositor_filter_blur(Menu):
    bl_idname = "NODE_MT_category_compositor_filter_blur"
    bl_label = "Blur"

    header_icon = "MOD_FLUIDSIM"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "CompositorNodeBlur")
        node_add_menu.add_node_type(layout, "CompositorNodeDefocus")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "CompositorNodeBilateralblur")
        node_add_menu.add_node_type(layout, "CompositorNodeBokehBlur")
        node_add_menu.add_node_type(layout, "CompositorNodeDBlur")
        node_add_menu.add_node_type(layout, "CompositorNodeVecBlur")

        #node_add_menu.draw_assets_for_catalog(layout, "Filter/Blur")


class NODE_MT_compositor_filter_effect(Menu):
    bl_idname = "NODE_MT_category_compositor_filter_effect"
    bl_label = "Effects"

    header_icon = "IMAGE_RGB_ALPHA"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "CompositorNodeFilter")
        node_add_menu.add_node_type(layout, "CompositorNodeGlare")
        node_add_menu.add_node_type(layout, "CompositorNodeKuwahara")
        node_add_menu.add_node_type(layout, "CompositorNodePixelate")
        node_add_menu.add_node_type(layout, "CompositorNodePosterize")
        node_add_menu.add_node_type(layout, "CompositorNodeSunBeams")


class NODE_MT_compositor_filter_utilities(Menu):
    bl_idname = "NODE_MT_category_compositor_filter_utilities"
    bl_label = "Utilities"

    header_icon = "MODIFIER_DATA"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "CompositorNodeAntiAliasing")
        node_add_menu.add_node_type(layout, "CompositorNodeDenoise")
        node_add_menu.add_node_type(layout, "CompositorNodeDespeckle")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "CompositorNodeDilateErode")
        node_add_menu.add_node_type(layout, "CompositorNodeInpaint")


class NODE_MT_compositor_group(Menu):
    bl_idname = "NODE_MT_category_compositor_group"
    bl_label = "Group"

    def draw(self, context):
        layout = self.layout
        draw_node_group_add_menu(context, layout)
        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_compositor_keying(Menu):
    bl_idname = "NODE_MT_category_compositor_keying"
    bl_label = "Keying"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "CompositorNodeChannelMatte")
        node_add_menu.add_node_type(layout, "CompositorNodeChromaMatte")
        node_add_menu.add_node_type(layout, "CompositorNodeColorMatte")
        node_add_menu.add_node_type(layout, "CompositorNodeColorSpill")
        node_add_menu.add_node_type(layout, "CompositorNodeDiffMatte")
        node_add_menu.add_node_type(layout, "CompositorNodeDistanceMatte")
        node_add_menu.add_node_type(layout, "CompositorNodeKeying")
        node_add_menu.add_node_type(layout, "CompositorNodeKeyingScreen")
        node_add_menu.add_node_type(layout, "CompositorNodeLumaMatte")

        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_compositor_mask(Menu):
    bl_idname = "NODE_MT_category_compositor_mask"
    bl_label = "Mask"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "CompositorNodeCryptomatteV2")
        node_add_menu.add_node_type(layout, "CompositorNodeCryptomatte")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "CompositorNodeBoxMask")
        node_add_menu.add_node_type(layout, "CompositorNodeEllipseMask")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "CompositorNodeDoubleEdgeMask")
        node_add_menu.add_node_type(layout, "CompositorNodeIDMask")

        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_compositor_tracking(Menu):
    bl_idname = "NODE_MT_category_compositor_tracking"
    bl_label = "Tracking"
    bl_translation_context = i18n_contexts.id_movieclip

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "CompositorNodePlaneTrackDeform")
        node_add_menu.add_node_type(layout, "CompositorNodeStabilize")
        node_add_menu.add_node_type(layout, "CompositorNodeTrackPos")

        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_compositor_transform(Menu):
    bl_idname = "NODE_MT_category_compositor_transform"
    bl_label = "Transform"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "CompositorNodeRotate")
        node_add_menu.add_node_type(layout, "CompositorNodeScale")
        node_add_menu.add_node_type(layout, "CompositorNodeTransform")
        node_add_menu.add_node_type(layout, "CompositorNodeTranslate")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "CompositorNodeCornerPin")
        node_add_menu.add_node_type(layout, "CompositorNodeCrop")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "CompositorNodeDisplace")
        node_add_menu.add_node_type(layout, "CompositorNodeFlip")
        node_add_menu.add_node_type(layout, "CompositorNodeMapUV")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "CompositorNodeLensdist")
        node_add_menu.add_node_type(layout, "CompositorNodeMovieDistortion")

        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_compositor_utilities(Menu):
    bl_idname = "NODE_MT_category_compositor_utilities"
    bl_label = "Utilities"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "CompositorNodeMapRange")
        node_add_menu.add_node_type(layout, "CompositorNodeMapValue")
        node_add_menu.add_node_type(layout, "CompositorNodeMath")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "CompositorNodeLevels")
        node_add_menu.add_node_type(layout, "CompositorNodeNormalize")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "CompositorNodeSplit")
        node_add_menu.add_node_type(layout, "CompositorNodeSwitch")
        node_add_menu.add_node_type(
            layout, "CompositorNodeSwitchView",
            label=iface_("Switch Stereo View"))

        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_compositor_vector(Menu):
    bl_idname = "NODE_MT_category_compositor_vector"
    bl_label = "Vector"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "CompositorNodeCombineXYZ")
        node_add_menu.add_node_type(layout, "CompositorNodeSeparateXYZ")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "CompositorNodeNormal")
        node_add_menu.add_node_type(layout, "CompositorNodeCurveVec")

        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_compositor_node_add_all(Menu):
    bl_idname = __qualname__
    bl_label = ""

    def draw(self, context):
        layout = self.layout
        layout.menu("NODE_MT_category_compositor_input")
        layout.menu("NODE_MT_category_compositor_output")
        add_separator(layout)
        layout.menu("NODE_MT_category_compositor_color")
        layout.menu("NODE_MT_category_compositor_filter")
        add_separator(layout)
        layout.menu("NODE_MT_category_compositor_keying")
        layout.menu("NODE_MT_category_compositor_mask")
        add_separator(layout)
        layout.menu("NODE_MT_category_compositor_tracking")
        add_separator(layout)
        layout.menu("NODE_MT_category_compositor_transform")
        layout.menu("NODE_MT_category_compositor_utilities")
        layout.menu("NODE_MT_category_compositor_vector")
        add_separator(layout)
        layout.menu("NODE_MT_category_compositor_group")
        layout.menu("NODE_MT_category_layout")

        draw_asset_menu(layout)


classes = (
    NODE_MT_compositor_node_add_all,
    NODE_MT_compositor_input,
    NODE_MT_compositor_input_constant,
    NODE_MT_compositor_input_data,
    NODE_MT_compositor_input_scene,
    NODE_MT_compositor_output,
    NODE_MT_compositor_color,
    NODE_MT_compositor_color_adjust,
    NODE_MT_compositor_color_mix,
    NODE_MT_compositor_color_misc,
    NODE_MT_compositor_filter,
    NODE_MT_compositor_filter_blur,
    NODE_MT_compositor_filter_effect,
    NODE_MT_compositor_filter_utilities,
    NODE_MT_compositor_keying,
    NODE_MT_compositor_mask,
    NODE_MT_compositor_tracking,
    NODE_MT_compositor_transform,
    NODE_MT_compositor_utilities,
    NODE_MT_compositor_vector,
    NODE_MT_compositor_group,
)

if __name__ == "__main__":  # only for live edit.
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
