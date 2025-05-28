# -*- coding: utf-8 -*-

import arcpy


class Toolbox:
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Raster Conversion Toolbox"
        self.alias = "rasterconvert"

        # List of tool classes associated with this toolbox
        self.tools = [BatchRasterFolderToTIFF]


class BatchRasterFolderToTIFF(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Batch Convert Raster Folders to TIFF"
        self.description = "Recursively process folders containing ESRI GRID or other raster datasets, " \
            "convert them to GeoTIFF (.tif), and save outputs into subfolders named after each dataset."
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define the tool parameters."""
        return [
            arcpy.Parameter(
                displayName="Top-Level Folder Containing Raster Subfolders",
                name="top_input_folder",
                datatype="DEFolder",
                parameterType="Required",
                direction="Input"
            ),
            arcpy.Parameter(
                displayName="Output Root Folder",
                name="output_root",
                datatype="DEFolder",
                parameterType="Required",
                direction="Output"
            )
        ]

    def isLicensed(self):
        """Set whether the tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        top_input_folder = parameters[0].valueAsText
        output_root = parameters[1].valueAsText

        for dirpath, dirnames, filenames in os.walk(top_input_folder):
            arcpy.env.workspace = dirpath
            rasters = arcpy.ListRasters()

            if not rasters:
                continue

            for raster in rasters:
                try:
                    raster_path = os.path.join(dirpath, raster)
                    raster_name = os.path.splitext(raster)[0]
                    out_folder = os.path.join(output_root, raster_name)

                    if not os.path.exists(out_folder):
                        os.makedirs(out_folder)

                    output_path = os.path.join(out_folder, raster_name + ".tif")

                    if os.path.exists(output_path):
                        arcpy.AddMessage(f"⏩ Skipping existing: {output_path}")
                        continue

                    arcpy.CopyRaster_management(raster_path, output_path)
                    arcpy.AddMessage(f"✅ Converted: {raster_path} → {output_path}")

                except Exception as e:
                    arcpy.AddError(f"❌ Failed to convert {raster_path}: {e}")
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
