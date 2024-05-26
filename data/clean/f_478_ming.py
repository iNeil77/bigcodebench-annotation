from random import randint, seed
import matplotlib.pyplot as plt
import pandas as pd
import re

# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000  # in dollars


def f_478(goals, penalties, rng_seed=None, teams=TEAMS):
    """
    Generate and analyze a Pandas DataFrame of football match results for multiple teams,
    incorporating random goals and penalties, then visualize the analyzed data with colomns 'Team', 'Goals',
    and 'Penalty Cost'. Penalties are converted into fines based on a predetermined penalty cost.

    Parameters:
    - goals (int): The maximum number of goals a team can score in a match.
    - penalties (int): The maximum number of penalties a team can receive in a match.
    - rng_seed (int, optional): Seed for the random number generator to ensure reproducibility. Defaults to None.
    - teams (list of str, optional): List of team names to assign players

    Returns:
    - DataFrame: A pandas DataFrame containing teams, their goals, and penalty costs, along with the original match results.

    Requirements:
    - pandas
    - matplotlib.pyplot
    - random
    - re

    Example:
    >>> analyzed_data = f_478(5, 3, rng_seed=42)
    >>> print(analyzed_data[['Team', 'Goals', 'Penalty Cost']])
         Team  Goals  Penalty Cost
    0  Team A      5             0
    1  Team B      0          2000
    2  Team C      1          1000
    3  Team D      1             0
    4  Team E      5             0
    """
    if rng_seed is not None:
        seed(rng_seed)

    match_results = []

    for team in teams:
        team_goals = randint(0, goals)
        team_penalties = randint(0, penalties)
        penalty_cost = PENALTY_COST * team_penalties
        result_string = f"({team_goals} goals, ${penalty_cost})"
        match_results.append([team, result_string])

    results_df = pd.DataFrame(match_results, columns=['Team', 'Match Result'])

    if not results_df.empty:
    # Extract goals and penalty cost from the result string
        results_df['Goals'] = results_df['Match Result'].apply(lambda x: int(re.search(r'\((\d+) goals', x).group(1)))
        results_df['Penalty Cost'] = results_df['Match Result'].apply(lambda x: int(re.search(r'\$(\d+)', x).group(1)))

        # Visualization - this part will not be tested directly in unit tests
        ax = results_df.set_index('Team')[['Goals', 'Penalty Cost']].plot(kind='bar', stacked=True)
        plt.ylabel('Counts')
        plt.title('Football Match Results Analysis')
        plt.tight_layout()
        plt.show()

    return results_df


import unittest


# Unit Tests
class TestCases(unittest.TestCase):
    def setUp(self):
        self.expected_columns = ['Team', 'Match Result', 'Goals', 'Penalty Cost']

    def test_dataframe_structure(self):
        """Test if the DataFrame contains the expected structure."""
        df = f_478(4, 2, rng_seed=1)
        self.assertListEqual(list(df.columns), self.expected_columns)

    def test_randomness_control(self):
        """Test if the rng_seed parameter controls randomness."""
        df1 = f_478(4, 2, rng_seed=42)
        df2 = f_478(4, 2, rng_seed=42)
        pd.testing.assert_frame_equal(df1, df2)

    def test_positive_goals_penalties(self):
        """Test for positive goals and penalties input."""
        df = f_478(5, 3, rng_seed=2)
        self.assertTrue((df['Goals'] >= 0).all() and (df['Goals'] <= 5).all())
        self.assertTrue((df['Penalty Cost'] % PENALTY_COST == 0).all())

    def test_zero_goals_penalties(self):
        """Test for zero goals and penalties."""
        df = f_478(0, 0, rng_seed=3)
        self.assertTrue((df['Goals'] == 0).all())
        self.assertTrue((df['Penalty Cost'] == 0).all())

    def test_no_teams(self):
        """Test function with no teams."""
        df = f_478(5, 3, rng_seed=4, teams=[])
        self.assertTrue(df.empty)


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()
