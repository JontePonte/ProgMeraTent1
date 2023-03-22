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
    print("  Region                          Freedom          Happiness        Trust")

    for _group, _freedom, _happiness, _trust in zip(df_groups.groups,   # iterate over all data
                                                mean_freedom,
                                                mean_happiness,
                                                mean_trust):
        _string_group = _group
        _string_freedom = f"{_freedom:.3f}"
        _string_happiness = f"{_happiness:.3f}"
        _string_trust = f"{_trust:.3f}"

        # Add some padding to make the table line up
        _padding_group = max(32 - len(_string_group), 0)
        _padding_freedom = max(17 - len(_string_freedom), 0)
        _padding_happiness = max(17 - len(_string_happiness), 0)

        # Print all data and padding to table
        print(\
            " "*2 +\
            _string_group + " "*_padding_group +\
            _string_freedom + " "*_padding_freedom +\
            _string_happiness + " "*_padding_happiness +\
            _string_trust)
    print("")


# Calculate means and plot the data using the function above
func_3b1(df_world_happiness_2015, 2015)
func_3b1(df_world_happiness_2016, 2016)


############################################################################################
# I changed my mind a couple of times here and landed on completely separating the second
# part of assignment 3 from the first. I could have reused some of the code above
############################################################################################

# Extract all data (again)
df_groups_2015 = df_world_happiness_2015.groupby('Region')
mean_freedom_2015 = df_groups_2015['Freedom'].mean()
mean_happiness_2015 = df_groups_2015['Happiness'].mean()
mean_trust_2015 = df_groups_2015['Trust'].mean()

df_groups_2016 = df_world_happiness_2016.groupby('Region')
mean_freedom_2016 = df_groups_2016['Freedom'].mean()
mean_happiness_2016 = df_groups_2016['Happiness'].mean()
mean_trust_2016 = df_groups_2016['Trust'].mean()

# Calculate change in percent using the formula given in assignment
change_freedom = (mean_freedom_2016 - mean_freedom_2015) / mean_freedom_2015 * 100
change_happiness = (mean_happiness_2016 - mean_happiness_2015) / mean_happiness_2015 * 100
change_trust = (mean_trust_2016 - mean_trust_2015) / mean_trust_2015 * 100

# Almost the exact same plot as in the function for 3b1
print("=======================================================================================")
print(" Relative change displayed in [%] Freedom, Happiness and Trust score from 2015 to 2016")
print("=======================================================================================")
print("  Region                          Freedom          Happiness        Trust")

for group, freedom, happiness, trust in zip(df_groups_2015.groups,   # iterate over all data
                                            change_freedom,
                                            change_happiness,
                                            change_trust):
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

