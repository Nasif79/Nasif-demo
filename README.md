# Nasif-demo
This is my first git Repository.
<b>
# 🚦 City Traffic Congestion Predictor

A machine learning project that predicts city traffic congestion levels based on historical data and time-based features.

---

## 📊 Features

- Predict congestion levels based on:
  - Hour of day
  - Day of week
  - Is weekend
  - Location (simulated)
- Interactive Streamlit dashboard
- Trained using Random Forest Regressor

---

## 📁 Dataset

**File:** `data/traffic_data.csv`  
**Columns:**
- `timestamp`: Time of observation
- `location`: Simulated area in the city
- `current_speed`: Current speed on the road
- `free_flow_speed`: Normal/expected speed on the road
- `congestion_level`: Computed as `(1 - current_speed / free_flow_speed) * 100`
