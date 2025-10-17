*Finalysis*
Finalysis is a Python-based tool that identifies promising pair trading opportunities using historical stock price data and statistical arbitrage techniques.

*Overview*
The application processes market data to uncover statistically correlated stock pairs that exhibit mean-reverting spreads. Analyzing these relationships helps traders discover potential arbitrage setups.

*Features*
•	Data Ingestion: Load and clean historical stock price data from CSV or API sources.
•	Price Matrix Construction: Build a time-series matrix of stock prices indexed by date.
•	Statistical Metrics:
     o	Correlation – measures the strength between stocks.
     o	Hedge Ratio – estimated via linear regression.
     o	Spread & Z-Score – quantifies deviation from historical mean.
     o	Arbitrage Frequency – tracks how often spreads revert to the mean.
     o	Mean Reversion Speed – evaluates how quickly the spread normalizes.
•	Arbitrage Scoring: Combines multiple statistical factors into a single weighted arbitrage score.
•	Results Output: Prints and optionally exports the top 3 most promising stock pairs based on the final score.

*Software Used*
•	Python 3.8+
•	numpy – numerical computations
•	matplotlib – data visualization

*Usage*
1.	Load your stock price dataset.
2.	Run the analysis script.
3.	Review the ranked list of optimal pairs for potential trading opportunities.

*Installation*
Ensure you have Python 3.8 or higher installed. Then install the required packages with:

bash
pip install numpy matplotlib

