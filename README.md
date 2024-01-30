**Running the GIS Data Visualization Application**

This Python application is a Flask-based web service that serves map tiles stored in a Mapbox Tileset (MBTiles) file. The served tiles are visualized as GeoJSON data on a plot using the Matplotlib library. Below are the steps to run the application:

### Prerequisites

1. **Python Installation:**
   - Ensure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

2. **Dependencies:**
   - Install the required Python libraries using the following command in your terminal or command prompt:
     ```
     pip install Flask geopandas matplotlib mapbox_vector_tile shapely
     ```

### Running the Application

1. **Download the Code:**
   - Download the provided Python code and save it in a directory of your choice.

2. **MBTiles File:**
   - Ensure you have the MBTiles file (`osm-2020-02-10-v3.11_africa_south-africa.mbtiles`) available. If not, you need to obtain this file or specify the correct path in the `MBTILES_PATH` variable within the code.

3. **Run the Application:**
   - Open a terminal or command prompt.
   - Navigate to the directory containing the Python code.
   - Run the following command:
     ```bash
     python filename.py
     ```
     Replace `filename.py` with the actual name of your Python script.

4. **Access the Web Service:**
   - Once the application is running, you can access the map tiles through the following URL:
     ```
     http://127.0.0.1:8282/wmtss/<x>/<y>/<z>
     ```
     Replace `<x>`, `<y>`, and `<z>` with the desired tile coordinates (zoom level, x, and y).

5. **View the Plot:**
   - The application will generate a GeoJSON file (`gegs.json`) and a PNG plot (`output.png`) in the same directory.
   - Open a web browser and go to the following URL to view the generated plot:
     ```
     http://127.0.0.1:8282/wmtss/<x>/<y>/<z>
     ```
     Replace `<x>`, `<y>`, and `<z>` with the tile coordinates used earlier.

6. **Shutdown the Application:**
   - To stop the Flask development server, press `Ctrl + C` in the terminal where the application is running.

### Notes

- Make sure that the required dependencies are installed, and the MBTiles file path is correctly specified in the code.
- The application is set to run on port 8282. If this port is already in use, you may need to modify the `port` parameter in the `app.run()` statement in the code.

Now you should have the GIS Data Visualization Application up and running!
