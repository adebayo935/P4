from views import menu, reports
from controlers import  create_tournament



choice = menu()
if int(choice) == 1:
    create_tournament()
elif int(choice) == 2:
    reports()
