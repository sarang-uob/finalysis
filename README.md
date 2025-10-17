This script identifies potential **pair trading (statistical arbitrage)** opportunities from historical stock prices.

## Overview
- Loads stock price data 
- Builds a clean price matrix (dates × stocks)
- Computes:
  - **Correlation** (relationship strength)
  - **Hedge ratio** (via regression)
  - **Spread & Z-score**
  - **Arbitrage frequency**
  - **Mean reversion speed**
- Combines these into a weighted **arbitrage score**
- Prints the **top 3 most promising pairs**
