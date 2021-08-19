# All Rocketleague Items

Need a list/database of ALL the possible items, cars, skins, boosts etc for RocketLeague? I needed this info for side project I'm working on and couldn't find a nice way to get it without webscraping etc from online sources (which, are mostly out-of-date). Using the below method and this repository, you can get yourself a neat JSON file with all the info you need! 

How To Start: 

1. You'll need BakkesMod for RocketLeague PC (https://www.bakkesmod.com/) 
\*Sorry, you can't do this on the console versions of the game\* 
2. Once installed, in-game hit F6 to bring up the command line for the Mod 
3. Type "dumpitems" into the command line and hit "Enter"
4. BakkesMod will generate a CSV file called "items.csv" in the same folder when the game's .EXE is located (eg. C:\Rocketleague\rocketleague\Binaries\Win64\items.csv)


This CSV contains all the info you'll need. It's as up-to-date as you'll get, as the info i'll pulled directly from the game at runtime

Now, if you need to clean up this info you can use this repository (specifically the 'csv_to_json.py') 


LEGEND:

- "items.csv" - This is the file Bakkesmod generates when using the 'dumpitems' command. Up-to-date list of ALL RocketLeague items (Season 4) as of 12/08/2021
- "csv_to_json.py" - Python file to clean up the aforementioned csv file and store it neatly as JSON
- "rl_items.json" - Outputted JSON file of the 'csv_to_json.py' file 





