import bpy
from pathlib import Path


def fetch_user_preferences(attr_id=None):
    prefs = bpy.context.preferences.addons[__package__].preferences

    if attr_id is None:
        return prefs
    else:
        return getattr(prefs, attr_id)
        

def fetch_asset_catalogs(context):
    for library in context.preferences.filepaths.asset_libraries:
        filepath = Path(library.path, "blender_assets.cats.txt")
        if filepath.exists():
            yield filepath 

    if context.blend_data.is_saved:
        filepath = Path(bpy.path.abspath("//"), "blender_assets.cats.txt") 
        if filepath.exists():
            yield filepath

def parse_catalog_files(catalog_paths):
    for filepath in catalog_paths:
        with open(filepath, "r") as f:
            for line in f:
                line = line.strip()
                if line.startswith(("VERSION", "#")) or line == "":
                    continue

                yield line.split(":")

def get_root_catalogs(context):
    catalog_data = parse_catalog_files(fetch_asset_catalogs(context))

    for uuid, catalog_path, simple_name in catalog_data:
        if "/" not in catalog_path:
            yield catalog_path

def read_all_assets(context):
    asset_libraries = context.preferences.filepaths.asset_libraries
    for asset_library in asset_libraries:
        library_name = asset_library.name
        library_path = Path(asset_library.path)
        blend_files = [fp for fp in library_path.glob("**/*.blend") if fp.is_file()]

        for blend_file in blend_files:
            bpy.ops.wm.open_mainfile(filepath=str(blend_file))
            for group in bpy.data.node_groups:
                if group.asset_data:
                    print(group, group.asset_data.catalog_id, group.asset_data.catalog_simple_name)

            bpy.ops.wm.open_mainfile(filepath=str(blend_file))


def draw_asset_menus(layout, context):
    layout.separator()

    for catalog_path in get_root_catalogs(context):
        layout.template_node_asset_menu_items(catalog_path=catalog_path)

    layout.separator()
    layout.menu_contents("NODE_MT_node_add_root_catalogs")