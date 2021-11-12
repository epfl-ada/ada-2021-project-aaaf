from argparse import ArgumentParser

from tqdm import tqdm
from wikidata.client import Client
import json
from urllib.error import HTTPError


if __name__ == "__main__":
    arg_parser = ArgumentParser()
    arg_parser.add_argument("--file", type=str)
    args = arg_parser.parse_args()

    client = Client()

    with open(args.file) as file:
        lines = json.load(file)
    occupations = set()
    countries = set()

    for line in tqdm(lines):
        for x in line["occupation_ids"]:
            if x is not None:
                occupations.update(x)
        for x in line["citizenship_id"]:
            if x is not None:
                print(x)
                countries.add(x)

    mapping = {}
    for name, data_set in zip(['countries', 'occupations'], [countries, occupations]):
        feature_dct = dict()
        for idx in tqdm(data_set):
            try:
                feature_dct[idx] = str(client.get(idx, load=True).label)
            except HTTPError:
                continue

        mapping[name] = feature_dct

    with open('mapping.json', "w") as file:
        json.dump(mapping, file)
