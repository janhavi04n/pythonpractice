import datetime

current_year = datetime.date.today().year
years = [yr for yr in range(1900, current_year)]

print(f"Printing all leap years between 1900 and {current_year}")
for yr in years:
    if yr % 4 == 0 and (yr % 400 == 0 or yr % 100 != 0):
        print(f"{yr}")
