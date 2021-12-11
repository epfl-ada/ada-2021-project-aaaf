import json
from argparse import ArgumentParser

from tqdm import tqdm


KEYS_TO_DROP = ["quoteID", "urls", "phase", "probas"]
TOPICS = [
    "brexit",
    "drugs",
    "sexism",
    "immigration",
    "islam",
    "ebola",
    "pandemy",
    "terrorism",
    "home violence",
    "meat consumption",
    "vegetarian",
    "feminism",
    "harassment",
    "darknet",
    "fraud",
    "privacy",
    "climate change",
    "global warming",
    "carbon emission",
    "mental disease",
    "mental health",
    "burn out",
    "burnout",
]


def iterate(file_name):
    """
    Create generator to read file line by line
    """
    with open(file_name) as f:
        for line in f:
            yield line


def drop_keys(line):
    """
    Remove redundant keys to use less memory
    """
    for key in KEYS_TO_DROP:
        del line[key]
    return line


def fetch(lines):
    """
    Iterate through all the lines and keep only the necessary ones
    """
    lines = filter(
        lambda x: (x["speaker"] != "None") and (x["qids"]),
        map(json.loads, lines),
    )
    lines = map(drop_keys, lines)
    lines = filter(lambda x: any(top in x['quotation'].lower() for top in TOPICS), lines)
    return lines


if __name__ == "__main__":
    arg_parser = ArgumentParser()
    arg_parser.add_argument("--year", type=int)
    args = arg_parser.parse_args()

    filename = f'quotes-{args.year}'

    fetched_lines = fetch(iterate(f'{filename}.json'))

    with open(f"{filename}-filtered.json", "w+") as file:
        for row in tqdm(fetched_lines):
            json.dump(row, file)
            file.write("\n")

        file.seek(0)
        selected_rows = []
        for line in file:
            selected_rows.append(json.loads(line))

        file.seek(0)
        json.dump(selected_rows, file)
