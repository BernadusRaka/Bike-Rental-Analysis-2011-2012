
# 🚲 **Bike Rental Analysis Dashboard & Consumer Behavior Insights**  

## 📋 **Project Description**  
This project has two main components:  

1. **Dashboard Application**  
   An interactive interface built with [Streamlit]([https://streamlit.io/](https://bike-rental-analysis-2011-2012-mes7c2vd6lqmpuzm5p8uh5.streamlit.app/)) to explore bike rental consumer behavior during 2011 and 2012.  

2. **Data Analysis with Jupyter Notebook**  
   A detailed analysis of bike rental data using Python, uncovering patterns based on seasons, weather, and time of day.  

---

## 🚀 **Key Features**  

### **Dashboard Application**  
- **Interactive Visualizations:**  
  Displays trends in bike rentals by time, season, and weather conditions.  
- **Dynamic Filtering:**  
  Filter data by date range, weather conditions, and other categories.  
- **Key Statistics:**  
  Summarized metrics such as average rentals per month or day.  

### **Data Analysis**  
- **Exploratory Data Analysis (EDA):**  
  Includes data cleaning and exploration to uncover key trends.  
- **Visualizations:**  
  Insights into bike rental behavior visualized through:  
  - *Number of Bike Rentals:* Comparison of rentals on holidays vs. weekdays.  
  - *Weather and Season Behavior:* Impact of weather conditions and seasons.  
  - *Correlation Between Rentals and Seasons:* Time series analysis of daily rentals.  
  - *Environmental Factors:*  
    - Humidity: Categorized into low, medium, and high.  
    - Temperature: Analyzed in low, medium, and high ranges.  
    - Wind Speed: Grouped into low, medium, and high levels.  
  Visualization techniques include bar charts for categorical data and time series plots for trends.  
- **Clustering Data:**  
  Environmental parameters (temperature, humidity, and wind speed) were clustered into three levels:  
  - Low: Lower range of conditions.  
  - Medium: Mid-range of conditions.  
  - High: Higher range of conditions.  
  This intuitive categorization aids further analysis and decision-making.  

---

## 📂 **Project Structure**  

```bash
.
├── dashboard/
│   ├── streamlit.py                
│   ├── requirements.txt      
│   ├── data/
│   │   └── bike_rental.csv   
├── notebooks/
│   └── bike_rental_analysis.ipynb  
|
├── README.md                
```  

---

## 📊 **Dataset**  
The dataset is sourced from the [UCI Machine Learning Repository - Bike Sharing Dataset](https://archive.ics.uci.edu/ml/datasets/Bike+Sharing+Dataset).  

### **Details:**  
- **Time Period:** 2011-2012  
- **Key Features:**  
  - `count`: Number of bike rentals  
  - `temp`: Temperature  
  - `season`: Season  
  - `weather`: Weather condition  

---

## 📦 **Installation**  

### **Prerequisites**  
- Python 3.8 or later  
- Pip  

### **Installation Steps**  
1. Clone this repository:  
   ```bash
   git clone https://github.com/BernadusRaka/Bike-Rental-Analysis-2011-2012.git
   cd Bike-Rental-Analysis-2011-2012
   ```  
2. Install dependencies:  
   ```bash
   pip install -r dashboard/requirements.txt
   ```  
3. Run the Streamlit app:  
   ```bash
   streamlit run dashboard/streamlit.py
   ```  
4. Open the Jupyter Notebook:  
   Use Jupyter Notebook or JupyterLab to open `notebooks/bike_rental_analysis.ipynb`.  

---

## 🎯 **Project Goals**  
1. Provide data-driven insights into bike rental behavior.  
2. Assist bike-sharing operators in making data-informed decisions.  
3. Offer an intuitive, interactive dashboard for data exploration.  

---
