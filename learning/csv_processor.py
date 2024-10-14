import csv
from datetime import datetime


def process_sales_data(input_file, output_file):
    # Open the input CSV file for reading and the output CSV file for writing
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        # Create a CSV reader object to read the input file as a dictionary
        reader = csv.DictReader(infile)
        
        # Define the fieldnames for the output file, adding 'Total' and 'Date' columns
        fieldnames = reader.fieldnames + ['Total', 'Date']
        
        # Create a CSV writer object to write to the output file with the specified fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        # Write the header row to the output file
        writer.writeheader()
        
        # Iterate over each row in the input file
        for row in reader:
            # Calculate total sales by multiplying quantity and price
            quantity = int(row['Quantity'])
            price = float(row['Price'])
            total = quantity * price
            
            # Add the calculated total and current date to the row
            row['Total'] = f"{total:.2f}"
            row['Date'] = datetime.now().strftime("%Y-%m-%d")
            
            # Write the updated row to the output file
            writer.writerow(row)

# Usage
input_file = 'sales_data.csv'
output_file = 'processed_sales_datas.csv'
process_sales_data(input_file, output_file)

print("complete!")
