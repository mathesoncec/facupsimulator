import random
import time

def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return userInput 
       break
    
def draw_round(teams):
    print("Teams in draw")
    print("--------------")
    time.sleep(2)
    teams.sort()
    for i in range(0, len(teams)):
        print(teams[i])
        time.sleep(0.2)
    print("--------------")
    print("\n")
    random.shuffle(teams)
    time.sleep(2)
    input("Press any key to begin the draw: ")
    print("\n")
    time.sleep(2)
    

def simulate_round(teams):
    winners = []
    replays = []
    matchnumber = 1
    replaynumber = 1
    for i in range(0, len(teams), 2):
        team1 = teams[i]
        team2 = teams[i+1]
        print(f"{team1} vs {team2}")
        time.sleep(2)
    print("-------------------------")
    print("\n")
    time.sleep(3)
    input("Press any key to begin the round: ")
    print("\n")
    time.sleep(2)
    
    for i in range(0, len(teams), 2):
        team1 = teams[i]
        team2 = teams[i+1]
        
        print(f"Match {matchnumber}: {team1} vs {team2}")
        score_team1 = int(inputNumber(f"Enter the score for {team1}: "))
        score_team2 = int(inputNumber(f"Enter the score for {team2}: "))
        
        if score_team1 > score_team2:
            winners.append(team1)
            print(f"{team1} defeats {team2} {score_team1}-{score_team2}!\n")
        elif score_team2 > score_team1:
            winners.append(team2)
            print(f"{team2} defeats {team1} {score_team2}-{score_team1}!\n")
        else:
            replays.append(team1)
            replays.append(team2)
            print(f"{team1} has drawn {score_team1}-{score_team2} with {team2}. Match will go to a replay.\n")
        matchnumber += 1
    
    if len(replays) > 0:
        
        print("Replays")
        for i in range(0, len(replays), 2):
            team2 = replays[i]
            team1 = replays[i+1]
            print(f"{team1} vs {team2}")
        print("-------------------------")
        time.sleep(3)
        input("Press any key to begin the replays: ")
        print("\n")
            
        for i in range(0, len(replays), 2):
            team1 = replays[i]
            team2 = replays[i+1]
        
            print(f"Match {replaynumber}: {team2} vs {team1}")
            score_team2 = int(inputNumber(f"Enter the score for {team2}: "))
            score_team1 = int(inputNumber(f"Enter the score for {team1}: "))
        
            if score_team1 > score_team2:
                winners.append(team1)
                print(f"{team1} defeats {team2} {score_team1}-{score_team2}!\n")
            elif score_team2 > score_team1:
                winners.append(team2)
                print(f"{team2} defeats {team1} {score_team2}-{score_team1}!\n")
            else:
                exscore_team2 = int(inputNumber(f"Enter the score for {team2} after extra time: "))
                exscore_team1 = int(inputNumber(f"Enter the score for {team1} after extra time: "))
                while exscore_team2 < score_team2 or exscore_team1 < score_team1:
                    exscore_team2 = int(inputNumber(f"Enter the score for {team2} after extra time: "))
                    exscore_team1 = int(inputNumber(f"Enter the score for {team1} after extra time: "))
                if exscore_team1 > exscore_team2:
                    winners.append(team1)
                    print(f"{team1} defeats {team2} {exscore_team1}-{exscore_team2}!\n")
                elif exscore_team2 > exscore_team1:
                    winners.append(team2)
                    print(f"{team2} defeats {team1} {exscore_team2}-{exscore_team1}!\n")
                else:
                    print("Match goes to a penalty shootout")
                    penscore_team2 = int(inputNumber(f"Enter the score for {team2} after penalties: "))
                    penscore_team1 = int(inputNumber(f"Enter the score for {team1} after penalties: "))
                    while penscore_team2 == penscore_team1:
                        penscore_team2 = int(inputNumber(f"Enter the score for {team2} after penalties: "))
                        penscore_team1 = int(inputNumber(f"Enter the score for {team1} after penalties: "))
                    if penscore_team1 > penscore_team2:
                        winners.append(team1)
                        print(f"{team1} defeats {team2} {penscore_team1}-{penscore_team2} on penalties!\n")
                    else:
                        winners.append(team2)
                        print(f"{team2} defeats {team1} {penscore_team2}-{penscore_team1} on penalties!\n")
            replaynumber += 1


    time.sleep(2)
    
    print("Round Winners")
    print("--------------")
    time.sleep(1)
    for i in range(0, len(winners)):
        team1 = winners[i]
        print(f"{team1}")
    print("\n")
    return winners
    time.sleep(2)

def main():
    teams = ["Barnsley (3)", "Blackpool (3)", "Bolton Wanderers (3)", "Bristol Rovers (3)", "Burton Albion (3)", "Cambridge United (3)", "Carlisle United (3)", "Charlton Athletic (3)",
            "Cheltenham Town (3)", "Derby County (3)", "Exeter City (3)", "Fleetwood Town (3)", "Leyton Orient (3)", "Lincoln City (3)", "Northampton Town (3)", "Oxford United (3)",
             "Peterborough United (3)", "Portsmouth (3)", "Port Vale (3)", "Reading (3)", "Shrewsbury Town (3)", "Stevenage (3)", "Wigan Athletic (3)", "Wycombe Wanderers (3)",
            "Accrington Stanley (4)", "AFC Wimbledon (4)", "Barrow (4)", "Bradford City (4)", "Colchester United (4)", "Crawley Town (4)", "Crewe Alexandra (4)", "Doncaster Rovers (4)",
            "Forest Green Rovers (4)", "Gillingham (4)", "Grimsby Town (4)", "Harrogate Town (4)", "Mansfield Town (4)", "Milton Keynes Dons (4)", "Morecambe (4)", "Newport County (4)",
            "Notts County (4)", "Salford City (4)", "Stockport County (4)", "Sutton United (4)", "Swindon Town (4)", "Tranmere Rovers (4)", "Walsall (4)", "Wrexham (4)",
        "Rochdale (5)", "Hartlepool United (5)", "Hereford (6)", "South Shields (7)", "Boreham Wood (5)", "Eastleigh (5)", "Maidenhead United (5)", "Dagenham & Redbridge (5)",
        "Solihull Moors (5)", "AFC Fylde (6)", "Farnborough (6)", "Taunton Town (6)", "Ebbsfleet United (6)", "Chippenham Town (6)", "Buxton (6)", "Merthyr Town (7)",
        "Coalville Town (7)", "Weymouth (6)", "King's Lynn Town (6)", "Gateshead (5)", "Oxford City (6)", "Needham Market (7)", "Chelmsford City (6)", "Chesterfield (5)",
        "Alvechurch (7)", "Oldham Athletic (5)", "Curzon Ashton (6)", "Torquay United (5)", "Bracknell Town (7)", "Woking (5)", "Aldershot Town (5)", "Barnet (5)"]
    thirdroundteams = ["Arsenal (1)", "AFC Bournemouth (1)", "Aston Villa (1)", "Brentford (1)", "Brighton & Hove Albion (1)", "Burnley (1)", "Chelsea (1)", "Crystal Palace (1)",
             "Everton (1)", "Fulham (1)", "Liverpool (1)", "Luton Town (1)", "Manchester City (1)", "Manchester United (1)", "Newcastle United (1)", "Nottingham Forest (1)", 
             "Sheffield United (1)", "Tottenham Hotspur (1)", "West Ham United (1)", "Wolverhampton Wanderers (1)", "Birmingham City (2)", "Blackburn Rovers (2)", "Bristol City (2)", "Cardiff City (2)",
            "Coventry City (2)", "Huddersfield Town (2)", "Hull City (2)", "Ipswich Town (2)", "Leeds United (2)", "Leicester City (2)", "Middlesbrough (2)", "Millwall (2)",
            "Norwich City (2)", "Plymouth Argyle (2)", "Preston North End (2)", "Queens Park Rangers (2)", "Rotherham United (2)", "Sheffield Wednesday (2)", "Southampton (2)", "Stoke City (2)",
            "Sunderland (2)", "Swansea City (2)", "Watford (2)", "West Bromwich Albion (2)"]
    
    print("FA CUP TOURNAMENT SIMULATOR")
    print("----------------------------")
    time.sleep(1)
    print("""
        Welcome to the FA Cup Simulator! Here is a simulation of the oldest association football tournament 
        in the world, 'The Football Association Challenge Cup'. In the FA Cup, teams from all the different tiers
        and divisions of English football compete in a knockout elimination tournament.

        Here is a little program designed to simulate the FA Cup, starting from the 1st Round
        with teams from the lower leagues, onto the 3rd Round when the top teams enter the competition.
        You can enter the scores for the matches that have been drawn, and determine who ends up the champion
        based on your scores. There might be a few surprises and upsets of bigger teams, this is the magic of the
        FA Cup at they say! I hope you will have fun with the program.""")
    time.sleep(3)
    input("\n Press any key to begin the simulation: ")
    print("\n")
    time.sleep(2)
    round_number = 1
    while len(teams) > 1:
        random.shuffle(teams)
        if round_number == 1:
            print("1st Round")
            print("--------------")
            time.sleep(2)
            draw_round(teams)
        if round_number == 2:
            print("2nd Round")
            print("--------------")
            time.sleep(2)
            draw_round(teams)            
        if round_number == 3:
            teams = teams + thirdroundteams
            print("3rd Round")
            print("--------------")
            time.sleep(2)
            draw_round(teams)
        if round_number == 4:
            print("4th Round")
            print("--------------")
            time.sleep(2)
            draw_round(teams)
        if round_number == 5:
            print("5th Round")
            print("--------------")
            time.sleep(2)
            draw_round(teams)
        if len(teams) == 8:
            print("Quarter-Finals")
            print("--------------")
            time.sleep(2)
            draw_round(teams)
        if len(teams) == 4:
            print("Semi-Finals")
            print("--------------")
            time.sleep(2)
            draw_round(teams)
        if len(teams) == 2:
            print("Final")
            print("--------------")
            print("\n")
            time.sleep(2)
        teams = simulate_round(teams)
        round_number += 1
        time.sleep(5)
    
    if len(teams) < 2:
        print(f"Winner of the tournament: {teams[0]}!")
        print("\n")
        print("Thanks for playing!")
        while True:
            play_again = input("Would you like to play again! Type Y or N: ")
            if play_again.lower() == 'y':
                print("\n")
                main()
            elif play_again.lower() == 'n':
                print("No problem, enjoy the rest of your day!")
                time.sleep(3)
                break
            else:
                print("Type Y or N: ")
            
            
    
if __name__ == "__main__":
    main()
    