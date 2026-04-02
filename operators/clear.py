# SPDX-License-Identifier: GPL-3.0-or-later
#
# Copyright (C) 2026 Pavel Círus, Jan Dvořáček
# Copyright (C) 1996-2026 SCS Software s.r.o.



import bpy

from .initialize import PRESET_NODE_GROUPS


# Operator that removes the Geometry Nodes preset modifier from the input mesh
class SAT_OT_CLEAR(bpy.types.Operator):
    bl_idname = "sat.clear"
    bl_label = "Clear Generator"
    bl_description = "Remove the generator applied by SCS Asset Toolkit"
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
                    return f"Remove '{node_group_name}' from '{sat.input_mesh.name}'"
        return "No generator to remove"

    # Disables the button if no mesh is selected or preset is not applied
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
                return True
        return False

    # Removes the matching Geometry Nodes modifier from the input mesh
    def execute(self, context):
        sat = context.scene.sat
        obj = sat.input_mesh
        node_group_name = PRESET_NODE_GROUPS.get(sat.preset)

        for mod in obj.modifiers:
            if mod.type == 'NODES' and mod.node_group and mod.node_group.name == node_group_name:
                obj.modifiers.remove(mod)
                self.report({'INFO'}, f"Removed '{node_group_name}' from '{obj.name}'")
                return {'FINISHED'}

        self.report({'WARNING'}, "No matching generator found")
        return {'CANCELLED'}
