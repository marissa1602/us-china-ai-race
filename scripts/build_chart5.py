import pandas as pd

def build_chart5():
    # Load raw data
    df = pd.read_csv('data/raw/epoch_notable_ai_models_20261020.csv')
    
    # Convert date to year
    df['Year'] = pd.to_datetime(df['Release_Date']).dt.year
    
    # Filter for US and China between 2023 and 2025
    df_filtered = df[(df['Country'].isin(['United States', 'China'])) & (df['Year'].between(2023, 2025))]
    
    # Group and count
    grouped = df_filtered.groupby(['Year', 'Country', 'Release_Strategy']).size().reset_index(name='count')
    
    # Calculate percentages
    grouped['total'] = grouped.groupby(['Year', 'Country'])['count'].transform('sum')
    grouped['percentage'] = (grouped['count'] / grouped['total']) * 100
    
    # Save processed data
    grouped.to_csv('data/processed/chart5_release_strategies.csv', index=False)
    print("Chart 5 processed data saved successfully.")

if __name__ == "__main__":
    build_chart5()
