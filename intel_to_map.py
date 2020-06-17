import csv
from PIL import Image
import annotate_map
from calc import DATA_PATH

WEEK_COLORS = ['lime', 'yellow', 'cyan', 'magenta', 'crimson', 'blueviolet']
ALT_LOC = [(2, 4), (4, 2)]  # hard-coded alternate text locations to prevent overlap


def main():
    with open(DATA_PATH / 'intel_challenges.csv') as f:
        table = csv.reader(f)

        with Image.open(DATA_PATH / 'stitched_map.png') as im:
            week = 0
            step = 1  # Current step

            for row in table:
                if row[2] == '1':  # Check if challenge has interactable (coords)
                    text_loc = (1, 1)
                    if (week, step) in ALT_LOC:
                        text_loc = (1, -3)
                    annotate_map.annotate(im, (int(row[5]), int(row[6])), f'W{week} S{step}',
                                          marker_color=WEEK_COLORS[week-1], text_loc=text_loc)
                    step += 1
                else:
                    week += 1
                    step = 1

            print("Success. Saving map.")
            im = annotate_map.rescale(im, 2)
            im.show()
            im.convert('RGB').save(DATA_PATH / 'intel_map.jpg', quality=85)


if __name__ == '__main__':
    main()
