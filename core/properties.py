# Copyright © 1996 – 2026 SCS Software s.r.o. All Rights Reserved.
# Proprietary and confidential. Unauthorized copying, modification,
# or distribution is strictly prohibited.



import bpy

from ..operators.initialize import PRESET_NODE_GROUPS


# Filter function that only allows mesh objects linked to the scene
def mesh_poll(self, object):
    return object.type == 'MESH' and object.name in bpy.context.scene.objects


# Syncs lod_level property value to the Geometry Nodes modifier socket
def lod_level_update(self, context):
    obj = self.input_mesh
    if obj is None:
        return
    node_group_name = PRESET_NODE_GROUPS.get(self.preset)
    if node_group_name is None:
        return
    for mod in obj.modifiers:
        if mod.type == 'NODES' and mod.node_group and mod.node_group.name == node_group_name:
            for item in mod.node_group.interface.items_tree:
                if item.item_type == 'SOCKET' and item.name == "Level of Detail:":
                    mod[item.identifier] = self.lod_level
                    obj.update_tag()
                    break
            break


# Syncs modifier socket value back to lod_level property on depsgraph updates
def on_depsgraph_update(scene, depsgraph):
    sat = scene.sat
    obj = sat.input_mesh
    if obj is None:
        return
    node_group_name = PRESET_NODE_GROUPS.get(sat.preset)
    if node_group_name is None:
        return
    for mod in obj.modifiers:
        if mod.type == 'NODES' and mod.node_group and mod.node_group.name == node_group_name:
            for item in mod.node_group.interface.items_tree:
                if item.item_type == 'SOCKET' and item.name == "Level of Detail:":
                    val = mod.get(item.identifier, 0)
                    if sat.lod_level != val:
                        sat["lod_level"] = val
                    break
            break


# Stores all addon properties accessible via context.scene.sat
class SAT_PROPERTIES(bpy.types.PropertyGroup):
    input_mesh: bpy.props.PointerProperty(
        type=bpy.types.Object,
        name="Input Mesh",
        description="Select a mesh object",
        poll=mesh_poll,
    ) # type: ignore

    preset: bpy.props.EnumProperty(
        name="Preset",
        description="Select a Generator Preset",
        items=[
            ('NONE', "None", "No preset selected"),
            ('HARDSURFACE', "Hardsurface", "LOD, Shadow & Collision for Hardsurface Assets"),
        ],
        default='NONE',
    ) # type: ignore

    lod_level: bpy.props.IntProperty(
        name="Level of Detail",
        description="Move slider to change Level of Detail",
        default=0,
        min=0,
        max=1,
        update=lod_level_update,
    ) # type: ignore
