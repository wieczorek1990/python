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
    case ['go', direction]:
        print(f'We go {direction}.')
    case [*directions]:
        print('How can we do so?')
    case _:
        print('Where do you want to go?')

