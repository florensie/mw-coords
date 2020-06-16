import json
from elasticsearch import Elasticsearch
import calc

# These are obfuscated
KEY_MAPPINGS = {
    '212': 'type',
    '709': 'translation',
    '80': 'rotation',
    '1072': 'desc1',
    '845': 'desc2',
    '652': 'model',
    '43840': 'modes',
    '43887': 'objective_letter?',

    # These were left in in one of the S03 builds
    '63913': 'lgbudgetingprobesize',
    '63914': 'lgsplittransients',
    '64017': 'locked_proxylod',
    '64197': 'mapnamefilter',
    '66774': 'scriptable_reserved_count',
    '68080': 'superterrainlightbakelodoverride',
    '68450': 'tr_vis_facing_dist_add_override',
    '68451': 'tr_vis_radius_override_lod1',
    '68452': 'tr_vis_radius_override_lod2',
    '68489': 'transient_prefab_group',
    '68490': 'transient_world_autolod_enabled'
}


def to_dict(f_in):
    result = []

    for line in f_in.readlines():
        line = line[:-1]  # Remove newline

        if line == '{':
            current_dict = {}
        elif line == '}':
            # noinspection PyUnboundLocalVariable
            result.append(current_dict)
        else:
            key, value = line.split(' ',  1)

            value = value[1:-1]  # Remove extra quotes at start and end

            # Remap keys to something readable
            if key in KEY_MAPPINGS.keys():
                key = KEY_MAPPINGS[key]

            # Reformat rotation and translation
            if key == 'rotation' or key == 'translation':
                value = value.split(' ')  # Split x, y, z values
                value = list(map(float,  value))  # Convert strings to floats

            current_dict[key] = value

    return result


def get_all_in_box(res, xy_sw, xy_ne):
    # Convert coords
    xy_sw = calc.calc_coord(*xy_sw, True)
    xy_ne = calc.calc_coord(*xy_ne, True)

    if xy_sw[0] >= xy_ne[0] or xy_sw[1] >= xy_ne[1]:
        raise TypeError("invalid bounding box")

    result = []
    for entity in res:
        if 'translation' in entity.keys():
            posx, posy = entity['translation'][:2]
            if xy_sw[0] <= posx <= xy_ne[0] and xy_sw[1] <= posy <= xy_ne[1]:
                result.append(entity)

    return result


if __name__ == '__main__':
    with open('data/mp_don3.d3dbsp') as f:
        res = to_dict(f)

    if input('bounding box?') in ['yes', 'y']:
        xy = []
        for i in range(4):
            if i % 2 == 0:
                xy.append(float(input('x?')))
            else:
                xy.append(float(input('y?')))
        res = get_all_in_box(res, xy[:-2], xy[-2:])

    # Dump
    dump_type = input('dump type? (es/json)')
    if dump_type == 'es':
        es = Elasticsearch()
        index = input('index?')
        for i, entity in enumerate(res):
            res = es.index(index=index, id=i, body=entity)
    elif dump_type == 'json':
        with open('data/mp_don3.json', 'w') as f_out:
            json.dump(res, f_out, indent=4, sort_keys=True)
