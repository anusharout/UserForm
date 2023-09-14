import json
import argparse
import os

def generate_html_content(data):
    html_content = ""
    
    # Add a heading for the report
    html_content += "<h1>JSON Report</h1>"

    # Loop through the JSON data and format each key-value pair
    for key, value in data.items():
        html_content += f"<div>"
        html_content += f"<h2>{key}</h2>"
        
        # Check if the value is a list and format it as an ordered list
        if isinstance(value, list):
            html_content += "<ul>"
            for item in value:
                if isinstance(item, dict):
                    html_content += "<li>"
                    html_content += "<ul>"
                    for sub_key, sub_value in item.items():
                        html_content += f"<li><strong>{sub_key}:</strong> {sub_value}</li>"
                    html_content += "</ul>"
                    html_content += "</li>"
                else:
                    html_content += f"<li>{item}</li>"
            html_content += "</ul>"
        else:
            # For other sections, just display the data
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    html_content += f"<p><strong>{sub_key}:</strong> {sub_value}</p>"
            else:
                html_content += f"<p>{value}</p>"
        
        html_content += "</div>"

    return html_content

# Initialize argument parser
parser = argparse.ArgumentParser(description='Convert JSON report to formatted HTML.')
parser.add_argument('json_file', metavar='JSON_FILE', type=str, help='Path to the JSON report file')
args = parser.parse_args()
json_file_path = args.json_file

if not os.path.exists(json_file_path):
    print(f"File not found: {json_file_path}")
else:
    try:
        with open(json_file_path, 'r') as json_file:
            report_data = json.load(json_file)

        # Generate HTML content with the formatted report data
        html_output = f"""
        <html>
        <body>
        {generate_html_content(report_data)}
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
