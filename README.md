# Simple Material Tool

## Description
Simple Material Tool is a Blender addon that provides a set of utilities for managing materials and textures in your 3D projects. It simplifies common tasks such as removing unused data, assigning random materials, and automatically linking texture maps.

## Features

### Remove Unused Data
- Delete Duplicate Materials: Removes duplicate materials from the scene.
- Delete Unused UV Map: Removes unused UV maps from selected objects.
- Remove Unused Material Slots: Removes unused material slots from selected objects.

### Random Material Assignment
- Assign random materials to selected objects based on a specified prefix.

### Auto Link Texture
- Automatically link texture maps to Principled BSDF shader inputs based on customizable texture name suffixes.

## Installation
1. Download the `simple_material_tool_V1.zip` file.
2. Open Blender and go to Edit > Preferences > Add-ons.
3. Click "Install" and select the downloaded file.
4. Enable the addon by checking the box next to "3D View: Simple Material Tool".

## Usage

The addon adds a new panel called "Simple Material Tool" in the 3D View sidebar. To access it:

1. In the 3D View, press N to open the sidebar.
2. Look for the "Simple Material Tool" tab.

### Remove Unused Data
- Click the respective buttons to perform each operation.

### Random Material Assignment
1. Set the prefix for materials you want to use in the random assignment.
2. Select the objects you want to assign materials to.
3. Click the "Random Material" button.

### Auto Link Texture
1. Customize the suffixes for different texture types if needed.
2. Select the object(s) with materials you want to process.
3. Click the "Auto Link Texture Map" button.

## Customization
- You can customize the suffixes used for auto-linking textures in the addon preferences.
- The default suffixes are:
  - Base Color: "_albedo"
  - Roughness: "_roughness"
  - Metalness: "_metalness"
  - Normal: "_normal"
  - Emissive: "_emissive"
  - Alpha: "_alpha"

## Compatibility
- Blender 2.82 and above

## Author
rvakato

## Version
1.0.0

## Support
For issues, suggestions, or contributions, please contact: rvakato@gmai.com