from finalysis.data_loader.data_loader import load_data
import numpy as np

# Path to your CSV file
csv_file_path = "C:/Users/Aritrajit Roy/Documents/programming_for_DS_Bath/finalysis/data/all_stocks_5yr.csv"

# Load data
data = load_data(csv_file_path)



def describe_dataset(data):
    # Check if structured array
    if data.dtype.names is not None:
        headers = data.dtype.names
        rows = data.shape[0]
        cols = len(headers)
        print(f"Number of rows: {rows}")
        print(f"Number of columns: {cols}\n")
        
        numeric_count = 0
        non_numeric_count = 0
        
        print("Column details:")
        for h in headers:
            col = data[h]
            if np.issubdtype(col.dtype, np.number):
                col_type = "Numeric"
                numeric_count += 1
            else:
                col_type = "Non-numeric"
                non_numeric_count += 1
            print(f"{h}: {col_type} (dtype={col.dtype})")
        
        print(f"\nTotal numeric columns: {numeric_count}")
        print(f"Total non-numeric columns: {non_numeric_count}")
        print("\nPreview (first 5 rows):")
        print(data[:5])
    
    else:  # regular ndarray
        rows, cols = data.shape
        print(f"Number of rows: {rows}")
        print(f"Number of columns: {cols}\n")
        numeric_count = np.sum(np.issubdtype(data.dtype, np.number))
        non_numeric_count = cols - numeric_count
        print(f"Total numeric columns: {numeric_count}")
        print(f"Total non-numeric columns: {non_numeric_count}")
        print("\nPreview (first 5 rows):")
        print(data[:5])


describe_dataset(data)