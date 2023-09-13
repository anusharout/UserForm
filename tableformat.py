import json
import argparse #used to parse command-line arguments 
import os
from json2html import json2html  # Import json2html

# Initialize argument parser
parser = argparse.ArgumentParser(description='Convert JSON report to HTML.')
parser.add_argument('json_file', metavar='JSON_FILE', type=str, help='Path to the JSON report file')
args = parser.parse_args() #parses the command-line arguments provided when running the script
json_file_path = args.json_file #contain the path to the JSON file provided as an argument

if not os.path.exists(json_file_path):
    print(f"File not found: {json_file_path}")
else:
    try:
        with open(json_file_path, 'r') as json_file:
            report_data = json.load(json_file)

        # Convert JSON to HTML using json2html
        html_output = json2html.convert(json=report_data)
        
       # Write the HTML to a file with the same name as the JSON file but with .html extension
        html_file_path = os.path.splitext(json_file_path)[0] + '.html'
        with open(html_file_path, 'w') as html_file:
            html_file.write(html_output)
        
        print(f"HTML report generated: {html_file_path}")
    except json.JSONDecodeError:
        print(f"Error decoding JSON in {json_file_path}")
