import pandas as pd
import matplotlib.pyplot as plt

df_h = pd.read_csv(
                r"C:\Users\Ilan\Desktop\DataP\DataPcsv\State_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv")
state_choice = "Alaska"
def plot_housing():
    data = df_h[df_h['RegionName'] == state_choice].iloc[:53, 5:283]
    fig, ax = plt.subplots()
    ax.plot(data.iloc[0])
    ax.plot(data)
    ax.set_xlabel('Date')
    ax.set_ylabel('Value')
    ax.set_title(f'Average housing Prices in {state_choice}')
    ax.set_xticks(range(0, len(data.columns), 24))
    plt.xticks(rotation=45)
    return fig

p = plot_housing()
plt.show()



# housing_sum = df_h.loc[df_h["RegionName"] != state_choice, '2000-01-31':'2023-02-28'].sum().sum()
# housing_sum_loop = df_h.loc[df_h["RegionName"] != state_choice, '2000-01-31':'2023-02-28'].mean()
# print(housing_sum)
#
#
# state = print(df_h.loc[df_h["RegionName"] != state_choice, "RegionName"])
# state_1 = df_h.loc[df_h["RegionName"]]
# data = df_h.iloc[:53, 5:283]
# result_dict = {}
# for _, row in data.iterrows():
#     state_mean = 0
#     for col in row:
#         state_mean += col
#     state_mean /= 278
#
#     result_dict.update({state_1: 1})
#     print(result_dict)


state_choice = "Texas"
def plot_housing(self):
    data = df_h[df_h['RegionName'] == state_choice].iloc[:53, 5:283]
    fig, ax = plt.subplots()
    ax.plot(data.iloc[0])
    ax.plot(data)
    ax.set_xlabel('Date')
    ax.set_ylabel('Value')
    ax.set_title(f'Average housing Prices in {state_choice}: {housing_mean}$')
    return fig

p = plot_housing(self)
p.show()

    # counter += 1
    # if counter == 51:
    #     break






# def mean_house_calculator(self):
#     try:
#         housing_sum = df_h.loc[df_h["RegionName"] != state_choice, '2000-01-31':'2023-02-28'].sum().sum()
#     except KeyError:
#         return f"{state_choice} is not a valid state name. Please enter a valid state name."
#     n = 278
#     housing_mean = housing_sum / n
#     print(int(housing_mean))



# data = df.iloc[1:53, 5:283]
# # for i in data:
# #     int(i)
# #     r = i.sum()
# # print(r)
#
# # Calculate the mean for each state
# #state_means = data.mean()
#
# print(data)











# sums = df.sum(axis=1)
#
# # Create a new line on the plot with the sum values
# plt.plot(sums)
#
# # Add axis labels and title
# plt.xlabel("X-axis label")
# plt.ylabel("Y-axis label")
# plt.title("Title of plot")
#
# # Display the plot
# #plt.show()



