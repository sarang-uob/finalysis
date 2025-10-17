This script identifies potential **pair trading (statistical arbitrage)** opportunities from historical stock prices.

## Overview
  - **Correlation** (relationship strength)
  - **Hedge ratio** (via regression)
  - **Spread & Z-score**
  - **Arbitrage frequency**
  - **Mean reversion speed**
<div align="center">
  <img src="https://img.shields.io/badge/Finalysis-Statistical%20Arbitrage-blueviolet" alt="Finalysis Badge" />
  <h1>📊 Finalysis: Statistical Arbitrage & Pairs Trading Analysis</h1>
</div>

Welcome to **Finalysis** – a Python package for identifying statistical arbitrage opportunities in stock markets using pairs trading strategies.

---

## 🚀 What is Finalysis?
Finalysis helps you:
- **Load** historical stock price data (CSV format)
- **Analyze** stock pairs for correlation and trading signals
- **Visualize** price relationships, spreads, and returns

Pairs trading is a market-neutral strategy that identifies two highly correlated stocks. When their price relationship diverges, you can:
- **Short** the overperforming stock
- **Long** the underperforming stock
- Profit when they revert to their historical relationship

---

## 📂 Data Handling
- **Current:** Handles stock market data in **CSV** format (most common in finance)
- **Planned:** Support for **SQL** and **JSON** data loaders coming soon!

---

## 🛠️ How to Use Finalysis

### 1. Data Loader Module
Load your stock data easily:
```python
from finalysis import load_data
# Load CSV data
data = load_data("data/all_stocks_5yr.csv")
```

### 2. Metrics Module
Analyze your dataset and discover trading pairs:
```python
from finalysis.metrics import describe_dataset, run_analysis
# Get dataset summary
describe_dataset(data)
# Run pairs trading analysis
prices, stock_names, top_pairs, unique_dates = run_analysis(data)
```

### 3. Visualisation Module
Visualize your findings with professional charts:
```python
from finalysis.visualisation import plot_price_series, plot_top_pairs_heatmap, plot_cumulative_returns, plot_spread_zscore, plot_top_pairs_scatter
# Example visualizations
plot_price_series(prices, stock_names, unique_dates)
plot_top_pairs_heatmap(prices, stock_names, top_pairs, unique_dates)
plot_cumulative_returns(prices, stock_names, top_pairs, unique_dates)
plot_spread_zscore(prices, stock_names, top_pairs, unique_dates)
plot_top_pairs_scatter(prices, stock_names, top_pairs)
```

---

## 📈 Visualisations Offered
- **Price Series:** Historical closing prices for all stocks
- **Correlation Heatmap:** Correlation coefficients between top pairs
- **Cumulative Returns:** Compare returns of top pairs over time
- **Spread & Z-Score Analysis:** Key for pairs trading signals
- **Scatter Plots:** Relationship between daily returns of pairs

---

## 🧩 Repo Structure
```
finalysis/
├── data_loader/        # Data loading utilities
├── metrics/            # Analysis & statistics
├── visualisation/      # Plotting & charts
└── tests/              # Unit tests
```

---

## 💡 Customization & Extensibility
- Change analysis parameters (e.g., correlation threshold) in `run_analysis()`
- Easily extend to new data formats (SQL, JSON planned)

---

## ⚠️ Disclaimer
This package is for **educational purposes only**. Pairs trading involves risks:
- Correlations can break down
- Mean reversion is not guaranteed
- Transaction costs affect profitability
- Always backtest before live trading

---

<div align="center">
  <b>Happy Analyzing! 📊✨</b>
</div>
