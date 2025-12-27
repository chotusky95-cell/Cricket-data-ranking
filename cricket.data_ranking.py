import pandas as pd
import matplotlib.pyplot as plt
batsman = {
    "Rank":[1,2,3,4,5,6,7,8,9,10],
    "Batsman name":["Rohit sharma","Virat Kohli","Daryl Mitchell","Ibrahim Zadran","Shubhman Gill","Babar Azam","Harry Tector","Shai Hope","Charith Asalanka","Shreyas Iyer"],
    "Ratings":[781,773,766,764,723,722,708,701,690,688],
    "Country":["India","India","New Zealand","Afghanistan","India","Pakistan","Irealand","West Indies","Sri lanka","India"],
    "Matches_played":[279,308,56,39,58,140,54,148,80,73],
    "Runs":[11516,14557,2338,1868,2818,6501,1992,6113,2659,1868],
    "Average":[49.21,58.46,53.14,51.89,56.36,53.73,46.33,50.11,42.89,47.82],
    "Strike Rate":[92,93.66,93.86,82.33,99.23,87.17,83.28,79.82,90.91,99.02],
    "No.of fours":[1080,1356,185,178,319,601,155,487,222,270],
    "No.of Sixes":[355,165,63,30,60,68,66,120,63,72],
    "No.of Hundred":[33,53,7,6,8,20,5,19,5,5],
}

bowler = {
    "Rank":[1,2,3,4,5,6,7,8,9,10],
    "Name":["Rashid Khan","Jofra Archer","Kuldeep Yadav","Maheesh Theekshana","Keshav Maharaj","Bernard Scholtz","Mitchell Santner","Josh Hazlewood","Abrar Ahmed","Wanindu Hasaranga"],
    "Country":["Afghanistan","England","India","Sri lanka","South Africa","Namibia","New Zealand","Australia","Pakistan","Sri lanka"],
    "Ratings":[710,670,655,647,646,645,636,628,624,619],
    "Matches_played":[117,36,117,59,56,64,124,96,14,68],
    "Wickets":[210,65,191,79,73,99,133,142,28,111],
    "Average":[19.65,24.38,26.3,28.03,31.12,19.08,35.47,27.66,20.79,24.22],
    "Economy":[4.21,7.98,5.03,4.6,4.73,3.36,4.82,4.73,4.44,5.06],
    "Strike-Rate":[28.04,29.15,31.38,36.57,39.52,34.04,44.17,35.06,28.07,28.69],
    "5_Wickets":[6,1,2,0,1,5,2,3,0,4],
    "Top_spell":["7/18","6/40","6/25","4/25","5/33","5/22","5/50","6/52","4/27","7/19"]
}
df_batting= pd.DataFrame(batsman)
print(df_batting)
df_bowling=pd.DataFrame(bowler)
print(df_bowling)
df_batting.head()
print(df_batting.head())
df_batting.tail()
print(df_batting.tail())
df_bowling.tail()
print(df_bowling.tail())
df_bowling.head()
print(df_bowling.head())
df_batting.to_csv('batsman.csv')
print(df_batting)
df_bowling.to_csv('bowling.csv')
print(df_bowling)
top_by_average = df_batting.loc[df_batting["Average"].idxmax()]
top_by_strike_rate = df_batting.loc[df_batting["Strike Rate"].idxmax()]
most_fours = df_batting.loc[df_batting["No.of fours"].idxmax()]
most_sixes = df_batting.loc[df_batting["No.of Sixes"].idxmax()]
most_by_ratings = df_batting.loc[df_batting["Ratings"].idxmax()]
most_hundreds = df_batting.loc[df_batting["No.of Hundred"].idxmax()]

least_by_average = df_batting.loc[df_batting["Average"].idxmin()]
least_by_strike_rate = df_batting.loc[df_batting["Strike Rate"].idxmin()]
least_fours = df_batting.loc[df_batting["No.of fours"].idxmin()]
least_sixes = df_batting.loc[df_batting["No.of Sixes"].idxmin()]
least_by_ratings = df_batting.loc[df_batting["Ratings"].idxmin()]
least_hundreds = df_batting.loc[df_batting["No.of Hundred"].idxmin()]

print("\nTop by Average:\n",top_by_average)
print("\nTop by Strike Rate:\n",top_by_strike_rate)
print("\nMost fours:\n",most_fours)
print("\nMost sixes:\n",most_sixes)
print("\nMost by Ratings:\n",most_by_ratings)
print("\nMost Hundreds:\n",most_hundreds)
print(df_batting)

print("\nLeast by Average:\n",least_by_average)
print("\nLeast by Strike Rate:\n",least_by_strike_rate)
print("\nLeast fours:\n",least_fours)
print("\nLeast sixes:\n",least_sixes)
print("\nLeast by Ratings:\n",least_by_ratings)
print("\nLeast Hundreds:\n",least_hundreds)
print(df_batting)

top_by_average = df_bowling.loc[df_bowling["Average"].idxmax()]
top_by_economy = df_bowling.loc[df_bowling["Economy"].idxmax()]
most_by_5_wickets = df_bowling.loc[df_bowling["5_Wickets"].idxmax()]
most_by_top_Spell = df_bowling.loc[df_bowling["Top_spell"].idxmax()]
most_by_ratings = df_bowling.loc[df_bowling["Ratings"].idxmax()]
top_by_strike_rate= df_bowling.loc[df_bowling["Strike-Rate"].idxmax()]

print("\nTop by Average:\n", top_by_average)
print("\nTop by Strike Rate:\n", top_by_strike_rate)
print("\nTop by Economy:\n", top_by_economy)
print("\nMost by 5_Wickets:\n", most_by_5_wickets)
print("\nMost by ratings:\n", most_by_ratings)
print("\nMost by top_Spell:\n", most_by_top_Spell)
print(df_bowling)

plt.figure()
plt.bar(df_batting["Batsman name"], df_batting["Average"])
plt.xticks(rotation=90)
plt.title("Batting Average of Players")
plt.xlabel("Player")
plt.ylabel("Average")
plt.tight_layout()
plt.show()

plt.figure()
plt.plot(df_batting["Batsman name"], df_batting["Strike Rate"], marker='o')
plt.xticks(rotation=90)
plt.title("Strike Rate Comparison")
plt.xlabel("Player")
plt.ylabel("Strike Rate")
plt.tight_layout()
plt.show()

plt.figure()
plt.bar(df_bowling["Name"], df_bowling["Wickets"])
plt.xticks(rotation=90)
plt.title("Wickets Taken by Bowlers")
plt.xlabel("Bowler")
plt.ylabel("Wickets")
plt.tight_layout()
plt.show()

plt.figure()
plt.scatter(df_bowling["Economy"], df_bowling["Wickets"])
plt.title("Economy vs Wickets")
plt.xlabel("Economy")
plt.ylabel("Wickets")
plt.tight_layout()
plt.show()

plt.figure()
plt.barh(df_batting["Batsman name"], df_batting["Runs"])
plt.title("Total Runs Scored by Batsmen")
plt.xlabel("Runs")
plt.ylabel("Player")
plt.tight_layout()
plt.show()

plt.figure()
plt.hist(df_batting["Strike Rate"], bins=6)
plt.title("Strike Rate Frequency")
plt.xlabel("Strike Rate")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

plt.figure()
plt.hist(df_bowling["Economy"], bins=10)
plt.title("Economy Frequency")
plt.xlabel("Economy")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

plt.figure()
plt.boxplot(df_batting["Average"])
plt.title("Distribution of Batting Averages")
plt.ylabel("Average")
plt.tight_layout()
plt.show()















