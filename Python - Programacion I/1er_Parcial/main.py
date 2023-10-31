from Equipo import Equipo
import re as regex
from eng_strings import menu_initial_mensage, mm_save_stats, mm_search_by_name

if __name__ == '__main__':
    team = Equipo('dream_team.json')

    flag = True
    while(flag):
        desired_option = 0
        digit_pattern = r'\b\d\b'
        name_pattern = r'<((?:[a-z]+|\s)*)>'
        menu_initial_mensage()
        try:
            desired_option = int(input())
        except ValueError as Error:
            print(f'Handled Error\n{Error}\n')
        match desired_option:
            case 1:
                team.print_players()
                input('Press enter key to continue...\n')
            case 2:
                optional = 'No'
                try:
                    chosen_player = int(input('Please, select a player by index\n'))
                    if regex.match(digit_pattern, str(chosen_player)):
                        print(team.players[chosen_player])
                        input('Press enter key to continue...\n')
                except ValueError as Error:
                    print(f'Handled Error\n{Error}\n')
                mm_save_stats()
                optional = input()
                if(optional.capitalize() == 'Yes'):
                    team.save_player_stats(chosen_player)
                    input('Saved...\nPress enter key to continue...\n')
            case 3:
                mm_search_by_name()
                try:
                    input_value = str(input())
                    team.search_player_by_name(input_value)
                except ValueError as Error:
                    print(f'Handled Error\n{Error}\n')
                input('Press enter key to continue...\n')
            case 4:pass
            case 5:pass
            case 6:
                flag = False