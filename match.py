try:
    matched = input('Input command: ').split(' ')
except ValueError:
    matched = None

match matched:
    case ['north']:
        print('North we go!')
    case ['south']:
        print('South we go!')
    case ['west'] | ['east']:
        print('Let\'s go south or north!')
    case ['go', argument]:
        direction = argument
        print(f'We go {direction}.')
    case _:
        print('Where do you want to go?')

