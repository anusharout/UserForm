import json
import argparse
import os

# Initialize argument parser
parser = argparse.ArgumentParser(description='Read JSON report and optionally save as HTML.')
parser.add_argument('json_file', metavar='JSON_FILE', type=str, help='Path to the JSON report file')
parser.add_argument('--html_file', metavar='HTML_FILE', type=str, help='Path to the HTML output file (optional)')
args = parser.parse_args()

# Read the JSON file path from the command-line argument
json_file_path = args.json_file

# Check if the JSON file exists
if not os.path.exists(json_file_path):
    print(f"File not found: {json_file_path}")
else:
    try:
        # Open and read the JSON file
        with open(json_file_path, 'r') as json_file:
            report_data = json.load(json_file)

        # Print or process the JSON data as needed
        print(report_data)  # You can print or process the JSON data here

        # Optionally save the JSON data as HTML if an HTML file path is provided
        if args.html_file:
            # Generate an HTML string with JSON data
            html_output = f'<html><body><pre>{json.dumps(report_data, indent=4)}</pre></body></html>'
            
            # Write the HTML string to the specified HTML file
            with open(args.html_file, 'w') as html_file:
                html_file.write(html_output)
                print(f"JSON data saved as HTML: {args.html_file}")
    except json.JSONDecodeError:
        print(f"Error decoding JSON in {json_file_path}")
    except PermissionError as e:
        print(f"Permission error: {e}")
