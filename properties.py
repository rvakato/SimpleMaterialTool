import bpy

class MATERIAL_TOOLS_Properties(bpy.types.PropertyGroup):
    random_material_prefix: bpy.props.StringProperty(
        name="Prefix",
        description="Prefix for materials to be used in random assignment",
        default="_"
    )

    base_color_suffix: bpy.props.StringProperty(
        name="Base Color Suffix",
        description="Suffix for base color textures",
        default="_albedo"
    )
    roughness_suffix: bpy.props.StringProperty(
        name="Roughness Suffix",
        description="Suffix for roughness textures",
        default="_roughness"
    )
    metalness_suffix: bpy.props.StringProperty(
        name="Metalness Suffix",
        description="Suffix for metalness textures",
        default="_metalness"
    )
    normal_suffix: bpy.props.StringProperty(
        name="Normal Suffix",
        description="Suffix for normal textures",
        default="_normal"
    )
    emissive_suffix: bpy.props.StringProperty(
        name="Emissive Suffix",
        description="Suffix for emissive textures",
        default="_emissive"
    )
    alpha_suffix: bpy.props.StringProperty(
        name="Alpha Suffix",
        description="Suffix for alpha textures",
        default="_alpha"
    )