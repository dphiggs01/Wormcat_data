import csv

base_url = "https://dphiggs01.github.io/Wormcat_data"

# Read CSV data from a file
csv_file = 'annotation_list.csv'
data = []
with open(csv_file, 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        data.append(row)

# Sort the data by the "Order" field
sorted_data = sorted(data, key=lambda x: int(x['order']))

markdown = "# Available WormCat Annotation Files\n\n"
markdown += "| Short Description | File Name |\n"
markdown += "| --- | --- |\n"

for entry in sorted_data:
    file_link = f"[{entry['file_name']}]({base_url}/{entry['location_suffix']}/{entry['file_name']})"
    markdown += f"| {entry['short_desc']} | {file_link} |\n"

# Write the Markdown table to a file
with open('annotation_list.md', 'w') as md_file:
    md_file.write(markdown)

print("Markdown table generated and saved to 'annotation_list.md'")
