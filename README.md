Finalysis is an interactive python application that accepts user input stock data and identifies **statistical arbitrage opportunities** (pairs trading candidates) from data
It uses **correlation analysis, hedge ratios, mean reversion metrics, and arbitrage frequency** to score and rank the best stock pairs for potential trading strategies.
Overview
 Loads historical price data
 Constructs a clean price matrix (rows = dates, columns = stocks).
 Filters out incomplete data.(data cleaning)
 Calculates pairwise metrics between stocks:
 
 **Correlation** (relationship strength)
 **Hedge ratio** (via linear regression)
 **Spread & Z-score** (mean reversion behavior)
 **Arbitrage frequency** (how often spread exceeds ±2σ)
 **Mean reversion speed** (1 - lag-1 autocorrelation)
 Normalizes metrics and computes a weighted **arbitrage score**.
 Prints the **top 3 pairs** with detailed metrics and correlation matrices.

Metric Description
 **Correlation** | Measures how closely two stocks move together (only pairs with corr > 0.85 are considered).
 **Hedge Ratio (β)** | Obtained from a linear regression between the two price series.
  **Spread** | Difference between stock prices adjusted by β (`spread = p1 - β * p2`)
  **Z-score** | Normalized spread used to identify deviations from the mean
  **Arbitrage Frequency** | Fraction of times the Z-score exceeds ±2 (potential trade signals)
  **Mean Reversion** | Computed as 1 - lag-1 autocorrelation of the spread (higher means faster mean reversion
  **Arbitrage Score** | Weighted combination of normalized metrics: 0.4*corr + 0.3*freq + 0.3*revert
