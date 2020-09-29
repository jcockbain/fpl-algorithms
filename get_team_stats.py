from fpl import FPL
import argparse
import aiohttp
import asyncio
from prettytable import PrettyTable


async def main(email, password, team_id):
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        await fpl.login(email, password)
        user = await fpl.get_user(3415098)
        team = await user.get_team()

        players = []
        for player in team:
            players.append(await fpl.get_player(player["element"]))

    form_table = PrettyTable()
    players.sort(key=lambda x: float(x.form), reverse=True)
    form_table.field_names = ["Player", "Form", "Total Points", "PP90", "ict_index"]

    for player in players:
        row = [
            player.web_name,
            player.form,
            player.total_points,
            round(player.pp90, 2),
            player.ict_index,
        ]
        form_table.add_row(row)

    print(form_table)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("Email", type=str)
    parser.add_argument("Password", type=str)
    parser.add_argument("team_id", type=int)
    args = parser.parse_args()
    asyncio.run(main(args.Email, args.Password, args.team_id))
