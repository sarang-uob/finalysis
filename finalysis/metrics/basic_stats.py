from finalysis.data_loader.data_loader import load_data
import numpy as np

# # Path to your CSV file
# csv_file_path = "C:/Users/Aritrajit Roy/Documents/programming_for_DS_Bath/finalysis/data/all_stocks_5yr.csv"

# # Load data
# data = load_data(csv_file_path)
def numeric_stats(data):
    # Determine numeric columns
    if data.dtype.names is not None:  # structured array
        headers = data.dtype.names
        numeric_columns = [h for h in headers if np.issubdtype(data[h].dtype, np.number)]
    else:  # regular ndarray
        numeric_columns = range(data.shape[1])
        headers = [f"col_{i}" for i in numeric_columns]
    
    print("Basic statistics for numeric columns:\n")
    
    for col in numeric_columns:
        col_data = data[col] if data.dtype.names is not None else data[:, col]
        
        mean_val = np.mean(col_data)
        median_val = np.median(col_data)
        std_val = np.std(col_data, ddof=1)
        
        # Compute mode manually
        values, counts = np.unique(col_data, return_counts=True)
        mode_val = values[np.argmax(counts)]
        
        print(f"{col}:")
        print(f"  Mean   : {mean_val:.4f}")
        print(f"  Median : {median_val:.4f}")
        print(f"  Mode   : {mode_val}")
        print(f"  StdDev : {std_val:.4f}\n")
# numeric_stats(data)