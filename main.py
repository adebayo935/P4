from game.views.asks import menu, reports
from game.controlers import create_tournament


def main():
    choice = menu()
    if int(choice) == 1:
        create_tournament()
    elif int(choice) == 2:
        reports()


main()
