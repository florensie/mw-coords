import json
from PIL import Image
from pathlib import Path
import annotate_map
from calc import DATA_PATH


if __name__ == '__main__':
    es = json.load(Path('data/es_mark.json').open())

    with Image.open(DATA_PATH / 'stitched_map.png') as im:
        for i, hit in enumerate(es['hits']['hits'], start=1):
            x, y, z = hit['_source']['translation']

            # DOM FLAG: text = hit['_source']['43887'][1:].upper()
            # text = hit['_source']['desc1']
            # text = ''
            # text = hit['_source']['model']
            text = hit['_source']['43632']

            annotate_map.annotate(im, (x, y), text, scale=1)

        print("Success. Saving map.")
        im = annotate_map.rescale(im, 2)
        im.show()
        im.convert('RGB').save(DATA_PATH / 'annotated_map.jpg')
