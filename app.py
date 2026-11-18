import streamlit as st
import pandas as pd
import plotly.express as px

# LOAD DATA
@st.cache_data
def load_data():
    return pd.read_csv('data/processed/chart5_release_strategies.csv')

try:
    df = load_data()
except FileNotFoundError:
    st.error("Data file not found. Please ensure chart5_release_strategies.csv is in the data/processed folder.")
    st.stop()

# CHART 5 SECTION 
st.header("Chart 5: Open vs Closed Release Strategies")
st.markdown("**User Story 2:** As a foreign policy analyst, I want to filter release strategy by developer type, so that I can examine whether openness varies more by organisations or by country.")

# Filters
col1, col2 = st.columns(2)
with col1:
    selected_years = st.multiselect("Select Years", options=sorted(df['Year'].unique()), default=[2023, 2024, 2025])
with col2:
    selected_countries = st.multiselect("Select Countries", options=['United States', 'China'], default=['United States', 'China'])

# Filter data
filtered_df = df[(df['Year'].isin(selected_years)) & (df['Country'].isin(selected_countries))]

if filtered_df.empty:
    st.warning("No models match these filters. Please widen your year or country selection.")
else:
    # Build Chart
    fig = px.bar(
        filtered_df, 
        x="Year", 
        y="percentage", 
        color="Release_Strategy", 
        facet_col="Country",
        text_auto='.1f', 
        title="Release Strategies of Notable AI Models by Country (2023-2025)",
        labels={"percentage": "Percentage of Models (%)", "Release_Strategy": "Release Strategy", "Year": "Year"},
        color_discrete_sequence=px.colors.qualitative.Safe 
    )
    fig.update_layout(yaxis_title="Percentage of Models (%)", legend_title="Strategy")
    st.plotly_chart(fig, use_container_width=True)
    
    # Required Analysis Boxes
    st.success("**Our Answer:** The data shows a structural difference. In 2023 to 2025, the US relies heavily on API access, while China relies heavily on Open Weights.")
    
    with st.expander("Limitations: What this data cannot show"):
        st.write("""
        - **Not exhaustive:** Epoch's notable model list is a selectively curated entry, not every AI model made in a country.
        - **Input vs Performance:** Release strategies measure commercial control and distribution, not actual capability or safety.
        """)

# Sources
st.caption("Source: Epoch AI Notable Models Dataset (2026-10-20 snapshot). Last data refresh: 20 October 2026.")
