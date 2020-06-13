import csv
import calc
from PIL import Image, ImageDraw

RADIUS = 20  # Radius for dots to be placed


def main():
    with open('intel_challenges.csv') as f:
        table = csv.reader(f)

        with Image.open('stitched_map.png') as im:
            draw = ImageDraw.Draw(im)
            for row in table:
                if row[2] == '1':  # Check if challenge has interactable (coords)
                    x, y = calc.calc_coord(int(row[5]), int(row[6]))
                    draw.ellipse((x-RADIUS, y-RADIUS, x+RADIUS, y+RADIUS), 'red')

            im.save('annotated_map.png')


if __name__ == '__main__':
    main()
