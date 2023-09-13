import json
import argparse
import os

# Initialize argument parser
parser = argparse.ArgumentParser(description='Convert JSON report to plain HTML.') #used to create a command-line interface for the script
parser.add_argument('json_file', metavar='JSON_FILE', type=str, help='Path to the JSON report file')
args = parser.parse_args() #parses the command-line arguments provided when running the script
json_file_path = args.json_file #contain the path to the JSON file

if not os.path.exists(json_file_path): # checks if the specified JSON file exists 
    print(f"File not found: {json_file_path}") 
else:
    try:
        with open(json_file_path, 'r') as json_file: # attempts to open and load its contents
            report_data = json.load(json_file) #JSON data is loaded into the report_data variable

        # Generate plain HTML content with the JSON data
        html_output = f"<html><body><pre>{json.dumps(report_data, indent=4)}</pre></body></html>" #generates by embedding the JSON data within a <pre> 
        
        # Write the HTML to a file with the same name as the JSON file but with .html extension
        #html_file_path = os.path.splitext(json_file_path)[0] + '.html'
        #with open(html_file_path, 'w') as html_file:
            #html_file.write(html_output) # used to generate the HTML file name
        
        print(f"HTML report generated: {html_output}")
    except json.JSONDecodeError:
        print(f"Error decoding JSON in {json_file_path}")
