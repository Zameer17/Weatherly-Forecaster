### 🔧 How it works — Summary of Functionality:

---

### ✅ **1. User Input Section**

* Takes user input:

  * **City name**
  * **Temperature unit** (Celsius/Fahrenheit)
  * **Graph type** (Bar, Line, Pie, Histogram, Scatter Plot, Heatmap)

---

### ☀️ **2. Current Weather Display**

* Fetches current weather using `weather_at_place(location)`:

  * Shows **temperature**, **feels-like**, **clouds**, **wind speed**, **humidity**, **pressure**, **visibility**
  * Displays weather **icon** and **status**.

---

### 🔮 **3. Weather Forecast (Next 5 Days)**

* Uses 3-hour interval forecasts from OpenWeatherMap via `forecast_at_place(location, '3h')`.
* Aggregates:

  * **Min/Max temperatures per day**
  * **Humidity**
  * **Weather conditions** (for pie chart)
* Displays **temperature trends** using chosen **graph type**.

---

### 📊 **4. Graph Options**

Based on the user's selection, it visualizes:

* **Bar/Line Graph**: Min and max daily temperatures
* **Pie Chart**: Distribution of weather types (e.g., Rain, Clear)
* **Histogram**: Frequency distribution of forecasted temperatures
* **Scatter Plot**: Temperature vs Humidity
* **Heatmap**: Combined temperature and humidity over time

It also shows **humidity data** through similar visualizations (bar, line, pie, histogram) unless already represented.

---

### 🚨 **5. Weather Alerts**

Displays alerts based on upcoming weather:

* Rain, Snow, Storm, Fog, Hurricane, Tornado, etc.

---

### 🌅 **6. Sunrise and Sunset Times**

* Displays sunrise and sunset times in UTC.

---

### ⛈️ **7. Rain Graph**

Rain Volume: Displays the predicted rain volume for the next 5 days in a bar chart.

---

### 🧠 **Error Handling**

* If location is not found, it shows a warning.
* Suggests using format like `City, CountryCode` (e.g., Mumbai, IN).
* Handles API or connection errors gracefully.

---
