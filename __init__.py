# Copyright © 1996 – 2026 SCS Software s.r.o. All Rights Reserved.
# Proprietary and confidential. Unauthorized copying, modification,
# or distribution is strictly prohibited.


import bpy

from .operators.open_url import SAT_OT_OPEN_URL
from .ui.main_panel import SAT_PT_MAIN
 
 
classes = (
    SAT_OT_OPEN_URL,
    SAT_PT_MAIN,
)
 
 
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
 
 
def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)