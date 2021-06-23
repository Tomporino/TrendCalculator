
import os

import os

clear = lambda: os.system('cls')


def main_menu():
    menu_list = ['Calculate Price', 'Quit']
    while True:
        clear()
        for i, x in enumerate(menu_list, 1):
            print(f'{i}. {x}')
        option = input(':')
        if option in [ f'{x}' for x in range(0, len(menu_list)+1)]:
            if option == f'{len(menu_list)}':
                quit()

def main():
    main_menu()


if __name__ == '__main__':
    main()
    
