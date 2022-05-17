from datetime import datetime, timedelta

birthday_dudes = [{'name': 'Serhii', 'birthday': '1996-05-18'},
                  {'name': 'Abraham', 'birthday': '2003-05-22'},
                  {'name': 'Kolai', 'birthday': '2008-05-11'},
                  {'name': 'Mike', 'birthday': '1983-05-14'},
                  {'name': 'Wonka', 'birthday': '1994-05-24'},
                  {'name': 'Splinter', 'birthday': '1809-05-24'},
                  {'name': 'Sam', 'birthday': '1957-05-23'},
                  {'name': 'Bruce Wayne', 'birthday': '1982-05-27'}]


def birthdays_next_week(users: list) -> None:
	checked_dudes = {'Monday': [], 'Tuesday': [], 'Wednesday': [],
	                 'Thursday': [], 'Friday': []}
	today_is = datetime.now().date()
	day_of_week = today_is.weekday()
	next_monday = (today_is + timedelta(days=7 - day_of_week))
	next_friday = (today_is + timedelta(days=11 - day_of_week))
	last_saturday = (next_monday - timedelta(days=2))

	for dude in users:
		get_dude_date = dude['birthday'].split('-')
		dude_date = datetime(year=today_is.year, month=int(get_dude_date[1]), day=int(get_dude_date[2])).date()
		if last_saturday <= dude_date < next_monday:
			checked_dudes['Monday'].append(dude['name'])
		elif next_monday <= dude_date <= next_friday:
			checked_dudes[dude_date.strftime('%A')].append(dude['name'])
	for day, celebrators in checked_dudes.items():
		if not celebrators:
			continue
		else:
			str_names = ', '.join(celebrators)
			print(f"{day}: {str_names}.")


birthdays_next_week(birthday_dudes)
