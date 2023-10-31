def menu_initial_mensage() -> str:
    mm_message = ['Please, choose an input from the following list:\n',
                    '1.- List all Dream Team players.',
                    '2.- Show stats from a player. Allowing also to save into csv file (Optional)',
                    '3.- Search player by name.',
                    '4.- ',
                    '5.-',
                    '6.-',
                    '7.-',
                    '8.-',
                    '9.-Exit']
    for message in mm_message:
        print(message)

def mm_bad_input() -> str:
    message = f'Wrong, you enter a wrong selection. Kindly to try again'
    print(message)

def mm_save_stats() -> str:
    message = f'Save stats to CSV file? Yes/No\n'
    print(message)

def mm_search_by_name() -> str:
    message = f'Please, write down pllayer name\n'
    print(message)