import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np


class SalesDataAnalyzer:

    def __init__(self):
        self.data = None
        self.graph = None

    def load_data(self):
        try:
            print("Load Dataset")
            self.data = input("Enter the path of the csv file: ")
            self.data = pd.read_csv(f"{self.data}")
            print("Dataset loaded successfully! ")
            return self.data
        except:
            print("Please enter valid path")

    def explore_data(self):
        try:
            print("Select an option: ")
            print("1. Display the first 5 rows")
            print("2. Display the last 5 rows")
            print("3. Display the column names")
            print("4. Display data types")
            print("5. Display basic info ")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                print(self.data.head())
            elif choice == 2:
                print(self.data.tail())
            elif choice == 3:
                print(self.data.columns)
            elif choice == 4:
                print(self.data.dtypes)
            elif choice == 5:
                print(self.data.info())
            else:
                print("Invalid Input")

        except:
            print("Something went wrong!!")


    def dataframe_op(self):
        try:
            if self.data is None :
                print("Please Load the Dataset First !")
                return
            print("=== DataFrame Operations ===")
            print("1. Sum of Sales")
            print("2. Top 5 Products with Highest Sales")
            print("3. Top 5 Products with Lowest Sales")
            print("4. Region with Highest Sales")
            print("5. Total Profit by Each Product")

            choice = int(input("Enter Your Choice :-"))


            if choice == 1 :
                print(self.data['TotalSales'].sum())

            elif choice == 2:
                print(self.data.groupby("Product")["TotalSales"].sum().nlargest(5))

            elif choice == 3:
                print(self.data.groupby("Product")["TotalSales"].sum().nsmallest(5))

            elif choice == 4:
                print(self.data.groupby("Region")["TotalSales"].sum().nlargest(1))

            elif choice == 5 :
                print(self.data.groupby('Product')['Profit'].sum())

            else:
                print("Enter a valid Choice !")

        except:
            print("Somehting went wrong!")

    def filter_data(self):
        try:
            print("Select an option:")
            print("1. Display rows With Missing Values ")
            print("2. Fill missing Values with mean")
            print("3. Drop rows with Missing Values")
            print("4. Replace Missing Values with a Specific Value ")
            
            choice=int(input("Enter your Chocie : "))
            if choice==1:
                if  self.data.isnull().empty:
                    print("No Missing Values Found in the Dataset !")
                else:
                    null=self.data.isnull()
                    print(null)

            elif choice==2:
                df=self.data.fillna(self.data.mean())
                print(df.head())
            elif choice==3:
                print("=== Before Cleaning ===")
                print(df.isnull().sum())
                df=self.data.dropna()
                print("=== After Cleaning ===")
                print(df.isnull().sum())
            elif choice==4:
                replace=input("Enter a Value to Replace it with Missing Value : ")
                dt=self.data.fillna(replace)
                print(f"Missing Values Replaced with {replace} Sucessfully ! ")
            else:
                print("Invalid Choice !!")

        except:
            print("Something went wrong!")

    def statistics_data(self):
        try:
            if self.data is None:
                print("Please Load the Dataset First!")
                return

            print("=== Descriptive Statistics ===")
            print("1. Display Summary Statistics")
            print("2. Display Mean of Numeric Columns")
            print("3. Display Median of Numeric Columns")
            print("4. Display Minimum and Maximum Values")
            print("5. Display Standard Deviation")
            print("6. Display Variance")

            choice = int(input("Enter  Your Choice :- "))


            if choice == 1 :
                print(self.data.describe())

            elif choice == 2 :
                print(self.data.mean(numeric_only=True))

            elif choice == 3 :
                print(self.data.median(numeric_only=True)) 

            elif choice == 4 :
                print("MINIMUM :\n",self.data.min(numeric_only=True))
                print("MAXIMUM :\n",self.data.max(numeric_only=True))

            elif choice == 5 :
                print(self.data.std(numeric_only=True))

            elif choice == 6 :
                print(self.data.var(numeric_only=True))

            else :
                print("Enter a valid Choice !")

        except:
            print("Something went wrong!")

    def data_visualization(self):
        try:
            if self.data is None:
                print("Please Load the Dataset First!")
                return
            print()
            print("1. Bar Plot")
            print("2. Line Plot")
            print("3. Scatter Plot")
            print("4. Pie Chart ")
            print("5. Histogram ")
            print("6. Stack Plot ")
            choice=int(input("Enter your Choice : "))

            if choice == 1:

                column = input("Enter column name for X-axis (e.g. Product): ")
                value = input("Enter numeric column for Y-axis (e.g. TotalSales): ")

                if column in self.data.columns and value in self.data.columns:

                    data = self.data.groupby(column)[value].sum()
                    data = data.sort_values(ascending=False)

                    ax = data.plot(
                        kind="bar",
                        figsize=(12, 6),
                        title=f"{value} by {column}"
                    )

                    plt.xlabel(column)
                    plt.ylabel(value)
                    plt.xticks(rotation=45, ha="right")
                    plt.grid(axis="y", alpha=0.3)
                    plt.tight_layout()
                    self.graph = ax.get_figure()
                    plt.show()
                    return self.graph
                else:
                    print("Invalid column name!")
    
            elif choice == 2 :
                x = input("Enter X-axis column (e.g. Date): ")
                y = input("Enter Y-axis column (e.g. Sales): ")

                if x in self.data.columns and y in self.data.columns:
                    data = self.data.groupby(x)[y].sum().sort_index()
                    data.plot(kind="line", marker=".", title=f"{y} by {x}")
                    plt.xlabel(x)
                    plt.ylabel(y)
                    plt.grid(True, alpha=0.3)
                    plt.tight_layout()
                    plt.show()
                    return self.graph
                    
                else:
                    print("Invalid column name!")

            elif choice == 3 :
                x = input("Enter X-axis column (e.g. Quantity): ")
                y = input("Enter Y-axis column (e.g. Sales): ")

                if x in self.data.columns and y in self.data.columns:
                    self.data.plot(kind="scatter", x=x, y=y, title=f"{y} vs {x}")
                    plt.xlabel(x)
                    plt.ylabel(y)
                    plt.grid(True, alpha=0.3)
                    plt.tight_layout()
                    plt.show()
                    return self.graph
                else:
                    print("Invalid column name!")

            elif choice == 4 :
                column = input("Enter category column (e.g. Region): ")
                value = input("Enter numeric column (e.g. Sales): ")

                if column in self.data.columns and value in self.data.columns:
                    data = self.data.groupby(column)[value].sum()
                    data.plot(kind="pie", autopct="%1.2f%%", title=f"{value} by {column}")
                    plt.ylabel("")
                    plt.tight_layout()
                    plt.show()
                    return self.graph
                else:
                    print("Invalid column name!")

            elif choice == 5 :
                column = input("Enter numeric column (e.g. Sales): ")

                if column in self.data.columns:
                    self.data[column].dropna().plot(
                        kind="hist", bins=10, edgecolor="black",
                        title=f"Distribution of {column}")
                    plt.xlabel(column)
                    plt.ylabel("Frequency")
                    plt.grid(axis="y", alpha=0.3)
                    plt.tight_layout()
                    plt.show()
                    return self.graph
                else:
                    print("Invalid column name!")

            elif choice == 6:
                required = ["Region", "TotalSales", "Profit"]

                if all(column in self.data.columns for column in required):
                    df = self.data.groupby("Region")[["TotalSales", "Profit"]].sum()
                    df.plot(kind="bar", stacked=True, title="Sales and Profit by Region")
                    plt.xlabel("Region")
                    plt.ylabel("Amount")
                    plt.tight_layout()
                    self.graph = plt.gcf()
                    plt.show()
                    return self.graph
                else:
                    print("CSV must contain Region, Sales, and Profit columns.")

            else :
                print("Enter a valid Choice !")
        except:
            print("Something went wrong !")

    def save_visualization(self):
        try:
            if self.data is None:
                print("Please Load the Dataset First!")
                return

            filename = input("Enter file name (e.g. sales_chart.png): ")

            if not filename.lower().endswith(".png"):
                filename += ".png"

            plt.savefig(filename, bbox_inches="tight")
            print(f"Visualization saved as {filename}")
        except:
            print("Something went wrong!")


    def main_menu(self):
        while True:
            print()
            print("========== Data Analysis and Visualization Program ==========")
            print("Select an option: ")
            print("1. Load Dataset")
            print("2. Explore Data")
            print("3. Perform Dataframe Operations")
            print("4. Handle Missing Dataset")
            print("5. Generate Descriptive Statistics")
            print("6. Data Visualization")
            print("7. Save Visualization")
            print("8. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.load_data()
            elif choice == 2:
                self.explore_data()
            elif choice == 3:
                self.dataframe_op()
            elif choice == 4:
                self.filter_data()
            elif choice == 5:
                self.statistics_data()
            elif choice == 6:
                self.data_visualization()
            elif choice == 7:
                self.save_visualization()
            elif choice == 8:
                break
            else:
                print("Invalid Choice!")


    def __del__(self):
        pass

obj=SalesDataAnalyzer()
obj.main_menu()