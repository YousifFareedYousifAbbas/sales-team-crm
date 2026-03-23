def updat_or_delete(team):

    action = input('For update type "U" , For Salesman delete type "D": ')
    while action != "U" and action != 'D':
        print("Invalid option")
        action = input('Please enter "U" or "D": ')

    name_old = input('Enter the Salesman Name: ')
    while name_old not in team:
        name_old = input('please Enter an existing Salesman: ')
    if action == 'U':
        updated_leads = int(input('Enter the updated leads: '))
        updated_sales = int(input('Enter the updated Sales: '))
        team[name_old]["leads"] = updated_leads
        team[name_old]["sales"] = updated_sales

        print(f'{name_old} -> leads: {updated_leads} | Sales: {updated_sales}')
    else:
        del team[name_old]
        print(f'{name_old} is Deleted successfully')
        