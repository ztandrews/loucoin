# LouCoin Calculator
### LouCoin Calculations Code
This is a simple python code that calculates every New York Islanders palyers LouCoin amount.

LouCoin is an advanced metric created by the [Obstructed Views Podcast](https://open.spotify.com/show/2msToI7dfUmcxExi8TC6Z8) that measuers a hockey teams hits and grit, which is what New York Islanders hockey is all about. It is calculated as:

(Current Value of Lou Coin * Amount of Hits A Player Has)

So for example, at the time of this initial commit, the value of LouCoin is 1.379437. So if Adam Pelech has 3 hits, his LouCoin would be:

(1.379437*3) = 4.138311 LouCoin

The way this program works is it uses an [NHL Python API](https://sportsipy.readthedocs.io/en/latest/nhl.html#sportsipy.nhl.boxscore.BoxscorePlayer.on_ice_shot_attempts_against) to acquire data, and then it loops through the Islanders roster and runs a function to calculate each players current LouCoin amount. It then adds every player and their respective LouCoin amount into a dictionary, where it is then sorted from highest to lowest using a sorting function. After the dictionary is sorted, I run it through a for loop to format the output (get rid of parentheses, quotes, etc.) to make it easier to read, and the formatted dictionary gets printed to the console in a line by line, clean fashion.

The data this program spits out is then used for the [LouCoin website](https://loucoin.com), where a leaderboard is made with the current LouCoin leaders.

