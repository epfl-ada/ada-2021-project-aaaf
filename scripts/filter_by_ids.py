import json
from argparse import ArgumentParser

from tqdm import tqdm

from filter import iterate, drop_keys


def fetch(lines, ids):
    """
    Iterate through all the lines and keep only the necessary ones
    """
    lines = filter(
        lambda x: any(idx in x["qids"] for idx in ids),
        map(json.loads, lines),
    )
    lines = map(drop_keys, lines)
    return lines


if __name__ == "__main__":
    arg_parser = ArgumentParser()
    arg_parser.add_argument("--data-file", type=str)
    arg_parser.add_argument("--ids-file", type=str)
    arg_parser.add_argument("--year", type=str)
    args = arg_parser.parse_args()

    with open(args.ids_file) as file:
        person_of_interest_ids = json.load(file)

    fetched_lines = fetch(iterate(args.data_file), person_of_interest_ids)

    with open(f"output-{args.year}.json", "w+") as file:
        for row in tqdm(fetched_lines):
            json.dump(row, file)
            file.write("\n")

        file.seek(0)
        selected_rows = []
        for line in file:
            selected_rows.append(json.loads(line))

        file.seek(0)
        json.dump(selected_rows, file)
