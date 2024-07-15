import os
import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# Define the data directory
data_dir = '/home/jonasamidu/Desktop/MyTown/data'

# Get a list of all subdirectories in the data directory
subdirs = sorted([os.path.join(data_dir, d) for d in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, d))])

# Initialize an empty list to store all the data
all_data_list = []

# Load data from each subdirectory
for subdir in subdirs:
    # Get a list of all CSV files in the subdirectory
    csv_files = [f for f in os.listdir(subdir) if f.endswith('.csv')]
    for csv_file in csv_files:
        file_path = os.path.join(subdir, csv_file)
        # Read the CSV file
        df = pd.read_csv(file_path)
        # Add a column for the date (using the subdirectory name)
        df['Date'] = os.path.basename(subdir)
        # Append the DataFrame to the list
        all_data_list.append(df)

# Concatenate all DataFrames in the list into a single DataFrame
all_data = pd.concat(all_data_list, ignore_index=True)

# Define the columns we are interested in
desired_columns = [
    'Date', 'Reported by', 'Longitude', 'Latitude', 
    'Location', 'LSOA code', 'LSOA name', 'Crime type', 'Last outcome category'
]

# Select only the columns that exist in the DataFrame
existing_columns = [col for col in desired_columns if col in all_data.columns]
all_data = all_data[existing_columns]

# Drop duplicate rows
all_data = all_data.drop_duplicates()

# Create a Streamlit app
st.title('Bedfordshire Crime Data 2021 - 2024')

# Sidebar for filtering
st.sidebar.header('Filter Options')

# Date range filter
date_min = all_data['Date'].min()
date_max = all_data['Date'].max()
start_date, end_date = st.sidebar.slider(
    'Select date range',
    min_value=pd.to_datetime(date_min).date(),
    max_value=pd.to_datetime(date_max).date(),
    value=(pd.to_datetime(date_min).date(), pd.to_datetime(date_max).date())
)

# Filter data based on date range
filtered_data = all_data[
    (pd.to_datetime(all_data['Date']) >= pd.to_datetime(start_date)) &
    (pd.to_datetime(all_data['Date']) <= pd.to_datetime(end_date))
]

# Crime type filter
crime_types = filtered_data['Crime type'].unique()
selected_crime_types = st.sidebar.multiselect('Select crime types', crime_types, default=crime_types)

# Filter data based on selected crime types
filtered_data = filtered_data[filtered_data['Crime type'].isin(selected_crime_types)]

# Visualization: Crime Trend Over Time
st.write('## Crime Trend Over Time')
crime_trend = filtered_data['Date'].value_counts().sort_index()
fig, ax = plt.subplots()
crime_trend.plot(ax=ax, kind='line')
ax.set_xlabel('Date')
ax.set_ylabel('Number of Crimes')
ax.set_title('Crime Trend Over Time')
st.pyplot(fig)

# Comment on the trend
st.write("**Observation:** The crime trend over time shows the number of crimes reported each month. Look for any notable peaks or declines.")

# Visualization: Crime Type Distribution
st.write('## Crime Type Distribution')
crime_type_dist = filtered_data['Crime type'].value_counts()
fig, ax = plt.subplots()
crime_type_dist.plot(ax=ax, kind='bar')
ax.set_xlabel('Crime Type')
ax.set_ylabel('Number of Crimes')
ax.set_title('Crime Type Distribution')
st.pyplot(fig)

# Comment on the distribution
st.write("**Observation:** This bar chart shows the distribution of different crime types. Notice which types of crimes are most and least common.")

# Visualization: Outcome Distribution
st.write('## Outcome Distribution')
outcome_dist = filtered_data['Last outcome category'].value_counts()
fig = px.pie(values=outcome_dist, names=outcome_dist.index, title='Outcome Distribution')
st.plotly_chart(fig)

# Comment on the distribution
st.write("**Observation:** This pie chart shows the distribution of crime outcomes. Observe which outcomes are most frequent.")

# Visualization: Crime Locations
st.write('## Crime Locations')

# Map zoom level slider
zoom_level = st.sidebar.slider('Select map zoom level', min_value=1, max_value=20, value=10)

fig = px.scatter_mapbox(
    filtered_data,
    lat="Latitude",
    lon="Longitude",
    hover_name="Crime type",
    hover_data=["Location", "Last outcome category"],
    color="Crime type",
    zoom=zoom_level,
    height=600,
    title="Crime Locations"
)
fig.update_layout(mapbox_style="open-street-map")
st.plotly_chart(fig)

# Comment on the map
st.write("**Observation:** This map shows the locations of crimes. The colors represent different crime types. Observe any clusters or patterns in specific areas.")
