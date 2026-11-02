# Pandas Analyzer and Data Visualization

## Subtitle of the Project

A simple Python project that loads, explores, cleans, manipulates, analyzes, and visualizes sales data using Pandas, NumPy, Matplotlib, and Seaborn.

## About the Project

This project is a beginner-friendly Python program that provides an interactive, menu-driven interface for analyzing sales data.

The program allows the user to select from the following options:

* Load sales data from a CSV file.
* Explore the dataset using `head()`, `info()`, and `describe()`.
* Identify and handle missing data.
* Perform necessary data type conversions.
* Convert DataFrame columns into NumPy arrays.
* Demonstrate indexing and slicing operations on arrays.
* Perform element-wise mathematical operations on sales data.
* Combine multiple DataFrames using concatenation, merging, or joining.
* Split DataFrames based on regions, products, or other criteria.
* Search for specific sales records or products.
* Sort and filter sales data based on user inputs.
* Apply aggregation functions such as `sum()`, `mean()`, and `count()`.
* Calculate statistical measures such as standard deviation, variance, and percentiles.
* Generate bar charts, line charts, scatter plots, pie charts, and histograms.
* Create stacked plots and display multiple plots using subplots.
* Generate advanced visualizations such as heatmaps and boxplots using Seaborn.
* Customize plots with titles, labels, legends, and styling options.
* Save visualizations as image files.
* Exit the program.

The program is organized using a `SalesDataAnalyzer` class. The class encapsulates the data analysis and visualization functionalities.

The project uses Pandas to load, explore, clean, and manipulate sales data. NumPy is used for array operations and mathematical calculations. Matplotlib and Seaborn are used to create different types of visualizations.

The program handles exceptions during file loading and data processing to manage invalid input and operation errors.

The program follows a structured workflow from initialization to data exploration, manipulation, analysis, visualization, and conclusion.

## Output

![Program Output](output.png)

## Features

* Displays a menu-driven interface for sales data analysis.
* Loads sales data from a CSV file.
* Explores datasets using Pandas functions.
* Displays dataset information and statistical summaries.
* Identifies and handles missing values.
* Performs data type conversions.
* Converts DataFrame columns into NumPy arrays.
* Performs indexing and slicing on NumPy arrays.
* Performs element-wise mathematical operations on sales data.
* Combines DataFrames using concatenation, merging, and joining.
* Splits DataFrames based on specified criteria.
* Searches for specific sales figures or products.
* Sorts sales data based on sales, profit, or other metrics.
* Filters data based on regions, products, or time periods.
* Applies aggregation functions to summarize sales data.
* Calculates statistical measures such as standard deviation, variance, and percentiles.
* Generates bar charts to compare sales data.
* Generates line charts to visualize sales trends.
* Generates scatter plots to analyze relationships between variables.
* Generates pie charts to display proportions.
* Generates histograms to visualize data distributions.
* Creates stacked plots for comparing multiple data categories.
* Uses subplots to display multiple charts in a single figure.
* Creates heatmaps and boxplots using Seaborn.
* Customizes charts using titles, labels, legends, and styling options.
* Saves visualizations as image files such as PNG and JPEG.
* Uses exception handling to manage invalid input and file-related errors.
* Uses functions and class methods to organize different operations.
* Uses loops and conditional statements to manage menu selections.
* Allows the user to return to the main menu or exit the program.

## Concepts Used

* Variables and data types.
* User input and output.
* Type conversion.
* Lists and dictionaries.
* Functions and method calls.
* Classes and objects.
* Object-oriented programming.
* Pandas library.
* NumPy library.
* Matplotlib library.
* Seaborn library.
* DataFrames and Series.
* Reading CSV files using `pd.read_csv()`.
* Exploring datasets using `head()`, `info()`, and `describe()`.
* Handling missing values using `isnull()`, `fillna()`, and `dropna()`.
* Data type conversion using `astype()`.
* DataFrame columns and indexing.
* Converting DataFrame columns into NumPy arrays using `to_numpy()`.
* NumPy array indexing and slicing.
* NumPy array attributes such as `ndim`, `size`, and `shape`.
* Element-wise mathematical operations.
* DataFrame concatenation using `pd.concat()`.
* DataFrame merging using `pd.merge()`.
* DataFrame joining using `join()`.
* Splitting DataFrames based on conditions.
* Searching and filtering using Boolean indexing.
* Sorting using `sort_values()`.
* Aggregation using `sum()`, `mean()`, and `count()`.
* Statistical calculations using `std()`, `var()`.
* Statistical summaries using `describe()`.
* Data visualization using Matplotlib.
* Creating bar, line, scatter, pie, and histogram plots.
* Creating stacked plots and subplots.
* Data visualization using Seaborn.
* Creating heatmaps and boxplots.
* Plot customization using titles, labels, legends, and styling.
* Saving plots using `savefig()`.
* Exception handling using `try` and `except`.
* Conditional statements using `if`, `elif`, and `else`.
* `while` loops and `for` loops.
* Menu-driven programming.
* Data analysis and visualization workflow.

## Built-in Functions and Methods Used

* `print()`
* `input()`
* `int()`
* `float()`
* `str()`
* `list()`
* `map()`
* `len()`
* `range()`
* `head()`
* `info()`
* `describe()`
* `read_csv()`
* `to_numpy()`
* `astype()`
* `isnull()`
* `fillna()`
* `dropna()`
* `concat()`
* `merge()`
* `join()`
* `sort_values()`
* `sum()`
* `mean()`
* `count()`
* `std()`
* `var()`
* `quantile()`
* `groupby()`
* `bar()`
* `plot()`
* `scatter()`
* `pie()`
* `hist()`
* `savefig()`
* `break`

## Technology Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* CSV
* Visual Studio Code (VS Code)
* Git
* GitHub

## How to Run

### Step 1: Install Python

Download and install Python from the official website:

```bash
https://www.python.org/downloads/
```

### Step 2: Install Required Libraries

Open the terminal and run:

```bash
python -m pip install pandas numpy matplotlib seaborn
```

### Step 3: Open the Project

Open the project folder `pandas_analyzer` in Visual Studio Code.

### Step 4: Check the Dataset

Make sure the sales dataset CSV file is available in the project directory or at the file path specified in the program.

### Step 5: Run the Program

Open the terminal in the project directory and execute:

```bash
python main.py
```

### Step 6: Analyze Sales Data

* Select the desired operation from the main menu.
* Explore and manipulate the sales dataset.
* Perform data analysis and statistical calculations.
* Generate visualizations to understand sales trends and patterns.
* Save the generated charts as image files.
* Return to the main menu or exit the program.

## Project Structure

```text
│
├── main.py
├── sales.csv
├── output.png
└── README.md
```

## Learning Objectives

By completing this project, you can learn:

* How to load and analyze CSV datasets using Pandas.
* How to explore datasets using `head()`, `info()`, and `describe()`.
* How to identify and handle missing values.
* How to perform data type conversions.
* How to convert DataFrame columns into NumPy arrays.
* How to perform indexing and slicing operations.
* How to perform mathematical operations on sales data.
* How to combine and split DataFrames.
* How to search, sort, and filter datasets.
* How to apply aggregation functions to summarize data.
* How to calculate statistical measures such as standard deviation and variance.
* How to analyze sales trends and patterns.
* How to create different types of charts using Matplotlib.
* How to create advanced visualizations using Seaborn.
* How to customize and save visualizations.
* How to use classes and methods to organize a Python program.
* How to handle invalid input using exception handling.
* How to use loops and conditional statements.
* How to create a menu-driven application.
* How to manage a Python project using VS Code, Git, and GitHub.

## Author

Anjali Mehta