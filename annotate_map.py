from PIL import Image, ImageDraw, ImageFont
import calc

DOT_RADIUS = 20
FONT_SIZE = 45


def annotate(im, xy, text='', scale=1):
    font = ImageFont.truetype('arial.ttf', round(FONT_SIZE*scale))
    draw = ImageDraw.Draw(im)
    x, y = calc.calc_coord(*xy)
    radius = DOT_RADIUS * scale
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), 'lime')
    draw.text((x + radius, y + radius), text, 'blue', font)
    return im


def rescale(im, factor):
    return im.resize((int(im.width/factor), int(im.height/factor)))
