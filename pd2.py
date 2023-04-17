import numpy as np
import pandas as pd

df_h = pd.read_csv(r"C:\Users\Ilan\Desktop\DataP\DataPcsv\State_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv")
# wages_df = pd.read_csv(r"C:\Users\Ilan\Desktop\DataP\DataPcsv\Quarterly Census of Employment and Wages - Bureau of Labor Statistics -.csv")
#
# def calculate_state_percentage_change():
#     df = wages_df
#     result = {}
#     # iterate over each row in the dataframe
#     for index, row in df.iterrows():
#         # calculate the percentage change from July to September
#         percentage_change = ((row["September Employment"] - row["July Employment"]) / row["July Employment"]) * 100
#         # add the state and the percentage change to the dictionary
#         result[row["State"]] = percentage_change
#     # return the dictionary
#     return result
#
# def wages_calculator():
#     state_choice = "Arizona"
#     df = wages_df
#     try:
#         september = int(df.loc[df["State"] == state_choice, 'September Employment'].iloc[0])
#         july = int(df.loc[df["State"] == state_choice, 'July Employment'].iloc[0])
#     except KeyError:
#         return f"{state_choice} is not a valid state name. Please enter a valid state name."
#     absolute_change = september - july
#     relative_change = absolute_change / july
#     change = relative_change * 100
#     percentage_change = "{:.2f}%".format(change)
#     return percentage_change
#
# def all_house_mean():
#      state = df_h["RegionName"].to_list()[:53]
#      data = df_h.iloc[:53, 5:283]
#      result_dict = {}
#      for i, row in data.iterrows():
#          state_mean = np.nanmean(row)  # Use np.nanmean() to ignore NaN values
#          result_dict[state[i]] = state_mean
#      return f' To make a more informative choice, ' \
#             f' here is a list of the average house price throughout the USA: ' \
#             f'{result_dict}'


import matplotlib.pyplot as plt
import pandas as pd

df_h = pd.read_csv(r"C:\Users\Ilan\Desktop\DataP\DataPcsv\State_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv")
wages_df = pd.read_csv(r"C:\Users\Ilan\Desktop\DataP\DataPcsv\Quarterly Census of Employment and Wages - Bureau of Labor Statistics -.csv")


# state_choice = "Alaska"
# state_data = wages_df.loc[wages_df['State'] == state_choice, ['July Employment', 'August Employment', 'September Employment']].values[0]
#
# # Create a list of month labels
# months = ['July', 'August', 'September']
#
# # Plot the line graph
# plt.plot(months, state_data, marker='o')
#
# # Set the chart title and axis labels
# plt.title(f"Employment Data for {state_choice}")
# plt.xlabel('Month')
# plt.ylabel('Employment')
#
# # Show the plot
# plt.show()

# fig, ax = plt.subplots()
# ax.plot(data.iloc[0])
# ax.plot(data)
# ax.set_xlabel('Date')
# ax.set_ylabel('Avarage wage price in $')
# ax.set_title(f'Wages in {state_choice}')
# plt.show()


state_choice = "Alaska"
data = state_data = df_h[df_h['RegionName'] == state_choice].iloc[:53, 5:283]
fig, ax = plt.subplots()
ax.plot(data.iloc[0])
ax.plot(data)
ax.set_xlabel('Date')
ax.set_ylabel('Avarage house price in $')
ax.set_title(f'Housing Prices in {state_choice}')
plt.show()




# def plot_state_data(state_choice):
# state_choice = "Alaska"
# data = state_data = df_h[df_h['RegionName'] == state_choice].iloc[:53, 5:283]
# fig, ax = plt.subplots()
# ax.plot(data.iloc[0])
# ax.plot(data)
# ax.set_xlabel('Date')
# ax.set_ylabel('Value')
# ax.set_title(f'Housing Prices in {state_choice}')
# plt.show()
#     # housing_df = df_h
#     # state_data = housing_df[housing_df['RegionName'] == state_choice].iloc[:53, 5:283]
#     # if state_data.isnull().values.any():
#     #     # If there are missing values, fill them with 0
#     #     state_data = state_data.fillna(0)
#     # state_data = state_data.transpose()
#     # state_data.plot(x=state_data.index, y=state_choice)
#     # plt.xlabel('Date')
#     # plt.ylabel('Price')
#     # plt.show()








# if __name__ == '__main__':
#     wa = calculate_state_percentage_change()
#     wa1 = wages_calculator()
#     al = all_house_mean()
#     print(wa)
#     print(wa1)
#     print(al)

    # state = df_h["RegionName"].to_list()[:53]
    # data = df_h.iloc[:53, 5:283]
    # result_dict = {}
    #
    # for i, row in data.iterrows():
    #     state_mean = np.nanmean(row) # Use np.nanmean() to ignore NaN values
    #     result_dict[state[i]] = state_mean
    #
    # print(result_dict)
    #
    #
    # def all_house_mean():
    #     state = df_h["RegionName"].to_list()[:53]
    #     data = df_h.iloc[:53, 5:283]
    #     result_dict = {}
    #     for i, row in data.iterrows():
    #         state_mean = np.nanmean(row)  # Use np.nanmean() to ignore NaN values
    #         result_dict[state[i]] = state_mean
    #     return f' To make a more informative choice, ' \
    #            f' here is a list of the average house price throughout the USA: ' \
    #            f'{result_dict}'

