# 🏁 Sprint 1 — Data Acquisition & Preprocessing  

**Duration**: ~5–6 days  
**Goal**: By the end of this sprint, you’ll have a **clean, feature-rich, ready-to-train dataset** and a notebook/script that preprocesses it reproducibly.  

---

## ✅ Steps

### **Step 1 — Dataset Selection & Setup**
- Explore **PJM Hourly Energy Consumption** (preferred: cleaner & widely used).  
- Download dataset → place in `data/raw/`.  
- Inspect file format (CSV, time column, missing entries).  
- Learn how to parse datetime (`pandas.to_datetime`).  

**Deliverables**:  
- Load dataset, display first rows, basic summary (`df.info()`, `df.describe()`).  

---

### **Step 2 — Data Cleaning**
- Handle missing values: forward-fill, interpolate, or drop.  
- Handle outliers: visualize with boxplots & z-scores.  
- Resample if needed (ensure consistent hourly intervals).  

**Deliverables**:  
- Clean dataset in `data/processed/`  
- Notebook cells that explain cleaning steps  

---

### **Step 3 — Exploratory Data Analysis (EDA)**
- Plot raw consumption trends (line plots over days/weeks).  
- Plot daily & weekly seasonality.  
- Histogram of demand distribution.  
- Correlation between weekdays vs weekends.  

**Deliverables**:  
- `matplotlib/seaborn` plots showing trends & seasonality  

---

### **Step 4 — Feature Engineering**
- Extract **time-based features**:  
  - Hour of day, day of week, weekend/weekday, holiday flags  
- Optional: Add **external data** like weather (open APIs or public datasets).  
- One-hot encode categorical features (e.g., weekdays).  

**Deliverables**:  
- Extended dataframe with extra feature columns  

---

### **Step 5 — Normalization & Windowing**
- Normalize data (MinMaxScaler or StandardScaler from scikit-learn).  
- Convert series into supervised learning format:  
  - Input = past *n* hours  
  - Output = next 24 hours  
- Write a reusable function:  
  ```python
  def create_windowed_dataset(series, input_width, label_width, shift):
      ...
      return X, y
