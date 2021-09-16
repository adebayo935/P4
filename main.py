from dev.views.asks import menu, reports
from dev.controlers import create_tournament


choice = menu()
if int(choice) == 1:
    create_tournament()
elif int(choice) == 2:
    reports()
