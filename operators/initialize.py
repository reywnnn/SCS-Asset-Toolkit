# Copyright © 1996 – 2026 SCS Software s.r.o. All Rights Reserved.
# Proprietary and confidential. Unauthorized copying, modification,
# or distribution is strictly prohibited.



import os
import bpy


# Path to the .blend file containing Geometry Nodes presets
ASSET_BLEND_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "assets", "scs_asset_toolkit.blend",
)

# Maps preset selection from UI to node group names in scs_asset_toolkit.blend
PRESET_NODE_GROUPS = {
    'HARDSURFACE': "Hardsurface",   # 'ID, EnumProperty' : "UI Name"
}


# Operator that loads and applies a Geometry Nodes preset to the input mesh
class SAT_OT_INITIALIZE(bpy.types.Operator):
    bl_idname = "sat.initialize"
    bl_label = "Initialize Generator"
    bl_description = "Apply generator from selected preset to the input mesh"
    bl_options = {'REGISTER', 'UNDO'}

    # Returns a dynamic tooltip explaining why the button may be disabled
    @classmethod
    def description(cls, context, properties):
        sat = context.scene.sat
        if sat.input_mesh is None:
            return "Select an input mesh first"
        node_group_name = PRESET_NODE_GROUPS.get(sat.preset)
        if node_group_name:
            for mod in sat.input_mesh.modifiers:
                if mod.type == 'NODES' and mod.node_group and mod.node_group.name == node_group_name:
                    return f"Generator is already applied on your input mesh"
        return "Apply generator from selected preset to the input mesh"

    # Disables the button if no mesh is selected or preset is already applied
    @classmethod
    def poll(cls, context):
        sat = context.scene.sat
        if sat.input_mesh is None:
            return False
        node_group_name = PRESET_NODE_GROUPS.get(sat.preset)
        if node_group_name is None:
            return False
        for mod in sat.input_mesh.modifiers:
            if mod.type == 'NODES' and mod.node_group and mod.node_group.name == node_group_name:
                return False
        return True

    # Loads the node group from the .blend asset file and adds it as a modifier
    def execute(self, context):
        sat = context.scene.sat
        obj = sat.input_mesh
        node_group_name = PRESET_NODE_GROUPS.get(sat.preset)

        if node_group_name not in bpy.data.node_groups:
            with bpy.data.libraries.load(ASSET_BLEND_PATH) as (data_from, data_to):
                if node_group_name in data_from.node_groups:
                    data_to.node_groups = [node_group_name]
                else:
                    self.report({'ERROR'}, f"Generator for '{node_group_name}' preset not found in asset file")
                    return {'CANCELLED'}

        node_group = bpy.data.node_groups[node_group_name]

        modifier = obj.modifiers.new(name=node_group_name, type='NODES')
        modifier.node_group = node_group

        self.report({'INFO'}, f"Applied '{node_group_name}' to '{obj.name}'")
        return {'FINISHED'}
