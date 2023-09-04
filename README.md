# FA Cup Simulator

My first completed project using Python - It's a simulation of the FA Cup, the oldest cup competition in association football. The
program simulates every round of the FA Cup, from the 1st Round up to the final. The teams I've used are based on the 2023-24
season, from all the Premier League teams to the Championship, League One, League Two and a couple of Conference and lower league
teams to round up the numbers

# How to Play

Once you load up the program, you'll be asked to press any key to begin the simulation and then press ENTER. This will begin the
1st Round Draw, where you will get a list of teams participating in that round, in the case of the 1st Round there are 80 teams from
League One, League Two and the Conference and lower league teams. Again you will be asked to press and key and then ENTER to begin the
draw; and then the draw will begin; the teams will be drawn randomly home and away so there should be 40 matches.

Once the draw has been made, you will be asked again to press any key and then ENTER to begin the round of fixtures. You will then go
through each of the games in the round, inputting scores for both the home team and away team. Remember to put an integer in the fields
as you will be asked to try again if you don't enter an integer.

If the score predicted is a win for the home team or the away team, you will get a message showing the result and the winning team 
advances to the next round, the losing team is eliminated from the competition. However, as in the real FA Cup, should the match end in
a draw, both teams will go to a replay once the other games in the round are completed.

After the round's fixtures are completed, any games that went to a replay will be shown, with whoever was drawn away in the first game 
scheduled to be the home team in the replayed fixture. Again you will be asked to input the results for the replayed fixture, and whoever 
has the higher number of goals advances. If the player has predicted a draw at the end of regular time, you will then be asked to
give the scores after 30 minutes extra time, as is the rule in real-life. I have made it so that the score after extra time cannot be
lower than the score after regular time, so the player has to enter the same number of goals for extra time as in regular time or more.

If the scores are still even after extra-time, of course there are then penalties, and the player is then asked to input the scores
for the penalty shootout, I have made sure the player has to input a definite winner for the penalties since penalties don't end in a
draw in real life.

Once the replays have been completed, that's the end of the round, you should get a full list of winners for that round, in the case of the
1st Round that should be 40 teams, and then the simulation moves onto the 2nd Round, where those 40 teams are drawn into 20 home and away ties.
The rules are the same as before, and 20 teams advance from this round. Then you have the 3rd Round, where now you will get the addition of the 20
Premier League teams and 24 Championship teams along with the 20 teams from the 2nd Round to make 64 teams in the draw for the 3rd Round.

The rest of the tournament should be quite straightforward, there are 32 teams in the 4th Round, 16 teams in the 5th Round, 8 teams in the
Quarter-Finals, 4 in the Semi-Finals and of course the final 2 in the Final; the format and rules are the same throughout the tournament.

Regarding replays, I'm aware that nowadays they only do replays up until the end of the 4th Round, with some talk of scrapping replays completely
in the future. I could probably add some code after a certain round, ties go straight to extra time in the event of a draw. But as a 90s/00s
football fan, with a rather nostalgic reverence for the FA Cups of old, that would be sacrelige in my view. So at the moment replays are
included up to and including the final, as that was what made part of the magic of the FA Cup as they say.

Anyhow, that's everything, I hope you enjoy this little game. It's only text-based for now, maybe I could adapt it to use Pygame or Turtle at
some point, we shall see. Hope you enjoy it!
