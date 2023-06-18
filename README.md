# CSV Data Analysis

This Python script performs analysis on data stored in CSV files and generates descriptive statistics and graphs. It allows you to analyze two types of data: event times and object-value pairs.

## Prerequisites

- Python 3.x
- `matplotlib` library

## Installation

1. Clone the repository or download the source code.
2. Install the required dependencies by running the following command:
   ```
   pip install matplotlib
   ```
3. Place the CSV files you want to analyze in the same directory as the Python script.

## Usage

Run the script by executing the Python file `data_analysis.py`. The script will prompt you to enter the names of the CSV files containing the data you want to analyze.

### Event Data Analysis

1. Enter the name of the CSV file containing event times when prompted.
2. Enter the desired graph title for the event data.
3. The script will analyze the event data, calculate descriptive statistics, and generate a histogram and boxplot.
4. The descriptive statistics will be saved in a file named `events_freq_table.txt`.
5. The generated graphs will be saved as `events_boxplot.png` and `events_histogram.png`.

### Object-Value Data Analysis

1. Enter the name of the CSV file containing object-value pairs when prompted.
2. Enter the desired graph title for the object-value data.
3. The script will analyze the object-value data, calculate descriptive statistics, and generate a histogram and boxplot.
4. The descriptive statistics will be saved in a file named `objects_freq_table.txt`.
5. The generated graphs will be saved as `objects_boxplot.png` and `objects_histogram.png`.

## Note

- This script assumes that the CSV files are properly formatted and contain valid data.
- The script uses the `matplotlib` library to generate graphs. Make sure it is installed before running the script.
- The generated graphs will be displayed on the screen and saved as PNG files for further reference.
- The descriptive statistics will be saved in text files for further analysis and reference.
- The script requires the `pandas` library to process the data. Make sure it is installed before running the script.
- The script provides a `DescriptiveStats` class that calculates mean, frequency table, standard deviation, and quartiles for the data.
- The `DescriptiveStats` class also provides methods to create graphs and print the descriptive statistics to a file.
- The script includes additional functions `find_inter_arrival_time` and `parse_csv_file` to handle event time calculations and parsing CSV files, respectively. These functions are used internally by the script and not meant to be called directly.
