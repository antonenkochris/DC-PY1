import json

INPUT_FILE = "input_1.csv"


def csv_to_list_dict(filename, delimiter=",", new_line='\n') -> list[dict]:
    with open(filename, 'r') as f:
        total = [line.rstrip(new_line).split(delimiter) for line in f.readlines()]
        headers = total[0]
        return [dict(zip(headers, rows)) for rows in total[1:]]


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
