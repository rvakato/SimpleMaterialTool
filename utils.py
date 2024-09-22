import bpy
import random
import os

class RemoveUnusedData:
    @staticmethod
    def delete_duplicate_materials():
        mats = bpy.data.materials
        for mat in mats:
            (original, _, ext) = mat.name.rpartition(".")
            if ext.isnumeric() and mats.find(original) != -1:
                print("%s -> %s" % (mat.name, original))
                mat.user_remap(mats[original])
                mats.remove(mat)

    @staticmethod
    def delete_unused_uv_map():
        selected_objects = bpy.context.selected_objects
        for obj in selected_objects:
            if obj.type == 'MESH' and obj.data.uv_layers:
                uv_layers = obj.data.uv_layers
                active_uv = uv_layers.active
                if len(uv_layers) > 1:
                    if active_uv != uv_layers[0]:
                        uv_layers.active_index = 0
                        uv_layers.remove(active_uv)
                    active_uv = uv_layers[0]
                while len(uv_layers) > 1:
                    uv_layers.remove(uv_layers[1])
                if uv_layers:
                    uv_layers[0].name = "UVMap"
        print("UV map cleanup and renaming completed.")

    @staticmethod
    def remove_unused_material_slots():
        selected_objects = bpy.context.selected_objects
        for obj in selected_objects:
            if obj.type == 'MESH':
                RemoveUnusedData.merge_duplicate_materials(obj)
                RemoveUnusedData.remove_unused_slots(obj)
            else:
                print(f"Skipped non-mesh object: {obj.name}")
        print("Finished processing all selected objects.")

    @staticmethod
    def merge_duplicate_materials(obj):
        if obj.type != 'MESH':
            return
        unique_materials = {}
        material_mapping = {}
        for slot in obj.material_slots:
            if slot.material:
                if slot.material.name not in unique_materials:
                    unique_materials[slot.material.name] = slot.material
                material_mapping[slot.material] = unique_materials[slot.material.name]
        for i, slot in enumerate(obj.material_slots):
            if slot.material:
                obj.material_slots[i].material = material_mapping[slot.material]
        used_materials = set(material_mapping.values())
        for i in range(len(obj.material_slots) - 1, -1, -1):
            if obj.material_slots[i].material not in used_materials:
                obj.data.materials.pop(index=i)
        for mat in bpy.data.materials:
            if mat not in used_materials and mat.users == 0:
                bpy.data.materials.remove(mat)

    @staticmethod
    def remove_unused_slots(obj):
        if obj.type != 'MESH':
            return
        used_indices = set(poly.material_index for poly in obj.data.polygons)
        for i in range(len(obj.material_slots) - 1, -1, -1):
            if i not in used_indices:
                obj.data.materials.pop(index=i)

class RandomMaterial:
    @staticmethod
    def assign_random_material(context):
        prefix = context.scene.material_tools.random_material_prefix
        materials = [mat for mat in bpy.data.materials if mat.name.startswith(prefix)]
        if not materials:
            return {'FINISHED'}
        for obj in context.selected_objects:
            obj.active_material = random.choice(materials)

class AutoLinkTexture:
    @staticmethod
    def link_textures_to_principled(material):
        if not material.use_nodes:
            material.use_nodes = True
        nodes = material.node_tree.nodes
        principled = next((n for n in nodes if n.type == 'BSDF_PRINCIPLED'), None)
        if not principled:
            return

        material_tools = bpy.context.scene.material_tools
        for node in nodes:
            if node.type == 'TEX_IMAGE':
                image = node.image
                if not image:
                    continue
                name = os.path.splitext(image.name)[0].lower()
                if name.endswith(material_tools.base_color_suffix.lower()):
                    material.node_tree.links.new(node.outputs['Color'], principled.inputs['Base Color'])
                elif name.endswith(material_tools.roughness_suffix.lower()):
                    node.image.colorspace_settings.name = 'Non-Color'
                    material.node_tree.links.new(node.outputs['Color'], principled.inputs['Roughness'])
                elif name.endswith(material_tools.metalness_suffix.lower()):
                    node.image.colorspace_settings.name = 'Non-Color'
                    material.node_tree.links.new(node.outputs['Color'], principled.inputs['Metallic'])
                elif name.endswith(material_tools.normal_suffix.lower()):
                    node.image.colorspace_settings.name = 'Non-Color'
                    normal_map = nodes.new(type='ShaderNodeNormalMap')
                    material.node_tree.links.new(node.outputs['Color'], normal_map.inputs['Color'])
                    material.node_tree.links.new(normal_map.outputs['Normal'], principled.inputs['Normal'])
                elif name.endswith(material_tools.emissive_suffix.lower()):
                    material.node_tree.links.new(node.outputs['Color'], principled.inputs['Emission'])
                elif name.endswith(material_tools.alpha_suffix.lower()):
                    material.node_tree.links.new(node.outputs['Color'], principled.inputs['Alpha'])

    @staticmethod
    def auto_link_textures():
        obj = bpy.context.active_object
        for material_slot in obj.material_slots:
            material = material_slot.material
            if material:
                AutoLinkTexture.link_textures_to_principled(material)
        print("Texture linking completed.")