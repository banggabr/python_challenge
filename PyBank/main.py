import os 
import csv 

# Path to collect data from resources folder
revenue_csv = os.path.join('..', 'Resources', 'budget_data.csv')

# Define function and set parameter
def financial_analysis(revenue_data): 
    # Assign values to variables for readibility 
    month = str(revenue_data[0])
    PnL = int(revenue_data[1])

    # Total number of months 
    month_count = len(month)
    
    # Net total of PnL
    net_PnL = sum(PnL)

    # Average PnL
    avg_PnL = net_PnL / month_count

    # Greatest Profit 
    max_profit = max(PnL) 

    # Greatest Loss
    max_loss = min(PnL)

    # Print header then print border using next line functionality
    print(f'Financial Analysis'+'\n')
    print(f'------------------------------------'+'\n')

    # Print calculations
    print(f'Total Month: ' + month_count)
    print(f'Total: $ ' + net_PnL)
    print(f'Average Change: $ ' + avg_PnL)
    print(f'Greatest Increase in Profits: ' + max_profit)
    print(f'Greatest Decrease in Profts: ' + max_loss) 

# Read in csv file
with open(revenue_csv, 'r') as csvfile:
    # Use csvreader functionality to specify variable to hold csv contents 
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip header of file
    header = next(csvreader)
    
    # Loop through data
    for row in csvreader: 
        financial_analysis(row)
