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

        box = layout.box()
        row = box.row(align=True)
        op = row.operator("sat.open_url", text="Docs", icon='HELP')
        op.url = (
            "https://scssoft.atlassian.net/wiki/spaces/"
            "~712020097edec4c2844607944fbd1e723e72ab/"
            "pages/2002845757/Documentation"
        )
        op.tooltip = "Open the SCS Asset Toolkit documentation"
        op = row.operator("sat.open_url", text="Report", icon='CURRENT_FILE')
        op.url = (
            "https://miro.com/app/board/uXjVGu_mvoU=/"
            "?moveToWidget=3458764664537798733&cot=10"
        )
        op.tooltip = "Report an issue or provide feedback"
 