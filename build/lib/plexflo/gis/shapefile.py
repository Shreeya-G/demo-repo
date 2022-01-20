from osgeo import gdal
import geopandas as gpd
import glob
import os
from zipfile import ZipFile
from pathlib import Path

from ..utils.fileops import remove_path


def shapefile2geojson(infile, outfile):
    '''Translate a shapefile to GEOJSON.'''
    options = gdal.VectorTranslateOptions(format="GeoJSON",
                                          dstSRS="EPSG:4326")
    gdal.VectorTranslate(outfile, infile, options=options)


def shapefile_centroid(infile, feature_column_name):
    pass

def split_shpfile_into_multiple_shpfiles(infile, feature_column_name):
    outfolder = Path(infile).stem
    Path(outfolder).mkdir(exist_ok=True, parents=True)
    file_of_interest = []

    with ZipFile(infile, 'r') as zip_ref:
        zip_ref.extractall(outfolder)
        os.chdir(f"{outfolder}/{outfolder}")
        for file in glob.glob("*.shp"):
            file_of_interest.append(file)

        file_of_interest = file_of_interest[0]

        data = gpd.read_file(file_of_interest)

        for idx, row in data.iterrows():
            output_name = f"{row[feature_column_name].replace(' ', '_')}.shp"
            shp_name = row[feature_column_name]
            Path(f"{shp_name}/ArcGIS_shpfile").mkdir(exist_ok=True, parents=True)
            output_path = os.path.join(shp_name, "ArcGIS_shpfile", output_name)
            tmp_df = data[data[feature_column_name] == shp_name]
            tmp_df.to_file(output_path)


def split_shpfile_into_multiple_geojson(infile, feature_column_name):
    outfolder = Path(infile).stem
    Path(outfolder).mkdir(exist_ok=True, parents=True)
    file_of_interest = []

    with ZipFile(infile, 'r') as zip_ref:
        zip_ref.extractall(outfolder)
        os.chdir(f"{outfolder}/{outfolder}")
        for file in glob.glob("*.shp"):
            file_of_interest.append(file)

        file_of_interest = file_of_interest[0]

        data = gpd.read_file(file_of_interest)

        for idx, row in data.iterrows():
            shpfile_output_name = f"{row[feature_column_name].replace(' ', '_')}.shp"
            geojson_output_name = f"{row[feature_column_name].replace(' ', '_')}.geojson"
            shp_name = row[feature_column_name]
            Path(f"{shp_name}/ArcGIS_shpfile").mkdir(exist_ok=True, parents=True)
            Path(f"{shp_name}/GeoJSON").mkdir(exist_ok=True, parents=True)
            shpfile_output_path = os.path.join(shp_name, "ArcGIS_shpfile", shpfile_output_name)
            geojson_output_path = os.path.join(shp_name, "GeoJSON", geojson_output_name)
            tmp_df = data[data[feature_column_name] == shp_name]
            tmp_df.to_file(shpfile_output_path)
            shapefile2geojson(shpfile_output_path, geojson_output_path)
            try:
                remove_path(Path(f"{shp_name}/ArcGIS_shpfile"))
            except OSError as e:
                print("Error Code 901: Could not delete temporary *.shpfile folder %s \n%s" % (
                    shpfile_output_path, e.strerror))
