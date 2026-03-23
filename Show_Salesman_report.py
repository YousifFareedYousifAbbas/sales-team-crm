def team_stat(team):

    total_leads = sum(data["leads"] for data in team.values())
    total_sales = sum(data["sales"] for data in team.values())

    max_sales = 0
    best_performer = ""

    for name, data in team.items():
        if data["sales"] > max_sales:
            max_sales = data["sales"]
            best_performer = name

    conversion = (total_sales / total_leads) * 100

    print(f"Total Leads: {total_leads}")
    print(f"Total Sales: {total_sales}")
    print(f"Best Performer: {best_performer}")
    print(f"Conversion Rate: {conversion:.2f}%")