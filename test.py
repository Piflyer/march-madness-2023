import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

city_data = pd.read_csv("data/Cities.csv")
conferences = pd.read_csv("data/Conferences.csv")
tourneygames = pd.read_csv("data/MConferenceTourneyGames.csv")
gamecities = pd.read_csv("data/MGameCities.csv")
massyor = pd.read_csv("data/MMasseyOrdinals.csv")
tourneyresults = pd.read_csv("data/MNCAATourneyCompactResults.csv")
tourneydetailedresults = pd.read_csv("data/MNCAATourneyDetailedResults.csv")
tourneyseeds = pd.read_csv("data/MNCAATourneySeeds.csv")
tourneyseedresutls = pd.read_csv("data/MNCAATourneySeedRoundSlots.csv")
regularseasoncompact = pd.read_csv("data/MRegularSeasonCompactResults.csv")
regularseasondetailed = pd.read_csv("data/MRegularSeasonDetailedResults.csv")
seasons = pd.read_csv("data/MSeasons.csv")
teams = pd.read_csv("data/MTeams.csv")
secondarytourneycompact = pd.read_csv("data/MSecondaryTourneyCompactResults.csv")
secondarytourneydetailed = pd.read_csv("data/MSecondaryTourneyTeams.csv")
team_conerences = pd.read_csv("data/MTeamConferences.csv")
# team_spellings = pd.read_csv("data/MTeamSpellings.csv")
sample_submission = pd.read_csv("data/SampleSubmission2023.csv")


regularseasondetailed.head()


def get_team_stats(team_id, season):
    team_stats = regularseasondetailed.loc[(regularseasondetailed["WTeamID"] == team_id) & (regularseasondetailed["Season"] == season)]
    team_stats = team_stats.append(regularseasondetailed.loc[(regularseasondetailed["LTeamID"] == team_id) & (regularseasondetailed["Season"] == season)])
    return team_stats

get_team_stats(1104, 2019)