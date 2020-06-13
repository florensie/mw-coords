import csv
import main
from PIL import Image

with open('intel.csv') as f:
    table = csv.reader(f)

    with Image.open('verdansk-12k2.jpg') as im:
        for row in table:
            x, y = main.calc_coord(row[6], row[7])
