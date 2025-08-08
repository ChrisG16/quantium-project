import pandas as pd

# Data files from the project in .csv
files = ['daily_sales_data_0.csv', 'daily_sales_data_1.csv', 'daily_sales_data_2.csv']

# Initialize an empty DataFrame to store results
results = pd.DataFrame()

# Iterate through each file, filter for 'pink morsel', and calculate sales
for file in files:
    
    df = pd.read_csv(file)
    
    df_filtered = df.loc[df['product'] == 'pink morsel'].copy()
    
    df_filtered['price'] = df_filtered['price'].replace({r'\$': '', ',': ''}, regex=True).astype(float)
    
    df_filtered.loc[:, 'sales'] = df_filtered['price'] * df_filtered['quantity']
    
    df_filtered = df_filtered[['sales', 'date', 'region']]
    
    results = pd.concat([results, df_filtered], ignore_index=True)

results.to_csv('filtered_results.csv', index=False)

# Print the final results DataFrame for testing purposes
print(results)
