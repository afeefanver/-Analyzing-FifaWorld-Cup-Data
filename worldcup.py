import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the World Cups and World Cup Matches datasets
world_cups = pd.read_csv(r"C:/Users/PC/Desktop/Afeef/unified/worldcup/WorldCups.csv")
world_cup_matches = pd.read_csv(r"C:/Users/PC/Desktop/Afeef/unified/worldcup/WorldCupMatches.csv")

# Extract team experience (number of World Cup appearances)
team_experience = world_cups.groupby('Winner')['Year'].count().reset_index(name='appearances')

# Extract home advantage (host team wins)
home_advantage = world_cups[world_cups['Country'] == world_cups['Winner']].shape[0] / world_cups.shape[0]

# Identify the winners of each match
df=world_cup_matches
winners = []
for index, row in df.iterrows():
    if row['Home Team Goals'] > row['Away Team Goals']:
        winners.append(row['Home Team Name'])
    elif row['Home Team Goals'] < row['Away Team Goals']:
        winners.append(row['Away Team Name'])
    else:
        winners.append('Draw')

# Add the winners column to the dataframe
df['Winner'] = winners

# Print the Winner list
print(df['Winner'])

# Extract goal difference (average goal difference for winners)
goal_difference = df['Home Team Goals'] - df['Away Team Goals']

# Identify the teams that kept clean sheets
clean_sheets = []
for index, row in df.iterrows():
    if row['Home Team Goals'] > 0 and row['Away Team Goals'] == 0:
        clean_sheets.append(row['Home Team Name'])
    elif row['Home Team Goals'] == 0 and row['Away Team Goals'] > 0:
        clean_sheets.append(row['Away Team Name'])
    else:
        clean_sheets.append(None)

# Add the clean sheets column to the dataframe
df['Clean Sheet'] = clean_sheets
defensive_solidity = df['Clean Sheet']

# Print Clean Shhet
print('defensive_solidity')

# Extract continental representation (number of winners from each confederation)
df1= world_cups
continental_representation = df1['Winner'].value_counts().reset_index(name='winners')
continental_representation.columns = ['Winner', 'Total Wins']

# Print the extracted information
print("Team Winners:")
print(team_experience.head())

print("\nHome Advantage:")
print("Host team wins:", home_advantage)

print("\nGoal Difference:")
print(goal_difference.head())

print("\nDefensive Solidity:")
print(defensive_solidity.head())

print("\nContinental Representation:")
print(continental_representation.head())


# Visualize the insights
plt.figure(figsize=(12, 6))

# Team Experience

team_experience.columns = ['winner', 'appearances']

plt.subplot(2, 4,1)
sns.barplot(x='winner', y='appearances', data=team_experience.head())
plt.title('Team Winners')
plt.xlabel('Team')
plt.ylabel('Appearances')
plt.show()

