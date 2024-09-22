import bpy
from . import utils

class MATERIAL_TOOLS_OT_DeleteDuplicateMaterials(bpy.types.Operator):
    bl_idname = "material_tools.delete_duplicate_materials"
    bl_label = "Delete Duplicate Materials"

    def execute(self, context):
        utils.RemoveUnusedData.delete_duplicate_materials()
        return {'FINISHED'}

class MATERIAL_TOOLS_OT_DeleteUnusedUVMap(bpy.types.Operator):
    bl_idname = "material_tools.delete_unused_uv_map"
    bl_label = "Delete Unused UV Map"

    def execute(self, context):
        utils.RemoveUnusedData.delete_unused_uv_map()
        return {'FINISHED'}

class MATERIAL_TOOLS_OT_RemoveUnusedMaterialSlots(bpy.types.Operator):
    bl_idname = "material_tools.remove_unused_material_slots"
    bl_label = "Remove Unused Material Slots"

    def execute(self, context):
        utils.RemoveUnusedData.remove_unused_material_slots()
        return {'FINISHED'}

class MATERIAL_TOOLS_OT_RandomMaterial(bpy.types.Operator):
    bl_idname = "material_tools.random_material"
    bl_label = "Random Material"

    def execute(self, context):
        utils.RandomMaterial.assign_random_material(context)
        return {'FINISHED'}

class MATERIAL_TOOLS_OT_AutoLinkTextures(bpy.types.Operator):
    bl_idname = "material_tools.auto_link_textures"
    bl_label = "Auto Link Texture Map"

    def execute(self, context):
        utils.AutoLinkTexture.auto_link_textures()
        return {'FINISHED'}
    
class MATERIAL_TOOLS_OT_ResetAutoLinkSuffixes(bpy.types.Operator):
    bl_idname = "material_tools.reset_auto_link_suffixes"
    bl_label = "Reset Suffixes to Default"

    def execute(self, context):
        material_tools = context.scene.material_tools
        material_tools.base_color_suffix = "_albedo"
        material_tools.roughness_suffix = "_roughness"
        material_tools.metalness_suffix = "_metalness"
        material_tools.normal_suffix = "_normal"
        material_tools.emissive_suffix = "_emissive"
        material_tools.alpha_suffix = "_alpha"
        self.report({'INFO'}, "Auto-link suffixes reset to default values.")
        return {'FINISHED'}