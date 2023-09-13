import argparse
import json
from jinja2 import Environment, FileSystemLoader
parser = argparse.ArgumentParser(description='Generate HTML from JSON files.') #to pass one or more json file paths
parser.add_argument('json_files', metavar='JSON_FILE', nargs='+',help='JSON files to process') #multiple json files are separeted by space
args = parser.parse_args()# Parse command line arguments
json_files = args.json_files #json file paths can be stored here
template_loader = FileSystemLoader(searchpath='./') # Initialize Jinja2
env = Environment(loader=template_loader)
template = env.get_template('template.html') #loaded a template file named 'template.html'
data = [] # iterate through the list of jSON files specified as arguments and load their content into the data list
for file_name in json_files:
    with open(file_name, 'r') as json_file:
        data.append(json.load(json_file))
rendered_html = template.render(data=data) #the data variable contains all the jason data from the files
with open('output.html', 'w') as output_file: #saved the rendered HTML to a file
    output_file.write(rendered_html)



