import pandas as pd

files = ['daily_sales_data_0.csv', 'daily_sales_data_1.csv', 'daily_sales_data_2.csv']

results = pd.DataFrame()

for file in files:
    
    df = pd.read_csv(file)
    
    df_filtered = df.loc[df['product'] == 'pink morsel'].copy()
    
    df_filtered['price'] = df_filtered['price'].replace({r'\$': '', ',': ''}, regex=True).astype(float)
    
    df_filtered.loc[:, 'sales'] = df_filtered['price'] * df_filtered['quantity']
    
    df_filtered = df_filtered[['sales', 'date', 'region']]
    
    results = pd.concat([results, df_filtered], ignore_index=True)

results.to_csv('filtered_results.csv', index=False)

print(results)
