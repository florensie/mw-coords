import csv
from PIL import Image
import annotate_map
import calc


def main():
    with open('data/intel_challenges.csv') as f:
        table = csv.reader(f)

        with Image.open('data/stitched_map.png') as im:
            step = 1  # Current step

            for row in table:
                if row[2] == '1':  # Check if challenge has interactable (coords)
                    annotate_map.annotate(im, (int(row[5]), int(row[6])), str(step))
                    step += 1

            print("Success. Saving map.")
            im.save('annotated_map.png')


if __name__ == '__main__':
    main()
