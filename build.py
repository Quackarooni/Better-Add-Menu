import re
import ast
import shutil
import tomllib

from typing import List
from pathlib import Path
from tempfile import TemporaryDirectory


root = Path(__file__).parent / "source"
RELEASE_FOLDER = Path("release")

exclude_filters = (
    "__pycache__", 
    "*.pyc", 
    "*.pyo", 
    "*.ruff_cache",
    "*.git",
    "*.gitignore",
    "*.blend",
    "*.blend1",
    "*.json"
)

ignored_files = (
    "blender_manifest.toml",
    Path(__file__).name, # Exclude this build script
)

versioned_modules = (
    "menus",
)


def version_to_string(version, depth=None, separator="."):
    if depth is not None:
        version = version[:depth]

    return separator.join(map(str, version[:depth]))


def get_bl_info(init_path):
    with open(init_path, 'r') as f:
        node = ast.parse(f.read())

    n: ast.Module
    for n in ast.walk(node):
        for b in n.body:
            if isinstance(b, ast.Assign) and isinstance(b.value, ast.Dict) and (
                    any(t.id == 'bl_info' for t in b.targets)):
                bl_info_dict = ast.literal_eval(b.value)
                return bl_info_dict
            
    raise ValueError('Cannot find bl_info')


class PackageConfig:
    version: tuple
    is_legacy: bool

    __slots__ = ("version", "archive_name", "is_legacy", "internal_folder_name")

    def __init__(self, version, base_name, addon_version, internal_folder_name, is_legacy=True):
        if version == "ALL":
            self.version = version
            version_string = "Multi-version"
        else:
            self.version = tuple(version)
            version_string = f"Blender {version_to_string(version, depth=2)}"

        self.archive_name = f"{base_name} {version_to_string(addon_version)} - {version_string}"
        self.is_legacy = is_legacy
        self.internal_folder_name = internal_folder_name
    
    def __repr__(self):
        attributes = (f'"{k}"={getattr(self, k)}' for k in self.__slots__)
        attributes = ", ".join(attributes)

        return f"{self.__class__.__name__}({attributes})"


class BuildConfig:
    base_name : str
    internal_folder_name : str
    builds : List[PackageConfig]

    __slots__ = ("base_name", "internal_folder_name", "builds")

    def __init__(self, data):
        base_name = str(data["base_name"])
        internal_folder_name = str(data["internal_folder_name"])
        addon_version = get_bl_info(Path("source", "__init__.py"))["version"]

        shared_data = {
            "base_name" : base_name,
            "internal_folder_name" : internal_folder_name,
            "addon_version" : addon_version
        }

        self.base_name = base_name
        self.internal_folder_name = internal_folder_name
        self.builds = [PackageConfig(**shared_data, **v) for v in data["builds"]]

    def __repr__(self):
        attributes = (f'"{k}"={getattr(self, k)}' for k in self.__slots__)
        attributes = ", ".join(attributes)

        return f"{self.__class__.__name__}({attributes})"


def make_empty(path):
    if path.exists():
        shutil.rmtree(path)
    path.mkdir()


def initialize(path):
    if not path.exists():
        path.mkdir()
        return

    for item in path.iterdir():
        if item.is_dir():
            shutil.rmtree(item)
        elif not str(item).endswith(".gitignore"):
            item.unlink()


def generate_blender_manifest(output_folder, version):
    manifest_base = Path(root, "blender_manifest.toml")
    output_path = Path(output_folder, "blender_manifest.toml")
    version_string = version_to_string(version)

    substitutions = (
        (r'^(blender_version_min *= *).*', rf'\1"{version_string}"'),
    )

    with open(manifest_base, 'r', encoding="utf-8") as f:
        strings = f.read()
        
        for target, replace_with in substitutions:
            # NOTE - This is intended to be a safeguard to avoid alterations where they aren't intended
            assert len(re.findall(target, strings, flags=re.MULTILINE)) == 1, (
                f"Multiple matches found of regular expression, cannot substitute: '{target}'\n{re.findall(target, strings, flags=re.MULTILINE)}"
            )

            strings = re.sub(target, replace_with, strings, flags=re.MULTILINE)
        
    with open(output_path, 'w', encoding="utf-8") as f:
        f.write(strings)


def generate_init_py(output_folder, version):
    init_base = Path(root, "__init__.py")
    output_path = Path(output_folder, "__init__.py")
    
    substitutions = (
        (r'^( *"blender" *: *).*', rf'\1{version},'),
    )

    with open(init_base, 'r', encoding="utf-8") as f:
        strings = f.read()
        
        for target, replace_with in substitutions:
            # NOTE - This is intended to be a safeguard to avoid alterations where they aren't intended
            assert len(re.findall(target, strings, flags=re.MULTILINE)) == 1, (
                f"Multiple matches found of regular expression, cannot substitute: '{target}'\n{re.findall(target, strings, flags=re.MULTILINE)}"
            )

            strings = re.sub(target, replace_with, strings, flags=re.MULTILINE)
        
    with open(output_path, 'w', encoding="utf-8") as f:
        f.write(strings)


def replace_strings_with_regex(target_path, substitutions):
    with open(target_path, 'r', encoding="utf-8") as f:
        strings = f.read()

        for target, replace_with in substitutions:
            # NOTE - This is intended to be a safeguard to avoid alterations where they aren't intended
            matches = re.findall(target, strings, flags=re.MULTILINE)

            assert len(matches) <= 1, (
                f"Multiple matches found of regular expression, cannot substitute: '{target}'\n{re.findall(target, strings, flags=re.MULTILINE)}"
            )

            strings = re.sub(target, replace_with, strings, flags=re.MULTILINE)

    with open(target_path, 'w', encoding="utf-8") as f:
        f.write(strings)
        

def generate_versioned_module(root, target, name, version):
    module_path = root/name
    target_path = target/name

    py_files_exclude = {
        "__init__.py",
        }

    version_string = version_to_string(version, depth=2, separator="_")
    shutil.copytree(module_path/version_string, target_path, ignore=shutil.ignore_patterns(*exclude_filters))

    for py_file in module_path.glob("*.py"):
        name = py_file.name
        if name not in py_files_exclude:
            shutil.copy(py_file, target_path)

    for py_file in target_path.glob("*.py"):
        if py_file.name != "utils.py": 
            replace_strings_with_regex(py_file, substitutions=(
                 (r'(^ *)from ..utils', r'\1from .utils'),
             ))


def build_package(package_config):
    with TemporaryDirectory(dir=RELEASE_FOLDER) as temp_dir:
        dest_folder = Path(temp_dir, package_config.internal_folder_name)
        archive_name = package_config.archive_name
        version = package_config.version

        if version == "ALL":
            ignore_patterns = shutil.ignore_patterns(*exclude_filters, *ignored_files)
            shutil.copytree(root, dest_folder, ignore=ignore_patterns)
        else:
            ignore_patterns = shutil.ignore_patterns(*exclude_filters, *ignored_files, *versioned_modules)
            shutil.copytree(root, dest_folder, ignore=ignore_patterns)

            for module in versioned_modules:
                generate_versioned_module(root, dest_folder, name=module, version=version)

            if not package_config.is_legacy:
                generate_blender_manifest(output_folder=dest_folder, version=version)

            generate_init_py(output_folder=dest_folder, version=version)

        replace_strings_with_regex(dest_folder/"prefs.py", substitutions=(
            (r'^( *bl_idname *= *).*', r'\1__package__'),
        ))
        replace_strings_with_regex(dest_folder/"utils.py", substitutions=(
            (r'preferences.addons\[\"Better Add Menu\"\].preferences', r'preferences.addons[__package__].preferences'),
        ))

        folder_to_pack = temp_dir if package_config.is_legacy else dest_folder
        shutil.make_archive(RELEASE_FOLDER / archive_name, "zip", folder_to_pack)

        print(f"Successfully created archive at '{archive_name}'")


def run():
    with open("build_config.toml", "rb") as f:
        config = BuildConfig(data=tomllib.load(f))
    
    initialize(RELEASE_FOLDER)
    for package_config in config.builds:
        build_package(package_config=package_config)

    return


if __name__ == "__main__":
    run()