import os
os.system("pip install plotly")
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Analysis of Bike Rental Behavior in 2011 and 2012")
st.write(
    """
    This analysis is made to understand the behavior of bike renters in 2011 and 2012.
    Choose the year to view the analysis based on working days and holidays.
    """
)

data = pd.read_csv('Dashboard/Data/bike_rental.csv')

year_map = {0: '2011', 1: '2012'}

data['yr'] = data['yr'].map(year_map)

year = st.sidebar.radio("Select Year", [2011, 2012])

filtered_data = data[data["yr"] == str(year)]  

filtered_data['temp'] = filtered_data['temp'] * 41
filtered_data['atemp'] = filtered_data['atemp'] * 50
filtered_data['hum'] = filtered_data['hum'] * 100
filtered_data['windspeed'] = filtered_data['windspeed'] * 67

my_weather_map = {1: "Clear", 2: "Foggy", 3: "Light Rain/Snow", 4: "Blizzard/Storm"}
filtered_data['weathersit'] = filtered_data['weathersit'].map(my_weather_map)

my_season_map = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
filtered_data['season'] = filtered_data['season'].map(my_season_map)


plot_option = st.sidebar.radio(
    "Select the plot to display:",
    ["Bike Rentals on Working Days vs Holidays", "Rented Bike Behavior Based on Weather and Season", 
     "Correlation Between Daily Rentals and Season", "Rented Bike Behavior Based on Humidity", 
     "Rented Bike Behavior Based on Temperature", "Rented Bike Behavior Based on Windspeed"]
)

if plot_option == "Bike Rentals on Working Days vs Holidays":
    st.subheader(f"Bike Rental Behavior in {year}")
    
    workingday_0 = filtered_data[filtered_data['workingday'] == 0]  
    workingday0 = workingday_0['cnt'].sum()

    workingday_1 = filtered_data[filtered_data['workingday'] == 1]  
    workingday1 = workingday_1['cnt'].sum()

    vis_workingday = pd.DataFrame(data=[workingday1, workingday0], index=['Working Day', 'Holiday'])

    fig = px.bar(vis_workingday, x=vis_workingday.index, y=0, text_auto=".2s", 
                 title=f'Bike Rentals on Working Days vs Holidays in {year}')
    fig.update_layout(  
        xaxis_title="Day",  
        yaxis_title="Count of Rides")
    st.plotly_chart(fig)

elif plot_option == "Rented Bike Behavior Based on Weather and Season":
    fig = px.histogram(filtered_data, color='weathersit', x="season", y='cnt', text_auto=".2s", 
                       title=f"Rented Bike Behavior Based on Season and Weather in {year}")
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    fig.update_layout(
        barmode='group',  
        xaxis_title="Season",  
        yaxis_title="Count of Rides"
    )
    st.plotly_chart(fig)

elif plot_option == "Correlation Between Daily Rentals and Season":
    my_season_map = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
    filtered_data['season'] = filtered_data['season'].map(my_season_map)

    fig = px.scatter(filtered_data, x="dteday", y="cnt", color="season", 
                     title=f'Correlation Between Daily Bike Rentals and Season in {year}')
    st.plotly_chart(fig)

elif plot_option == "Rented Bike Behavior Based on Humidity":

    def percent_hum(hum):
        if hum <= 60:
            hum = filtered_data['hum']
            return 'Low Humidity'
        elif hum > 60 and hum <= 80:
            return 'Mid Humidity'
        else:
            return 'High Humidity'

    filtered_data['humidity level'] = filtered_data['hum'].apply(percent_hum)

    fig = px.histogram(filtered_data, color='humidity level', x="humidity level", y='cnt', text_auto=".2s", 
                       title=f"Rented Bike Behavior Based on Humidity Level in {year}")
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    st.plotly_chart(fig)

elif plot_option == "Rented Bike Behavior Based on Temperature":
    def percent_temp(temp):
        if temp <= 15:
            temp = filtered_data['temp']
            return 'Low Temperature'
        elif temp > 15 and temp <= 25:
            return 'Mid Temperature'
        else:
            return 'High Temperature'

    filtered_data['temperature level'] = filtered_data['temp'].apply(percent_temp)

    fig = px.histogram(filtered_data, color='temperature level', x="temperature level", y='cnt', text_auto=".2s", 
                       title=f"Rented Bike Behavior Based on Temperature Level in {year}")
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    st.plotly_chart(fig)

elif plot_option == "Rented Bike Behavior Based on Windspeed":
    def percent_wind(wind):
        if wind <= 10:
            wind = filtered_data['windspeed']
            return 'Low Windspeed'
        elif wind > 10 and wind <= 20:
            return 'Mid Windspeed'
        else:
            return 'High Windspeed'

    filtered_data['windspeed level'] = filtered_data['windspeed'].apply(percent_wind)

    fig = px.histogram(filtered_data, color='windspeed level', x="windspeed level", y='cnt', text_auto=".2s", 
                       title=f"Rented Bike Behavior Based on Windspeed in {year}")
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    st.plotly_chart(fig)
