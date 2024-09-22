"""
rvakato@gmail.com
https://github.com/rvakato/Python_for_Blender
"""

bl_info = {
    "name": "Simple Material Tool",
    "author": "rvakato",
    "version": (1,0,0),
    "description": "simple material tool",
    "location": "3D Viewport > Sidebar > Simple Material Tool",
    "blender": (2, 82, 0),
    "category": "3D View",
}

import bpy
from . import operators, panels, properties
#from .panels import MATERIAL_TOOLS_PT_Panel
#from .properties import MATERIAL_TOOLS_Properties
#from .operators import MATERIAL_TOOLS_OT_DeleteDuplicateMaterials,  MATERIAL_TOOLS_OT_DeleteUnusedUVMap, MATERIAL_TOOLS_OT_RemoveUnusedMaterialSlots, MATERIAL_TOOLS_OT_RandomMaterial, MATERIAL_TOOLS_OT_AutoLinkTextures

classes = (
    properties.MATERIAL_TOOLS_Properties,
    panels.MATERIAL_TOOLS_PT_Panel,
    operators.MATERIAL_TOOLS_OT_DeleteDuplicateMaterials,
    operators.MATERIAL_TOOLS_OT_DeleteUnusedUVMap,
    operators.MATERIAL_TOOLS_OT_RemoveUnusedMaterialSlots,
    operators.MATERIAL_TOOLS_OT_RandomMaterial,
    operators.MATERIAL_TOOLS_OT_AutoLinkTextures,
    operators.MATERIAL_TOOLS_OT_ResetAutoLinkSuffixes,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.material_tools = bpy.props.PointerProperty(type=properties.MATERIAL_TOOLS_Properties)
    bpy.types.Scene.remove_unused_data_expand = bpy.props.BoolProperty(default=False)
    bpy.types.Scene.random_material_expand = bpy.props.BoolProperty(default=False)
    bpy.types.Scene.auto_link_texture_expand = bpy.props.BoolProperty(default=False)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.material_tools
    del bpy.types.Scene.remove_unused_data_expand
    del bpy.types.Scene.random_material_expand
    del bpy.types.Scene.auto_link_texture_expand

if __name__ == "__main__":
    register()