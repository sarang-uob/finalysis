# Finalysis package
from .data_loader.data_loader import load_data
from .metrics.basic_info import describe_dataset
from .metrics.stock_pairs_trading_analysis import run_analysis
from .visualisation.graphs import plot_price_series


__all__ = ['load_data', 'describe_dataset', 'run_analysis',"plot_price_series"]


