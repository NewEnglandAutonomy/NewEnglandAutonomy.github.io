# convert a directory of shapefiles into GeoJSON
import os, sys
import pandas as pd
import geopandas as gpd
from pathlib import Path

def shp2geojson(shapefile_path,geojson_path):
    try:
        # open shapefile at path as GeoDataFrame
        gdf = gpd.read_file(shapefile_path)
        gdf.to_file(geojson_path, driver="GeoJSON")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__=="__main__":
    from_dir = sys.argv[1]
    to_dir = sys.argv[2]
    for shapefile_path in Path(from_dir).glob('*.shp'):
        try:
            geojson_path = os.path.join(to_dir, os.path.split(shapefile_path)[1].split(".")[0] + ".geojson")
            shp2geojson(shapefile_path, geojson_path)
            print(f"{shapefile_path} -> {geojson_path}")
        except Exception as e:
            print(f"Error: {e}")