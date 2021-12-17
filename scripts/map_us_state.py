from argparse import ArgumentParser

from tqdm import tqdm
from wikidata.client import Client
import json
from urllib.error import HTTPError

from wikidata_merge import extract_value


def get_citizenship(e):
    if "P27" in e:
        citizenship_id = extract_value(e["P27"][0])
        if citizenship_id is not None:
            return citizenship_id["id"] if "id" in citizenship_id else None
    return None


def get_us_state(place_id):
    if place_id == 'Q61':
        return 'Washington City'
    try:
        place_data = client.get(place_id, load=True).data["claims"]
    except HTTPError:
        return None

    if 'P31' not in place_data:  # property 'instance of'
        return None

    if extract_value(place_data['P31'][0])['id'] == 'Q35657':  # if instance of us state
        if 'P1705' not in place_data: # if doesn't have label for item in its official or original language
            return None

        name_dct = extract_value(place_data['P1705'][0])
        if name_dct is None or 'text' not in name_dct:
            return None
        return name_dct['text']
    else:
        if 'P131' not in place_data:  # located in the administrative territorial entity
            return None

        parent_id = extract_value(place_data['P131'][0])['id']
        return get_us_state(parent_id)


if __name__ == "__main__":
    arg_parser = ArgumentParser()
    arg_parser.add_argument("--file", type=str)
    args = arg_parser.parse_args()

    client = Client()

    with open(args.file) as file:
        person_of_interest_ids = json.load(file)

    person2state = {}
    c = 0

    for person_idx in tqdm(person_of_interest_ids):
        try:
            wikidata_person = client.get(person_idx, load=True).data["claims"]
        except HTTPError:
            continue

        citizenship_id = get_citizenship(wikidata_person)
        if citizenship_id != 'Q30':  # USA
            continue

        c += 1
        # now person is usa citizen

        # check if he has work location
        if 'P937' in wikidata_person and len(wikidata_person['P937']) > 0:
            place_id = extract_value(wikidata_person['P937'][0])['id']
            us_state = get_us_state(place_id)
            person2state[person_idx] = us_state
            continue

        # check if he has place of birth
        if 'P19' in wikidata_person and len(wikidata_person['P19']) > 0:
            place_id = extract_value(wikidata_person['P19'][0])['id']
            us_state = get_us_state(place_id)
            person2state[person_idx] = us_state
            continue

    print(f'total americans: {c} / {len(person_of_interest_ids)}')
    print(f'total states: {len(person2state)} / {c}')

    with open('person2state.json', "w") as file:
        json.dump(person2state, file)
