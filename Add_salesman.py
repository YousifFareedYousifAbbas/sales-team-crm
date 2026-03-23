def sales_person(team):

    number = int(input('how many sales persons?'))
    for x in range(number):
        name = input("Enter salesperson name: ")
        while name in team:
            print('Salesperson already exists')
            name = input('inter another name:')
        
        leads = int(input("Enter leads: "))
        sales = int(input("Enter sales: "))
        team[name] = {"leads": leads, "sales": sales}

    print('Added')
    print(team)
