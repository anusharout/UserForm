
from jinja2 import Environment,FileSystemLoader
import json
import os
import argparse
def main(json_file_path):
 with open(json_file_path,'r')as json_file:
     data = json.load(json_file)
     script_dir = os.path.dirname(os.path.abspath(__file__))
     template_dir = os.path.join(script_dir,'ERRORDATATEMPLATE')
     env = Environment(loader = FileSystemLoader(template_dir))
     template = env.get_template('HTMLFORSUMMARY.html')
     output = template.render(data = data)
     print(output)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a performance report from JSON data")
    parser.add_argument("json_file", help="Path to the JSON file")
    args = parser.parse_args()
    main(args.json_file)




