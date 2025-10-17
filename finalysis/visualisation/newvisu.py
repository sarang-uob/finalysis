import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from finalysis.metrics.stock_pairs_trading_analysis import run_analysis, daily_returns
import matplotlib.dates as mdates

# === 1. Price Series of All Stocks ===
def plot_price_series(prices, stock_names, unique_dates):
    plt.figure(figsize=(14,6))
    dates_np = np.array(unique_dates, dtype='datetime64[D]')
    for i, name in enumerate(stock_names):
        plt.plot(dates_np, prices[:, i], alpha=0.7)
    plt.title("Price Series of All Stocks")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# === 2. Scatter Plots of Top Correlated Pairs ===
def plot_top_pairs_scatter(prices, stock_names, top_pairs):
    returns = daily_returns(prices)
    for score, name1, name2 in top_pairs:
        i = np.where(stock_names == name1)[0][0]
        j = np.where(stock_names == name2)[0][0]
        plt.figure(figsize=(8,6))
        plt.scatter(returns[:, i], returns[:, j], alpha=0.6)
        plt.title(f"Scatter Plot of Returns: {name1} vs {name2}")
        plt.xlabel(f"{name1} Daily Returns")
        plt.ylabel(f"{name2} Daily Returns")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

# === 3. Correlation Heatmap of Top Pairs ===
def plot_top_pairs_correlation_heatmap(prices, stock_names, top_pairs):
    top_names = []
    indices = []
    for _, name1, name2 in top_pairs:
        i = np.where(stock_names == name1)[0][0]
        j = np.where(stock_names == name2)[0][0]
        top_names.extend([name1, name2])
        indices.extend([i, j])
    
    # Remove duplicates while keeping order
    top_names_unique, unique_idx = np.unique(top_names, return_index=True)
    indices_unique = [indices[i] for i in unique_idx]

    top_prices = prices[:, indices_unique]
    corr_matrix = np.corrcoef(top_prices.T)

    plt.figure(figsize=(10,8))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm',
                xticklabels=top_names_unique, yticklabels=top_names_unique)
    plt.title("Correlation Heatmap of Top Pairs")
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.show()

# === 4. Cumulative Returns of Top Pairs ===
def plot_cumulative_returns(prices, stock_names, top_pairs, unique_dates):
    dates_np = np.array(unique_dates, dtype='datetime64[D]')
    returns = daily_returns(prices)
    for score, name1, name2 in top_pairs:
        i = np.where(stock_names == name1)[0][0]
        j = np.where(stock_names == name2)[0][0]
        cum_ret1 = np.cumprod(1 + returns[:, i]) - 1
        cum_ret2 = np.cumprod(1 + returns[:, j]) - 1
        plt.figure(figsize=(12,6))
        plt.plot(dates_np[1:], cum_ret1, label=f"{name1} Cumulative Return")
        plt.plot(dates_np[1:], cum_ret2, label=f"{name2} Cumulative Return")
        plt.title(f"Cumulative Returns: {name1} vs {name2}")
        plt.xlabel("Date")
        plt.ylabel("Cumulative Return")
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

# === Run all plots ===
def plot_all(prices, stock_names, top_pairs, unique_dates):
    plot_price_series(prices, stock_names, unique_dates)
    plot_top_pairs_scatter(prices, stock_names, top_pairs)
    plot_top_pairs_correlation_heatmap(prices, stock_names, top_pairs)
    plot_cumulative_returns(prices, stock_names, top_pairs, unique_dates)

if __name__ == "__main__":
    # Example usage:
    # prices, stock_names, top_pairs, unique_dates = run_analysis(data)
    plot_all(prices, stock_names, top_pairs, unique_dates)
