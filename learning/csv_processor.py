import csv
from datetime import datetime


def process_sales_data(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ['Total', 'Date']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        for row in reader:
            # Calculate total sales
            quantity = int(row['Quantity'])
            price = float(row['Price'])
            total = quantity * price
            
            # Add new fields
            row['Total'] = f"{total:.2f}"
            row['Date'] = datetime.now().strftime("%Y-%m-%d")
            
            writer.writerow(row)

# Usage
input_file = 'sales_data.csv'
output_file = 'processed_sales_data.csv'
process_sales_data(input_file, output_file)

print("complete!")
