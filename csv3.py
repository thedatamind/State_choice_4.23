import pandas as pd
import matplotlib.pyplot as plt

class Input:
    def __init__(self):
        self.data = []
        self.customer = []
        self.wages_df = None
        self.housing_df = None
        self.state_info = []

    print("This program is designed to give you information that will help you"
          "decide what state to move to.")
    print("To help you make an informed decision, we have gathered data about the housing market and the job market.")
    print("We will ask you a few questions that will help us choose the right state for you.")
    input("Press any key to start: ")

    def employment_csv(self):
        if self.wages_df is None:
            self.wages_df = pd.read_csv(
                r"C:\Users\Ilan\Desktop\DataP\DataPcsv\Quarterly Census of Employment and Wages - Bureau of Labor Statistics -.csv")
        return self.wages_df

    def housing_csv(self):
        if self.housing_df is None:
            self.housing_df = pd.read_csv(
                r"C:\Users\Ilan\Desktop\DataP\DataPcsv\State_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv")
        return self.housing_df

    def state(self):
        if not self.state_info:
            self.state_info = input("Enter the name of the state you wish to get information about: ")
            self.state_info = self.state_info.title()  # Convert the state name to title case
        return self.state_info

    def personal_info(self):
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        self.customer.append(name)
        self.customer.append(age)

    def risk_gathering(self):
        risk_necessity = input("Do you believe that taking risks is necessary for achieving success in life? \n"
                               "Yes / No? ")
        self.data.append("1" if risk_necessity.lower() == "yes" else "0")


        risk_general = input("How comfortable are you with taking risks in general? \n"
                             "Choose a number from 1 to 10\n"
                             "1 - not comfortable\n"
                             "10 - very comfortable ")
        self.data.append(risk_general)

        impulsivity = input("On a scale of 1 to 10, rate your impulsivity\n"
                            "Choose a number from 1 to 10\n"
                            "1 - Not impulsive\n"
                            "10 - very impulsive ")
        self.data.append(impulsivity)

        familiarity = input("On a scale of 1 to 10, rate your comfort level with new activities: \n"
                            "1 - do not like new things\n"
                            "10 - like new things ")
        self.data.append(familiarity)

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


to = Input()
state_choice = to.state()
di = to.dictionary()
df = to.employment_csv()
df_h = to.housing_csv()


class Calculator:
    all_states_housing = df_h.loc[:, 'RegionName']
    all_states_wages = df.loc[:, 'State']

    def wages_calculator(self):
        september = int(df.loc[df["State"] == state_choice, 'September Employment'].iloc[0])
        july = int(df.loc[df["State"] == state_choice, 'July Employment'].iloc[0])
        absolute_change = september - july
        relative_change = absolute_change / july
        change = relative_change * 100
        percentage_change = "{:.2f}%".format(change)
        return percentage_change

    def wages_calculator_all(self):
        september = int(df.loc[df["State"] == all_states_wages, 'September Employment'].iloc[0])
        july = int(df.loc[df["State"] == all_states_wages, 'July Employment'].iloc[0])
        absolute_change = september - july
        relative_change = absolute_change / july
        change = relative_change * 100
        percentage_change = "{:.2f}%".format(change)
        return percentage_change

    def mean_house_calculator(self):
        first_month = float(df_h.loc[df_h["RegionName"] == state_choice, '2000-01-31'].iloc[0])
        last_month = float(df_h.loc[df_h["RegionName"] == state_choice, '2023-02-28'].iloc[0])
        n = 273
        housing_sum = first_month + last_month
        housing_mean = housing_sum / n
        return int(housing_mean)

    def mean_house_calculator_all(self):
        first_month = float(df_h.loc[df_h["RegionName"] == all_states_housing, '2000-01-31'].iloc[0])
        last_month = float(df_h.loc[df_h["RegionName"] == all_states_housing, '2023-02-28'].iloc[0])
        n = 273
        housing_sum = first_month + last_month
        housing_mean = housing_sum / n
        return int(housing_mean)

    def risk_index(self):
        risk_general = 7.5 if int(di['Risk General']) == 1 else 0
        impulsivity = int(di['Impulsivity'])
        familiarity = int(di['Familiarity'])
        risk_necessity = int(di['Risk Necessity'])
        index = (risk_general + impulsivity + familiarity + risk_necessity) / 3
        return index

    def plot(self):
        row = df_h.loc[df_h["RegionName"] == state_choice]
        row = row.drop(['RegionID', 'SizeRank', 'RegionName', 'RegionType', 'StateName'], axis=1)
        start_date = "2000-01-31"
        end_date = "2023-02-28"
        data = df_h.loc[:, start_date:end_date]
        fig, ax = plt.subplots()
        ax.plot(data.iloc[0])
        ax.set_xlabel('Date')
        ax.set_ylabel('Value')
        ax.set_title(f'Housing Prices in {state_choice}')
        return fig





if __name__ == '__main__':
    calc = Calculator()
    index = calc.risk_index()
    wages_percentage_change = calc.wages_calculator()
    housing_mean = calc.mean_house_calculator()
    wages_percentage_change_all = calc.wages_calculator_all()
    housing_mean_all = calc.mean_house_calculator_all()
    fig = calc.plot()

    print(housing_mean_all, wages_percentage_change_all)
    print("Personal Information:")
    print("\nState Information:")
    print(f"State: {state_choice}")
    print(f"Percentage Change in Employment from July to September 2022: {wages_percentage_change}")
    print(f"Mean Housing Price from 2000 to 2023: {housing_mean}$")
    print(f"you score a {index} on the risk index")
    plt.show()




