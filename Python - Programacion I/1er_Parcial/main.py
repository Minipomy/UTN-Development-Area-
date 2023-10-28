from Equipo import Equipo


if __name__ == '__main__':
    team = Equipo('dream_team.json')

    team.get_players_position()
    team.select_player()