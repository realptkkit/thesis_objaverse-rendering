import json
import os
from pathlib import Path

def create_json(input_dir, output_dir, json_file):
    """
    Creates a JSON file containing a list of tuples (input_object, output_dir).

    Args:
        input_dir (str): Path to the input directory.
        output_dir (str): Path to the output directory.
        json_file (str): Path to the output JSON file.
    """

    data = []
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".obj"):
                input_path = Path(root) / file
                category_name = input_path.parts[-2]
                part_number = input_path.parts[-1]
                output_path = Path(output_dir) / category_name / part_number.split(".")[0]
                os.makedirs(output_path, exist_ok=True)  # Create output directory if not exists
                data.append((str(input_path), str(output_path)))

    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)

# Example usage:
input_dir = "/mnt/c/Users/PhilippKataliakos/data/train-data/MCB/MCB_A/dataset_org_norm/train"
output_dir = "/mnt/c/Users/PhilippKataliakos/data/train-data/MCB/MCB_A/img/train"
json_file = "train_data.json"

create_json(input_dir, output_dir, json_file)

# input_dir = "/mnt/c/Users/PhilippKataliakos/data/train-data/MCB/MCB_A/dataset_org_norm/test"
# output_dir = "/mnt/c/Users/PhilippKataliakos/data/train-data/MCB/MCB_A/img/train"
# json_file = "test_data.json"

# create_json(input_dir, output_dir, json_file)