import json
from json2html import json2html
import argparse
parser = argparse.ArgumentParser(description = 'Convert JSON report to HTML.')
parser.add_argument('json_file',metavar='JSON_FILE',type=str,help='path to the JSON report file')#Specifies the path to the JSON report file
parser.add_argument('html_file',metavar='HTML_FILE',type=str,help='path for the generated HTML report file')#Specifies the path for the generated HTML report file
args = parser.parse_args()#assigns the values of json_file and html_file to the respective variables json_file_path and html_file_path
json_file_path = args.json_file
html_file_path = args.html_file
try:
    with open(json_file_path,'r')as json_file: #open and read the JSON file
                                            report_data = json.load(json_file) #load the JSON data from the file into a python dictionary and stored in report_data
                                            html_output = json2html.convert(json=report_data) #convert the JSON data to an HTML string
                                            with open(html_file_path,'w')as html_file: #open an HTML file for writing
                                                                         #html_file.write(html_output)#write the HTML content from html_output to the HTML file using html_file.write(html_output).

                                                        print(f"HTML report generated:{html_file_path}")
except FileNotFoundError:
    print(f"file not found:{json_file_path}")
except json.JSONDecoderError:
    print(f"error decoding JSON in{json_file_path}")
except PermissionError as e:
    print(f"Permission error: {e}")
