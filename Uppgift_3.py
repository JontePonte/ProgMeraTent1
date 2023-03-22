""" Solutions to assignment 3 in the final exams by John Nordstrand S2300891"""


import pandas as pd
import matplotlib.pyplot as plt


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

# The plot isn't pretty in its current state. I'll make it better if I have time and energy left
plot_frame = pd.DataFrame({'freedom':change_freedom, 'happiness':change_happiness, 'trust':change_trust})
plot_frame.plot(kind="bar", ylabel="Relative Change in %")
# plt.show() # show in the end replaces this one


#---------------------------------------- c) ---------------------------------------------------

df_2015 =  df_world_happiness_2015[['Country', 'Health (Life Expectancy)', 'Happiness Rank']].copy()
df_2016 =  df_world_happiness_2016[['Country', 'Health (Life Expectancy)', 'Happiness Rank']].copy()

# Renaming of columns
df_2015 = df_2015.rename(
    columns={
    'Health (Life Expectancy)':'Health_Expectancy_2015',
    'Happiness Rank':'Rank_2015'})
df_2016 = df_2016.rename(
    columns={
    'Health (Life Expectancy)':'Health_Expectancy_2016',
    'Happiness Rank':'Rank_2016'})

# Sort the data based on Health_Expectancy
df_2015 = df_2015.sort_values(by='Health_Expectancy_2015', ascending=False)
df_2016 = df_2016.sort_values(by='Health_Expectancy_2016', ascending=False)

df_2015_10 = df_2015.head(10)
df_2016_10 = df_2016.head(10)

def plot_3c(dataframe, year):
    """ Plot the tables for 3c for both 2015 and 2016 """
    print( "===================================================================================")
    print(f"      Top 10 high life expectancy countries for the year {year}")
    print( "===================================================================================")
    print(f"  Country                       Health Expectancy {year}     Rank {year}")

    for _, _row in dataframe.iterrows():
        _string_country = _row['Country']
        _string_health = f"{_row[f'Health_Expectancy_{year}']:.3f}"
        _string_rank = f"{_row[f'Rank_{year}']:.3f}"

        # Add some padding to make the table line up
        _padding_country = max(30 - len(_string_country), 0)
        _padding_health = max(27 - len(_string_health), 0)


        # Print all data and padding to table
        print(\
            " "*2 +\
            _string_country + " "*_padding_country +\
            _string_health + " "*_padding_health +\
            _string_rank)
    print("")

# Call the print table function
plot_3c(df_2015_10, 2015)
plot_3c(df_2016_10, 2016)

# Create the scatter plot and add 2015 values
ax = df_2015_10.plot.scatter(x='Health_Expectancy_2015',
                             y='Rank_2015',
                             color='blue',
                             label='2015',
                             figsize=(10,8),
                             )

# Add 2016 values to the same scatter plot
df_2016_10.plot.scatter(ax=ax,
                        x='Health_Expectancy_2016',
                        y='Rank_2016',
                        color='red',
                        label=2016)

# Title and labels
title_text = 'Top 10 countries for the year 2015 and 2016 by Health Expectancy and their corresponding rank'

ax.set_title(title_text)
ax.set_xlabel('Health Expectancy')
ax.set_ylabel('Rank')

# Add names to the dots
for index, row in df_2015_10.iterrows():
    ax.annotate(row['Country'], (row['Health_Expectancy_2015'], row['Rank_2015']))

for index, row in df_2016_10.iterrows():
    ax.annotate(row['Country'], (row['Health_Expectancy_2016'], row['Rank_2016']))

# I didn't use subplot as you said but I hope it's ok anyway
# plt.show() # Show in the end replaces this one

# pick out the five countries
countries = ['Hong Kong', 'Singapore', 'Japan', 'South Korea', 'Italy']

# I create boolean masks for each df
countries_mask_2015 = df_2015_10['Country'].isin(countries)
countries_mask_2016 = df_2016_10['Country'].isin(countries)

df_2015_5 = df_2015_10[countries_mask_2015]
df_2016_5 = df_2016_10[countries_mask_2016]

df_merged = pd.merge(df_2015_5, df_2016_5, on="Country", suffixes=('_2015', '_2016'))

# Create a subplot object to enable subplots (_ = fig and isn't used)
_, axes = plt.subplots(nrows=2,
                        ncols=1,
                        figsize=(8, 7),)

# Plot the Health Expectancy
df_merged.plot(ax=axes[0],
               x='Country',
               y=['Health_Expectancy_2015', 'Health_Expectancy_2016'],
               kind='bar',
               sharex=True)

# Plot the Health Expectancy
df_merged.plot(ax=axes[1],
               x='Country',
               y=['Rank_2015', 'Rank_2016'],
               kind='bar',
               sharex=True)

# Fix the label rotation
axes[0].tick_params('x', labelrotation=60, labelsize=8)
axes[0].tick_params('y', labelrotation=0, labelsize=8)
axes[1].tick_params('x', labelrotation=60, labelsize=8)
axes[1].tick_params('y', labelrotation=0, labelsize=8)

# y-axis labels
axes[0].set_ylabel('Health Expectancy', fontsize=8)
axes[1].set_ylabel('Rank', fontsize=8)

# Remove x-labels (could probably be done better)
axes[0].set_xlabel('')
axes[1].set_xlabel('')

# Set titles with fontsize
axes[0].set_title('Countries with Highest Health Expectancy', fontsize=10)
axes[1].set_title('Happiest Countries Ranking', fontsize=10)

# This one sets the plots higher up on screen and add space between them
plt.subplots_adjust(top=0.9, bottom=0.25, hspace=0.6)
plt.show()
