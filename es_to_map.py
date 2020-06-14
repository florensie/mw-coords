import json
from PIL import Image
import annotate_map

with open('es_mark.json') as f:
    es = json.load(f)

    with Image.open('stitched_map.png') as im:
        for hit in es['hits']['hits']:
            x, y, z = hit['_source']['translation']

            # DOM FLAG: text = hit['_source']['43887'][1:].upper()
            # text = hit['_source']['desc']
            text = ''

            annotate_map.annotate(im, (x, y), text, scale=.5)

        print("Success. Saving map.")
        annotate_map.rescale(im, 2).show()
