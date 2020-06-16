import json
from PIL import Image
import annotate_map

with open('data/es_mark.json') as f:
    es = json.load(f)

    with Image.open('data/stitched_map.png') as im:
        for hit in es['hits']['hits']:
            x, y, z = hit['_source']['translation']

            # DOM FLAG: text = hit['_source']['43887'][1:].upper()
            # text = hit['_source']['desc']
            text = ''
            # text = hit['_source']['desc']

            annotate_map.annotate(im, (x, y), text, scale=.2)

        print("Success. Saving map.")
        annotate_map.rescale(im, 2).show()
        im.save('data/annotated_map.png')
