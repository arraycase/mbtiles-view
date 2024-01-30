import os
import sqlite3
import gzip
import mapbox_vector_tile 
import io 
import matplotlib.pyplot as plt
from flask import send_file
from flask import Flask
import geopandas as gpd
from shapely.affinity import translate
import geopandas as gpd
import json 

app = Flask(__name__)


MBTILES_PATH = os.path.abspath("./app/uploads/osm-2020-02-10-v3.11_africa_south-africa.mbtiles")


def serve_tile(z,x,y):
    try:
      
        conn = sqlite3.connect(MBTILES_PATH)
        c = conn.cursor()
        c.execute("SELECT tile_data FROM tiles WHERE zoom_level=? AND tile_column=? AND tile_row=?", (z, x, y))
        cc = c.fetchone()
        decompressed_data = gzip.decompress(cc[0])
        decompressed_data_pk = mapbox_vector_tile.decode(decompressed_data)
        with open('gegs.json', 'w+') as outfile:
            json.dump(decompressed_data_pk, outfile)
        conn.close()
        return True
    except Exception as e:
        return False
    

@app.route('/wmtss/<x>/<y>/<z>')
def serve_tiless(x,y,z):
    # Call serve_tile function to retrieve tile data
    try:
        x = int(x)
        y = int(y)
        z = int(z)
        tile_data = serve_tile(z=z , x=x, y=y)

        if tile_data:
            gdf = gpd.read_file('./gegs.json', driver='GeoJSON')

            # Find the minimum x and y values
            min_x, min_y = gdf.total_bounds[:2]

            # Translate all geometries to ensure non-negative coordinates
            gdf['geometry'] = gdf['geometry'].apply(lambda geom: translate(geom, xoff=-min_x, yoff=-min_y))

            # Create a plot
            fig, ax = plt.subplots(figsize=(10, 10))

            # Plot the GeoDataFrame
            gdf.plot(ax=ax, facecolor='lightblue', edgecolor='black')

            # Set equal aspect ratio
            ax.set_aspect('equal', adjustable='box')

            # Remove x and y axis labels
            ax.set_xticks([])
            ax.set_yticks([])
            
            # Save the plot as a PNG file
            plt.savefig("output.png", bbox_inches='tight', pad_inches=0, transparent=True)

            final_immg_bytes  = None 
            with open("output.png", "rb") as image_file:
                final_immg_bytes = image_file.read()
            

            return send_file(
                io.BytesIO(final_immg_bytes),
                mimetype='image/jpeg')
        else:
            return "Tile not found ", 404
    except Exception as e:
        return "Error (tile might not be available) : "+str(e)


if __name__ == "__main__":
    app.run(debug=True, port=8282)
