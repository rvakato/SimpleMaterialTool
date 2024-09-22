import bpy

class MATERIAL_TOOLS_PT_Panel(bpy.types.Panel):
    bl_label = "Simple Material Tool"
    bl_idname = "MATERIAL_TOOLS_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Simple Material Tool'

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        # Check if material_tools is available
        if hasattr(scene, "material_tools"):
            material_tools = scene.material_tools

            # Remove Unused Data
            box = layout.box()
            row = box.row()
            row.prop(scene, "remove_unused_data_expand", icon="TRIA_DOWN" if scene.remove_unused_data_expand else "TRIA_RIGHT", icon_only=True, emboss=False)
            row.label(text="Remove Unused Data")
            if scene.remove_unused_data_expand:
                box.operator("material_tools.delete_duplicate_materials")
                box.operator("material_tools.delete_unused_uv_map")
                box.operator("material_tools.remove_unused_material_slots")

            # Random Material
            box = layout.box()
            row = box.row()
            row.prop(scene, "random_material_expand", icon="TRIA_DOWN" if scene.random_material_expand else "TRIA_RIGHT", icon_only=True, emboss=False)
            row.label(text="Random Material")
            if scene.random_material_expand:
                box.prop(material_tools, "random_material_prefix")
                box.operator("material_tools.random_material")

            # Auto Link Texture
            box = layout.box()
            row = box.row()
            row.prop(context.scene, "auto_link_texture_expand", icon="TRIA_DOWN" if context.scene.auto_link_texture_expand else "TRIA_RIGHT", icon_only=True, emboss=False)
            row.label(text="Auto Link Texture")
            if context.scene.auto_link_texture_expand:
                box.prop(material_tools, "base_color_suffix")
                box.prop(material_tools, "roughness_suffix")
                box.prop(material_tools, "metalness_suffix")
                box.prop(material_tools, "normal_suffix")
                box.prop(material_tools, "emissive_suffix")
                box.prop(material_tools, "alpha_suffix")
                box.operator("material_tools.reset_auto_link_suffixes")
                box.operator("material_tools.auto_link_textures")