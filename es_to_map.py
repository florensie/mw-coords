import json
from PIL import Image
from pathlib import Path
import annotate_map
from calc import DATA_PATH

es = json.load(Path('data/es_mark.json').open())

with Image.open(DATA_PATH / 'stitched_map.png') as im:
    for hit in es['hits']['hits']:
        x, y, z = hit['_source']['translation']

        # DOM FLAG: text = hit['_source']['43887'][1:].upper()
        # text = hit['_source']['desc']
        text = ''
        # text = hit['_source']['desc']

        annotate_map.annotate(im, (x, y), text, scale=.2)

    print("Success. Saving map.")
    annotate_map.rescale(im, 2).show()
    im.save(DATA_PATH / 'annotated_map.png')
