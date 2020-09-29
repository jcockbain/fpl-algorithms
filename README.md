# FPL-Algorithms ⚽

Algorithms used to assist with [Fantasy Premier League](https://fantasy.premierleague.com/).

Uses this [FPL Python Wrapper](https://fpl.readthedocs.io/en/latest/).

## Scripts

### Select Team

Uses a [bounded-knapsack](https://en.wikipedia.org/wiki/Knapsack_problem) style recursive function to compare possible player combinations based on any of the valid metrics.

```bash
python select_team.py {goalkeepers} {defenders} {midfielders} {attackers} {budget} {metric}

# e.g
python select_team.py 2 5 5 3 100 form

# example output
Max form
164.0
Martínez  Alisson
Konsa  Castagne  Mings  Gabriel  Justin
De Bruyne  Son  Zaha  Costa  Klich
Calvert-Lewin  Kane  Bamford
```

#### Valid Metrics

| Player Metric       | Command Line Argument |
|---------------------|-----------------------|
| Form                | form                  |
| Value Season        | value_season          |
| ICT Index           | ict_index             |
| Total Points        | total_points          |
| Goals Scored        | goals_scored          |
| Seasons Cost Change | cost_change_start     |

### Get Team Stats

Get statistics for each player in the team given bt input `team_id`, ordered by form.

Requires being logged in, in this case this is handled by the command line arguments.
Environment variables can also be set for this purpose, see [FPL Python Wrapper](https://fpl.readthedocs.io/en/latest/) for more info on authentication.

```bash
python get_team_stats.py {email} {password} {team_id}

# example output
+------------------+------+--------------+-------+-----------+
|      Player      | Form | Total Points |  PP90 | ict_index |
+------------------+------+--------------+-------+-----------+
|  Calvert-Lewin   | 10.3 |      31      | 11.25 |    41.7   |
|    De Bruyne     | 7.5  |      15      |  7.5  |    28.4   |
|    Fernandes     | 7.0  |      14      |  7.0  |    24.9   |
|      Justin      | 5.7  |      17      |  5.67 |    15.5   |
|     Pereira      | 5.7  |      17      |  6.12 |    18.4   |
|      James       | 5.3  |      16      |  5.33 |    28.1   |
| Alexander-Arnold | 5.0  |      15      |  5.04 |    18.4   |
|     Mitrović     | 5.0  |      15      |  6.52 |    22.6   |
|      Adams       | 2.7  |      8       |  3.01 |    18.1   |
|     McCarthy     | 2.7  |      8       |  2.67 |    5.1    |
|      Traoré      | 2.3  |      7       |  2.61 |    11.5   |
|       Pope       | 1.5  |      3       |  1.5  |    2.5    |
|  Saint-Maximin   | 1.3  |      4       |  3.4  |    1.2    |
|     Doherty      | 1.3  |      4       |  1.41 |    12.2   |
|       Egan       | -0.7 |      -2      | -1.78 |    1.6    |
+------------------+------+--------------+-------+-----------+
```

### Fixture Difficulty Rating

> From the examples at [FPL](https://fpl.readthedocs.io/en/latest/)

Prints a table to show more detailed `Fixture Difficulty Rating` statistics about playing against each team, than are displayed on the FPL site.

This relates to the difficulty specific to position, and whether the match is to be played Home or Away.

```bash
python fixture_difficulty_rating.py

# example output
+----------------+---------+---------+--------+--------+---------+---------+---------+---------+---------+---------+
| Team           | All (H) | All (A) | GK (H) | GK (A) | DEF (H) | DEF (A) | MID (H) | MID (A) | FWD (H) | FWD (A) |
+----------------+---------+---------+--------+--------+---------+---------+---------+---------+---------+---------+
| West Ham       |   2.84  |   3.51  |  4.38  |  3.86  |   4.18  |   3.40  |   3.06  |   3.20  |   2.11  |   4.72  |
| Liverpool      |   4.88  |   4.02  |  4.38  |  4.43  |   5.0   |   4.23  |   4.88  |   3.50  |   4.78  |   4.40  |
| Fulham         |   2.36  |   1.0   |  4.38  |  3.14  |   4.54  |   1.0   |   1.0   |   1.70  |   2.11  |   4.53  |
| Sheffield Utd  |   1.0   |   1.83  |  1.0   |  2.71  |   1.0   |   1.65  |   3.55  |   3.37  |   4.78  |   4.07  |
| Chelsea        |   3.52  |   1.57  |  4.38  |  1.0   |   4.03  |   1.38  |   3.99  |   2.95  |   3.56  |   4.20  |
| Newcastle      |   4.07  |   1.76  |  4.54  |  3.29  |   4.37  |   2.28  |   4.27  |   4.01  |   4.26  |   2.80  |
| Man Utd        |   3.62  |   2.52  |  4.69  |  4.14  |   4.66  |   3.32  |   3.52  |   1.80  |   3.22  |   4.60  |
| Southampton    |   2.80  |   2.21  |  3.15  |  4.43  |   3.30  |   4.25  |   3.36  |   2.24  |   4.56  |   1.0   |
| Leicester      |   4.18  |   4.37  |  4.69  |  4.71  |   4.50  |   4.03  |   3.74  |   3.87  |   5.0   |   4.67  |
| West Brom      |   1.98  |   2.39  |  4.69  |  4.00  |   3.86  |   2.55  |   3.21  |   2.77  |   1.0   |   4.10  |
| Brighton       |   4.69  |   3.00  |  4.38  |  4.43  |   4.77  |   2.91  |   4.88  |   2.88  |   4.85  |   4.50  |
| Everton        |   4.07  |   4.68  |  4.23  |  5.0   |   4.35  |   5.0   |   4.21  |   3.06  |   4.78  |   4.80  |
| Spurs          |   4.14  |   2.94  |  5.0   |  2.71  |   4.89  |   2.43  |   4.42  |   4.38  |   3.52  |   4.40  |
| Crystal Palace |   4.32  |   3.98  |  4.69  |  4.43  |   4.77  |   3.37  |   4.01  |   4.59  |   4.78  |   4.44  |
| Aston Villa    |   5.0   |   5.0   |  4.69  |  4.43  |   4.92  |   4.05  |   5.0   |   5.0   |   4.78  |   5.0   |
| Arsenal        |   3.55  |   4.49  |  4.54  |  4.71  |   3.63  |   3.93  |   3.79  |   4.59  |   4.85  |   4.50  |
| Leeds          |   3.37  |   3.79  |  4.23  |  4.71  |   3.95  |   4.01  |   2.91  |   4.43  |   4.89  |   3.50  |
| Burnley        |   2.47  |   1.84  |  4.38  |  3.29  |   2.94  |   1.22  |   2.68  |   3.78  |   4.56  |   4.20  |
| Man City       |   3.89  |   2.71  |  4.08  |  4.43  |   4.54  |   3.96  |   3.97  |   1.70  |   3.89  |   3.40  |
| Wolves         |   2.58  |   2.67  |  3.77  |  4.43  |   3.46  |   3.74  |   1.95  |   1.0   |   4.47  |   4.00  |
+----------------+---------+---------+--------+--------+---------+---------+---------+---------+---------+---------+
```
