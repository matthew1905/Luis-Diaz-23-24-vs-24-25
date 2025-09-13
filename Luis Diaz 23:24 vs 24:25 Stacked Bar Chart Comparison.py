'''

Luis Diaz 23/24 vs 24/25 seasons comparison of key stats via a percantage stacked bar chart

Calculates percentage stacked bar charts for key performance statistics to compare Luis Diaz' last two domestic league seasons at liverpool

Created: 24/08/25
Amended (to update for full 24/25 season) : 12/09/25
'''


#Importing Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Reading in stats

def scraping_fbref(table_ID):
    table = pd.read_html("https://fbref.com/en/players/4a1a9578/Luis-Diaz",
             attrs= {"id":table_ID})[0]
    table_array=np.array(table)
    table_2425 = table_array[-13]
    table_2324 = table_array[-14]
    return table_2425, table_2324

shooting_stats_2425, shooting_stats_2324 = scraping_fbref('stats_shooting_dom_lg')
passing_stats_2425, passing_stats_2324 = scraping_fbref('stats_passing_dom_lg')
possession_stats_2425, possession_stats_2324 = scraping_fbref('stats_possession_dom_lg')
misc_stats_2425, misc_stats_2324 = scraping_fbref('stats_misc_dom_lg')

#23/24 Stats
Nineteys_2324 = float(shooting_stats_2324[6])
Goals_2324 = shooting_stats_2324[7]
xG_2324 = shooting_stats_2324[19]
Shots_2324 =  shooting_stats_2324[8]
xG_per_shot_2324 = float(xG_2324) / float(Shots_2324)
SOT_2324 =  shooting_stats_2324[9]
SOT_Ratio_2324 = float(SOT_2324) / float(Shots_2324) 
Assists_2324 = passing_stats_2324[21]
xAG_2324 = passing_stats_2324[22]
Prog_carries_2324 = possession_stats_2324[22]
Crosses_2324 = misc_stats_2324[13]

#24/25 Stats
Nineteys_2425 = float(shooting_stats_2425[6])
Goals_2425 = shooting_stats_2425[7]
xG_2425 = shooting_stats_2425[19]
Shots_2425 =  shooting_stats_2425[8]
xG_per_shot_2425 = float(xG_2425) / float(Shots_2425)
SOT_2425 =  shooting_stats_2425[9]
SOT_Ratio_2425 = float(SOT_2425) / float(Shots_2425) 
Assists_2425 = passing_stats_2425[21]
xAG_2425 = passing_stats_2425[22]
Prog_carries_2425 = possession_stats_2425[22]
Crosses_2425 = misc_stats_2425[13]

#Combining them as a dataframe 

stats = {
    "Crosses": [Crosses_2324, Crosses_2425],
    "Progressive carries": [Prog_carries_2324, Prog_carries_2425],
    "Shots on Target Ratio": [SOT_Ratio_2324, SOT_Ratio_2425],
    "Shots on Target": [SOT_2324, SOT_2425],
    "Shots": [Shots_2324, Shots_2425],
    "xG per shot": [xG_per_shot_2324, xG_per_shot_2425],
    "xG": [xG_2324, xG_2425],
    "xAG": [xAG_2324, xAG_2425],
    "Assists": [Assists_2324, Assists_2425],
    "Goals": [Goals_2324, Goals_2425]
}

df = pd.DataFrame(stats, index=["23/24", "24/25"])

#Converting dataframe to floats
df = df.astype(float)

#Finding stats per 90
cols_per_90 = df.columns.drop(["Shots on Target Ratio", "xG per shot"]) #Drops the ratio columns as they do not need to be divided by nineteys
df.loc["23/24", cols_per_90] = df.loc["23/24", cols_per_90] / Nineteys_2324
df.loc["24/25", cols_per_90] = df.loc["24/25", cols_per_90] / Nineteys_2425



#Transposing dataframe so columns and rows are ordered correctly for the bar charts
df_t = df.T 


#Finding label names
variables = df_t.index
years = df_t.columns

# Normalising to percentage
df_percent = df_t.div(df_t.sum(axis=1), axis=0) * 100

#Finding positional info for the bar charts
y_pos = np.arange(len(variables))
height = 0.5
bottom = np.zeros(len(variables))


#PLotting Graph
fig, ax = plt.subplots(figsize=(8,6))

colors = ['#40B78A', '#DBD7AC'] #Colours of the two different sides of each bar

for i, year in enumerate(years):
    ax.barh(y_pos, df_percent[year], left=bottom, height=height, label=year, color = colors[i])
    bottom += df_percent[year].values 
    
    
#Adding in  a dotted line at the 50% mark to show the midpoint of each bar 
for i in y_pos:
    ax.vlines(x=50, ymin = i - height/2 , ymax = i + height/2, color="white", linestyle="--", linewidth=1)


#Adding in the actual value of each statistic at the start and end of each bar 
for i,j in zip(y_pos, df_t.index):
    value_2324 = df_t.loc[j].values[0]
    value_2425 = df_t.loc[j].values[1]
    ax.text(0, i, f"{value_2324:.2g}", va='center', ha='right', color='black', fontsize=8)
    ax.text(100, i, f"{value_2425:.2g}", va='center', ha='left', color='black', fontsize=8)     

#Adding category labels to the middle of each bar
for i, j in zip(y_pos, variables):
    ax.text(50, i, j, va='center', ha='center', color='black', fontsize=8, fontweight='bold')

#Adding title and legend at the top
fig.suptitle("Luis Diaz 23/24 vs 24/25", y=0.96, fontsize = 15, fontweight='bold') 
ax.legend(title='Year', loc='lower center', bbox_to_anchor=(0.5, 0.97), ncol=2) 
plt.tight_layout()



#Setting automatic x and y labels to invisible and removing all axis lines
ax.set_yticks([]) 
ax.set_xticks([])
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
plt.show()

#Saving the figure
fig.savefig("Luis Diaz 23:24 VS 24:25 % Stacked Bar Chart.png", dpi=500 )
'''

Luis Diaz 23/24 vs 24/25 seasons comparison of key stats via a percantage stacked bar chart

Calculates percentage stacked bar charts for key performance statistics to compare Luis Diaz' last two domestic league seasons at liverpool

Created: 24/08/25
Amended (to update for full 24/25 season) : 12/09/25
'''


#Importing Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Reading in stats

def scraping_fbref(table_ID):
    table = pd.read_html("https://fbref.com/en/players/4a1a9578/Luis-Diaz",
             attrs= {"id":table_ID})[0]
    table_array=np.array(table)
    table_2425 = table_array[-13]
    table_2324 = table_array[-14]
    return table_2425, table_2324

shooting_stats_2425, shooting_stats_2324 = scraping_fbref('stats_shooting_dom_lg')
passing_stats_2425, passing_stats_2324 = scraping_fbref('stats_passing_dom_lg')
possession_stats_2425, possession_stats_2324 = scraping_fbref('stats_possession_dom_lg')
misc_stats_2425, misc_stats_2324 = scraping_fbref('stats_misc_dom_lg')

#23/24 Stats
Nineteys_2324 = float(shooting_stats_2324[6])
Goals_2324 = shooting_stats_2324[7]
xG_2324 = shooting_stats_2324[19]
Shots_2324 =  shooting_stats_2324[8]
xG_per_shot_2324 = float(xG_2324) / float(Shots_2324)
SOT_2324 =  shooting_stats_2324[9]
SOT_Ratio_2324 = float(SOT_2324) / float(Shots_2324) 
Assists_2324 = passing_stats_2324[21]
xAG_2324 = passing_stats_2324[22]
Prog_carries_2324 = possession_stats_2324[22]
Crosses_2324 = misc_stats_2324[13]

#24/25 Stats
Nineteys_2425 = float(shooting_stats_2425[6])
Goals_2425 = shooting_stats_2425[7]
xG_2425 = shooting_stats_2425[19]
Shots_2425 =  shooting_stats_2425[8]
xG_per_shot_2425 = float(xG_2425) / float(Shots_2425)
SOT_2425 =  shooting_stats_2425[9]
SOT_Ratio_2425 = float(SOT_2425) / float(Shots_2425) 
Assists_2425 = passing_stats_2425[21]
xAG_2425 = passing_stats_2425[22]
Prog_carries_2425 = possession_stats_2425[22]
Crosses_2425 = misc_stats_2425[13]

#Combining them as a dataframe 

stats = {
    "Crosses": [Crosses_2324, Crosses_2425],
    "Progressive carries": [Prog_carries_2324, Prog_carries_2425],
    "Shots on Target Ratio": [SOT_Ratio_2324, SOT_Ratio_2425],
    "Shots on Target": [SOT_2324, SOT_2425],
    "Shots": [Shots_2324, Shots_2425],
    "xG per shot": [xG_per_shot_2324, xG_per_shot_2425],
    "xG": [xG_2324, xG_2425],
    "xAG": [xAG_2324, xAG_2425],
    "Assists": [Assists_2324, Assists_2425],
    "Goals": [Goals_2324, Goals_2425]
}

df = pd.DataFrame(stats, index=["23/24", "24/25"])

#Converting dataframe to floats
df = df.astype(float)

#Finding stats per 90
cols_per_90 = df.columns.drop(["Shots on Target Ratio", "xG per shot"]) #Drops the ratio columns as they do not need to be divided by nineteys
df.loc["23/24", cols_per_90] = df.loc["23/24", cols_per_90] / Nineteys_2324
df.loc["24/25", cols_per_90] = df.loc["24/25", cols_per_90] / Nineteys_2425



#Transposing dataframe so columns and rows are ordered correctly for the bar charts
df_t = df.T 


#Finding label names
variables = df_t.index
years = df_t.columns

# Normalising to percentage
df_percent = df_t.div(df_t.sum(axis=1), axis=0) * 100

#Finding positional info for the bar charts
y_pos = np.arange(len(variables))
height = 0.5
bottom = np.zeros(len(variables))


#PLotting Graph
fig, ax = plt.subplots(figsize=(8,6))

colors = ['#40B78A', '#DBD7AC'] #Colours of the two different sides of each bar

for i, year in enumerate(years):
    ax.barh(y_pos, df_percent[year], left=bottom, height=height, label=year, color = colors[i])
    bottom += df_percent[year].values 
    
    
#Adding in  a dotted line at the 50% mark to show the midpoint of each bar 
for i in y_pos:
    ax.vlines(x=50, ymin = i - height/2 , ymax = i + height/2, color="white", linestyle="--", linewidth=1)


#Adding in the actual value of each statistic at the start and end of each bar 
for i,j in zip(y_pos, df_t.index):
    value_2324 = df_t.loc[j].values[0]
    value_2425 = df_t.loc[j].values[1]
    ax.text(0, i, f"{value_2324:.2g}", va='center', ha='right', color='black', fontsize=8)
    ax.text(100, i, f"{value_2425:.2g}", va='center', ha='left', color='black', fontsize=8)     

#Adding category labels to the middle of each bar
for i, j in zip(y_pos, variables):
    ax.text(50, i, j, va='center', ha='center', color='black', fontsize=8, fontweight='bold')

#Adding title and legend at the top
fig.suptitle("Luis Diaz 23/24 vs 24/25", y=0.96, fontsize = 15, fontweight='bold') 
ax.legend(title='Year', loc='lower center', bbox_to_anchor=(0.5, 0.97), ncol=2) 
plt.tight_layout()



#Setting automatic x and y labels to invisible and removing all axis lines
ax.set_yticks([]) 
ax.set_xticks([])
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
plt.show()

#Saving the figure
fig.savefig("Luis Diaz 23:24 VS 24:25 % Stacked Bar Chart.png", dpi=500 )
