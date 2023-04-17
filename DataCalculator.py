from DataMain import Input

to = Input()
state_choice = to.state()

di = to.dictionary()

df = to.employment_csv()
df_h = to.housing_csv()


class Calculator:
    def wages_calculator(self):
        september = int(df.loc[df["State"] == state_choice, 'September Employment'].iloc[0])
        july = int(df.loc[df["State"] == state_choice, 'July Employment'].iloc[0])
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
        hosing_mean = housing_sum / n
        return hosing_mean



    # def risk_index(self):
    #     int(di[2])





