# Copyright © 1996 – 2026 SCS Software s.r.o. All Rights Reserved.
# Proprietary and confidential. Unauthorized copying, modification,
# or distribution is strictly prohibited.


import bpy


class SAT_PT_MAIN(bpy.types.Panel):
    bl_label = "SCS Asset Toolkit"
    bl_idname = "SAT_PT_MAIN"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "SCS Asset Toolkit"

    def draw(self, context):
        layout = self.layout