import pandas as pd
import numpy as np

def build_chart5():
    # Load raw data
    df = pd.read_csv('data/raw/epoch_notable_ai_models_20261020.csv')
    
    # Extract Year from 'Publication date'
    df['Year'] = pd.to_datetime(df['Publication date'], errors='coerce').dt.year
    
    # Filter for US and China 
    df_filtered = df[
        (df['Country (of organization)'].isin(['United States of America', 'China'])) & 
        (df['Year'].between(2023, 2025))
    ].copy()
    
    # Map 'Model accessibility' to the 4 categories
    def map_strategy(access):
        if pd.isna(access):
            return 'Unknown'
        access = str(access).lower()
        if 'open' in access:
            return 'Open Weights'
        elif 'api' in access or 'hosted' in access:
            return 'API/Hosted'
        elif 'unreleased' in access or 'not released' in access:
            return 'Unreleased'
        else:
            return 'Unknown'
            
    df_filtered['Release_Strategy'] = df_filtered['Model accessibility'].apply(map_strategy)
    
    # Rename 'United States of America' to 'United States' for the chart labels
    df_filtered['Country'] = df_filtered['Country (of organization)'].replace({'United States of America': 'United States'})
    
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
