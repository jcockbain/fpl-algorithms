# FPL-Algorithms ⚽

Algorithms used to assist with [Fantasy Premier League](https://fantasy.premierleague.com/).

Uses this [FPL Python Wrapper](https://fpl.readthedocs.io/en/latest/).

## Scripts

### Select Team

Uses a [bounded-knapsack](https://en.wikipedia.org/wiki/Knapsack_problem) style recursive function to compare possible player combinations based on of the valid metrics.

#### Usage

```bash
python select_team.py {defenders} {midfielders} {attackers} {budget} {metric}

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