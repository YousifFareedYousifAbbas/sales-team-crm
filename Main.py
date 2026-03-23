from Show_Salesman_report import team_stat
from Search_Salesman import sales_report
from Update_or_Delete_salesperson import updat_or_delete
from Add_salesman import sales_person

def menu():
    team = {}
    while True:
        print("\nSales Team CRM")
        print("1 Add salesperson")
        print("2 Update/Delete salesperson")
        print("3 Reports & Statistics")
        print("4 Exit")

        choice = input("Choose option: ")

        if choice == "1":
            sales_person(team)
        elif choice == "2" :
            updat_or_delete(team)
        elif choice == "3" :
            team_stat(team)
        elif choice == "4" : 
            break
menu()