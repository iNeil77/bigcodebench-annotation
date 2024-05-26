from random import choice
import numpy as np
import pandas as pd


# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTIES_COSTS = [100, 200, 300, 400, 500]


def f_473(goals, penalties, teams=TEAMS, penalties_costs=PENALTIES_COSTS):
    """
    Generates a performance report DataFrame for teams, detailing goals and penalties. For each team, the function fetches
    goal and penalty counts, calculates 'Penalties Cost' using a random multiplier from a predefined list, and computes
    a 'Performance Score' as the non-negative difference between goals and penalties. Return a Dataframe with colomns 'Team',
    'Goals', 'Penalties', 'Penalties Cost' and 'Performance Score'.

    Parameters:
    - goals (dict): Team names as keys, numbers of goals scored as values.
    - penalties (dict): Team names as keys, numbers of penalties incurred as values.
    - teams (list, optioanl): input teams. Default value is ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
    - penalties_costs (list, optional): input penalties_costs. Default value is [100, 200, 300, 400, 500].

    Returns:
    - pd.DataFrame: DataFrame with Team, Goals, Penalties, Penalties Cost, Performance Score.

    Requirements:
    - pandas
    - numpy
    - random.choice

    Example:
    >>> goals = {'Team A': 3, 'Team B': 2}
    >>> penalties = {'Team A': 1, 'Team B': 0}
    >>> report = f_473(goals, penalties)
    """
    report_data = []
    for team in teams:
        team_goals = goals.get(team, 0)
        team_penalties = penalties.get(team, 0)
        penalties_cost = team_penalties * choice(penalties_costs)
        performance_score = np.max([0, team_goals - team_penalties])
        report_data.append({
            'Team': team,
            'Goals': team_goals,
            'Penalties': team_penalties,
            'Penalties Cost': penalties_cost,
            'Performance Score': performance_score
        })

    report_df = pd.DataFrame(report_data)
    return report_df


import unittest
from unittest.mock import patch


class TestCases(unittest.TestCase):
    @patch(__name__ + '.choice', return_value=400)
    def test_goals_greater_than_penalties(self, mock_choice):
        goals = {'Team A': 4, 'Team B': 2, 'Team C': 0, 'Team D': 0, 'Team E': 0}
        penalties = {'Team A': 1, 'Team B': 1, 'Team C': 0, 'Team D': 0, 'Team E': 0}
        expected_data = {
            'Team': TEAMS,
            'Goals': [4, 2, 0, 0, 0],
            'Penalties': [1, 1, 0, 0, 0],
            'Penalties Cost': [400, 400, 0, 0, 0],  # Mocked value is reflected here
            'Performance Score': [3, 1, 0, 0, 0]  # Assuming Performance Score is Goals - Penalties
        }
        expected_df = pd.DataFrame(expected_data)
        result_df = f_473(goals, penalties)
        pd.testing.assert_frame_equal(result_df.reset_index(drop=True), expected_df.reset_index(drop=True))

    @patch(__name__ + '.choice', return_value=200)
    def test_some_teams_missing(self, mock_choice):
        goals = {'Team A': 2, 'Team E': 5}
        penalties = {'Team A': 0, 'Team E': 3}
        expected_data = {
            'Team': TEAMS,
            'Goals': [2, 0, 0, 0, 5],
            'Penalties': [0, 0, 0, 0, 3],
            'Penalties Cost': [0, 0, 0, 0, 600],
            'Performance Score': [2, 0, 0, 0, 2]
        }
        expected_df = pd.DataFrame(expected_data)
        result_df = f_473(goals, penalties)
        pd.testing.assert_frame_equal(result_df, expected_df)

    @patch(__name__ + '.choice', return_value=500)
    def test_penalties_greater_than_goals(self, mock_choice):
        goals = {'Team B': 1, 'Team D': 2}
        penalties = {'Team B': 3, 'Team D': 5}
        expected_data = {
            'Team': TEAMS,
            'Goals': [0, 1, 0, 2, 0],
            'Penalties': [0, 3, 0, 5, 0],
            'Penalties Cost': [0, 1500, 0, 2500, 0],
            'Performance Score': [0, 0, 0, 0, 0]
        }
        expected_df = pd.DataFrame(expected_data)
        result_df = f_473(goals, penalties)
        pd.testing.assert_frame_equal(result_df, expected_df)

    @patch(__name__ + '.choice', return_value=300)
    def test_all_teams_penalty(self, mock_choice):
        goals = {'Team A': 0, 'Team B': 0, 'Team C': 0, 'Team D': 0, 'Team E': 0}
        penalties = {'Team A': 2, 'Team B': 1, 'Team C': 3, 'Team D': 1, 'Team E': 4}
        expected_penalties_cost = [penalty * mock_choice.return_value for penalty in penalties.values()]
        expected_data = {
            'Team': list(goals.keys()),  # The list of teams from the goals dictionary keys
            'Goals': list(goals.values()),  # The list of goals from the goals dictionary values
            'Penalties': list(penalties.values()),  # The list of penalties from the penalties dictionary values
            'Penalties Cost': expected_penalties_cost,
            'Performance Score': [0] * len(TEAMS)  # A list of zeros for performance score
        }
        expected_df = pd.DataFrame(expected_data)
        result_df = f_473(goals, penalties)
        pd.testing.assert_frame_equal(result_df.reset_index(drop=True), expected_df.reset_index(drop=True))

    @patch(__name__ + '.choice', return_value=100)
    def test_empty_goals_and_penalties(self, mock_choice):
        goals = {}
        penalties = {}
        expected_data = {
            'Team': TEAMS,
            'Goals': [0, 0, 0, 0, 0],
            'Penalties': [0, 0, 0, 0, 0],
            'Penalties Cost': [0, 0, 0, 0, 0],
            'Performance Score': [0, 0, 0, 0, 0]
        }
        expected_df = pd.DataFrame(expected_data)
        result_df = f_473(goals, penalties)
        pd.testing.assert_frame_equal(result_df, expected_df)


    @patch(__name__ + '.choice', return_value=300)
    def test_no_penalties(self, mock_choice):
        goals = {'Team A': 3, 'Team B': 2}
        penalties = {'Team A': 0, 'Team B': 0}
        expected_data = {
            'Team': ['Team A', 'Team B'] + ['Team C', 'Team D', 'Team E'],
            'Goals': [3, 2] + [0, 0, 0],
            'Penalties': [0, 0] + [0, 0, 0],
            'Penalties Cost': [0, 0] + [0, 0, 0],
            'Performance Score': [3, 2] + [0, 0, 0]
        }
        expected_df = pd.DataFrame(expected_data)
        result_df = f_473(goals, penalties)
        pd.testing.assert_frame_equal(result_df, expected_df)


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()