# Define exchange rate for JPY to USD (approximation, subject to fluctuation)
exchange_rate = 0.007  # 1 JPY = 0.007 USD

# Financial data for FY2023 and FY2024 in JPY (approximate figures)
financial_data = {
    "Metric": ["Net Sales", "Income Before Taxes", "Net Income", "Total Assets", "Total Equity"],
    "FY2024 (JPY, billions)": [3865.1, 575.7, 393.4, 5636.7, 3198.5],
    "FY2023 (JPY, billions)": [3527.3, 491.6, 331.2, 5248.3, 3062.4],
}

# Convert to USD
financial_data["FY2024 (USD, billions)"] = [value * exchange_rate for value in financial_data["FY2024 (JPY, billions)"]]
financial_data["FY2023 (USD, billions)"] = [value * exchange_rate for value in financial_data["FY2023 (JPY, billions)"]]

import pandas as pd

# Create a DataFrame
df_financial = pd.DataFrame(financial_data)

# Display the DataFrame to the user
#import ace_tools as tools; tools.display_dataframe_to_user(name="Komatsu Financial Analysis FY2023 vs FY2024", dataframe=df_financial)