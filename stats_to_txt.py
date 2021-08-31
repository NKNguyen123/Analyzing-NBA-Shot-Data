import requests
import json
from pprint import pprint
from pyspark import SparkContext
url_base = 'https://stats.nba.com/stats/shotchartdetail'

headers = {
		'Host': 'stats.nba.com',
		'Connection': 'keep-alive',
		'Accept': 'application/json, text/plain, */*',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
		'Referer': 'https://stats.nba.com/',
		"x-nba-stats-origin": "stats",
		"x-nba-stats-token": "true",
		'Accept-Encoding': 'gzip, deflate, br',
		'Accept-Language': 'en-US,en;q=0.9',
	}

parameters = {
	'ContextMeasure': 'FGA',
	'LastNGames': 0,
	'LeagueID': '00',
	'Month': 0,
	'OpponentTeamID': 0,
	'Period': 0,
	'PlayerID': input("Enter player ID: "),
	'SeasonType': 'Regular Season',
	'TeamID': 0,
	'VsDivision': '',
	'VsConference': '',
	'SeasonSegment': '',
	'Season': '2020-21',
	'RookieYear': '',
	'PlayerPosition': '',
	'Outcome': '',
	'Location': '',
	'GameSegment': '',
	'GameId': '',
	'DateTo': '',
	'DateFrom': ''
}


response = requests.get(url_base, params=parameters, headers=headers)
content = json.loads(response.content)
import pandas as pd
# transform contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
df = pd.DataFrame(rows)
df.columns = headers

#get rid of irrelevant data
df.drop('GRID_TYPE', inplace=True, axis=1)
df.drop('GAME_ID', inplace=True, axis=1)
df.drop('GAME_EVENT_ID', inplace=True, axis=1)
df.drop('TEAM_ID', inplace=True, axis=1)
df.drop('TEAM_NAME', inplace=True, axis=1)
df.drop('PERIOD', inplace=True, axis=1)
df.drop('MINUTES_REMAINING', inplace=True, axis=1)
df.drop('SECONDS_REMAINING', inplace=True, axis=1)
df.drop('EVENT_TYPE', inplace=True, axis=1)
df.drop('SHOT_ZONE_RANGE', inplace=True, axis=1)
df.drop('SHOT_ATTEMPTED_FLAG', inplace=True, axis=1)
df.drop('GAME_DATE', inplace=True, axis=1)
df.drop('HTM', inplace=True, axis=1)
df.drop('VTM', inplace=True, axis=1)

df.drop('ACTION_TYPE', inplace=True, axis=1)
df.drop('SHOT_TYPE', inplace=True, axis=1)
df.drop('SHOT_ZONE_BASIC', inplace=True, axis=1)
df.drop('SHOT_ZONE_AREA', inplace=True, axis=1)

df.drop("PLAYER_ID", inplace=True, axis=1)
df.drop("PLAYER_NAME", inplace=True, axis=1)
df.drop("SHOT_DISTANCE", inplace=True, axis=1)


pprint(df)
# write to csv file
# df.to_csv(input("Enter file name: ")+'.csv', index=False)

data = df.values.tolist()

textfile=open(input("Enter txt file name: ")+'.txt','w')
for element in data:
	textfile.write(str(element)+'\n')
textfile.close()
