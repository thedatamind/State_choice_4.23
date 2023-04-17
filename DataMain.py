import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import os



# Define a class for collecting input from the user
class Input:
    def __init__(self):
        # Initialize instance variables for collected data
        self.data = []
        self.customer = []
        self.wages_df = None
        self.housing_df = None
        self.state_info = []

        # Print introductory message for the user
        print("This program is designed to give you information that will help you"
              " decide what state to move to.")
        print("To help you make an informed decision, we have gathered data about the housing market and the job market.")
        print("We will ask you a few questions to help us evaluate your the state you choose. ")
        input("Press enter to start: ")

    # Define a method for loading a CSV file of 2022 third quarter across all industries in the USA
    # Link to source: https://data.bls.gov/cew/apps/table_maker/v4/table_maker.htm#type=0&year=2022&qtr=3&own=5&ind=10&supp=0
    def employment_csv(self):
        if self.wages_df is None:
            self.wages_df = pd.read_csv(
                r"C:\Users\Ilan\Desktop\DataP\DataPcsv\Quarterly Census of Employment and Wages - Bureau of Labor Statistics -.csv")
        return self.wages_df

    # Define a method for loading housing data from a CSV file between '2000-01-31' and '2023-02-28'.
    # Link to source: https://www.zillow.com/research/data/
    def housing_csv(self):
        if self.housing_df is None:
            self.housing_df = pd.read_csv(
                r"C:\Users\Ilan\Desktop\DataP\DataPcsv\State_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv")

        return self.housing_df

    # Define a method for collecting the name of the state the user is interested in
    def state(self):
        # If the state_info variable is empty, ask the user for the name of the state
        if not self.state_info:
            while True:
                self.state_info = input("Enter the name of the state you wish to get information about: ")
                self.state_info = self.state_info.title()  # Convert the state name to title case
                # Check if the state name entered by the user is valid
                if self.state_info in self.employment_csv()["State"].unique():
                    break
                else:
                    print(f"{self.state_info} is not a valid state name. Please enter a valid state name.")
        return self.state_info

    # Define a method for collecting personal information from the user
    def personal_info(self):
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        self.customer.append(name)
        self.customer.append(age)

    # Collect risk-related information from the user and append it to the data list
    def risk_gathering(self):
        risk_necessity = input("Do you believe that taking risks is necessary for achieving success in life? \n"
                               "Yes / No? ")
        self.data.append("1" if risk_necessity.lower() == "yes" else "0")

        risk_general = input("How comfortable are you with taking risks in general? \n"
                             "Choose a number from 1 to 10\n"
                             "1 - not comfortable\n"
                             "10 - very comfortable: ")
        self.data.append(risk_general)

        impulsivity = input("On a scale of 1 to 10, rate your impulsivity level\n"
                            "Choose a number from 1 to 10\n"
                            "1 - Not impulsive\n"
                            "10 - very impulsive: ")
        self.data.append(impulsivity)

        familiarity = input("On a scale of 1 to 10, rate your comfort level with new activities: \n"
                            "1 - do not like new things\n"
                            "10 - like new things: ")
        self.data.append(familiarity)

    # Create a dictionary with the collected data
    def dictionary(self):
        self.personal_info()
        self.risk_gathering()
        input_dict = {
            'Name': self.customer[0],
            'Age': self.customer[1],
            'Risk General': self.data[0],
            'Impulsivity': self.data[1],
            'Familiarity': self.data[2],
            'Risk Necessity': self.data[3]
        }
        return input_dict

    # Create a file with the collected data
    def create_file(self, input_dict, state_choice):
        path = os.path.dirname(os.path.abspath(r"C:\Users\Ilan\Desktop\DataP\DataPcsv"))
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"{self.customer[0]}_{timestamp}.txt"
        file_path = os.path.join(path, file_name)

        with open(file_path, 'a') as f:
            f.write("Date,Name,Age,Risk General,Impulsivity,Familiarity,Risk Necessity,State\n")
            f.write(f"{timestamp},{input_dict['Name']},{input_dict['Age']},{input_dict['Risk General']},"
                    f"{input_dict['Impulsivity']},{input_dict['Familiarity']},{input_dict['Risk Necessity']},{state_choice}\n")

# define the Input class functions
inp = Input()
state_choice = inp.state()
di = inp.dictionary()
df = inp.employment_csv()
df_h = inp.housing_csv()
wages_df = inp.wages_df
inp.create_file(di, state_choice)

# Define a class that will use the data gathered from the user and the data from the database
# to calculate assit the user in making a better choice
class Calculator:
    # Calculate of the change in wages in the selected state
    def wages_calculator(self):
        try:
            september = int(df.loc[df["State"] == state_choice, 'September Employment'].iloc[0])
            july = int(df.loc[df["State"] == state_choice, 'July Employment'].iloc[0])
        except KeyError:
            return f"{state_choice} is not a valid state name. Please enter a valid state name."
        absolute_change = september - july
        relative_change = absolute_change / july
        change = relative_change * 100
        percentage_change = "{:.2f}%".format(change)
        return percentage_change

    # Calculate the change in wages in the all states in USA
    def wages_calculator_all(self):
        df = wages_df
        result = {}
        for index, row in df.iterrows():
            percentage_change = ((row["September Employment"] - row["July Employment"]) / row["July Employment"]) * 100
            result[row["State"]] = percentage_change
        result_df = pd.DataFrame.from_dict(result, orient='index', columns=['Percentage Change in Wages'])
        return f'Last quarter wage change across the USA:\n{result_df}'

    # Calculate the average house price within the 65th to 95th percentile range of the state chosen by the user
    def mean_house_calculator(self):
        try:
            housing_sum = df_h.loc[df_h["RegionName"] == state_choice, '2000-01-31':'2023-02-28'].sum().sum()
        except KeyError:
            return f"{state_choice} is not a valid state name. Please enter a valid state name: "
        n = 278
        housing_mean = housing_sum / n
        return int(housing_mean)

    # Calculate the average house price within the 65th to 95th percentile range of all states in USA
    def all_house_mean(self):
        state = df_h["RegionName"].to_list()[:53]
        data = df_h.iloc[:53, 5:283]
        result_dict = {}
        for i, row in data.iterrows():
            state_mean = np.nanmean(row)
            result_dict[state[i]] = state_mean
        result_df = pd.DataFrame.from_dict(result_dict, orient='index', columns=['Average House Price'])
        return f' To make a more informative choice, ' \
               f' here is a list of the average house price throughout the USA: ' \
               f'{result_df}'

    # Calculate an index based on the user input in "dictionary()" to be used for the final output of the program.
    def risk_index(self):
        risk_general = 7.5 if int(di['Risk General']) == 1 else 0
        impulsivity = int(di['Impulsivity'])
        familiarity = int(di['Familiarity'])
        risk_necessity = int(di['Risk Necessity'])
        index = (risk_general + impulsivity + familiarity + risk_necessity) / 3
        return index

    # Return a string that will be printed in case the calculation results suggest the moving to a different state,
    # but the risk_index() shows a willingness to take risks.
    def index_mark(self):
        index_result = float(self.risk_index())
        if index_result >= 7.5 and self.wages_calculator()[0] == '-':
            return f"However, according to your answers, you seem to be comfortable with risks, " \
                   f"so {state_choice} might be a good fit."
        else:
            return None

    # Plot a graph representing the change housing price from between '2000-01-31' and '2023-02-28' for the state input.
    def plot_housing(self):
        data = df_h[df_h['RegionName'] == state_choice].iloc[:53, 5:283]
        fig, ax = plt.subplots()
        ax.plot(data.iloc[0])
        ax.plot(data)
        ax.set_xlabel('Date')
        ax.set_ylabel('Value')
        ax.set_title(f'Average housing Prices in {state_choice}: {housing_mean}$')
        ax.set_xticks(range(0, len(data.columns), 24))
        plt.xticks(rotation=45)
        return fig

    # Plot a graph representing the change of wages in 2022 third quarter at the state input.
    def plot_wages(self):
        state_data = wages_df.loc[
            wages_df['State'] == state_choice, ['July Employment', 'August Employment', 'September Employment']].values[
            0]
        months = ['July', 'August', 'September']
        fig, ax = plt.subplots()
        ax.plot(months, state_data, marker='o')
        ax.set_title(f"Employment Data for {state_choice}: {wages_percentage_change}")
        ax.set_xlabel('Month')
        ax.set_ylabel('Employment')
        return fig

# Main block
if __name__ == '__main__':
    calc = Calculator()
    index = calc.risk_index()
    index_mark = calc.index_mark()
    wages_percentage_change = calc.wages_calculator()
    housing_mean = calc.mean_house_calculator()
    all_h_mean = calc.all_house_mean()
    all_wages_change = calc.wages_calculator_all()
    fig = calc.plot_housing()
    fig_wages = calc.plot_wages()

    # Print the results of the program.
    print(f"State: {state_choice}")
    print(f"Mean Housing Price from 2000 to 2023: {housing_mean}$")
    print(f"The percentage change in employment from July to September 2022 in {state_choice} was: {wages_percentage_change}")

    # If there has been a decrease in wages but the user is comfortable with risk.
    if index_mark and wages_percentage_change[0] == '-':
        # Let the user know of the decline, but let them know that being a risk-taker, their choice might be good fo them.
        print(index_mark)
    # Print the recommendation to look for a different state to move to.
    elif wages_percentage_change[0] == '-':
        print(f'There has been a decrease in wages during the last quarter of 2022 in {state_choice}.\n'
              f'It might be a better idea to move to a different state.\n'
              f'Here is a list of wage changes for all states:\n{all_wages_change}')
    # Print that the state chosen is a good choice according to the data analysis.
    else:
        print(f'It seems like {state_choice} is a good state to move to.')

    # Plot the graphs
    plt.show()
    plt.show()

