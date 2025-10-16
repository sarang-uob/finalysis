# Data loading functions
import numpy as np
from typing import Tuple, List, Optional


def load_data(file_path: str, delimiter: str = ',', skip_header: int = 1, 
              dtype: Optional[type] = None) -> Tuple[np.ndarray, List[str]]:

    # Read the header row
    with open(file_path, 'r') as f:
        header_line = f.readline().strip()
        headers = header_line.split(delimiter)
    
    # Load the data using numpy
    try:
        if dtype is None:
            # Try to load as float, mixed types will be handled
            data = np.genfromtxt(file_path, delimiter=delimiter, skip_header=skip_header, 
                                dtype=None, encoding='utf-8')
        else:
            data = np.genfromtxt(file_path, delimiter=delimiter, skip_header=skip_header, 
                                dtype=dtype)
    except Exception as e:
        raise ValueError(f"Error loading data from {file_path}: {str(e)}")
    
    return data, headers


# Test the function
if __name__ == "__main__":
    # Create a variable for the file path
    csv_file_path = ""  
    
    try:
        # Load the data
        data, headers = load_data(csv_file_path)
        
        # Print headers
        print("Headers:")
        print(headers)
        print("\n" + "="*50 + "\n")

        # Print first 10 entries
        print("First 10 entries:")
        print(data[:10])

        
        # Print data shape
        print(f"Data shape: {data.shape}")
        
    except FileNotFoundError:
        print(f"Error: File '{csv_file_path}' not found.")
        print("Please update the 'csv_file_path' variable with the correct path to your CSV file.")
    except Exception as e:
        print(f"Error: {e}")