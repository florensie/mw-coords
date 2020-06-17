import annotate_map
from pathlib import Path
from PIL import Image
import sys

DATA_PATH = Path(sys.path[0]) / 'data'

TV_STATION = {'orig': (14561, 18433), 'new': (4442, 3756)}  # Intel location 1 (front desk TV station)
AIRPORT = {'orig': (-22512, 19712), 'new': (2386, 3673)}  # Intel location 2 (airport gate)
AFB = {'orig': (3775, 48420), 'new': (3847, 2089)}  # Intel location 5 (AFB)

# Calculate scale using distance between tv_station and airport intel locations
diff_orig = abs(TV_STATION['orig'][0] - AIRPORT['orig'][0])
diff_new = abs(TV_STATION['new'][0] - AIRPORT['new'][0])
scale_x = diff_new / diff_orig
diff_orig = abs(TV_STATION['orig'][1] - AFB['orig'][1])
diff_new = abs(TV_STATION['new'][1] - AFB['new'][1])
scale_y = diff_new / diff_orig * -1  # y-axis is flipped!

# Calculate map origin
offset_x = TV_STATION['new'][0] - scale_x * TV_STATION['orig'][0]
offset_y = TV_STATION['new'][1] - scale_y * TV_STATION['orig'][1]


def calc_coord(x, y, invert=False):
    # Calculate new coord for x and y
    if not invert:
        x = x * scale_x + offset_x
        y = y * scale_y + offset_y
    else:
        x = (x - offset_x) / scale_x
        y = (y - offset_y) / scale_y
    return x, y


def main():
    x_orig = float(input('x: '))
    y_orig = float(input('y: '))

    x, y = calc_coord(x_orig, y_orig, input('invert?') in ['yes', 'y'])
    print(x, y)

    with Image.open(DATA_PATH / 'stitched_map.png') as im:
        im = annotate_map.annotate(im, (x_orig, y_orig), f'({round(x)}, {round(y)})', marker_color='yellow', scale=.2)
        annotate_map.rescale(im, 2).show()
        if input('save?') in ['yes', 'y']:
            im.save(DATA_PATH / 'annotated_map.png')


if __name__ == '__main__':
    main()
