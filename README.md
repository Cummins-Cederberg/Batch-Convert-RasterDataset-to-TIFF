# Batch-Convert-RasterDataset-to-TIFF-Toolbox
# 🗺️ Raster Conversion Toolbox

This ArcGIS Python Toolbox (`.pyt`) automates the batch conversion of raster datasets (a fundamental type of geographic data that stores information as a grid of cells, also known as pixels) into GeoTIFF (`.tif`) format. The tool scans through a top-level directory, detects rasters in subfolders, and writes output files into structured subdirectories.

---

## Tool: **Batch Convert Raster Folders to TIFF**

### Description

This tool recursively processes all folders under a specified top-level directory, identifies raster datasets, and converts each to a GeoTIFF file. Output files are organized into subfolders named after the original raster datasets.

---

## Parameters

| Parameter | Type | Description |
|----------|------|-------------|
| `Top-Level Folder Containing Raster Subfolders` | Folder | The root directory where the tool will look for raster datasets recursively. |
| `Output Root Folder` | Folder | The root output directory where TIFF files and subfolders will be saved. Each raster will be placed in its own folder. |

---

## How It Works

1. Walks through the folder tree starting at the given top-level input folder.
2. Detects raster datasets in each subfolder using `arcpy.ListRasters()`.
3. For each raster:
   - A subfolder is created in the output root (if not already present).
   - The raster is converted to `.tif` using `arcpy.CopyRaster_management()`.
   - Converted files are saved as `<rastername>.tif` in a matching subfolder.

4. Existing `.tif` files are skipped to prevent duplicate processing.

---


## Notes

- Works with RasterDataset supported by ArcPy.
- Requires the ArcGIS Spatial Analyst or Advanced license.
- Make sure raster folder names are valid and consistent.

---

## License

Developed for use with ArcGIS Pro and Python 3.11.11 Requires licensed ArcPy environment.
