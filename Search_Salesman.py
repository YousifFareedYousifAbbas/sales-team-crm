def sales_report(team):
    option =input('Enter the Salesman name , if want show all Enter "All": ').capitalize()
    while option != "All" and option not in team:
        print('NA')
        option = input("please Enter an existing option or all: ").capitalize()
    if option == "All":
        for name, data in team.items():
            print(f'{name} -> Leads: {data["leads"]} | Sales: {data["sales"]}')
    else:
                print(f'{option} -> Leads: {team[option]["leads"]} | Sales: {team[option]["sales"]}')

