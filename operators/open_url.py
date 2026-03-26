# Copyright © 1996 – 2026 SCS Software s.r.o. All Rights Reserved.
# Proprietary and confidential. Unauthorized copying, modification,
# or distribution is strictly prohibited.



import bpy


# Universal operator for opening URLs in the browser with dynamic tooltips
class SAT_OT_OPEN_URL(bpy.types.Operator):
    bl_idname = "sat.open_url"
    bl_label = "Open URL"

    url: bpy.props.StringProperty() # type: ignore
    tooltip: bpy.props.StringProperty() # type: ignore

    # Returns a dynamic tooltip based on the tooltip property
    @classmethod
    def description(cls, context, properties):
        return properties.tooltip

    # Opens the URL in the default browser
    def execute(self, context):
        bpy.ops.wm.url_open(url=self.url)
        return {'FINISHED'}
