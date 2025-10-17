import numpy as np
from typing import Tuple


def load_data(file_path: str, delimiter: str = ',', skip_header: int = 1) -> np.ndarray:
    """
    Loads CSV data into a structured NumPy array so columns can be accessed by name.
    Example: data['Name']
    """

    # Read the header row
    with open(file_path, 'r') as f:
        header_line = f.readline().strip()
        headers = header_line.split(delimiter)

    # Load as structured array with named columns
    try:
        data = np.genfromtxt(
            file_path,
            delimiter=delimiter,
            names=True,          # use first row as field names
            dtype=None,          # auto-detect column types
            encoding='utf-8'
        )
    except Exception as e:
        raise ValueError(f"Error loading data from {file_path}: {str(e)}")

    return data


# Test the function
if __name__ == "__main__":
    csv_file_path = "/Users/sarang/uob/Programming for Data Science/finalysis/data/all_stocks_5yr.csv"  # put your path here

    try:
        data = load_data(csv_file_path)

        # Print headers
        print("Headers:", data.dtype.names)  # structured array field names
        print("\n" + "="*50 + "\n")

        # Access by column name
        print("First 10 'Name' entries:")
        print(data['Name'][:10])

        # Print data shape
        print(f"Data length: {len(data)}")

    except FileNotFoundError:
        print(f"Error: File '{csv_file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")