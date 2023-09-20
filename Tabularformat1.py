import json
import argparse
import os

def generate_table(data, is_nested=False):
    table_html = ""

    # Add a heading for the report if it's not nested
    if not is_nested:
        table_html += ""

    # Start the table
    table_html += "<table>"

    # Loop through the JSON data and format each key-value pair as a table row
    for key, value in data.items():
        table_html += "<tr>"

        if isinstance(value, dict):
            # If the value is a dictionary, format it recursively
            table_html += f"<th colspan='2'>{key}</th>"
            table_html += "</tr><tr>"
            table_html += "<td colspan='2'>"
            table_html += generate_table(value, is_nested=True)
            table_html += "</td>"
        elif isinstance(value, list) and value and isinstance(value[0], dict):
            # If the value is a list of dictionaries (common case for stages), format it
            table_html += f"<th colspan='2'>{key}</th>"
            table_html += "</tr><tr>"
            table_html += "<td colspan='2'>"
            table_html += "<ul>"
            for item in value:
                table_html += "<li>"
                table_html += generate_table(item, is_nested=True)
                table_html += "</li>"
            table_html += "</ul>"
            table_html += "</td>"
        else:
            # For other sections, display the data in table cells
            table_html += f"<td><strong>{key}</strong></td><td>{value}</td>"

        table_html += "</tr>"

    # End the table
    table_html += "</table>"

    return table_html

# Initialize argument parser
parser = argparse.ArgumentParser(description='Convert JSON report to formatted HTML table.')
parser.add_argument('json_file', metavar='JSON_FILE', type=str, help='Path to the JSON report file')
args = parser.parse_args()
json_file_path = args.json_file

if not os.path.exists(json_file_path):
    print(f"File not found: {json_file_path}")
else:
    try:
        with open(json_file_path, 'r') as json_file:
            report_data = json.load(json_file)

        # Generate the HTML table with the formatted report data
        table_html = generate_table(report_data)
        banner_url1 = r"C:\Users\anurout\Downloads\MicrosoftTeams-image (12).png"
        banner_url2 = r"C:\Users\anurout\Downloads\MicrosoftTeams-image (13).png"


        # Wrap the table in an HTML document
        html_output = f"""
        <html>
        <head>
            <style>
                table {{
                    border-collapse: collapse;
                    width: 100%;
                }}
                th, td {{
                    text-align: left;
                    padding: 8px;
                    border-bottom: 1px solid #ddd;
                }}
                th {{
                    background-color: #e8d7a1;
                    font-weight: bold;
                    text-transform: uppercase;
                }}
                /* Target sub-heading elements and change font size and color */
                th[colspan="2"] {{
                                 font-size: 16px; /* Change the font size as needed */
                                color: #4b3c15; /* Change the color as needed (e.g., blue) */
}}

                tr:nth-child(even) {{
                    background-color: #f2f2f2;
                }}
                h1 {{
                    
                }}
                .header {{
                text-align: center; /* Center the text horizontally */
                font-weight: bold; /* Make the text bold */
                background-color: #333; /* Set a shadow background color */
                color: white; /* Set the text color to white for better visibility */
                padding: 10px 0; /* Add some padding for spacing */
                box-shadow: 0px 1px 2px rgba(0, 0, 0, 0.1); /* Add a shadow */
                
                }}
                .banner1 {{
                    position: relative;
                    display: flex; /* Use flexbox to align items horizontally */
                    align-items: center; /* Vertically center items */
}}

.header-image {{
  max-width: 100px; /* Adjust the width of the header image as needed */
    height: auto;
}}

.banner2 {{
                padding: 1px 300px;
                    max-width: 350px;
                    height: auto;
                    
}}

.banner-image {{
                max-width: 100%;
                height: auto;
}}
/* ... Other CSS rules ... */

/* Remove bullet points from unordered lists and list items */
ul {{
  list-style-type: none;
  margin: 0;
  padding: 0;
}}

li {{
  margin-left: 0;
  padding-left: 0;
}}

/* ... Rest of your CSS ... */


            </style>
        </head>
        <body>
            <div class="banner1">
                <img src="{banner_url1}" alt="Header Image" class="header-image">
                    <div class="banner2">
                <img src="{banner_url2}" class="banner-image">
                    </div>
                </div>

            <div class="header">
                <h1 >ONE CLICK CONSOLIDATED REPORT</h1>
            </div>
            {table_html}
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
