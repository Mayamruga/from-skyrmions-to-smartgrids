# ⚡ From Skyrmions to Smart Grids: Energy Consumption Forecasting

**Analogy**: Just like predicting how skyrmions respond to currents, here we predict electricity demand from past consumption.  
**Goal**: Build an end-to-end time-series forecasting system that progresses from classical models to advanced deep learning and an interactive demo app.  

---

## 🔋 Project Overview
- **Dataset**: UCI Electricity Load dataset or PJM Hourly Energy Consumption  
- **Models**: ARIMA, Prophet, LSTM, GRU, Transformer  
- **Deliverables**:
  - Compare classical (ARIMA, Prophet) vs. deep learning (LSTM, GRU, Transformer)  
  - Forecast load 24h ahead with confidence intervals  
  - Visualize actual vs. predicted loads  
  - Deploy an interactive forecasting demo app  

---

## 🔁 Sprint Workflow
Each sprint lasts **4–5 days** and follows the cycle:  

1. **Plan** → Define one clear deliverable  
2. **Code** → Implement in a feature branch  
3. **Review** → Test & document results  
4. **Merge** → Merge into `main` once stable  

---

## 📅 Roadmap

### Sprint 1 — Data Acquisition & Preprocessing
**Goal**: Prepare dataset for forecasting.  
**Tasks**:
- Select dataset (UCI Electricity Load or PJM Hourly Energy Consumption)  
- Handle missing values & outliers  
- Feature engineering: time of day, weekday/weekend, holidays, weather  
- Normalize & windowize data for supervised learning  
- Visualize consumption trends (matplotlib / seaborn)  

**Deliverables**:
- Notebook: `01_data_preprocessing.ipynb`  
- Script: `src/data/preprocess.py`  

---

### Sprint 2 — Classical Baseline Models
**Goal**: Establish baseline with statistical methods.  
**Tasks**:
- Implement **ARIMA / SARIMA**  
- Implement **Prophet**  
- Evaluate with RMSE, MAE, MAPE  
- Save baseline metrics for later comparison  

**Deliverables**:
- Notebook: `02_baseline_models.ipynb`  
- Scripts:  
  - `src/models/arima.py`  
  - `src/models/prophet.py`  

---

### Sprint 3 — Deep Learning (LSTM/GRU)
**Goal**: Build neural forecasting models.  
**Tasks**:
- Implement LSTM & GRU models in PyTorch  
- Train/test with sliding windows  
- Visualize predicted vs. actual load  
- Save trained model checkpoints  

**Deliverables**:
- Notebook: `03_lstm_forecasting.ipynb`  
- Script: `src/models/lstm.py`  

---

### Sprint 4 — Transformer for Time-Series
**Goal**: Capture long-term dependencies with attention.  
**Tasks**:
- Implement Transformer forecasting model  
- Compare performance vs. LSTM/GRU  
- Perform error analysis (success & failure cases)  

**Deliverables**:
- Notebook: `04_transformer_forecasting.ipynb`  
- Script: `src/models/transformer.py`  

---

### Sprint 5 — Model Comparison & Visualization
**Goal**: Make results clear & professional.  
**Tasks**:
- Compare **ARIMA, Prophet, LSTM, Transformer**  
- Create dashboard plots (matplotlib / plotly)  
- Write a markdown summary with key findings  

**Deliverables**:
- Notebook: `05_model_comparison.ipynb`  
- Report: `reports/model_summary.md`  

---

### Sprint 6 — Deployment
**Goal**: Build an interactive forecasting demo.  
**Tasks**:
- Streamlit/Gradio app:  
  - Upload dataset → forecast next 24/48h  
  - Show predictions + error metrics  
- Package with `requirements.txt` / `environment.yml`  
- (Optional) Dockerize for portability  

**Deliverables**:
- App: `app/forecast_app.py`  
- Dockerfile  

---

### Sprint 7 — Polish & Documentation
**Goal**: Make repo recruiter-ready.  
**Tasks**:
- Refactor repo structure (`src/`, `notebooks/`, `reports/`, `app/`)  
- Write blog-style `README.md`:  
  - Problem statement  
  - Approach (from ARIMA → Transformers)  
  - Results with plots  
  - Demo link (Streamlit app)  
- Add CI/CD for linting & tests (optional)  

**Deliverables**:
- Final repo + documentation  

---

## 📂 Suggested Repo Structure

```bash
from-skyrmions-to-smartgrids/
├── src/
│   ├── data/
│   │   └── preprocess.py
│   └── models/
│       ├── arima.py
│       ├── prophet.py
│       ├── lstm.py
│       └── transformer.py
├── notebooks/
│   ├── 01_data_preprocessing.ipynb
│   ├── 02_baseline_models.ipynb
│   ├── 03_lstm_forecasting.ipynb
│   ├── 04_transformer_forecasting.ipynb
│   └── 05_model_comparison.ipynb
├── reports/
│   └── model_summary.md
├── app/
│   └── forecast_app.py
├── data/                # (raw datasets, not committed to git)
├── requirements.txt
├── environment.yml
├── Dockerfile
└── README.md
