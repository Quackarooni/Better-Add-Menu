# SPDX-FileCopyrightText: 2022-2023 Blender Authors
#
# SPDX-License-Identifier: GPL-2.0-or-later

import bpy
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

class NODE_MT_geometry_node_attribute(Menu):
    bl_idname = "NODE_MT_geometry_node_attribute"
    bl_label = "Attribute"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeAttributeStatistic")
        node_add_menu.add_node_type(layout, "GeometryNodeAttributeDomainSize")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "GeometryNodeBlurAttribute")
        node_add_menu.add_node_type(layout, "GeometryNodeCaptureAttribute")
        node_add_menu.add_node_type(layout, "GeometryNodeRemoveAttribute")
        node_add_menu.add_node_type(layout, "GeometryNodeStoreNamedAttribute")
        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_geometry_node_color(Menu):
    bl_idname = "NODE_MT_geometry_node_color"
    bl_label = "Color"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "ShaderNodeValToRGB")
        node_add_menu.add_node_type(layout, "ShaderNodeRGBCurve")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "FunctionNodeCombineColor")
        props = node_add_menu.add_node_type(layout, "ShaderNodeMix", label=iface_("Mix Color"))
        ops = props.settings.add()
        ops.name = "data_type"
        ops.value = "'RGBA'"
        node_add_menu.add_node_type(layout, "FunctionNodeSeparateColor")
        #node_add_menu.draw_assets_for_catalog(layout, "Utilities/Color")


class NODE_MT_geometry_node_curve(ColumnMenu, Menu):
    bl_idname = "NODE_MT_geometry_node_curve"
    bl_label = "Curve"

    def draw(self, _context):
        layout = self.layout.row()

        self.draw_column(layout, menus=(NODE_MT_geometry_node_curve_read,))
        self.draw_column(layout, menus=(NODE_MT_geometry_node_curve_write, NODE_MT_geometry_node_curve_sample,))
        self.draw_column(layout, menus=(NODE_MT_geometry_node_curve_operations,))
        
        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_geometry_node_curve_read(Menu):
    bl_idname = "NODE_MT_geometry_node_curve_read"
    bl_label = "Read"

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
    bl_idname = "NODE_MT_geometry_node_curve_sample"
    bl_label = "Sample"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeSampleCurve")
        #node_add_menu.draw_assets_for_catalog(layout, "Curve/Sample")


class NODE_MT_geometry_node_curve_write(Menu):
    bl_idname = "NODE_MT_geometry_node_curve_write"
    bl_label = "Write"

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
    bl_idname = "NODE_MT_geometry_node_curve_operations"
    bl_label = "Operations"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeCurveToMesh")
        node_add_menu.add_node_type(layout, "GeometryNodeCurveToPoints")
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
    bl_idname = "NODE_MT_geometry_node_primitives_curve"
    bl_label = "Curve"

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


class NODE_MT_geometry_node_curve_topology(Menu):
    bl_idname = "NODE_MT_geometry_node_curve_topology"
    bl_label = "Curve"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeCurveOfPoint")
        node_add_menu.add_node_type(layout, "GeometryNodeOffsetPointInCurve")
        node_add_menu.add_node_type(layout, "GeometryNodePointsOfCurve")
        #node_add_menu.draw_assets_for_catalog(layout, "Curve/Topology")


class NODE_MT_geometry_node_geometry(ColumnMenu, Menu):
    bl_idname = "NODE_MT_geometry_node_geometry"
    bl_label = "Geometry"

    def draw(self, _context):
        layout = self.layout.row()

        self.draw_column(layout, menus=(NODE_MT_geometry_node_geometry_read,))
        self.draw_column(layout, menus=(NODE_MT_geometry_node_geometry_write, NODE_MT_geometry_node_geometry_sample,))
        self.draw_column(layout, menus=(NODE_MT_geometry_node_geometry_operations,))
        
        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_geometry_node_geometry_read(Menu):
    bl_idname = "NODE_MT_geometry_node_geometry_read"
    bl_label = "Read"

    def draw(self, context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeInputID")
        node_add_menu.add_node_type(layout, "GeometryNodeInputIndex")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "GeometryNodeInputNormal")
        node_add_menu.add_node_type(layout, "GeometryNodeInputPosition")
        node_add_menu.add_node_type(layout, "GeometryNodeInputRadius")
        if context.space_data.geometry_nodes_type == 'TOOL':
            node_add_menu.add_node_type(layout, "GeometryNodeToolSelection")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "GeometryNodeInputNamedAttribute")
        #node_add_menu.draw_assets_for_catalog(layout, "Geometry/Read")


class NODE_MT_geometry_node_geometry_write(Menu):
    bl_idname = "NODE_MT_geometry_node_geometry_write"
    bl_label = "Write"

    def draw(self, context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeSetID")
        node_add_menu.add_node_type(layout, "GeometryNodeSetPosition")
        if context.space_data.geometry_nodes_type == 'TOOL':
            node_add_menu.add_node_type(layout, "GeometryNodeToolSetSelection")
        #node_add_menu.draw_assets_for_catalog(layout, "Geometry/Write")


class NODE_MT_geometry_node_geometry_operations(Menu):
    bl_idname = "NODE_MT_geometry_node_geometry_operations"
    bl_label = "Operations"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeBoundBox")
        node_add_menu.add_node_type(layout, "GeometryNodeConvexHull")
        node_add_menu.add_node_type(layout, "GeometryNodeDuplicateElements")
        node_add_menu.add_node_type(layout, "GeometryNodeMergeByDistance")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "GeometryNodeDeleteGeometry")
        node_add_menu.add_node_type(layout, "GeometryNodeSeparateGeometry")
        node_add_menu.add_node_type(layout, "GeometryNodeTransform")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "GeometryNodeGeometryToInstance")
        node_add_menu.add_node_type(layout, "GeometryNodeJoinGeometry")
        node_add_menu.add_node_type(layout, "GeometryNodeSeparateComponents")

        #node_add_menu.draw_assets_for_catalog(layout, "Geometry/Operations")


class NODE_MT_geometry_node_geometry_sample(Menu):
    bl_idname = "NODE_MT_geometry_node_geometry_sample"
    bl_label = "Sample"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeProximity")
        node_add_menu.add_node_type(layout, "GeometryNodeIndexOfNearest")
        node_add_menu.add_node_type(layout, "GeometryNodeRaycast")
        node_add_menu.add_node_type(layout, "GeometryNodeSampleIndex")
        node_add_menu.add_node_type(layout, "GeometryNodeSampleNearest")
        #node_add_menu.draw_assets_for_catalog(layout, "Geometry/Sample")


class NODE_MT_geometry_node_primitives(ColumnMenu, Menu):
    bl_idname = "NODE_MT_geometry_node_primitives"
    bl_label = "Primitives"

    def draw(self, _context):
        layout = self.layout.row()
        self.draw_column(layout, menus=(NODE_MT_geometry_node_primitives_mesh,))
        self.draw_column(layout, menus=(NODE_MT_geometry_node_primitives_curve,))


class NODE_MT_geometry_node_topology(ColumnMenu, Menu):
    bl_idname = "NODE_MT_geometry_node_topology"
    bl_label = "Topology"

    def draw(self, _context):
        layout = self.layout.row()
        self.draw_column(layout, menus=(NODE_MT_geometry_node_mesh_topology,))
        self.draw_column(layout, menus=(NODE_MT_geometry_node_curve_topology,))


class NODE_MT_geometry_node_input(ColumnMenu, Menu):
    bl_idname = "NODE_MT_geometry_node_input"
    bl_label = "Input"

    def draw(self, _context):
        layout = self.layout.row()

        self.draw_column(layout, menus=(NODE_MT_geometry_node_input_constant,))
        #self.draw_column(layout, menu_name="NODE_MT_geometry_node_input_group")
        self.draw_column(layout, menus=(NODE_MT_geometry_node_input_scene,))

        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_geometry_node_input_constant(Menu):
    bl_idname = "NODE_MT_geometry_node_input_constant"
    bl_label = "Constant"
    bl_translation_context = i18n_contexts.id_nodetree

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "FunctionNodeInputBool")
        node_add_menu.add_node_type(layout, "FunctionNodeInputInt")
        node_add_menu.add_node_type(layout, "ShaderNodeValue")

        add_separator(layout)

        node_add_menu.add_node_type(layout, "FunctionNodeInputColor")
        node_add_menu.add_node_type(layout, "FunctionNodeInputVector")
        
        add_separator(layout)

        node_add_menu.add_node_type(layout, "GeometryNodeInputImage")
        node_add_menu.add_node_type(layout, "GeometryNodeInputMaterial")
        node_add_menu.add_node_type(layout, "FunctionNodeInputString")

        #node_add_menu.draw_assets_for_catalog(layout, "Input/Constant")


class NODE_MT_geometry_node_input_group(Menu):
    bl_idname = "NODE_MT_geometry_node_input_group"
    bl_label = "Group"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "NodeGroupInput")
        #node_add_menu.draw_assets_for_catalog(layout, "Input/Group")


class NODE_MT_geometry_node_input_scene(ColumnMenu, Menu):
    bl_idname = "NODE_MT_geometry_node_input_scene"
    bl_label = "Scene"

    def draw(self, context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeCollectionInfo")
        node_add_menu.add_node_type(layout, "GeometryNodeImageInfo")
        node_add_menu.add_node_type(layout, "GeometryNodeObjectInfo")

        add_separator(layout)

        if context.space_data.geometry_nodes_type == 'TOOL':
            node_add_menu.add_node_type(layout, "GeometryNodeTool3DCursor")
        node_add_menu.add_node_type(layout, "GeometryNodeIsViewport")
        node_add_menu.add_node_type(layout, "GeometryNodeInputSceneTime")
        node_add_menu.add_node_type(layout, "GeometryNodeSelfObject")
        #node_add_menu.draw_assets_for_catalog(layout, "Input/Scene")


class NODE_MT_geometry_node_instance(Menu):
    bl_idname = "NODE_MT_geometry_node_instance"
    bl_label = "Instances"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeInstanceOnPoints")
        node_add_menu.add_node_type(layout, "GeometryNodeInstancesToPoints")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "GeometryNodeRealizeInstances")
        node_add_menu.add_node_type(layout, "GeometryNodeRotateInstances")
        node_add_menu.add_node_type(layout, "GeometryNodeScaleInstances")
        node_add_menu.add_node_type(layout, "GeometryNodeTranslateInstances")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "GeometryNodeInputInstanceRotation")
        node_add_menu.add_node_type(layout, "GeometryNodeInputInstanceScale")
        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_geometry_node_material(Menu):
    bl_idname = "NODE_MT_geometry_node_material"
    bl_label = "Material"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeReplaceMaterial")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "GeometryNodeInputMaterialIndex")
        node_add_menu.add_node_type(layout, "GeometryNodeMaterialSelection")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "GeometryNodeSetMaterial")
        node_add_menu.add_node_type(layout, "GeometryNodeSetMaterialIndex")
        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_geometry_node_mesh(ColumnMenu, Menu):
    bl_idname = "NODE_MT_geometry_node_mesh"
    bl_label = "Mesh"

    def draw(self, _context):
        layout = self.layout.row()

        self.draw_column(layout, menus=(NODE_MT_geometry_node_mesh_read,))
        self.draw_column(layout, menus=(
            NODE_MT_geometry_node_mesh_write, 
            NODE_MT_geometry_node_mesh_sample, 
            NODE_MT_geometry_node_uv,
            ))

        self.draw_column(layout, menus=(NODE_MT_geometry_node_mesh_operations,))
        
        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_geometry_node_mesh_read(Menu):
    bl_idname = "NODE_MT_geometry_node_mesh_read"
    bl_label = "Read"

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
    bl_idname = "NODE_MT_geometry_node_mesh_sample"
    bl_label = "Sample"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeSampleNearestSurface")
        node_add_menu.add_node_type(layout, "GeometryNodeSampleUVSurface")
        #node_add_menu.draw_assets_for_catalog(layout, "Mesh/Sample")


class NODE_MT_geometry_node_mesh_write(Menu):
    bl_idname = "NODE_MT_geometry_node_mesh_write"
    bl_label = "Write"

    def draw(self, context):
        layout = self.layout
        if context.space_data.geometry_nodes_type == 'TOOL':
            node_add_menu.add_node_type(layout, "GeometryNodeToolSetFaceSet")
        node_add_menu.add_node_type(layout, "GeometryNodeSetShadeSmooth")
        #node_add_menu.draw_assets_for_catalog(layout, "Mesh/Write")


class NODE_MT_geometry_node_mesh_operations(Menu):
    bl_idname = "NODE_MT_geometry_node_mesh_operations"
    bl_label = "Operations"

    def draw(self, context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeMeshToCurve")
        node_add_menu.add_node_type(layout, "GeometryNodeMeshToPoints")
        if context.preferences.experimental.use_new_volume_nodes:
            node_add_menu.add_node_type(layout, "GeometryNodeMeshToSDFVolume")
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
    bl_idname = "NODE_MT_geometry_node_primitives_mesh"
    bl_label = "Mesh"

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


class NODE_MT_geometry_node_mesh_topology(Menu):
    bl_idname = "NODE_MT_geometry_node_mesh_topology"
    bl_label = "Mesh"

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
    bl_idname = "NODE_MT_geometry_node_output"
    bl_label = "Output"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "NodeGroupOutput")
        node_add_menu.add_node_type(layout, "GeometryNodeViewer")
        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_geometry_node_point(Menu):
    bl_idname = "NODE_MT_geometry_node_point"
    bl_label = "Point"

    def draw(self, context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeDistributePointsInVolume")
        node_add_menu.add_node_type(layout, "GeometryNodeDistributePointsOnFaces")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "GeometryNodePoints")
        node_add_menu.add_node_type(layout, "GeometryNodePointsToCurves")
        node_add_menu.add_node_type(layout, "GeometryNodePointsToVertices")
        if context.preferences.experimental.use_new_volume_nodes:
            node_add_menu.add_node_type(layout, "GeometryNodePointsToSDFVolume")
        node_add_menu.add_node_type(layout, "GeometryNodePointsToVolume")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "GeometryNodeSetPointRadius")
        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_geometry_node_simulation(Menu):
    bl_idname = "NODE_MT_geometry_node_simulation"
    bl_label = "Simulation"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_simulation_zone(layout, label="Simulation Zone")
        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_geometry_node_text(Menu):
    bl_idname = "NODE_MT_geometry_node_text"
    bl_label = "Text"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeStringJoin")
        node_add_menu.add_node_type(layout, "FunctionNodeReplaceString")
        node_add_menu.add_node_type(layout, "FunctionNodeSliceString")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "FunctionNodeStringLength")
        node_add_menu.add_node_type(layout, "GeometryNodeStringToCurves")
        node_add_menu.add_node_type(layout, "FunctionNodeValueToString")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "FunctionNodeInputSpecialCharacters")
        #node_add_menu.draw_assets_for_catalog(layout, "Utilities/Text")


class NODE_MT_geometry_node_texture(Menu):
    bl_idname = "NODE_MT_geometry_node_texture"
    bl_label = "Texture"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "ShaderNodeTexBrick")
        node_add_menu.add_node_type(layout, "ShaderNodeTexChecker")
        node_add_menu.add_node_type(layout, "ShaderNodeTexGradient")
        node_add_menu.add_node_type(layout, "GeometryNodeImageTexture")
        node_add_menu.add_node_type(layout, "ShaderNodeTexMagic")
        node_add_menu.add_node_type(layout, "ShaderNodeTexMusgrave")
        node_add_menu.add_node_type(layout, "ShaderNodeTexNoise")
        node_add_menu.add_node_type(layout, "ShaderNodeTexVoronoi")
        node_add_menu.add_node_type(layout, "ShaderNodeTexWave")
        node_add_menu.add_node_type(layout, "ShaderNodeTexWhiteNoise")
        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_geometry_node_utilities(ColumnMenu, Menu):
    bl_idname = "NODE_MT_geometry_node_utilities"
    bl_label = "Utilities"

    def draw(self, _context):
        layout = self.layout.row()

        self.draw_column(layout, menus=(NODE_MT_geometry_node_color, NODE_MT_geometry_node_vector,))
        self.draw_column(layout, menus=(NODE_MT_geometry_node_text, NODE_MT_geometry_node_utilities_field,))
        col = self.draw_column(layout, menus=(NODE_MT_geometry_node_utilities_math,))

        add_separator(col)
        col.label(text="Miscellaneous")
        add_separator(col)
        node_add_menu.add_node_type(col, "FunctionNodeRandomValue")
        node_add_menu.add_repeat_zone(col, label="Repeat Zone")
        node_add_menu.add_node_type(col, "GeometryNodeSwitch")

        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_geometry_node_utilities_field(Menu):
    bl_idname = "NODE_MT_geometry_node_utilities_field"
    bl_label = "Field"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeAccumulateField")
        node_add_menu.add_node_type(layout, "GeometryNodeFieldAtIndex")
        node_add_menu.add_node_type(layout, "GeometryNodeFieldOnDomain")
        #node_add_menu.draw_assets_for_catalog(layout, "Utilities/Field")


class NODE_MT_geometry_node_utilities_rotation(Menu):
    bl_idname = "NODE_MT_geometry_node_utilities_rotation"
    bl_label = "Rotation"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "FunctionNodeAlignEulerToVector")
        node_add_menu.add_node_type(layout, "FunctionNodeInvertRotation")
        props = node_add_menu.add_node_type(layout, "ShaderNodeMix", label=iface_("Mix Rotation"))
        ops = props.settings.add()
        ops.name = "data_type"
        ops.value = "'ROTATION'"
        node_add_menu.add_node_type(layout, "FunctionNodeRotateEuler")
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


class NODE_MT_geometry_node_utilities_math(Menu):
    bl_idname = "NODE_MT_geometry_node_utilities_math"
    bl_label = "Math"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "FunctionNodeBooleanMath")
        node_add_menu.add_node_type(layout, "ShaderNodeClamp")
        node_add_menu.add_node_type(layout, "FunctionNodeCompare")
        node_add_menu.add_node_type(layout, "ShaderNodeFloatCurve")
        node_add_menu.add_node_type(layout, "FunctionNodeFloatToInt")
        node_add_menu.add_node_type(layout, "ShaderNodeMapRange")
        node_add_menu.add_node_type(layout, "ShaderNodeMath")
        node_add_menu.add_node_type(layout, "ShaderNodeMix")
        #node_add_menu.draw_assets_for_catalog(layout, "Utilities/Math")


class NODE_MT_geometry_node_uv(Menu):
    bl_idname = "NODE_MT_geometry_node_uv"
    bl_label = "UV"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeUVPackIslands")
        node_add_menu.add_node_type(layout, "GeometryNodeUVUnwrap")
        #node_add_menu.draw_assets_for_catalog(layout, "Mesh/UV")


class NODE_MT_geometry_node_vector(Menu):
    bl_idname = "NODE_MT_geometry_node_vector"
    bl_label = "Vector"

    def draw(self, _context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "ShaderNodeVectorCurve")
        node_add_menu.add_node_type(layout, "ShaderNodeVectorMath")
        node_add_menu.add_node_type(layout, "ShaderNodeVectorRotate")
        add_separator(layout)
        node_add_menu.add_node_type(layout, "ShaderNodeCombineXYZ")
        props = node_add_menu.add_node_type(layout, "ShaderNodeMix", label=iface_("Mix Vector"))
        ops = props.settings.add()
        ops.name = "data_type"
        ops.value = "'VECTOR'"
        node_add_menu.add_node_type(layout, "ShaderNodeSeparateXYZ")
        #node_add_menu.draw_assets_for_catalog(layout, "Utilities/Vector")


class NODE_MT_geometry_node_volume(Menu):
    bl_idname = "NODE_MT_geometry_node_volume"
    bl_label = "Volume"
    bl_translation_context = i18n_contexts.id_id

    def draw(self, context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeVolumeCube")
        node_add_menu.add_node_type(layout, "GeometryNodeVolumeToMesh")
        if context.preferences.experimental.use_new_volume_nodes:
            add_separator(layout)
            node_add_menu.add_node_type(layout, "GeometryNodeMeanFilterSDFVolume")
            node_add_menu.add_node_type(layout, "GeometryNodeOffsetSDFVolume")
            node_add_menu.add_node_type(layout, "GeometryNodeSampleVolume")
            node_add_menu.add_node_type(layout, "GeometryNodeSDFVolumeSphere")
            node_add_menu.add_node_type(layout, "GeometryNodeInputSignedDistance")
        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_geometry_node_group(Menu):
    bl_idname = "NODE_MT_geometry_node_group"
    bl_label = "Group"

    def draw(self, context):
        layout = self.layout
        draw_node_group_add_menu(context, layout)
        #node_add_menu.draw_assets_for_catalog(layout, self.bl_label)


class NODE_MT_geometry_node_add_all(Menu):
    bl_idname = "NODE_MT_geometry_node_add_all"
    bl_label = ""

    def draw(self, context):
        layout = self.layout
        layout.menu("NODE_MT_geometry_node_attribute")
        layout.menu("NODE_MT_geometry_node_input")
        layout.menu("NODE_MT_geometry_node_output")
        add_separator(layout)
        layout.menu("NODE_MT_geometry_node_geometry")
        add_separator(layout)
        layout.menu("NODE_MT_geometry_node_curve")
        layout.menu("NODE_MT_geometry_node_instance")
        layout.menu("NODE_MT_geometry_node_mesh")
        layout.menu("NODE_MT_geometry_node_point")
        layout.menu("NODE_MT_geometry_node_volume")
        add_separator(layout)
        layout.menu("NODE_MT_geometry_node_primitives")
        layout.menu("NODE_MT_geometry_node_topology")
        add_separator(layout)
        layout.menu("NODE_MT_geometry_node_simulation")
        add_separator(layout)
        layout.menu("NODE_MT_geometry_node_material")
        layout.menu("NODE_MT_geometry_node_utilities_rotation")
        layout.menu("NODE_MT_geometry_node_texture")
        layout.menu("NODE_MT_geometry_node_utilities")
        add_separator(layout)
        layout.menu("NODE_MT_geometry_node_group")
        layout.menu("NODE_MT_category_layout")

        draw_asset_menu(layout)


classes = (
    NODE_MT_geometry_node_add_all,
    NODE_MT_geometry_node_attribute,
    NODE_MT_geometry_node_input,
    NODE_MT_geometry_node_input_constant,
    NODE_MT_geometry_node_input_group,
    NODE_MT_geometry_node_input_scene,
    NODE_MT_geometry_node_output,
    NODE_MT_geometry_node_curve,
    NODE_MT_geometry_node_curve_read,
    NODE_MT_geometry_node_curve_sample,
    NODE_MT_geometry_node_curve_write,
    NODE_MT_geometry_node_curve_operations,
    NODE_MT_geometry_node_primitives_curve,
    NODE_MT_geometry_node_curve_topology,
    NODE_MT_geometry_node_geometry,
    NODE_MT_geometry_node_geometry_read,
    NODE_MT_geometry_node_geometry_write,
    NODE_MT_geometry_node_geometry_operations,
    NODE_MT_geometry_node_geometry_sample,
    NODE_MT_geometry_node_primitives,
    NODE_MT_geometry_node_topology,
    NODE_MT_geometry_node_instance,
    NODE_MT_geometry_node_mesh,
    NODE_MT_geometry_node_mesh_read,
    NODE_MT_geometry_node_mesh_sample,
    NODE_MT_geometry_node_mesh_write,
    NODE_MT_geometry_node_mesh_operations,
    NODE_MT_geometry_node_uv,
    NODE_MT_geometry_node_primitives_mesh,
    NODE_MT_geometry_node_mesh_topology,
    NODE_MT_geometry_node_point,
    NODE_MT_geometry_node_simulation,
    NODE_MT_geometry_node_volume,
    NODE_MT_geometry_node_material,
    NODE_MT_geometry_node_texture,
    NODE_MT_geometry_node_utilities,
    NODE_MT_geometry_node_color,
    NODE_MT_geometry_node_text,
    NODE_MT_geometry_node_vector,
    NODE_MT_geometry_node_utilities_field,
    NODE_MT_geometry_node_utilities_math,
    NODE_MT_geometry_node_utilities_rotation,
    NODE_MT_geometry_node_group,
)

if __name__ == "__main__":  # only for live edit.
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
