# Finalysis package
from .data_loader.data_loader import load_data
from .metrics.basic_info import describe_dataset
from .metrics.stock_pairs_trading_analysis import run_analysis
from .visualisation.graphs import plot_price_series, plot_top_pairs_heatmap,plot_top_pairs_scatter,plot_spread_zscore,plot_cumulative_returns,plot_top_pairs_heatmap,plot_all


__all__ = ['load_data', 'describe_dataset', 'run_analysis',"plot_price_series","plot_top_pairs_heatmap","plot_top_pairs_scatter","plot_spread_zscore","plot_cumulative_returns","plot_top_pairs_heatmap","plot_all",]


