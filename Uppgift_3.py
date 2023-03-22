""" Solutions to assignment 3 in the final exams by John Nordstrand S2300891"""


import pandas as pd
# import matplotlib.pyplot as plt


#---------------------------------------- a) ---------------------------------------------------

df_world_happiness_2015 = pd.read_csv("2015.csv", sep=";")
df_world_happiness_2016 = pd.read_csv("2016.csv", sep=";")

# print(df_world_happiness_2015.head(5))
# print(df_world_happiness_2016.head(5))


#---------------------------------------- b) ---------------------------------------------------

# Renaming of columns
df_world_happiness_2015.rename(
    columns={
    'Happiness Score':'Happiness',
    'Trust (Government Corruption)':'Trust'}, 
    inplace=True)
df_world_happiness_2016.rename(
    columns={
    'Happiness Score':'Happiness',
    'Trust (Government Corruption)':'Trust'}, 
    inplace=True)

def func_3b1(dataframe, year):
    """ Calculate mean values and plot table """
    df_groups = dataframe.groupby('Region')
    mean_freedom = df_groups['Freedom'].mean()
    mean_happiness = df_groups['Happiness'].mean()
    mean_trust = df_groups['Trust'].mean()


    print("=============================================================================")
    print(f"   Average Freedom, Happiness Score and Trust by Region for the year {year}")
    print("=============================================================================")
    print("  Region                         Freedom          Happiness        Trust")

    for group, freedom, happiness, trust in zip(df_groups.groups,   # iterate over all data
                                                mean_freedom,
                                                mean_happiness,
                                                mean_trust):
        string_group = group
        string_freedom = f"{freedom:.3f}"
        string_happiness = f"{happiness:.3f}"
        string_trust = f"{trust:.3f}"

        # Add some padding to make the table line up
        padding_group = max(32 - len(string_group), 0)
        padding_freedom = max(17 - len(string_freedom), 0)
        padding_happiness = max(17 - len(string_happiness), 0)

        # Print all data and padding to table
        print(\
            " "*2 +\
            string_group + " "*padding_group +\
            string_freedom + " "*padding_freedom +\
            string_happiness + " "*padding_happiness +\
            string_trust)
    print("")


func_3b1(df_world_happiness_2015, 2015)
func_3b1(df_world_happiness_2016, 2016)
