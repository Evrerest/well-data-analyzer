# Well Data Analyzer

This project is a starter Python app for loading Excel-based well/core data and exploring it with an interactive geologist-facing cross-plot.

## What it does

- Loads an `.xlsx` workbook that follows the sample layout in `Viking Core Data.xlsx`
- Uses cell `A1` as the screen title
- Uses column `A` as the area grouping and column `B` as the well grouping
- Defaults the graph to `Por` on the X axis and `kmax` on the Y axis
- Provides an interactive graph plus a settings tab for:
  - linear or logarithmic axes
  - X start and end
  - Y start and end
  - major and minor tick spacing

## Run it

From PowerShell in this folder:

```powershell
.\run_app.ps1
```

If you prefer running it manually:

```powershell
& "C:\Users\ekost\AppData\Local\Programs\Python\Python312\python.exe" -m streamlit run app.py
```

## Build A Windows Executable

Windows packaging is currently archived for later use because the preferred beta path is public web deployment.
The packaging files are kept under `archive\packaging\`.

This project includes a PyInstaller-based packaging flow for beta testers.

Build it from PowerShell:

```powershell
.\archive\packaging\build_exe.ps1
```

The packaged app will be created in:

```text
archive\packaging\build_outputs\dist_release\WellDataAnalyzer\
```

Send the whole `WellDataAnalyzer` folder to testers, not just the `.exe` by itself.

### What testers do

1. Unzip the folder
2. Run `WellDataAnalyzer.exe`
3. The app opens in their browser as a local app

### Packaging notes

- The build bundles `app.py` and the Python runtime dependencies.
- If `C:\Users\ekost\Downloads\Viking Core Data.xlsx` exists at build time, it is included as a sample workbook inside the package.
- Testers can still upload their own `.xlsx` files even if no sample workbook is bundled.
- This is currently a Windows build process.

## Deploy Publicly

For the current beta phase, the recommended path is Streamlit Community Cloud.

See `DEPLOY_STREAMLIT_CLOUD.md` for the deployment steps.

## Notes

- The app starts with `C:\Users\ekost\Downloads\Viking Core Data.xlsx` as the default sample workbook path.
- You can also upload another `.xlsx` file from the sidebar.
- The workbook parser currently treats the first worksheet as the source sheet and carries `Area` and `Well` values downward when the sheet leaves those cells blank between rows.
