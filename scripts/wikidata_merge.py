from argparse import ArgumentParser
from wikidata.client import Client
import json
from urllib.error import HTTPError


def extract_value(pos):
    try:
        return pos["mainsnak"]["datavalue"]["value"]
    except KeyError:
        return None


def get_features(elem):
    """
    Extract list of 3 features from wiki data element
    """
    features = []

    citizenship_feature = None
    if "P27" in elem:
        citizenship_id = extract_value(elem["P27"][0])
        if citizenship_id is not None:
            citizenship_feature = citizenship_id.get("id", None)
    features.append(citizenship_feature)

    gender_feature = None
    if "P21" in elem:
        gender_id = extract_value(elem["P21"][0])
        if gender_id is not None:
            if "id" in gender_id:
                if gender_id["id"] == 'Q6581072':
                    gender_feature = 'female'
                elif gender_id["id"] == 'Q6581097':
                    gender_feature = 'male'
    features.append(gender_feature)

    occupations_feature = []
    if "P106" in elem:
        for j in range(len(elem["P106"])):
            occupation_id = extract_value(elem["P106"][j])
            occupation_id = occupation_id.get("id", None)
            occupations_feature.append(occupation_id)
    features.append(occupations_feature or None)

    return features


def add_wiki_features(line, client):
    """
    Add wikipedia features to data element (quotation info dct)
    """
    arr = []

    for i, id_ in enumerate(line["qids"]):
        try:
            entity = client.get(id_, load=True).data["claims"]
            arr.append(get_features(entity))
        except HTTPError:
            continue

    line['citizenship_id'], line['gender'], line['occupation_ids'] = list(map(list, zip(*arr)))
    return line


if __name__ == "__main__":
    arg_parser = ArgumentParser()
    arg_parser.add_argument("--year", type=str)
    args = arg_parser.parse_args()

    c = Client()

    input_file = f'quotes-{args.year}-filtered.json'
    output_file = f'quotes-{args.year}-wikimerged.json'
    
    with open(input_file) as file:
        lines = json.load(file)
    merged = [add_wiki_features(line, client=c) for line in lines]

    with open(output_file, "w") as file:
        json.dump(merged, file)
