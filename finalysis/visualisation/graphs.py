import numpy as np
import matplotlib.pyplot as plt
from finalysis.metrics.stock_pairs_trading_analysis import run_analysis, daily_returns, spread_zscore
import matplotlib.dates as mdates

# === Run metrics analysis to get data ===
# prices, stock_names, top_pairs, unique_dates = run_analysis()

# Convert dates to numpy datetime64
# dates_np = np.array(unique_dates, dtype='datetime64[D]')

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

# === 3. Spread and Z-score Plots for Top Pairs ===
def plot_spread_zscore(prices , stock_names, top_pairs, unique_dates):
    dates_np = np.array(unique_dates, dtype='datetime64[D]')
    for score, name1, name2 in top_pairs:
        i = np.where(stock_names == name1)[0][0]
        j = np.where(stock_names == name2)[0][0]
        price1 = prices[:, i]
        price2 = prices[:, j]
        spread, zscore = spread_zscore(price1, price2)

        fig, ax = plt.subplots(2,1, figsize=(14,8), sharex=True)
        ax[0].plot(dates_np, spread, label='Spread', color='purple')
        ax[0].axhline(spread.mean(), color='black', linestyle='--', label='Mean')
        ax[0].set_ylabel("Spread")
        ax[0].set_title(f"Spread between {name1} and {name2}")
        ax[0].legend()

        ax[1].plot(dates_np, zscore, label='Z-score', color='orange')
        ax[1].axhline(0, color='black', linestyle='--')
        ax[1].axhline(2, color='red', linestyle='--', label='Upper Threshold')
        ax[1].axhline(-2, color='green', linestyle='--', label='Lower Threshold')
        ax[1].set_ylabel("Z-score")
        ax[1].set_title(f"Z-score of Spread: {name1} vs {name2}")
        ax[1].legend()

        ax[1].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
        plt.xticks(rotation=45)
        plt.xlabel("Date")
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

# === 5. Heatmap delle top arbitrage pairs ===
def plot_top_pairs_heatmap(prices, stock_names, top_pairs, unique_dates):
    returns = daily_returns(prices)
    top_names = []
    indices = []
    for _, name1, name2 in top_pairs:
        i = np.where(stock_names == name1)[0][0]
        j = np.where(stock_names == name2)[0][0]
        top_names.extend([name1, name2])
        indices.extend([i,j])
    # Rimuove duplicati mantenendo ordine
    top_names_unique, unique_idx = np.unique(top_names, return_index=True)
    indices_unique = [indices[i] for i in unique_idx]

    top_returns = returns[:, indices_unique]
    corr_matrix = np.corrcoef(top_returns.T)

    fig, ax = plt.subplots(figsize=(10,8))
    im = ax.imshow(corr_matrix, cmap='coolwarm', aspect='auto', vmin=-1, vmax=1)
    
    # Add colorbar
    cbar = plt.colorbar(im, ax=ax)
    cbar.set_label('Correlation', rotation=270, labelpad=15)
    
    # Set ticks and labels
    ax.set_xticks(np.arange(len(top_names_unique)))
    ax.set_yticks(np.arange(len(top_names_unique)))
    ax.set_xticklabels(top_names_unique, rotation=45, ha='right')
    ax.set_yticklabels(top_names_unique, rotation=0)
    
    # Add correlation values as text annotations
    for i in range(len(top_names_unique)):
        for j in range(len(top_names_unique)):
            text = ax.text(j, i, f'{corr_matrix[i, j]:.2f}',
                          ha="center", va="center", color="black" if abs(corr_matrix[i, j]) < 0.5 else "white")
    
    plt.title("Correlation Heatmap of Top Arbitrage Pairs")
    plt.tight_layout()
    plt.show()

# === Run all plots ===
def plot_all():
    plot_price_series()
    plot_top_pairs_scatter()
    plot_top_pairs_heatmap()
    plot_spread_zscore()
    plot_cumulative_returns()
    

if __name__ == "__main__":
    plot_all()
