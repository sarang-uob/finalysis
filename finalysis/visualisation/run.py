import numpy as np
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import seaborn as sns

# Import the data loading function from data_loader
from finalysis.data_loader.data_loader import load_data


# === Ask user to select file ===
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(
    title="Select CSV File",
    filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
)
if not file_path:
    raise ValueError("No file selected!")

print(f"Selected file: {file_path}")


# === Load CSV using data_loader ===
# Unpack both structured data and headers
data, headers = load_data(file_path)

# Access columns by header name
try:
    dates_all = data['Date']
    close_all = data['Close'].astype(float)
    names_all = data['Name']
except KeyError as e:
    raise KeyError(
        f"Missing expected column in CSV: {e}. "
        f"Please make sure your CSV has columns named 'Date', 'Close', and 'Name'."
    )


# === Extract unique values ===
unique_dates = np.unique(dates_all)
unique_names = np.unique(names_all)

n_dates = len(unique_dates)
n_stocks = len(unique_names)

# === Build price matrix ===
prices = np.full((n_dates, n_stocks), np.nan)

for j, name in enumerate(unique_names):
    mask = names_all == name
    stock_dates = dates_all[mask]
    stock_prices = close_all[mask]
    for d, p in zip(stock_dates, stock_prices):
        idx = np.where(unique_dates == d)[0][0]
        prices[idx, j] = p

# === Remove columns with missing data ===
valid = ~np.isnan(prices).any(axis=0)
prices = prices[:, valid]
unique_names = unique_names[valid]

# === Compute returns ===
returns = np.log(prices[1:] / prices[:-1])
metrics = []
n = prices.shape[1]

for i in range(n):
    for j in range(i + 1, n):
        p1 = prices[:, i]
        p2 = prices[:, j]

        # Skip if constant or NaNs
        if np.std(p1) == 0 or np.std(p2) == 0:
            continue

        # 1️⃣ Correlation
        corr = np.corrcoef(p1, p2)[0, 1]
        if corr < 0.85:
            continue  # skip weak pairs

        # 2️⃣ Hedge ratio via regression
        beta = np.polyfit(p2, p1, 1)[0]

        # 3️⃣ Spread
        spread = p1 - beta * p2
        spread_mean = np.mean(spread)
        spread_std = np.std(spread)
        zscore = (spread - spread_mean) / spread_std

        # 4️⃣ Arbitrage frequency
        arb_freq = np.mean(np.abs(zscore) > 2)

        # 5️⃣ Mean reversion = 1 - lag-1 autocorrelation
        acf1 = np.corrcoef(spread[1:], spread[:-1])[0, 1] if len(spread) > 1 else 0
        mean_reversion = 1 - acf1

        metrics.append([i, j, corr, arb_freq, mean_reversion])

metrics = np.array(metrics)

# === Normalize metrics ===
def normalize(x):
    return (x - np.min(x)) / (np.max(x) - np.min(x) + 1e-8)

corrs_n = normalize(metrics[:, 2])
freqs_n = normalize(metrics[:, 3])
reverts_n = normalize(metrics[:, 4])

arb_score = 0.4 * corrs_n + 0.3 * freqs_n + 0.3 * reverts_n
metrics = np.column_stack((metrics, arb_score))

# === Sort by score and take top 3 ===
sorted_idx = np.argsort(metrics[:, -1])[::-1]
top3 = metrics[sorted_idx[:3]]

# === Print results ===
print("\nTop 3 Arbitrage Opportunities:\n")

# === Plot all top 3 correlation heatmaps in one figure ===
fig, axes = plt.subplots(1, 3, figsize=(12, 4))
fig.suptitle("Top 3 Arbitrage Pair Correlation Heatmaps", fontsize=14)

for k, (row, ax) in enumerate(zip(top3, axes), 1):
    i, j = int(row[0]), int(row[1])
    name_i, name_j = unique_names[i], unique_names[j]
    score = row[-1]

    corr_matrix = np.corrcoef(prices[:, i], prices[:, j])

    # Print to terminal
    print(f"{k}. {name_i} vs {name_j}  |  Score: {score:.3f}")
    print("Correlation matrix:\n", corr_matrix, "\n")

    # Draw heatmap in subplot
    sns.heatmap(
        corr_matrix,
        annot=True,
        cmap="coolwarm",
        xticklabels=[name_i, name_j],
        yticklabels=[name_i, name_j],
        ax=ax,
        cbar=False
    )
    ax.set_title(f"{name_i} vs {name_j}\nScore: {score:.3f}")

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()