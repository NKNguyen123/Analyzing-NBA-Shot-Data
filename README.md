# Analyzing-NBA-Shot-Data
Comparing the field goal success rates of the most prolific close, mid, and long range shooter in the NBA

# Purpose of Project
In the NBA is it easier to score when closer to the basket than farther? Of course this applies in an empty gym by yourself when practicing but in professional basketball there's countless more factors to keep track of. I wanted to find out whether this is true by using PySpark and Python.

# Hypothesis
The closer you are to the basket the easier it is to the score in the NBA.

# Experiment
I chose players from the NBA 2020-2021 regular season that shot a high volume at each range and considered the best of among the best at that range. It helped that these 3 were among my favorite players: Stephen Curry for long range, Chris Paul for mid range, and Zion Williamson for short range. Then I roughly chose ranges from the basket that roughly represented each category: 0-10ft. for short, 10-22ft. for mid, 22ft.+ for long. Using the actual data, linear regression, and logistic regression I aimed to show that despite being experts at their ranges, these 3 players still had an easier time scoring closer to the basket. These were coded in Python and later run by PySpark in a Hadoop environment. You can see the functions I wrote and used in "StatAnalyzer.py", "txt_to_linear_regression_model.py", and "txt_to_logistic_regression_model.py".

# Data Collection
I wrote "stats_to_txt.py" to convert a player's stats from the nba.com/stats by ID to a text file. This text file was specifically formatted to fit into a PySpark RDD and to be analyzed using "StatAnalyzer.py". Additionally I wrote "txt_to_graph.py" to convert these text files to a visual diagram for each player at each range.

# Conclusion
If you read my project report or scroll through my presentation slides you'll see that my hypothesis held true. Some future insights I could use if I revisit this project is perhaps analyzing the stats of the entire league, and not just 3 prolificly ranged players. Additionally I can even consider specific team or player match-ups in the calculations.
