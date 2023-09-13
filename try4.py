import json
import argparse
import os

def generate_html_list(data):
    html_list = "<ul>"
    for key, value in data.items():
        html_list += f"<li><strong>{key}:</strong> {value}</li>"
    html_list += "</ul>"
    return html_list

# Initialize argument parser
parser = argparse.ArgumentParser(description='Convert JSON report to simplified HTML.')
parser.add_argument('json_file', metavar='JSON_FILE', type=str, help='Path to the JSON report file')
args = parser.parse_args()
json_file_path = args.json_file

if not os.path.exists(json_file_path):
    print(f"File not found: {json_file_path}")
else:
    try:
        with open(json_file_path, 'r') as json_file:
            report_data = json.load(json_file)

        # Generate plain HTML content with the report data in a simplified format
        html_output = f"""
        <html>
        <body>
        <h1>JSON Report</h1>
        {generate_html_list(report_data)}
        </body>
        </html>
        """
        
        # Write the HTML to a file with the same name as the JSON file but with .html extension
        html_file_path = os.path.splitext(json_file_path)[0] + '.html'
        with open(html_file_path, 'w') as html_file:
            html_file.write(html_output)
        
        print(f"HTML report generated: {html_file_path}")
    except json.JSONDecodeError:
        print(f"Error decoding JSON in {json_file_path}")
