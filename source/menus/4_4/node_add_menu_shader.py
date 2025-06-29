# SPDX-FileCopyrightText: 2022-2023 Blender Authors
#
# SPDX-License-Identifier: GPL-2.0-or-later

from bpy.types import Menu
from bl_ui import node_add_menu
from bpy.app.translations import (
    pgettext_iface as iface_,
    contexts as i18n_contexts,
)

from ..utils import ColumnMenu, add_separator, draw_asset_menu, draw_node_group_add_menu

# only show input/output nodes when editing line style node trees
def line_style_shader_nodes_poll(context):
    snode = context.space_data
    return (snode.tree_type == 'ShaderNodeTree' and
            snode.shader_type == 'LINESTYLE')


# only show nodes working in world node trees
def world_shader_nodes_poll(context):
    snode = context.space_data
    return (snode.tree_type == 'ShaderNodeTree' and
            snode.shader_type == 'WORLD')


# only show nodes working in object node trees
def object_shader_nodes_poll(context):
    snode = context.space_data
    return (snode.tree_type == 'ShaderNodeTree' and
            snode.shader_type == 'OBJECT')


def cycles_shader_nodes_poll(context):
    return context.engine == 'CYCLES'


def eevee_shader_nodes_poll(context):
    return context.engine in {'BLENDER_EEVEE', 'BLENDER_EEVEE_NEXT'}


def object_cycles_shader_nodes_poll(context):
    return (object_shader_nodes_poll(context) and
            cycles_shader_nodes_poll(context))


def object_not_eevee_shader_nodes_poll(context):
    return (object_shader_nodes_poll(context) and
            not eevee_shader_nodes_poll(context))


def object_eevee_shader_nodes_poll(context):
    return (object_shader_nodes_poll(context) and
            eevee_shader_nodes_poll(context))


class NODE_MT_shader_input(ColumnMenu, Menu):
    bl_idname = "NODE_MT_category_shader_input"
    bl_label = "Input"

    def draw(self, context):
        layout = self.layout.row()

        self.draw_column(layout, menus=(NODE_MT_shader_input_constant, NODE_MT_shader_input_info,))
        self.draw_column(layout, menus=(NODE_MT_shader_input_attribute, NODE_MT_shader_input_coordinates,))
        self.draw_column(layout, menus=(NODE_MT_shader_input_misc,))

        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_shader_input_constant(Menu):
    bl_idname = "NODE_MT_category_shader_input_constant"
    bl_label = "Constant"

    header_icon = "CON_TRANSFORM"

    def draw(self, context):
        layout = self.layout

        node_add_menu.add_node_type(layout, "ShaderNodeRGB")
        node_add_menu.add_node_type(layout, "ShaderNodeValue")


class NODE_MT_shader_input_attribute(Menu):
    bl_idname = "NODE_MT_category_shader_input_attribute"
    bl_label = "Attribute"

    header_icon = "GROUP_UVS"

    def draw(self, context):
        layout = self.layout

        node_add_menu.add_node_type(layout, "ShaderNodeAttribute")
        node_add_menu.add_node_type(layout, "ShaderNodeVertexColor")
        node_add_menu.add_node_type(layout, "ShaderNodeUVAlongStroke", poll=line_style_shader_nodes_poll(context))
        node_add_menu.add_node_type(layout, "ShaderNodeUVMap")


class NODE_MT_shader_input_info(Menu):
    bl_idname = "NODE_MT_category_shader_input_info"
    bl_label = "Info"

    header_icon = "INFO"

    def draw(self, context):
        layout = self.layout

        node_add_menu.add_node_type(layout, "ShaderNodeHairInfo")
        node_add_menu.add_node_type(layout, "ShaderNodeObjectInfo")
        node_add_menu.add_node_type(layout, "ShaderNodeParticleInfo")
        node_add_menu.add_node_type(layout, "ShaderNodePointInfo")
        node_add_menu.add_node_type(layout, "ShaderNodeVolumeInfo")


class NODE_MT_shader_input_coordinates(Menu):
    bl_idname = "NODE_MT_category_shader_input_coordinates"
    bl_label = "Coordinates"

    header_icon = "MOD_EDGESPLIT"

    def draw(self, context):
        layout = self.layout

        node_add_menu.add_node_type(layout, "ShaderNodeCameraData")
        node_add_menu.add_node_type(layout, "ShaderNodeNewGeometry")
        node_add_menu.add_node_type(layout, "ShaderNodeTangent")
        node_add_menu.add_node_type(layout, "ShaderNodeTexCoord")


class NODE_MT_shader_input_misc(Menu):
    bl_idname = "NODE_MT_category_shader_input_misc"
    bl_label = "Miscellaneous"

    header_icon = "COLLAPSEMENU"

    def draw(self, context):
        layout = self.layout

        node_add_menu.add_node_type(layout, "ShaderNodeAmbientOcclusion")
        node_add_menu.add_node_type(layout, "ShaderNodeBevel")
        node_add_menu.add_node_type(layout, "ShaderNodeFresnel")
        node_add_menu.add_node_type(layout, "ShaderNodeLayerWeight")
        node_add_menu.add_node_type(layout, "ShaderNodeLightPath")
        node_add_menu.add_node_type(layout, "ShaderNodeWireframe")


class NODE_MT_shader_output(Menu):
    bl_idname = "NODE_MT_category_shader_output"
    bl_label = "Output"

    def draw(self, context):
        layout = self.layout

        node_add_menu.add_node_type(layout, "ShaderNodeOutputAOV")
        node_add_menu.add_node_type(layout, "ShaderNodeOutputLight", poll=object_not_eevee_shader_nodes_poll(context))
        node_add_menu.add_node_type(layout, "ShaderNodeOutputLineStyle", poll=line_style_shader_nodes_poll(context))
        node_add_menu.add_node_type(layout, "ShaderNodeOutputMaterial", poll=object_shader_nodes_poll(context))
        node_add_menu.add_node_type(layout, "ShaderNodeOutputWorld", poll=world_shader_nodes_poll(context))

        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_shader_shader(ColumnMenu, Menu):
    bl_idname = "NODE_MT_category_shader_shader"
    bl_label = "Shader"

    def draw(self, context):
        layout = self.layout.row()

        self.draw_column(layout, menus=(NODE_MT_shader_shader_basic, NODE_MT_shader_shader_volume_and_scatter,))
        self.draw_column(layout, menus=(NODE_MT_shader_shader_bsdf,))
        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_shader_shader_basic(Menu):
    bl_idname = "NODE_MT_shader_shader_basic"
    bl_label = "Basic"
        
    header_icon = "NODE_MATERIAL"

    def draw(self, context):
        layout = self.layout

        node_add_menu.add_node_type(layout, "ShaderNodeAddShader")
        node_add_menu.add_node_type(layout, "ShaderNodeMixShader")
        add_separator(layout)

        node_add_menu.add_node_type(layout, "ShaderNodeBackground", poll=world_shader_nodes_poll(context))
        node_add_menu.add_node_type(layout, "ShaderNodeEmission")
        node_add_menu.add_node_type(layout, "ShaderNodeHoldout", poll=object_shader_nodes_poll(context))


class NODE_MT_shader_shader_bsdf(Menu):
    bl_idname = "NODE_MT_shader_shader_bsdf"
    bl_label = "BSDF"
        
    header_icon = "SHADING_TEXTURE"

    def draw(self, context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "ShaderNodeBsdfDiffuse", poll=object_shader_nodes_poll(context))
        node_add_menu.add_node_type(layout, "ShaderNodeBsdfGlass", poll=object_shader_nodes_poll(context))
        node_add_menu.add_node_type(layout, "ShaderNodeBsdfGlossy", poll=object_shader_nodes_poll(context))
        node_add_menu.add_node_type(layout, "ShaderNodeBsdfMetallic", poll=object_shader_nodes_poll(context))
        node_add_menu.add_node_type(layout, "ShaderNodeBsdfPrincipled", poll=object_shader_nodes_poll(context))
        node_add_menu.add_node_type(layout, "ShaderNodeBsdfRefraction", poll=object_shader_nodes_poll(context))
        node_add_menu.add_node_type(layout, "ShaderNodeEeveeSpecular", poll=object_eevee_shader_nodes_poll(context))
        node_add_menu.add_node_type(layout, "ShaderNodeBsdfTranslucent", poll=object_shader_nodes_poll(context))
        node_add_menu.add_node_type(layout, "ShaderNodeBsdfTransparent", poll=object_shader_nodes_poll(context))

        if object_not_eevee_shader_nodes_poll(context):
            add_separator(layout)
            node_add_menu.add_node_type(layout, "ShaderNodeBsdfHair", poll=object_not_eevee_shader_nodes_poll(context))
            node_add_menu.add_node_type(layout, "ShaderNodeBsdfHairPrincipled", poll=object_not_eevee_shader_nodes_poll(context))
            node_add_menu.add_node_type(layout, "ShaderNodeBsdfRayPortal", poll=object_not_eevee_shader_nodes_poll(context))
            node_add_menu.add_node_type(layout, "ShaderNodeBsdfSheen", poll=object_not_eevee_shader_nodes_poll(context))
            node_add_menu.add_node_type(layout, "ShaderNodeBsdfToon", poll=object_not_eevee_shader_nodes_poll(context))


class NODE_MT_shader_shader_volume_and_scatter(Menu):
    bl_idname = "NODE_MT_shader_shader_volume_and_scatter"
    bl_label = "Volume & Scatter"
        
    header_icon = "OUTLINER_DATA_VOLUME"

    def draw(self, context):
        layout = self.layout

        node_add_menu.add_node_type(layout, "ShaderNodeSubsurfaceScattering", poll=object_shader_nodes_poll(context))
        node_add_menu.add_node_type(layout, "ShaderNodeVolumePrincipled")
        node_add_menu.add_node_type(layout, "ShaderNodeVolumeAbsorption")
        node_add_menu.add_node_type(layout, "ShaderNodeVolumeScatter")


class NODE_MT_shader_color(Menu):
    bl_idname = "NODE_MT_category_shader_color"
    bl_label = "Color"

    def draw(self, _context):
        layout = self.layout
        
        node_add_menu.add_node_type(layout, "ShaderNodeCombineColor")
        props = node_add_menu.add_node_type(layout, "ShaderNodeMix", label=iface_("Mix Color"))
        ops = props.settings.add()
        ops.name = "data_type"
        ops.value = "'RGBA'"
        node_add_menu.add_node_type(layout, "ShaderNodeSeparateColor")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "ShaderNodeBrightContrast")
        node_add_menu.add_node_type(layout, "ShaderNodeGamma")
        node_add_menu.add_node_type(layout, "ShaderNodeHueSaturation")
        node_add_menu.add_node_type(layout, "ShaderNodeInvert")
        node_add_menu.add_node_type(layout, "ShaderNodeLightFalloff")
        node_add_menu.add_node_type(layout, "ShaderNodeRGBCurve")

        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_shader_converter(Menu):
    bl_idname = "NODE_MT_category_shader_converter"
    bl_label = "Converter"

    def draw(self, context):
        layout = self.layout

        node_add_menu.add_node_type(layout, "ShaderNodeMath")
        node_add_menu.add_node_type(layout, "ShaderNodeMix")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "ShaderNodeClamp")
        node_add_menu.add_node_type(layout, "ShaderNodeFloatCurve")
        node_add_menu.add_node_type(layout, "ShaderNodeMapRange")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "ShaderNodeValToRGB")
        node_add_menu.add_node_type(layout, "ShaderNodeRGBToBW")
        node_add_menu.add_node_type(layout, "ShaderNodeShaderToRGB", poll=object_eevee_shader_nodes_poll(context))
        add_separator(layout)
        node_add_menu.add_node_type(layout, "ShaderNodeBlackbody")
        node_add_menu.add_node_type(layout, "ShaderNodeWavelength")

        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_shader_texture(ColumnMenu, Menu):
    bl_idname = "NODE_MT_category_shader_texture"
    bl_label = "Texture"

    def draw(self, _context):
        layout = self.layout.row()

        self.draw_column(layout, menus=(NODE_MT_shader_texture_image,NODE_MT_shader_texture_noise))
        self.draw_column(layout, menus=(NODE_MT_shader_texture_procedural, NODE_MT_shader_texture_misc,))

        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_shader_texture_image(ColumnMenu, Menu):
    bl_idname = "NODE_MT_shader_texture_image"
    bl_label = "Image"
        
    header_icon = "IMAGE_DATA"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "ShaderNodeTexImage")
        node_add_menu.add_node_type(layout, "ShaderNodeTexEnvironment")


class NODE_MT_shader_texture_noise(ColumnMenu, Menu):
    bl_idname = "NODE_MT_shader_texture_noise"
    bl_label = "Noise"
        
    header_icon = "MOD_OCEAN"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "ShaderNodeTexNoise")
        node_add_menu.add_node_type(layout, "ShaderNodeTexWhiteNoise")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "ShaderNodeTexGabor")
        node_add_menu.add_node_type(layout, "ShaderNodeTexWave")


class NODE_MT_shader_texture_misc(ColumnMenu, Menu):
    bl_idname = "NODE_MT_shader_texture_misc"
    bl_label = "Miscellaneous"
    
    header_icon = "COLLAPSEMENU"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "ShaderNodeTexIES")
        node_add_menu.add_node_type(layout, "ShaderNodeTexPointDensity")
        node_add_menu.add_node_type(layout, "ShaderNodeTexSky")


class NODE_MT_shader_texture_procedural(ColumnMenu, Menu):
    bl_idname = "NODE_MT_shader_texture_procedural"
    bl_label = "Procedural"
        
    header_icon = "NODE_TEXTURE"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "ShaderNodeTexBrick")
        node_add_menu.add_node_type(layout, "ShaderNodeTexChecker")
        node_add_menu.add_node_type(layout, "ShaderNodeTexGradient")
        node_add_menu.add_node_type(layout, "ShaderNodeTexMagic")
        node_add_menu.add_node_type(layout, "ShaderNodeTexVoronoi")


class NODE_MT_shader_vector(ColumnMenu, Menu):
    bl_idname = "NODE_MT_category_shader_vector"
    bl_label = "Vector"

    def draw(self, _context):
        layout = self.layout.row()

        self.draw_column(layout, menus=(NODE_MT_shader_vector_operations,))
        self.draw_column(layout, menus=(NODE_MT_shader_vector_texture_and_shading,))

        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_shader_vector_operations(Menu):
    bl_idname = "NODE_MT_shader_vector_operations"
    bl_label = "Operations"

    header_icon = "CON_TRANSFORM_CACHE"

    def draw(self, _context):
        layout = self.layout

        node_add_menu.add_node_type(layout, "ShaderNodeCombineXYZ")        
        props = node_add_menu.add_node_type(layout, "ShaderNodeMix", label=iface_("Mix Vector"))
        ops = props.settings.add()
        ops.name = "data_type"
        ops.value = "'VECTOR'"
        node_add_menu.add_node_type(layout, "ShaderNodeSeparateXYZ")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "ShaderNodeVectorCurve")
        node_add_menu.add_node_type(layout, "ShaderNodeVectorMath")
        node_add_menu.add_node_type(layout, "ShaderNodeVectorRotate")
        node_add_menu.add_node_type(layout, "ShaderNodeVectorTransform")


class NODE_MT_shader_vector_texture_and_shading(Menu):
    bl_idname = "NODE_MT_shader_vector_texture_and_shading"
    bl_label = "Texture & Shading"

    header_icon = "IMAGE_RGB_ALPHA"

    def draw(self, _context):
        layout = self.layout

        node_add_menu.add_node_type(layout, "ShaderNodeBump")
        node_add_menu.add_node_type(layout, "ShaderNodeDisplacement")
        node_add_menu.add_node_type(layout, "ShaderNodeMapping")
        node_add_menu.add_node_type(layout, "ShaderNodeVectorDisplacement")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "ShaderNodeNormal")
        node_add_menu.add_node_type(layout, "ShaderNodeNormalMap")


class NODE_MT_shader_script(Menu):
    bl_idname = "NODE_MT_category_shader_script"
    bl_label = "Script"

    def draw(self, _context):
        layout = self.layout

        node_add_menu.add_node_type(layout, "ShaderNodeScript")

        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_shader_group(Menu):
    bl_idname = "NODE_MT_category_shader_group"
    bl_label = "Group"

    def draw(self, context):
        layout = self.layout
        draw_node_group_add_menu(context, layout)
        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_shader_node_add_all(Menu):
    bl_idname = __qualname__
    bl_label = "Add"
    bl_translation_context = i18n_contexts.operator_default

    def draw(self, context):
        layout = self.layout
        layout.menu("NODE_MT_category_shader_input")
        layout.menu("NODE_MT_category_shader_output")
        add_separator(layout)
        layout.menu("NODE_MT_category_shader_color")
        layout.menu("NODE_MT_category_shader_converter")
        layout.menu("NODE_MT_category_shader_shader")
        layout.menu("NODE_MT_category_shader_texture")
        layout.menu("NODE_MT_category_shader_vector")
        add_separator(layout)
        layout.menu("NODE_MT_category_shader_script")
        add_separator(layout)
        layout.menu("NODE_MT_category_shader_group")
        layout.menu("NODE_MT_category_layout")
        
        draw_asset_menu(layout)


classes = (
    NODE_MT_shader_node_add_all,
    NODE_MT_shader_input,
    NODE_MT_shader_input_attribute,
    NODE_MT_shader_input_constant,
    NODE_MT_shader_input_coordinates,
    NODE_MT_shader_input_info,
    NODE_MT_shader_input_misc,
    NODE_MT_shader_output,
    NODE_MT_shader_color,
    NODE_MT_shader_converter,
    NODE_MT_shader_shader,
    NODE_MT_shader_shader_basic,
    NODE_MT_shader_shader_bsdf,
    NODE_MT_shader_shader_volume_and_scatter,
    NODE_MT_shader_texture,
    NODE_MT_shader_texture_image,
    NODE_MT_shader_texture_noise,
    NODE_MT_shader_texture_misc,
    NODE_MT_shader_texture_procedural,
    NODE_MT_shader_vector,
    NODE_MT_shader_vector_operations,
    NODE_MT_shader_vector_texture_and_shading,
    NODE_MT_shader_script,
    NODE_MT_shader_group,
)


if __name__ == "__main__":  # only for live edit.
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
