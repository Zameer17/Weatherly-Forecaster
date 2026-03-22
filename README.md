<div align="center">

<!-- ☁️ ANIMATED WEATHER HEADER -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0F2027,25:203A43,50:2C5364,75:1a6b8a,100:56CCF2&height=220&section=header&text=🌤️%20Weatherly%20Forecaster&fontSize=48&fontColor=ffffff&fontAlignY=38&desc=Real-Time%20Weather%20%7C%20Forecasts%20%7C%20Smart%20Visualizations&descAlignY=58&descSize=17&animation=fadeIn" />

<br/>

<!-- TYPING ANIMATION -->
[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=1000&color=56CCF2&center=true&vCenter=true&width=700&lines=⛅+Live+Weather+%7C+5-Day+Forecast+%7C+6+Graph+Types;🌡️+Temperature+%7C+Humidity+%7C+Wind+%7C+Pressure;🚨+Smart+Weather+Alerts+%7C+Sunrise+%26+Sunset;📊+Bar+%7C+Line+%7C+Pie+%7C+Heatmap+%7C+Scatter+Plot;🌍+Search+Any+City+Worldwide!)](https://git.io/typing-svg)

<br/>

<!-- BADGES -->
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenWeatherMap](https://img.shields.io/badge/OpenWeatherMap-API-FF6B35?style=for-the-badge&logo=icloud&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyOWM](https://img.shields.io/badge/PyOWM-Library-56CCF2?style=for-the-badge&logo=icloud&logoColor=white)

<br/>

![Status](https://img.shields.io/badge/Status-Active-6BCB77?style=flat-square)
![Made with](https://img.shields.io/badge/Made%20with-Python-3776AB?style=flat-square&logo=python)
![Weather](https://img.shields.io/badge/Data-OpenWeatherMap-FF6B35?style=flat-square)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Zameer%20Shaikh-0077B5?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/zameer-shaikh-1a9482345)

</div>

---

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

## 🌍 What is Weatherly Forecaster?

> **Weatherly Forecaster** is a Python-powered weather intelligence app that fetches **real-time weather data** and **5-day forecasts** for any city worldwide using the OpenWeatherMap API. It lets you visualize weather patterns through **6 different graph types** and alerts you about extreme conditions — all from the terminal or GUI.

```python
# Just type a city. Get everything.
city    = "Mumbai, IN"
unit    = "Celsius"
graph   = "Heatmap"
# → Real-time weather + 5-day forecast + smart alerts 🚀
```

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

---

## ✨ Features At a Glance

<div align="center">

| 🌟 Feature | 📝 Description |
|:---|:---|
| 🌡️ **Live Weather** | Temperature, Feels-Like, Humidity, Wind, Pressure, Visibility |
| 🔮 **5-Day Forecast** | 3-hour interval forecasts aggregated into daily min/max trends |
| 📊 **6 Graph Types** | Bar, Line, Pie, Histogram, Scatter Plot, Heatmap |
| 🚨 **Weather Alerts** | Auto-detects Rain, Snow, Storm, Fog, Hurricane, Tornado & more |
| 🌅 **Sunrise & Sunset** | Displays exact sunrise and sunset times in UTC |
| 🌧️ **Rain Volume Graph** | 5-day predicted rain volume visualized in a bar chart |
| 🧠 **Smart Error Handling** | Friendly warnings with city format suggestions |
| 🌍 **Global City Search** | Works with any city using `City, CountryCode` format |

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

---

## 🔧 How It Works

<br/>

### 🧩 1. User Input Section

```
📥  Enter City Name      →   e.g. Mumbai, IN
🌡️  Choose Temp Unit     →   Celsius / Fahrenheit
📊  Choose Graph Type    →   Bar | Line | Pie | Histogram | Scatter | Heatmap
```

Takes simple inputs from the user and connects to the **OpenWeatherMap API** to fetch live + forecast data instantly.

---

### ☀️ 2. Current Weather Display

Fetches real-time data using `weather_at_place(location)` and displays a full snapshot:

<div align="center">

| 🌡️ Temperature | 🤔 Feels Like | ☁️ Clouds | 💨 Wind Speed |
|:---:|:---:|:---:|:---:|
| 💧 Humidity | 🔵 Pressure | 👁️ Visibility | 🌤️ Weather Icon & Status |

</div>

---

### 🔮 3. Weather Forecast — Next 5 Days

Uses **3-hour interval forecasts** via `forecast_at_place(location, '3h')` and smartly aggregates:

```
📅 Per Day Aggregation:
   ├── 🌡️  Min & Max Temperature
   ├── 💧  Humidity levels
   └── ⛅  Weather conditions (for pie chart distribution)
```

Then visualizes the trend using your **chosen graph type**.

---

### 📊 4. Graph Visualizations

<div align="center">

| 📈 Graph Type | 🔍 What It Shows |
|:---|:---|
| **📊 Bar Graph** | Daily Min & Max temperatures |
| **📉 Line Graph** | Temperature trend over 5 days |
| **🥧 Pie Chart** | Distribution of weather types (Rain, Clear, Clouds…) |
| **📶 Histogram** | Frequency of forecasted temperature ranges |
| **⚡ Scatter Plot** | Temperature vs Humidity relationship |
| **🌡️ Heatmap** | Combined temperature & humidity over time |

</div>

> 💡 Humidity data is also visualized separately through bar, line, pie & histogram views!

---

### 🚨 5. Weather Alerts

Auto-detects and displays alerts based on upcoming forecast conditions:

<div align="center">

🌧️ `Rain` &nbsp; | &nbsp; ❄️ `Snow` &nbsp; | &nbsp; ⛈️ `Storm` &nbsp; | &nbsp; 🌫️ `Fog` &nbsp; | &nbsp; 🌀 `Hurricane` &nbsp; | &nbsp; 🌪️ `Tornado`

</div>

---

### 🌅 6. Sunrise & Sunset

```
🌅  Sunrise  →  Displayed in UTC
🌇  Sunset   →  Displayed in UTC
```

---

### 🌧️ 7. Rain Volume Graph

Displays a **5-day rain volume bar chart** showing predicted rainfall in mm — great for planning ahead!

---

### 🧠 8. Error Handling

```python
# ❌ City not found?
⚠️  Warning shown with suggestion:
    → Use format: "City, CountryCode"  e.g. "Mumbai, IN"

# ❌ API / Connection error?
✅  Handled gracefully — no crashes, clean error messages
```

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

---

## 🛠️ Tech Stack

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/PyOWM-OpenWeatherMap%20API-FF6B35?style=for-the-badge&logo=icloud&logoColor=white" />
  <img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
</p>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

---

## 🚀 How to Run

```bash
# 1️⃣ Clone the repository
git clone https://github.com/Zameer17/Weatherly-Forecaster.git

# 2️⃣ Navigate into the folder
cd Weatherly-Forecaster

# 3️⃣ Install dependencies
pip install pyowm matplotlib seaborn numpy pandas

# 4️⃣ Add your OpenWeatherMap API key in the code
API_KEY = "your_api_key_here"

# 5️⃣ Run the app
python weatherly.py
```

> 🔑 Get your free API key at **[openweathermap.org](https://openweathermap.org/api)**

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

---

## 📁 Project Structure

```
Weatherly-Forecaster/
│
├── 📄 weatherly.py          # Main application file
├── 📄 requirements.txt      # Dependencies
└── 📄 README.md             # You are here!
```

---

## 🌐 Connect with Me

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Zameer%20Shaikh-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/zameer-shaikh-1a9482345)
[![GitHub](https://img.shields.io/badge/GitHub-Zameer17-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Zameer17)

<br/>

> *"Storms make trees take deeper roots."* 🌳

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:56CCF2,25:1a6b8a,50:2C5364,75:203A43,100:0F2027&height=120&section=footer&animation=fadeIn" />

</div>
