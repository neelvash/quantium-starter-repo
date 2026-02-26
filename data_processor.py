import pandas as pd

# 1. Load the three CSV files from the data folder
df1 = pd.read_csv('./data/daily_sales_data_0.csv')
df2 = pd.read_csv('./data/daily_sales_data_1.csv')
df3 = pd.read_csv('./data/daily_sales_data_2.csv')

# 2. Combine them into a single dataset
all_data = pd.concat([df1, df2, df3])

# 3. Filter for only "pink morsel" (use .str.lower() in case some are capitalised like "Pink Morsel")
pink_morsels = all_data[all_data['product'].str.lower() == 'pink morsel'].copy()

# 4. Clean the price column and calculate Sales
# Remove the '$' sign and convert the text to a float (decimal number)
pink_morsels['price'] = pink_morsels['price'].str.replace('$', '').astype(float)

# Multiply quantity by price to get the new 'sales' column
pink_morsels['sales'] = pink_morsels['quantity'] * pink_morsels['price']

# 5. Keep only the requested columns
final_data = pink_morsels[['sales', 'date', 'region']]

# Optional: Rename columns to start with capital letters as requested in the prompt
final_data = final_data.rename(columns={'sales': 'Sales', 'date': 'Date', 'region': 'Region'})

# 6. Save the final formatted data to a new CSV file
final_data.to_csv('./data/formatted_sales_data.csv', index=False)

print("Data processing complete! Saved to formatted_sales_data.csv")