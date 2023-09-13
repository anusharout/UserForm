import json
import argparse
import os
parser = argparse.ArgumentParser(description='Read JSON report.')
parser.add_argument('json_file', metavar='JSON_FILE', type=str, help='Path to the JSON report file')
args = parser.parse_args()
json_file_path = args.json_file
if not os.path.exists(json_file_path):
    print(f"File not found: {json_file_path}")
else:
    try:
        with open(json_file_path, 'r') as json_file:
            report_data = json.load(json_file)
        print(report_data)
    except json.JSONDecodeError:
        print(f"Error decoding JSON in {json_file_path}")
    except PermissionError as e:
         print(f"Permission error: {e}")


