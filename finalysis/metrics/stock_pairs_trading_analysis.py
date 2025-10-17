import finalysis
import numpy as np

from finalysis.data_loader.data_loader import load_data

data = load_data('data/all_stocks_5yr.csv')
names_all = data['Name']  # Assuming structured array
dates_all = data['date']
close_all = data['close']

unique_names = np.unique(names_all)
unique_dates = np.unique(dates_all)
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

# === Remove columns (stocks) with missing data ===
valid = ~np.isnan(prices).any(axis=0)
prices = prices[:, valid]
stock_names = unique_names[valid]

# ==== Pair Trading Evaluation Functions ====
def daily_returns(prices):
    return (prices[1:] / prices[:-1]) - 1

def compute_correlation(returns):
    return np.corrcoef(returns.T)

def find_high_corr_pairs(corr_matrix, threshold=0.9):
    n = corr_matrix.shape[0]
    pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            if corr_matrix[i, j] > threshold:
                pairs.append((i, j))
    return pairs

def spread_zscore(price1, price2):
    spread = np.log(price1) - np.log(price2)
    zscore = (spread - spread.mean()) / spread.std()
    return spread, zscore

def sharpe_ratio(returns):
    mean_ret = np.mean(returns)
    std_ret = np.std(returns)
    if std_ret == 0:
        return 0
    return mean_ret / std_ret * np.sqrt(252)

def max_drawdown(returns):
    cumulative = np.cumprod(1 + returns) - 1
    peak = np.maximum.accumulate(cumulative)
    drawdown = cumulative - peak
    return drawdown.min()

def alpha_beta(returns1, returns2):
    X = np.vstack([returns2, np.ones(len(returns2))]).T
    beta, alpha = np.linalg.lstsq(X, returns1, rcond=None)[0]
    return alpha, beta

def profit_factor(returns):
    gains = returns[returns > 0].sum()
    losses = -returns[returns < 0].sum()
    if losses == 0:
        return np.inf
    return gains / losses

def win_rate(returns):
    wins = np.sum(returns > 0)
    total = len(returns)
    return wins / total if total > 0 else 0

def evaluate_pairs(prices, stock_names, corr_threshold=0.9):
    returns = daily_returns(prices)
    corr_matrix = compute_correlation(returns)
    pairs = find_high_corr_pairs(corr_matrix, corr_threshold)
    
    scores = []
    for i, j in pairs:
        price1, price2 = prices[:, i], prices[:, j]
        ret1, ret2 = returns[:, i], returns[:, j]
        _, zscore = spread_zscore(price1, price2)
        max_z = np.max(np.abs(zscore))
        sharpe1 = sharpe_ratio(ret1)
        sharpe2 = sharpe_ratio(ret2)
        mdd1 = max_drawdown(ret1)
        mdd2 = max_drawdown(ret2)
        alpha1, beta1 = alpha_beta(ret1, ret2)
        alpha2, beta2 = alpha_beta(ret2, ret1)
        pf1 = profit_factor(ret1)
        pf2 = profit_factor(ret2)
        wr1 = win_rate(ret1)
        wr2 = win_rate(ret2)
        score = (max_z * 0.4 +
                 (sharpe1 + sharpe2) * 0.2 -
                 (abs(mdd1) + abs(mdd2)) * 0.2 +
                 (pf1 + pf2) * 0.1 +
                 (wr1 + wr2) * 0.1)
        scores.append((score, stock_names[i], stock_names[j]))
    scores.sort(key=lambda x: x[0], reverse=True)
    return scores[:5]

# === Run evaluation and print pairs ===
top_pairs = evaluate_pairs(prices, stock_names, corr_threshold=0.85)
for score, name1, name2 in top_pairs:
    print(f"{name1} vs {name2}: Score = {score:.4f}")