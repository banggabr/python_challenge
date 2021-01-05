import os 
import csv 
budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')

# Read in csv file
with open(budget_csv, 'r') as csvfile:
    # Use csvreader functionality to specify variable to hold csv contents, 
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip header
    header = next(csvreader)

# 
    
    
    # Print header then print border using next line functionality
    print(f'Financial Analysis'+'\n')
    print(f'------------------------------------'+'\n')

    
# Total months
