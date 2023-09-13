import json
from json2html import json2html
with open('report.json','r') as json_file: #opens the 'report.json' file in read ('r') mode
    report_data = json.load(json_file) #reads the contents of 'report.json' and parses it into a python dictionary
    html_output = json2html.convert(json = report_data) #convert json to HTML
    with open('report.html','w') as html_file: #opens the 'report.html' file in write ('w') mode
        html_file.write(html_output) #writes the HTML content stored in the html_output variable to the 'report.html' file
        print("HTML report generated: report.html") #html report has been successfully generated
