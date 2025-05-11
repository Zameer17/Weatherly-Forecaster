from datetime import datetime
import pyowm
import streamlit as st
from matplotlib import dates
from matplotlib import pyplot as plt
import numpy as np  # Required for heatmap

# Using streamlit secrets to fetch the secret ApiKey.
api_key = st.secrets["API_KEY"]

sign = u"\N{DEGREE SIGN}"
owm = pyowm.OWM(api_key)
mgr = owm.weather_manager()

st.title("Weatherly Forecaster")
st.write("### Enter the city name, choose a Temperature unit and a graph type from the bottom:")

location = st.text_input("Name of The City :", "")
units = st.selectbox("Select Temperature Unit: ", ('celsius', 'fahrenheit'))
graph = st.selectbox("Select Graph Type:", ('Bar Graph', 'Line Graph', 'Pie Chart', 'Histogram', 'Scatter Plot', 'Heatmap'))

degree = 'C' if units == 'celsius' else 'F'

def get_temperature():
    forecaster = mgr.forecast_at_place(location, '3h')
    forecast = forecaster.forecast

    days = []
    unique_dates = []
    temp_min = []
    temp_max = []
    for weather in forecast:
        day = datetime.utcfromtimestamp(weather.reference_time())
        date = day.date()
        if date not in unique_dates:
            unique_dates.append(date)
            temp_min.append(None)
            temp_max.append(None)
            days.append(date)
        temp = weather.temperature(unit=units)['temp']
        if temp_min[-1] is None or temp < temp_min[-1]:
            temp_min[-1] = temp
        if temp_max[-1] is None or temp > temp_max[-1]:
            temp_max[-1] = temp
    return (days, temp_min, temp_max)

def init_plot():
    plt.style.use('ggplot')
    plt.figure('PyOWM Weather')
    plt.xlabel('Day')
    plt.ylabel(f'Temperature ({sign}{degree})')
    plt.title("Weekly Forecast")

def plot_temperature(days, temp_min, temp_max):
    day_nums = dates.date2num(days)
    bar_x = plt.bar(day_nums - 0.25, temp_min, width=0.5, color='#42bff4', label='Min')
    bar_y = plt.bar(day_nums + 0.25, temp_max, width=0.5, color='#ff5349', label='Max')
    plt.legend(fontsize='x-small')
    return (bar_x, bar_y)

def label_xaxis(days):
    day_nums = dates.date2num(days)
    plt.xticks(day_nums)
    axes = plt.gca()
    axes.xaxis.set_major_formatter(dates.DateFormatter('%m/%d'))

def show_max_temp_on_barchart(bar_x, bar_y):
    axes = plt.gca()
    y_axis_max = axes.get_ylim()[1]
    label_offset = y_axis_max * 0.1
    for bar_chart in [bar_x, bar_y]:
        for bar in bar_chart:
            bar_height = bar.get_height()
            xpos = bar.get_x() + bar.get_width() / 2.0
            ypos = bar_height - label_offset
            label_text = f"{int(bar_height)}{sign}"
            plt.text(xpos, ypos, label_text, ha='center', va='bottom', color='white')

def weather_forecast():
    obs = mgr.weather_at_place(location)
    weather = obs.weather
    icon = weather.weather_icon_url(size='4x')

    temp = weather.temperature(unit=units)['temp']
    temp_felt = weather.temperature(unit=units)['feels_like']

    st.image(icon, caption=(weather.detailed_status).title())
    st.markdown(f"## 🌡️ Temperature: **{round(temp)}{sign}{degree}**")
    st.write(f"### Feels Like: {round(temp_felt)}{sign}{degree}")
    st.write(f"### ☁️ Clouds Coverage: {weather.clouds}%")
    st.write(f"### 💨 Wind Speed: {weather.wind()['speed']} m/s")
    st.write(f"### 💧 Humidity: {weather.humidity}%")
    st.write(f"### ⏲️ Pressure: {weather.pressure['press']} mBar")
    st.write(f"### 🛣️ Visibility: {weather.visibility(unit='kilometers')} km")

def upcoming_weather_alert():
    forecaster = mgr.forecast_at_place(location, '3h')
    flag = 0
    st.write("_____________________________________")
    st.title("Upcoming Weather Alerts")
    if forecaster.will_have_clouds():
        st.write("### - Cloud Alert ⛅")
        flag += 1
    if forecaster.will_have_rain():
        st.write("### - Rain Alert 🌧️")
        flag += 1
    if forecaster.will_have_snow():
        st.write("### - Snow Alert ❄️")
        flag += 1
    if forecaster.will_have_hurricane():
        st.write("### - Hurricane Alert 🌀")
        flag += 1
    if forecaster.will_have_tornado():
        st.write("### - Tornado Alert 🌪️")
        flag += 1
    if forecaster.will_have_fog():
        st.write("### - Fog Alert 🌫️")
        flag += 1
    if forecaster.will_have_storm():
        st.write("### - Storm Alert 🌩️")
        flag += 1
    if flag == 0:
        st.write("### No Upcoming Alerts!")

def sunrise_sunset():
    st.write("_____________________________________")
    st.title("Sunrise and Sunset")
    obs = mgr.weather_at_place(location)
    weather = obs.weather

    sunrise = datetime.utcfromtimestamp(int(weather.sunrise_time()))
    sunset = datetime.utcfromtimestamp(int(weather.sunset_time()))

    st.write(f"#### Sunrise Date: {sunrise.date()}  -- Time: {sunrise.time()}")
    st.write(f"#### Sunset Date: {sunset.date()}  -- Time: {sunset.time()}")

def get_humidity():
    days = []
    unique_dates = []
    humidity_max = []
    forecaster = mgr.forecast_at_place(location, '3h')
    forecast = forecaster.forecast

    for weather in forecast:
        day = datetime.utcfromtimestamp(weather.reference_time())
        date = day.date()
        if date not in unique_dates:
            unique_dates.append(date)
            humidity_max.append(None)
            days.append(date)
        humidity = weather.humidity
        if humidity_max[-1] is None or humidity > humidity_max[-1]:
            humidity_max[-1] = humidity
    return (days, humidity_max)

def plot_humidity_graph():
    days, humidity = get_humidity()
    st.write("_____________________________________")
    st.title("Humidity Index of 5 Days")
    plt.style.use('ggplot')
    plt.figure('PyOWM Weather')
    plt.xlabel('Day')
    plt.ylabel('Humidity (%)')
    plt.title('Humidity Forecast')

    day_nums = dates.date2num(days)
    plt.xticks(day_nums)
    axes = plt.gca()
    axes.xaxis.set_major_formatter(dates.DateFormatter('%m/%d'))

    bars = plt.bar(day_nums, humidity, color='#42bff4')

    y_max = axes.get_ylim()[1]
    label_offset = y_max * 0.1
    for bar in bars:
        height = bar.get_height()
        xpos = bar.get_x() + bar.get_width() / 2.0
        ypos = height - label_offset
        plt.text(xpos, ypos, f"{str(height)}%", ha='center', va='bottom', color='white')

    st.pyplot(plt.gcf())

def plot_humidity_line_graph():
    days, humidity = get_humidity()
    st.write("_____________________________________")
    st.title("Humidity Line Graph")

    plt.figure('Humidity Line')
    plt.style.use('ggplot')
    plt.xlabel('Day')
    plt.ylabel('Humidity (%)')
    plt.title('Humidity Forecast')

    day_nums = dates.date2num(days)
    plt.xticks(day_nums)
    axes = plt.gca()
    axes.xaxis.set_major_formatter(dates.DateFormatter('%m/%d'))

    plt.plot(day_nums, humidity, color='#42bff4', marker='o')
    st.pyplot(plt.gcf())

def plot_humidity_pie_chart():
    days, humidity = get_humidity()
    st.write("_____________________________________")
    st.title("Humidity Distribution Pie Chart")

    labels = [day.strftime('%m/%d') for day in days]
    plt.figure()
    plt.pie(humidity, labels=labels, autopct='%1.1f%%', colors=plt.cm.Pastel2.colors, startangle=140)
    plt.axis('equal')
    st.pyplot(plt.gcf())

def plot_humidity_histogram():
    _, humidity = get_humidity()
    st.write("_____________________________________")
    st.title("Humidity Histogram")

    plt.figure()
    plt.hist(humidity, bins=10, color='#87CEEB', edgecolor='black')
    plt.xlabel('Humidity (%)')
    plt.ylabel('Frequency')
    plt.title('Histogram of Forecasted Humidity')
    st.pyplot(plt.gcf())

def plot_pie_chart():
    st.write("_____________________________________")
    st.title("Weather Condition Distribution (Next 5 Days)")

    forecaster = mgr.forecast_at_place(location, '3h')
    forecast = forecaster.forecast

    condition_count = {}
    for weather in forecast:
        status = weather.status
        condition_count[status] = condition_count.get(status, 0) + 1

    labels = list(condition_count.keys())
    sizes = list(condition_count.values())

    plt.figure()
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=plt.cm.Pastel1.colors, startangle=140)
    plt.axis('equal')
    st.pyplot(plt.gcf())

def plot_temperature_histogram():
    st.write("_____________________________________")
    st.title("Temperature Distribution Histogram")

    forecaster = mgr.forecast_at_place(location, '3h')
    forecast = forecaster.forecast

    temps = [weather.temperature(unit=units)['temp'] for weather in forecast]

    plt.figure()
    plt.hist(temps, bins=10, color='#ffb347', edgecolor='black')
    plt.xlabel(f'Temperature ({sign}{degree})')
    plt.ylabel('Frequency')
    plt.title('Histogram of Forecasted Temperatures')
    st.pyplot(plt.gcf())

def plot_temperature_vs_humidity():
    st.write("_____________________________________")
    st.title("Scatter Plot: Temperature vs Humidity")

    forecaster = mgr.forecast_at_place(location, '3h')
    forecast = forecaster.forecast

    temps = []
    humidities = []

    for weather in forecast:
        temps.append(weather.temperature(unit=units)['temp'])
        humidities.append(weather.humidity)

    plt.figure()
    plt.scatter(temps, humidities, color='#42bff4')
    plt.xlabel(f'Temperature ({sign}{degree})')
    plt.ylabel('Humidity (%)')
    plt.title('Temperature vs Humidity')
    st.pyplot(plt.gcf())

def plot_temp_humidity_heatmap():
    st.write("_____________________________________")
    st.title("Heatmap: Temperature and Humidity Over Time")

    forecaster = mgr.forecast_at_place(location, '3h')
    forecast = forecaster.forecast

    timestamps = []
    temps = []
    humidities = []

    for weather in forecast:
        dt = datetime.utcfromtimestamp(weather.reference_time())
        timestamps.append(dt.strftime('%m/%d %Hh'))
        temps.append(weather.temperature(unit=units)['temp'])
        humidities.append(weather.humidity)

    data = np.array([temps, humidities])
    fig, ax = plt.subplots()
    cax = ax.imshow(data, cmap='YlGnBu', aspect='auto')

    ax.set_yticks([0, 1])
    ax.set_yticklabels(['Temperature', 'Humidity'])
    ax.set_xticks(np.arange(len(timestamps))[::4])
    ax.set_xticklabels(timestamps[::4], rotation=45, ha='right')
    ax.set_title('Forecasted Temperature and Humidity')
    fig.colorbar(cax, orientation='vertical')
    st.pyplot(fig)

# Main Execution Block
if __name__ == '__main__':
    if st.button('Submit'):
        if location == '':
            st.warning('Provide a city name!!')
        else:
            try:
                weather_forecast()
                days, temp_min, temp_max = get_temperature()

                if graph == 'Bar Graph':
                    st.write("_____________________________________")
                    st.title("5 Day Min and Max Temperature")
                    init_plot()
                    bar_x, bar_y = plot_temperature(days, temp_min, temp_max)
                    label_xaxis(days)
                    show_max_temp_on_barchart(bar_x, bar_y)
                    st.pyplot(plt.gcf())

                elif graph == 'Line Graph':
                    st.write("_____________________________________")
                    st.title("5 Day Min and Max Temperature")
                    init_plot()
                    day_nums = dates.date2num(days)
                    plt.plot(day_nums, temp_min, label='Min', color='#42bff4', marker='o')
                    plt.plot(day_nums, temp_max, label='Max', color='#ff5349', marker='o')
                    label_xaxis(days)
                    plt.legend(fontsize='x-small')
                    st.pyplot(plt.gcf())

                elif graph == 'Pie Chart':
                    plot_pie_chart()

                elif graph == 'Histogram':
                    plot_temperature_histogram()

                elif graph == 'Scatter Plot':
                    plot_temperature_vs_humidity()

                elif graph == 'Heatmap':
                    plot_temp_humidity_heatmap()

                upcoming_weather_alert()
                sunrise_sunset()

                if graph == 'Bar Graph':
                    plot_humidity_graph()
                elif graph == 'Line Graph':
                    plot_humidity_line_graph()
                elif graph == 'Pie Chart':
                    plot_humidity_pie_chart()
                elif graph == 'Histogram':
                    plot_humidity_histogram()
                elif graph == 'Scatter Plot':
                    st.write("Humidity already represented in Scatter Plot.")
                elif graph == 'Heatmap':
                    st.write("Humidity already represented in Heatmap.")

            except Exception as e:
                st.error("⚠️ Location Not Found! Try using 'City, CountryCode' format (e.g., Mumbai, IN)")
                st.exception(e)
                st.write("Please check the API key and internet connection.")
