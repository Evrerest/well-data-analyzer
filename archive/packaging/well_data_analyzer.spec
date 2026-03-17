# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path

from PyInstaller.utils.hooks import collect_data_files, collect_submodules, copy_metadata


project_dir = Path.cwd()
sample_source = Path(r"C:\Users\ekost\Downloads\Viking Core Data.xlsx")
datas = collect_data_files("streamlit")
datas += collect_data_files("altair")
datas += collect_data_files("pydeck")
datas += collect_data_files("plotly")
datas += copy_metadata("streamlit")
datas += [(str(project_dir / "app.py"), ".")]

if sample_source.exists():
    datas += [(str(sample_source), "sample_data")]

hiddenimports = []
for package_name in ["streamlit", "altair", "pydeck", "plotly"]:
    hiddenimports += collect_submodules(package_name)


a = Analysis(
    ["launcher.py"],
    pathex=[str(project_dir)],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="WellDataAnalyzer",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="WellDataAnalyzer",
)
