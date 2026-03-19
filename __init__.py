# Copyright © 1996 – 2026 SCS Software s.r.o. All Rights Reserved.
# Proprietary and confidential. Unauthorized copying, modification,
# or distribution is strictly prohibited.


import bpy
 
from .ui.main_panel import SAT_PT_MAIN
 
 
classes = (
    SAT_PT_MAIN,
)
 
 
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
 
 
def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)