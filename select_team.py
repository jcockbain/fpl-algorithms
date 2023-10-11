import aiohttp
from prettytable import PrettyTable
import asyncio
import argparse

from fpl import FPL


def get_number_of_players_to_search(positions):
    total = sum(positions)
    players_to_search = [int(25 * (pos / total)) for pos in positions]
    return players_to_search


def get_value_from_metric(player, metric):
    if metric == "form":
        return float(player.form)
    elif metric == "value_season":
        return float(player.value_season)
    elif metric == "ict_index":
        return float(player.ict_index)
    elif metric == "total_points":
        return float(player.total_points)
    elif metric == "goals_scored":
        return float(player.goals_scored)
    elif metric == "dreamteam_count":
        return float(player.dreamteam_count)
    elif metric == "cost_change_start":
        return float(player.cost_change_start)
    else:
        raise Exception("Invalid metric")


async def main(positions, budget, metric):
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        players = await fpl.get_players()

    GOALKEEPERS, DEFENDERS, MIDFIELDERS, ATTACKERS = positions

    players_to_search = get_number_of_players_to_search(positions)

    performers = sorted(
        players, key=lambda x: get_value_from_metric(x, metric), reverse=True
    )

    top_keepers, top_defenders, top_midfielders, top_attackers = [], [], [], []
    positions = [top_keepers, top_defenders, top_midfielders, top_attackers]
    for player in performers:
        positions[player.element_type - 1].append(player)

    top_performers = (
        top_keepers[: players_to_search[0]]
        + top_defenders[: players_to_search[1]]
        + top_midfielders[: players_to_search[2]]
        + top_attackers[: players_to_search[3]]
    )

    keepers, defenders, midfielders, attackers, max_team = [], [], [], [], []
    max_score = 0

    def get_form_team(budget, player_idx, score):
        nonlocal max_score
        nonlocal max_team

        if player_idx == len(top_performers):
            return

        if budget < 0:
            return

        if (
            len(keepers) == GOALKEEPERS
            and len(defenders) == DEFENDERS
            and len(midfielders) == MIDFIELDERS
            and len(attackers) == ATTACKERS
            and score > max_score
        ):
            max_score = score
            max_team = [keepers[:], defenders[:], midfielders[:], attackers[:]]

        player = top_performers[player_idx]
        position = player.element_type
        cost = player.now_cost / 10
        player_score = get_value_from_metric(player, metric)

        if position == 1 and len(keepers) < GOALKEEPERS:
            keepers.append(player.web_name)
            get_form_team(
                budget - cost, player_idx + 1, score + player_score,
            )
            keepers.pop()

        elif position == 2 and len(defenders) < DEFENDERS:
            defenders.append(player.web_name)
            get_form_team(
                budget - cost, player_idx + 1, score + player_score,
            )
            defenders.pop()

        elif position == 3 and len(midfielders) < MIDFIELDERS:
            midfielders.append(player.web_name)
            get_form_team(
                budget - cost, player_idx + 1, score + player_score,
            )
            midfielders.pop()

        elif position == 4 and len(attackers) < ATTACKERS:
            attackers.append(player.web_name)
            get_form_team(
                budget - cost, player_idx + 1, score + player_score,
            )
            attackers.pop()
        get_form_team(budget, player_idx + 1, score)

    get_form_team(budget, 0, 0)

    print("Max {}".format(metric))
    print(max_score)
    for position in max_team:
        if position:
            print("  ".join(position))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("Keepers", type=int)
    parser.add_argument("Defenders", type=int)
    parser.add_argument("Midfielders", type=int)
    parser.add_argument("Attackers", type=int)
    parser.add_argument("Budget", type=int)
    parser.add_argument("Metric", type=str)

    args = parser.parse_args()
    positions = [args.Keepers, args.Defenders, args.Midfielders, args.Attackers]
    asyncio.run(main(positions, args.Budget, args.Metric))
