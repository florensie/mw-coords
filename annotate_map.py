from PIL import Image, ImageDraw, ImageFont
import calc

MARKER_RADIUS = 20
FONT_SIZE = 55
MAP_OUT_OF_BOUNDS = (819, 819, 7373, 7373)  # Crop this box to remove out of bounds area


def annotate(im, xy, text='', scale=1, marker_color='lime', text_color='white', text_loc=(1, 1)):
    """
    Place a marker and text on the map
    :param im: The map PIL image
    :param xy: The game coordinates
    :param text: Text annotation to place next to marker
    :param scale: Size of marker and text
    :param marker_color: Color to fill marker with
    :param text_color: Color to fill text with
    :param text_loc: xy tuple of which corner of marker to render text at
                    -1 for left/up, 0 for center, 1 for right/down
                    default is bottom right
    :return: the annotated image
    """
    if text_loc is None:
        text_loc = [1, 0]
    font = ImageFont.truetype('arial.ttf', round(FONT_SIZE*scale))
    draw = ImageDraw.Draw(im)
    x, y = calc.calc_coord(*xy)
    radius = MARKER_RADIUS * scale
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), marker_color,
                 outline='black', width=5)
    draw.text((x + radius * text_loc[0], y + radius * text_loc[1]), text, text_color, font,
              stroke_width=3, stroke_fill='black')
    return im


def rescale(im, factor):
    """
    Utility function to rescale a PIL image by a single factor
    :param im: image to rescale
    :param factor: factor to rescale by
    :return: rescaled image
    """
    return im.resize((int(im.width/factor), int(im.height/factor)))


def crop_out_of_bounds(im):
    return im.crop(MAP_OUT_OF_BOUNDS)
