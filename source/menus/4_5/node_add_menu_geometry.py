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
    draw_node_group_add_menu,
    fetch_user_preferences
    )

class NODE_MT_geometry_node_attribute(Menu):
    bl_idname = "NODE_MT_geometry_node_GEO_ATTRIBUTE"
    bl_label = "Attribute"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeAttributeStatistic")
        node_add_menu.add_node_type(layout, "GeometryNodeAttributeDomainSize")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "GeometryNodeBlurAttribute")
        node_add_menu.add_node_type(layout, "GeometryNodeCaptureAttribute")
        node_add_menu.add_node_type(layout, "GeometryNodeRemoveAttribute")
        node_add_menu.add_node_type(layout, "GeometryNodeStoreNamedAttribute", search_weight=1.0)
        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_geometry_node_utilities_color(Menu):
    bl_idname = "NODE_MT_geometry_node_GEO_COLOR"
    bl_label = "Color"

    header_icon = "COLOR"

    def draw(self, context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "ShaderNodeBlackbody")
        node_add_menu.add_node_type(layout, "ShaderNodeValToRGB")
        node_add_menu.add_node_type(layout, "ShaderNodeRGBCurve")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "FunctionNodeCombineColor")
        node_add_menu.add_color_mix_node(context, layout)
        node_add_menu.add_node_type(layout, "FunctionNodeSeparateColor")
        #node_add_menu.draw_assets_for_catalog(layout, "Utilities/Color")


class NODE_MT_geometry_node_curve(ColumnMenu, Menu):
    bl_idname = "NODE_MT_geometry_node_GEO_CURVE"
    bl_label = "Curve"

    def draw(self, _context):
        layout = self.layout.row()

        self.draw_column(layout, menus=(NODE_MT_geometry_node_curve_read,))
        self.draw_column(layout, menus=(NODE_MT_geometry_node_curve_write, NODE_MT_geometry_node_curve_sample,))
        self.draw_column(layout, menus=(NODE_MT_geometry_node_curve_operations,))
        
        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_geometry_node_curve_read(Menu):
    bl_idname = "NODE_MT_geometry_node_GEO_CURVE_READ"
    bl_label = "Read"

    header_icon = "COPYDOWN"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeInputCurveHandlePositions")
        node_add_menu.add_node_type(layout, "GeometryNodeCurveLength")
        node_add_menu.add_node_type(layout, "GeometryNodeInputTangent")
        node_add_menu.add_node_type(layout, "GeometryNodeInputCurveTilt")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "GeometryNodeCurveEndpointSelection")
        node_add_menu.add_node_type(layout, "GeometryNodeCurveHandleTypeSelection")
        node_add_menu.add_node_type(layout, "GeometryNodeInputSplineCyclic")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "GeometryNodeSplineLength")
        node_add_menu.add_node_type(layout, "GeometryNodeSplineParameter")
        node_add_menu.add_node_type(layout, "GeometryNodeInputSplineResolution")
        #node_add_menu.draw_assets_for_catalog(layout, "Curve/Read")


class NODE_MT_geometry_node_curve_sample(Menu):
    bl_idname = "NODE_MT_geometry_node_GEO_CURVE_SAMPLE"
    bl_label = "Sample"

    header_icon = "DRIVER"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeSampleCurve")
        #node_add_menu.draw_assets_for_catalog(layout, "Curve/Sample")


class NODE_MT_geometry_node_curve_write(Menu):
    bl_idname = "NODE_MT_geometry_node_GEO_CURVE_WRITE"
    bl_label = "Write"

    header_icon = "CURRENT_FILE"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeSetCurveNormal")
        node_add_menu.add_node_type(layout, "GeometryNodeSetCurveRadius")
        node_add_menu.add_node_type(layout, "GeometryNodeSetCurveTilt")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "GeometryNodeSetCurveHandlePositions")
        node_add_menu.add_node_type(layout, "GeometryNodeCurveSetHandles")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "GeometryNodeSetSplineCyclic")
        node_add_menu.add_node_type(layout, "GeometryNodeSetSplineResolution")
        node_add_menu.add_node_type(layout, "GeometryNodeCurveSplineType")
        #node_add_menu.draw_assets_for_catalog(layout, "Curve/Write")


class NODE_MT_geometry_node_curve_operations(Menu):
    bl_idname = "NODE_MT_geometry_node_GEO_CURVE_OPERATIONS"
    bl_label = "Operations"

    header_icon = "MODIFIER"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeCurveToMesh")
        node_add_menu.add_node_type(layout, "GeometryNodeCurveToPoints")
        node_add_menu.add_node_type(layout, "GeometryNodeGreasePencilToCurves")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "GeometryNodeFillCurve")
        node_add_menu.add_node_type(layout, "GeometryNodeFilletCurve")
        node_add_menu.add_node_type(layout, "GeometryNodeResampleCurve")
        node_add_menu.add_node_type(layout, "GeometryNodeReverseCurve")
        node_add_menu.add_node_type(layout, "GeometryNodeSubdivideCurve")
        node_add_menu.add_node_type(layout, "GeometryNodeTrimCurve")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "GeometryNodeInterpolateCurves")
        node_add_menu.add_node_type(layout, "GeometryNodeDeformCurvesOnSurface")
        #node_add_menu.draw_assets_for_catalog(layout, "Curve/Operations")


class NODE_MT_geometry_node_primitives_curve(Menu):
    bl_idname = "NODE_MT_geometry_node_GEO_PRIMITIVES_CURVE"
    bl_label = "Curve"

    header_icon = "CURVE_DATA"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeCurveArc")
        node_add_menu.add_node_type(layout, "GeometryNodeCurvePrimitiveBezierSegment")
        node_add_menu.add_node_type(layout, "GeometryNodeCurvePrimitiveCircle")
        node_add_menu.add_node_type(layout, "GeometryNodeCurvePrimitiveLine")
        node_add_menu.add_node_type(layout, "GeometryNodeCurveSpiral")
        node_add_menu.add_node_type(layout, "GeometryNodeCurveQuadraticBezier")
        node_add_menu.add_node_type(layout, "GeometryNodeCurvePrimitiveQuadrilateral")
        node_add_menu.add_node_type(layout, "GeometryNodeCurveStar")
        #node_add_menu.draw_assets_for_catalog(layout, "Curve/Primitives")


class NODE_MT_geometry_node_topology_curve(Menu):
    bl_idname = "NODE_MT_geometry_node_curve_topology"
    bl_label = "Curve"

    header_icon = "CURVE_DATA"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeCurveOfPoint")
        node_add_menu.add_node_type(layout, "GeometryNodeOffsetPointInCurve")
        node_add_menu.add_node_type(layout, "GeometryNodePointsOfCurve")
        #node_add_menu.draw_assets_for_catalog(layout, "Curve/Topology")


class NODE_MT_geometry_node_grease_pencil(ColumnMenu, Menu):
    bl_idname = "NODE_MT_geometry_node_grease_pencil"
    bl_label = "Grease Pencil"

    def draw(self, _context):
        layout = self.layout.row()
        self.draw_column(layout, menus=(NODE_MT_geometry_node_grease_pencil_read, NODE_MT_geometry_node_grease_pencil_write,))
        self.draw_column(layout, menus=(NODE_MT_geometry_node_grease_pencil_operations,))
        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_geometry_node_grease_pencil_read(Menu):
    bl_idname = "NODE_MT_geometry_node_grease_pencil_read"
    bl_label = "Read"

    header_icon = "COPYDOWN"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeInputNamedLayerSelection")
        #node_add_menu.draw_assets_for_catalog(layout, "Grease Pencil/Read")


class NODE_MT_geometry_node_grease_pencil_write(Menu):
    bl_idname = "NODE_MT_geometry_node_grease_pencil_write"
    bl_label = "Write"

    header_icon = "CURRENT_FILE"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeSetGreasePencilColor")
        node_add_menu.add_node_type(layout, "GeometryNodeSetGreasePencilDepth")
        node_add_menu.add_node_type(layout, "GeometryNodeSetGreasePencilSoftness")
        #node_add_menu.draw_assets_for_catalog(layout, "Grease Pencil/Write")


class NODE_MT_geometry_node_grease_pencil_operations(Menu):
    bl_idname = "NODE_MT_geometry_node_grease_pencil_operations"
    bl_label = "Operations"

    header_icon = "MODIFIER"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeGreasePencilToCurves")
        node_add_menu.add_node_type(layout, "GeometryNodeMergeLayers")
        #node_add_menu.draw_assets_for_catalog(layout, "Grease Pencil/Operations")


class NODE_MT_geometry_node_geometry(ColumnMenu, Menu):
    bl_idname = "NODE_MT_geometry_node_GEO_GEOMETRY"
    bl_label = "Geometry"

    def draw(self, _context):
        layout = self.layout.row()

        self.draw_column(layout, menus=(NODE_MT_geometry_node_geometry_read,))
        self.draw_column(layout, menus=(NODE_MT_geometry_node_geometry_write, NODE_MT_geometry_node_geometry_sample,))
        self.draw_column(layout, menus=(NODE_MT_geometry_node_geometry_operations,))
        
        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_geometry_node_geometry_read(Menu):
    bl_idname = "NODE_MT_geometry_node_GEO_GEOMETRY_READ"
    bl_label = "Read"

    header_icon = "COPYDOWN"

    def draw(self, context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeInputID")
        node_add_menu.add_node_type(layout, "GeometryNodeInputIndex")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "GeometryNodeInputNormal")
        node_add_menu.add_node_type(layout, "GeometryNodeInputPosition", search_weight=1.0)
        node_add_menu.add_node_type(layout, "GeometryNodeInputRadius")
        if context.space_data.geometry_nodes_type == 'TOOL':
            add_separator(layout)
            node_add_menu.add_node_type(layout, "GeometryNodeToolActiveElement")
            node_add_menu.add_node_type(layout, "GeometryNodeToolSelection")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "GeometryNodeInputNamedAttribute", search_weight=1.0)
        #node_add_menu.draw_assets_for_catalog(layout, "Geometry/Read")


class NODE_MT_geometry_node_geometry_write(Menu):
    bl_idname = "NODE_MT_geometry_node_GEO_GEOMETRY_WRITE"
    bl_label = "Write"

    header_icon = "CURRENT_FILE"

    def draw(self, context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeSetGeometryName")
        node_add_menu.add_node_type(layout, "GeometryNodeSetID")
        node_add_menu.add_node_type(layout, "GeometryNodeSetPosition", search_weight=1.0)
        if context.space_data.geometry_nodes_type == 'TOOL':
            node_add_menu.add_node_type(layout, "GeometryNodeToolSetSelection")
        #node_add_menu.draw_assets_for_catalog(layout, "Geometry/Write")


class NODE_MT_geometry_node_geometry_operations(Menu):
    bl_idname = "NODE_MT_geometry_node_GEO_GEOMETRY_OPERATIONS"
    bl_label = "Operations"

    header_icon = "MODIFIER"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeBake")
        node_add_menu.add_node_type(layout, "GeometryNodeBoundBox")
        node_add_menu.add_node_type(layout, "GeometryNodeConvexHull")
        node_add_menu.add_node_type(layout, "GeometryNodeDuplicateElements")
        node_add_menu.add_node_type(layout, "GeometryNodeMergeByDistance")
        node_add_menu.add_node_type(layout, "GeometryNodeSortElements")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "GeometryNodeDeleteGeometry")
        node_add_menu.add_node_type(layout, "GeometryNodeSeparateGeometry")
        node_add_menu.add_node_type(layout, "GeometryNodeTransform", search_weight=1.0)
        add_separator(layout)
        node_add_menu.add_node_type(layout, "GeometryNodeGeometryToInstance")
        node_add_menu.add_node_type(layout, "GeometryNodeJoinGeometry")
        node_add_menu.add_node_type(layout, "GeometryNodeSeparateComponents")
        node_add_menu.add_node_type(layout, "GeometryNodeSplitToInstances")

        #node_add_menu.draw_assets_for_catalog(layout, "Geometry/Operations")


class NODE_MT_geometry_node_geometry_sample(Menu):
    bl_idname = "NODE_MT_geometry_node_GEO_GEOMETRY_SAMPLE"
    bl_label = "Sample"

    header_icon = "DRIVER"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeProximity")
        node_add_menu.add_node_type(layout, "GeometryNodeIndexOfNearest")
        node_add_menu.add_node_type(layout, "GeometryNodeRaycast")
        node_add_menu.add_node_type(layout, "GeometryNodeSampleIndex")
        node_add_menu.add_node_type(layout, "GeometryNodeSampleNearest")
        #node_add_menu.draw_assets_for_catalog(layout, "Geometry/Sample")


class NODE_MT_geometry_node_primitives(ColumnMenu, Menu):
    bl_idname = "NODE_MT_category_GEO_PRIMITIVES"
    bl_label = "Primitives"

    def draw(self, _context):
        layout = self.layout.row()
        self.draw_column(layout, menus=(NODE_MT_geometry_node_primitives_mesh,))
        self.draw_column(layout, menus=(NODE_MT_geometry_node_primitives_curve,))


class NODE_MT_geometry_node_topology(ColumnMenu, Menu):
    bl_idname = "NODE_MT_category_GEO_TOPOLOGY"
    bl_label = "Topology"

    def draw(self, _context):
        layout = self.layout.row()
        self.draw_column(layout, menus=(NODE_MT_geometry_node_topology_mesh,))
        self.draw_column(layout, menus=(NODE_MT_geometry_node_topology_curve,))


class NODE_MT_geometry_node_input(ColumnMenu, Menu):
    bl_idname = "NODE_MT_geometry_node_GEO_INPUT"
    bl_label = "Input"

    def draw(self, context):
        layout = self.layout.row()

        self.draw_column(layout, menus=(NODE_MT_geometry_node_input_constant,))
        self.draw_column(layout, menus=(NODE_MT_geometry_node_input_gizmo, NODE_MT_geometry_node_input_import,))
        #self.draw_column(layout, menu_name="NODE_MT_geometry_node_input_group")
        self.draw_column(layout, menus=(NODE_MT_geometry_node_input_scene,))

        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_geometry_node_input_constant(Menu):
    bl_idname = "NODE_MT_geometry_node_GEO_INPUT_CONSTANT"
    bl_label = "Constant"
    bl_translation_context = i18n_contexts.id_nodetree

    header_icon = "CON_TRANSFORM"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "FunctionNodeInputBool")
        node_add_menu.add_node_type(layout, "FunctionNodeInputInt")
        node_add_menu.add_node_type(layout, "ShaderNodeValue")

        add_separator(layout)

        node_add_menu.add_node_type(layout, "FunctionNodeInputColor")
        node_add_menu.add_node_type(layout, "FunctionNodeInputRotation")
        node_add_menu.add_node_type(layout, "FunctionNodeInputVector")
        
        add_separator(layout)
        node_add_menu.add_node_type(layout, "GeometryNodeInputCollection")
        node_add_menu.add_node_type(layout, "GeometryNodeInputImage")
        node_add_menu.add_node_type(layout, "GeometryNodeInputMaterial")
        node_add_menu.add_node_type(layout, "GeometryNodeInputObject")
        node_add_menu.add_node_type(layout, "FunctionNodeInputString")

        #node_add_menu.draw_assets_for_catalog(layout, "Input/Constant")


class NODE_MT_geometry_node_input_group(Menu):
    bl_idname = "NODE_MT_category_GEO_GROUP"
    bl_label = "Group"

    header_icon = "NODETREE"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "NodeGroupInput")
        #node_add_menu.draw_assets_for_catalog(layout, "Input/Group")


class NODE_MT_geometry_node_input_scene(ColumnMenu, Menu):
    bl_idname = "NODE_MT_geometry_node_GEO_INPUT_SCENE"
    bl_label = "Scene"

    header_icon = "SCENE_DATA"

    def draw(self, context):
        layout = self.layout
        node_add_menu.add_node_type_with_outputs(context, layout, "GeometryNodeCameraInfo", ["Projection Matrix", "Focal Length", "Sensor", "Shift", "Clip Start", "Clip End", "Focus Distance", "Is Orthographic", "Orthographic Scale"])
        node_add_menu.add_node_type(layout, "GeometryNodeCollectionInfo")
        node_add_menu.add_node_type(layout, "GeometryNodeImageInfo")
        node_add_menu.add_node_type(layout, "GeometryNodeObjectInfo")

        add_separator(layout)
        node_add_menu.add_node_type(layout, "GeometryNodeInputActiveCamera")
        node_add_menu.add_node_type(layout, "GeometryNodeIsViewport")
        node_add_menu.add_node_type(layout, "GeometryNodeInputNamedLayerSelection")
        node_add_menu.add_node_type_with_outputs(context, layout, "GeometryNodeInputSceneTime", ["Frame", "Seconds"])
        node_add_menu.add_node_type(layout, "GeometryNodeSelfObject")

        if context.space_data.geometry_nodes_type == 'TOOL':
            add_separator(layout)
            node_add_menu.add_node_type(layout, "GeometryNodeTool3DCursor")
            node_add_menu.add_node_type_with_outputs(context, layout, "GeometryNodeToolMousePosition", ["Mouse X", "Mouse Y", "Region Width", "Region Height"])
            node_add_menu.add_node_type_with_outputs(context, layout, "GeometryNodeViewportTransform", ["Projection", "View", "Is Orthographic"])

        #node_add_menu.draw_assets_for_catalog(layout, "Input/Scene")


class NODE_MT_geometry_node_input_gizmo(Menu):
    bl_idname = "NODE_MT_geometry_node_GEO_INPUT_GIZMO"
    bl_label = "Gizmo"

    header_icon = "GIZMO"

    def draw(self, context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeGizmoDial")
        node_add_menu.add_node_type(layout, "GeometryNodeGizmoLinear")
        node_add_menu.add_node_type(layout, "GeometryNodeGizmoTransform")
        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_geometry_node_input_import(Menu):
    bl_idname = "NODE_MT_category_import"
    bl_label = "Import"

    header_icon = "IMPORT"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeImportCSV", label="CSV (.csv)")
        node_add_menu.add_node_type(layout, "GeometryNodeImportOBJ", label="Wavefront (.obj)")
        node_add_menu.add_node_type(layout, "GeometryNodeImportPLY", label="Stanford PLY (.ply)")
        node_add_menu.add_node_type(layout, "GeometryNodeImportSTL", label="STL (.stl)")
        node_add_menu.add_node_type(layout, "GeometryNodeImportText", label="Text (.txt)")
        node_add_menu.add_node_type(layout, "GeometryNodeImportVDB", label="OpenVDB (.vdb)")
        #node_add_menu.draw_assets_for_catalog(layout, "Input/Import")


class NODE_MT_geometry_node_instance(Menu):
    bl_idname = "NODE_MT_geometry_node_GEO_INSTANCE"
    bl_label = "Instances"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeInstanceOnPoints", search_weight=2.0)
        node_add_menu.add_node_type(layout, "GeometryNodeInstancesToPoints")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "GeometryNodeRealizeInstances", search_weight=1.0)
        node_add_menu.add_node_type(layout, "GeometryNodeRotateInstances")
        node_add_menu.add_node_type(layout, "GeometryNodeScaleInstances")
        node_add_menu.add_node_type(layout, "GeometryNodeTranslateInstances")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "GeometryNodeInputInstanceBounds")
        node_add_menu.add_node_type(layout, "GeometryNodeInputInstanceRotation")
        node_add_menu.add_node_type(layout, "GeometryNodeInputInstanceScale")
        node_add_menu.add_node_type(layout, "GeometryNodeInstanceTransform")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "GeometryNodeSetInstanceTransform")

        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_geometry_node_material(Menu):
    bl_idname = "NODE_MT_geometry_node_GEO_MATERIAL"
    bl_label = "Material"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeReplaceMaterial")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "GeometryNodeInputMaterialIndex")
        node_add_menu.add_node_type(layout, "GeometryNodeMaterialSelection")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "GeometryNodeSetMaterial", search_weight=1.0)
        node_add_menu.add_node_type(layout, "GeometryNodeSetMaterialIndex")
        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_geometry_node_mesh(ColumnMenu, Menu):
    bl_idname = "NODE_MT_geometry_node_GEO_MESH"
    bl_label = "Mesh"

    def draw(self, _context):
        layout = self.layout.row()

        self.draw_column(layout, menus=(NODE_MT_geometry_node_mesh_read,))
        self.draw_column(layout, menus=(
            NODE_MT_geometry_node_mesh_write, 
            NODE_MT_geometry_node_mesh_sample, 
            NODE_MT_geometry_node_mesh_uv,
            ))

        self.draw_column(layout, menus=(NODE_MT_geometry_node_mesh_operations,))
        
        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_geometry_node_mesh_read(Menu):
    bl_idname = "NODE_MT_geometry_node_GEO_MESH_READ"
    bl_label = "Read"

    header_icon = "COPYDOWN"

    def draw(self, context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeInputMeshVertexNeighbors")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "GeometryNodeInputMeshEdgeAngle")
        node_add_menu.add_node_type(layout, "GeometryNodeInputMeshEdgeNeighbors")
        node_add_menu.add_node_type(layout, "GeometryNodeInputMeshEdgeVertices")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "GeometryNodeInputMeshFaceArea")
        node_add_menu.add_node_type(layout, "GeometryNodeInputMeshFaceNeighbors")
        if context.space_data.geometry_nodes_type == 'TOOL':
            node_add_menu.add_node_type(layout, "GeometryNodeToolFaceSet")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "GeometryNodeInputMeshFaceIsPlanar")
        node_add_menu.add_node_type(layout, "GeometryNodeInputShadeSmooth")
        node_add_menu.add_node_type(layout, "GeometryNodeInputEdgeSmooth")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "GeometryNodeEdgesToFaceGroups")
        node_add_menu.add_node_type(layout, "GeometryNodeMeshFaceSetBoundaries")
        node_add_menu.add_node_type(layout, "GeometryNodeInputMeshIsland")
        node_add_menu.add_node_type(layout, "GeometryNodeInputShortestEdgePaths")
        #node_add_menu.draw_assets_for_catalog(layout, "Mesh/Read")


class NODE_MT_geometry_node_mesh_sample(Menu):
    bl_idname = "NODE_MT_geometry_node_GEO_MESH_SAMPLE"
    bl_label = "Sample"

    header_icon = "DRIVER"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeSampleNearestSurface")
        node_add_menu.add_node_type(layout, "GeometryNodeSampleUVSurface")
        #node_add_menu.draw_assets_for_catalog(layout, "Mesh/Sample")


class NODE_MT_geometry_node_mesh_write(Menu):
    bl_idname = "NODE_MT_geometry_node_GEO_MESH_WRITE"
    bl_label = "Write"

    header_icon = "CURRENT_FILE"

    def draw(self, context):
        layout = self.layout
        if context.space_data.geometry_nodes_type == 'TOOL':
            node_add_menu.add_node_type(layout, "GeometryNodeToolSetFaceSet")
        node_add_menu.add_node_type(layout, "GeometryNodeSetMeshNormal")
        node_add_menu.add_node_type(layout, "GeometryNodeSetShadeSmooth")
        #node_add_menu.draw_assets_for_catalog(layout, "Mesh/Write")


class NODE_MT_geometry_node_mesh_operations(Menu):
    bl_idname = "NODE_MT_geometry_node_GEO_MESH_OPERATIONS"
    bl_label = "Operations"

    header_icon = "MODIFIER"

    def draw(self, context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeMeshToCurve")
        if context.preferences.experimental.use_new_volume_nodes:
            node_add_menu.add_node_type(layout, "GeometryNodeMeshToDensityGrid")
        node_add_menu.add_node_type(layout, "GeometryNodeMeshToPoints")
        if context.preferences.experimental.use_new_volume_nodes:
            node_add_menu.add_node_type(layout, "GeometryNodeMeshToSDFGrid")
        node_add_menu.add_node_type(layout, "GeometryNodeMeshToVolume")
            
        add_separator(layout)
        node_add_menu.add_node_type(layout, "GeometryNodeDualMesh")
        node_add_menu.add_node_type(layout, "GeometryNodeExtrudeMesh")
        node_add_menu.add_node_type(layout, "GeometryNodeFlipFaces")
        node_add_menu.add_node_type(layout, "GeometryNodeMeshBoolean")
        node_add_menu.add_node_type(layout, "GeometryNodeScaleElements")
        node_add_menu.add_node_type(layout, "GeometryNodeSplitEdges")
        node_add_menu.add_node_type(layout, "GeometryNodeSubdivideMesh")
        node_add_menu.add_node_type(layout, "GeometryNodeSubdivisionSurface")
        node_add_menu.add_node_type(layout, "GeometryNodeTriangulate")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "GeometryNodeEdgePathsToCurves")
        node_add_menu.add_node_type(layout, "GeometryNodeEdgePathsToSelection")
        #node_add_menu.draw_assets_for_catalog(layout, "Mesh/Operations")


class NODE_MT_geometry_node_primitives_mesh(Menu):
    bl_idname = "NODE_MT_category_PRIMITIVES_MESH"
    bl_label = "Mesh"

    header_icon = "MESH_DATA"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeMeshCone")
        node_add_menu.add_node_type(layout, "GeometryNodeMeshCube")
        node_add_menu.add_node_type(layout, "GeometryNodeMeshCylinder")
        node_add_menu.add_node_type(layout, "GeometryNodeMeshGrid")
        node_add_menu.add_node_type(layout, "GeometryNodeMeshIcoSphere")
        node_add_menu.add_node_type(layout, "GeometryNodeMeshCircle")
        node_add_menu.add_node_type(layout, "GeometryNodeMeshLine")
        node_add_menu.add_node_type(layout, "GeometryNodeMeshUVSphere")
        #node_add_menu.draw_assets_for_catalog(layout, "Mesh/Primitives")


class NODE_MT_geometry_node_topology_mesh(Menu):
    bl_idname = "NODE_MT_geometry_node_mesh_topology"
    bl_label = "Mesh"

    header_icon = "MESH_DATA"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeCornersOfEdge")
        node_add_menu.add_node_type(layout, "GeometryNodeCornersOfFace")
        node_add_menu.add_node_type(layout, "GeometryNodeCornersOfVertex")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "GeometryNodeEdgesOfCorner")
        node_add_menu.add_node_type(layout, "GeometryNodeEdgesOfVertex")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "GeometryNodeFaceOfCorner")
        node_add_menu.add_node_type(layout, "GeometryNodeOffsetCornerInFace")
        node_add_menu.add_node_type(layout, "GeometryNodeVertexOfCorner")
        #node_add_menu.draw_assets_for_catalog(layout, "Mesh/Topology")


class NODE_MT_geometry_node_output(Menu):
    bl_idname = "NODE_MT_category_GEO_OUTPUT"
    bl_label = "Output"

    def draw(self, context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "NodeGroupOutput")
        node_add_menu.add_node_type(layout, "GeometryNodeViewer")
        node_add_menu.add_node_type_with_searchable_enum(context, layout, "GeometryNodeWarning", "warning_type")
        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_geometry_node_point(Menu):
    bl_idname = "NODE_MT_category_GEO_POINT"
    bl_label = "Point"

    def draw(self, context):
        layout = self.layout
        if context.preferences.experimental.use_new_volume_nodes:
            node_add_menu.add_node_type(layout, "GeometryNodeDistributePointsInGrid")
        node_add_menu.add_node_type(layout, "GeometryNodeDistributePointsInVolume")
        node_add_menu.add_node_type(layout, "GeometryNodeDistributePointsOnFaces")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "GeometryNodePoints")
        node_add_menu.add_node_type(layout, "GeometryNodePointsToCurves")        
        if context.preferences.experimental.use_new_volume_nodes:
            node_add_menu.add_node_type(layout, "GeometryNodePointsToSDFGrid")
        node_add_menu.add_node_type(layout, "GeometryNodePointsToVertices")
        node_add_menu.add_node_type(layout, "GeometryNodePointsToVolume")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "GeometryNodeSetPointRadius")
        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_geometry_node_simulation(Menu):
    bl_idname = "NODE_MT_category_simulation"
    bl_label = "Simulation"

    def draw(self, _context):
        layout = self.layout
        #node_add_menu.add_simulation_zone(layout, label="Simulation Zone")
        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_geometry_node_utilities_text(Menu):
    bl_idname = "NODE_MT_category_GEO_TEXT"
    bl_label = "Text"

    header_icon = "OUTLINER_OB_FONT"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeStringJoin")
        node_add_menu.add_node_type(layout, "FunctionNodeMatchString")
        node_add_menu.add_node_type(layout, "FunctionNodeReplaceString")
        node_add_menu.add_node_type(layout, "FunctionNodeSliceString")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "FunctionNodeFindInString")
        node_add_menu.add_node_type(layout, "FunctionNodeFormatString")
        node_add_menu.add_node_type(layout, "FunctionNodeStringLength")
        node_add_menu.add_node_type(layout, "GeometryNodeStringToCurves")
        node_add_menu.add_node_type(layout, "FunctionNodeValueToString")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "FunctionNodeInputSpecialCharacters")
        #node_add_menu.draw_assets_for_catalog(layout, "Utilities/Text")


class NODE_MT_geometry_node_texture(Menu):
    bl_idname = "NODE_MT_category_GEO_TEXTURE"
    bl_label = "Texture"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeImageTexture")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "ShaderNodeTexNoise")
        node_add_menu.add_node_type(layout, "ShaderNodeTexWhiteNoise")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "ShaderNodeTexBrick")
        node_add_menu.add_node_type(layout, "ShaderNodeTexChecker")
        node_add_menu.add_node_type(layout, "ShaderNodeTexGabor")
        node_add_menu.add_node_type(layout, "ShaderNodeTexGradient")
        node_add_menu.add_node_type(layout, "ShaderNodeTexMagic")
        node_add_menu.add_node_type(layout, "ShaderNodeTexVoronoi")
        node_add_menu.add_node_type(layout, "ShaderNodeTexWave")
        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_geometry_node_utilities(ColumnMenu, Menu):
    bl_idname = "NODE_MT_category_GEO_UTILITIES"
    bl_label = "Utilities"

    def draw(self, _context):
        layout = self.layout.row()

        self.draw_column(layout, menus=(NODE_MT_geometry_node_utilities_color, NODE_MT_geometry_node_utilities_vector,))
        self.draw_column(layout, menus=(NODE_MT_geometry_node_utilities_text, NODE_MT_geometry_node_utilities_field,))
        self.draw_column(layout, menus=(NODE_MT_geometry_node_utilities_math, NODE_MT_geometry_node_utilities_misc))

        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_geometry_node_utilities_misc(Menu):
    bl_idname = "NODE_MT_geometry_node_utilities_misc"
    bl_label = "Miscellaneous"
        
    header_icon = "COLLAPSEMENU"

    def draw(self, context):
        layout = self.layout
        #node_add_menu.add_foreach_geometry_element_zone(layout, label="For Each Element Zone")
        #node_add_menu.add_node_type(layout, "GeometryNodeIndexSwitch")
        #node_add_menu.add_node_type(layout, "GeometryNodeMenuSwitch")
        node_add_menu.add_node_type(layout, "FunctionNodeRandomValue")
        #node_add_menu.add_repeat_zone(layout, label="Repeat Zone")
        #node_add_menu.add_node_type(layout, "GeometryNodeSwitch")

        if context.preferences.experimental.use_bundle_and_closure_nodes:
            add_separator(layout)
            node_add_menu.add_closure_zone(layout, label="Closure")
            node_add_menu.add_node_type(layout, "GeometryNodeEvaluateClosure")
            node_add_menu.add_node_type(layout, "GeometryNodeCombineBundle")
            node_add_menu.add_node_type(layout, "GeometryNodeSeparateBundle")
        #node_add_menu.draw_assets_for_catalog(layout, "Utilities/Miscellaneous")


class NODE_MT_geometry_node_utilities_field(Menu):
    bl_idname = "NODE_MT_category_GEO_UTILITIES_FIELD"
    bl_label = "Field"

    header_icon = "LIGHTPROBE_PLANE"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeAccumulateField")
        node_add_menu.add_node_type(layout, "GeometryNodeFieldAtIndex")
        node_add_menu.add_node_type(layout, "GeometryNodeFieldOnDomain")
        node_add_menu.add_node_type(layout, "GeometryNodeFieldAverage")
        node_add_menu.add_node_type(layout, "GeometryNodeFieldMinAndMax")
        node_add_menu.add_node_type(layout, "GeometryNodeFieldVariance")
        #node_add_menu.draw_assets_for_catalog(layout, "Utilities/Field")


class NODE_MT_geometry_node_rotation(Menu):
    bl_idname = "NODE_MT_category_GEO_UTILITIES_ROTATION"
    bl_label = "Rotation"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "FunctionNodeAlignRotationToVector")
        node_add_menu.add_node_type(layout, "FunctionNodeAxesToRotation")
        node_add_menu.add_node_type(layout, "FunctionNodeInvertRotation")
        props = node_add_menu.add_node_type(layout, "ShaderNodeMix", label=iface_("Mix Rotation"))
        ops = props.settings.add()
        ops.name = "data_type"
        ops.value = "'ROTATION'"
        node_add_menu.add_node_type(layout, "FunctionNodeRotateRotation")
        node_add_menu.add_node_type(layout, "FunctionNodeRotateVector")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "FunctionNodeAxisAngleToRotation")
        node_add_menu.add_node_type(layout, "FunctionNodeEulerToRotation")
        node_add_menu.add_node_type(layout, "FunctionNodeQuaternionToRotation")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "FunctionNodeRotationToAxisAngle")
        node_add_menu.add_node_type(layout, "FunctionNodeRotationToEuler")
        node_add_menu.add_node_type(layout, "FunctionNodeRotationToQuaternion")
        #node_add_menu.draw_assets_for_catalog(layout, "Utilities/Rotation")

class NODE_MT_geometry_node_matrix(Menu):
    bl_idname = "NODE_MT_category_utilities_matrix"
    bl_label = "Matrix"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "FunctionNodeCombineTransform")
        node_add_menu.add_node_type(layout, "FunctionNodeSeparateTransform")

        add_separator(layout)
        node_add_menu.add_node_type(layout, "FunctionNodeCombineMatrix")
        node_add_menu.add_node_type(layout, "FunctionNodeMatrixDeterminant", label="Determinant")
        node_add_menu.add_node_type(layout, "FunctionNodeInvertMatrix")
        node_add_menu.add_node_type(layout, "FunctionNodeSeparateMatrix")
        node_add_menu.add_node_type(layout, "FunctionNodeTransposeMatrix")
        
        add_separator(layout)
        node_add_menu.add_node_type(layout, "FunctionNodeMatrixMultiply")
        
        add_separator(layout)
        node_add_menu.add_node_type(layout, "FunctionNodeProjectPoint")
        node_add_menu.add_node_type(layout, "FunctionNodeTransformDirection")
        node_add_menu.add_node_type(layout, "FunctionNodeTransformPoint")
        
        #node_add_menu.draw_assets_for_catalog(layout, "Utilities/Matrix")


class NODE_MT_geometry_node_utilities_math(Menu):
    bl_idname = "NODE_MT_category_GEO_UTILITIES_MATH"
    bl_label = "Math"

    header_icon = "CON_TRANSFORM_CACHE"

    def draw(self, context):
        layout = self.layout        
        node_add_menu.add_node_type_with_searchable_enum(context, layout, "FunctionNodeBitMath", "operation", search_weight=-1.0)
        node_add_menu.add_node_type_with_searchable_enum(context, layout, "FunctionNodeBooleanMath", "operation")
        node_add_menu.add_node_type_with_searchable_enum(context, layout, "FunctionNodeIntegerMath", "operation")
        node_add_menu.add_node_type_with_searchable_enum(context, layout, "ShaderNodeMath", "operation")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "ShaderNodeClamp")
        node_add_menu.add_node_type(layout, "FunctionNodeCompare")
        node_add_menu.add_node_type(layout, "ShaderNodeFloatCurve")
        node_add_menu.add_node_type(layout, "FunctionNodeFloatToInt")
        node_add_menu.add_node_type(layout, "FunctionNodeHashValue")
        node_add_menu.add_node_type(layout, "ShaderNodeMapRange")
        node_add_menu.add_node_type(layout, "ShaderNodeMix")
        #node_add_menu.draw_assets_for_catalog(layout, "Utilities/Math")


class NODE_MT_geometry_node_mesh_uv(Menu):
    bl_idname = "NODE_MT_category_GEO_UV"
    bl_label = "UV"

    header_icon = "UV"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeUVPackIslands")
        node_add_menu.add_node_type(layout, "GeometryNodeUVUnwrap")
        #node_add_menu.draw_assets_for_catalog(layout, "Mesh/UV")


class NODE_MT_geometry_node_utilities_vector(Menu):
    bl_idname = "NODE_MT_category_GEO_VECTOR"
    bl_label = "Vector"

    header_icon = "ORIENTATION_GLOBAL"

    def draw(self, context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "ShaderNodeVectorCurve")
        node_add_menu.add_node_type_with_searchable_enum(context, layout, "ShaderNodeVectorMath", "operation")
        node_add_menu.add_node_type(layout, "ShaderNodeVectorRotate")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "ShaderNodeCombineXYZ")
        props = node_add_menu.add_node_type(layout, "ShaderNodeMix", label=iface_("Mix Vector"))
        ops = props.settings.add()
        ops.name = "data_type"
        ops.value = "'VECTOR'"
        node_add_menu.add_node_type(layout, "ShaderNodeSeparateXYZ")
        #node_add_menu.draw_assets_for_catalog(layout, "Utilities/Vector")


class NODE_MT_geometry_node_volume(ColumnMenu, Menu):
    bl_idname = "NODE_MT_category_GEO_VOLUME"
    bl_label = "Volume"
    bl_translation_context = i18n_contexts.id_id

    def draw(self, context):
        layout = self.layout
        if not context.preferences.experimental.use_new_volume_nodes:
            node_add_menu.add_node_type(layout, "GeometryNodeVolumeCube")
            node_add_menu.add_node_type(layout, "GeometryNodeVolumeToMesh")
        else:
            layout = layout.row()

            self.draw_column(layout, menus=(
                NODE_MT_geometry_node_volume_read,
                NODE_MT_geometry_node_volume_write,
                NODE_MT_geometry_node_volume_sample,
                ))
            
            self.draw_column(layout, menus=(
                NODE_MT_geometry_node_volume_operations, 
                NODE_MT_geometry_node_volume_primitives,
                ))
        
        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_geometry_node_volume_read(Menu):
    bl_idname = "NODE_MT_geometry_node_GEO_VOLUME_READ"
    bl_label = "Read"

    header_icon = "COPYDOWN"

    def draw(self, context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeGetNamedGrid")
        node_add_menu.add_node_type(layout, "GeometryNodeGridInfo")
        #node_add_menu.draw_assets_for_catalog(layout, "Volume/Read")


class NODE_MT_geometry_node_volume_write(Menu):
    bl_idname = "NODE_MT_geometry_node_GEO_VOLUME_WRITE"
    bl_label = "Write"

    header_icon = "CURRENT_FILE"

    def draw(self, context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeStoreNamedGrid")
        #node_add_menu.draw_assets_for_catalog(layout, "Volume/Write")


class NODE_MT_geometry_node_volume_sample(Menu):
    bl_idname = "NODE_MT_geometry_node_volume_sample"
    bl_label = "Sample"

    header_icon = "DRIVER"

    def draw(self, context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeSampleGrid")
        node_add_menu.add_node_type(layout, "GeometryNodeSampleGridIndex")
        #node_add_menu.draw_assets_for_catalog(layout, "Volume/Sample")


class NODE_MT_geometry_node_volume_operations(Menu):
    bl_idname = "NODE_MT_geometry_node_GEO_VOLUME_OPERATIONS"
    bl_label = "Operations"

    header_icon = "MODIFIER"

    def draw(self, context):
        layout = self.layout
        if context.preferences.experimental.use_new_volume_nodes:
            node_add_menu.add_node_type(layout, "GeometryNodeGridToMesh")
            node_add_menu.add_node_type(layout, "GeometryNodeSDFGridBoolean")
        node_add_menu.add_node_type(layout, "GeometryNodeVolumeToMesh")

        #node_add_menu.draw_assets_for_catalog(layout, "Volume/Operations")


class NODE_MT_geometry_node_volume_primitives(Menu):
    bl_idname = "NODE_MT_geometry_node_GEO_VOLUME_PRIMITIVES"
    bl_label = "Primitives"

    header_icon = "OUTLINER_DATA_VOLUME"

    def draw(self, context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeVolumeCube")
        #node_add_menu.draw_assets_for_catalog(layout, "Volume/Primitives")


class NODE_MT_geometry_node_switch(Menu):
    bl_idname = "NODE_MT_geometry_node_switch"
    bl_label = "Switches"

    header_icon = "STICKY_UVS_LOC"

    def draw(self, context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeIndexSwitch")
        node_add_menu.add_node_type(layout, "GeometryNodeMenuSwitch")
        node_add_menu.add_node_type(layout, "GeometryNodeSwitch")


class NODE_MT_geometry_node_zones(Menu):
    bl_idname = "NODE_MT_geometry_node_zones"
    bl_label = "Zones"

    header_icon = "STICKY_UVS_LOC"

    def draw(self, context):
        layout = self.layout
        node_add_menu.add_foreach_geometry_element_zone(layout, label="For Each Element")
        node_add_menu.add_repeat_zone(layout, label="Repeat")
        node_add_menu.add_simulation_zone(layout, label="Simulation")


class NODE_MT_geometry_node_group(Menu):
    bl_idname = "NODE_MT_geometry_node_GEO_GROUP"
    bl_label = "Group"

    def draw(self, context):
        layout = self.layout
        draw_node_group_add_menu(context, layout)
        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_geometry_node_add_all(Menu):
    bl_idname = __qualname__
    bl_label = ""

    def draw(self, context):
        layout = self.layout
        layout.menu("NODE_MT_geometry_node_GEO_ATTRIBUTE")
        layout.menu("NODE_MT_geometry_node_GEO_INPUT")
        layout.menu("NODE_MT_category_GEO_OUTPUT")
        add_separator(layout)
        layout.menu("NODE_MT_geometry_node_GEO_GEOMETRY")
        add_separator(layout)
        layout.menu("NODE_MT_geometry_node_GEO_CURVE")
        layout.menu("NODE_MT_geometry_node_grease_pencil")
        layout.menu("NODE_MT_geometry_node_GEO_INSTANCE")
        layout.menu("NODE_MT_geometry_node_GEO_MESH")
        layout.menu("NODE_MT_category_GEO_POINT")
        layout.menu("NODE_MT_category_GEO_VOLUME")
        add_separator(layout)
        layout.menu("NODE_MT_category_GEO_PRIMITIVES")
        layout.menu("NODE_MT_category_GEO_TOPOLOGY")
        add_separator(layout)
        layout.menu("NODE_MT_geometry_node_GEO_MATERIAL")
        layout.menu("NODE_MT_category_utilities_matrix")
        layout.menu("NODE_MT_category_GEO_UTILITIES_ROTATION")
        layout.menu("NODE_MT_category_GEO_TEXTURE")
        layout.menu("NODE_MT_category_GEO_UTILITIES")
        add_separator(layout)
        layout.menu("NODE_MT_geometry_node_switch")
        layout.menu("NODE_MT_geometry_node_zones")
        add_separator(layout)
        layout.menu("NODE_MT_geometry_node_GEO_GROUP")
        layout.menu("NODE_MT_category_layout")
        add_separator(layout)

        if fetch_user_preferences("show_deprecated_menu"):
            layout.menu("NODE_MT_category_GEO_UTILITIES_DEPRECATED", icon="INFO")
            add_separator(layout)
        
        draw_asset_menu(layout)


class NODE_MT_geometry_node_deprecated(Menu):
    bl_idname = "NODE_MT_category_GEO_UTILITIES_DEPRECATED"
    bl_label = "Deprecated"

    def draw(self, context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "FunctionNodeAlignEulerToVector")
        node_add_menu.add_node_type(layout, "FunctionNodeRotateEuler")
        
        #node_add_menu.draw_assets_for_catalog(layout, "Utilities/Deprecated")


classes = (
    NODE_MT_geometry_node_add_all,
    NODE_MT_geometry_node_attribute,
    NODE_MT_geometry_node_input,
    NODE_MT_geometry_node_input_constant,
    NODE_MT_geometry_node_input_gizmo,
    NODE_MT_geometry_node_input_import,
    #NODE_MT_geometry_node_input_group,
    NODE_MT_geometry_node_input_scene,
    NODE_MT_geometry_node_output,
    NODE_MT_geometry_node_geometry,
    NODE_MT_geometry_node_geometry_read,
    NODE_MT_geometry_node_geometry_write,
    NODE_MT_geometry_node_geometry_sample,
    NODE_MT_geometry_node_geometry_operations,
    NODE_MT_geometry_node_curve,
    NODE_MT_geometry_node_curve_read,
    NODE_MT_geometry_node_curve_sample,
    NODE_MT_geometry_node_curve_write,
    NODE_MT_geometry_node_curve_operations,
    NODE_MT_geometry_node_grease_pencil,
    NODE_MT_geometry_node_grease_pencil_read,
    NODE_MT_geometry_node_grease_pencil_write,
    NODE_MT_geometry_node_grease_pencil_operations,
    NODE_MT_geometry_node_instance,
    NODE_MT_geometry_node_mesh,
    NODE_MT_geometry_node_mesh_read,
    NODE_MT_geometry_node_mesh_write,
    NODE_MT_geometry_node_mesh_sample,
    NODE_MT_geometry_node_mesh_uv,
    NODE_MT_geometry_node_mesh_operations,
    NODE_MT_geometry_node_point,
    NODE_MT_geometry_node_volume,
    NODE_MT_geometry_node_volume_read,
    NODE_MT_geometry_node_volume_write,
    NODE_MT_geometry_node_volume_sample,
    NODE_MT_geometry_node_volume_operations,
    NODE_MT_geometry_node_volume_primitives,
    NODE_MT_geometry_node_primitives,
    NODE_MT_geometry_node_primitives_mesh,
    NODE_MT_geometry_node_primitives_curve,
    NODE_MT_geometry_node_topology,
    NODE_MT_geometry_node_topology_mesh,
    NODE_MT_geometry_node_topology_curve,
    NODE_MT_geometry_node_simulation,
    NODE_MT_geometry_node_material,
    NODE_MT_geometry_node_matrix,
    NODE_MT_geometry_node_rotation,
    NODE_MT_geometry_node_texture,
    NODE_MT_geometry_node_utilities,
    NODE_MT_geometry_node_utilities_color,
    NODE_MT_geometry_node_utilities_vector,
    NODE_MT_geometry_node_utilities_text,
    NODE_MT_geometry_node_utilities_field,
    NODE_MT_geometry_node_utilities_math,
    NODE_MT_geometry_node_utilities_misc,
    NODE_MT_geometry_node_switch,
    NODE_MT_geometry_node_zones,
    NODE_MT_geometry_node_group,
    NODE_MT_geometry_node_deprecated,
)

if __name__ == "__main__":  # only for live edit.
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
