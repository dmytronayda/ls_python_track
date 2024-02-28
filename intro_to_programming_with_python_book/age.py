user_age = int(input("What's your age?\n"))
years_from_now = 10

for i in range(4):
    print(f"In {years_from_now} years, you will be {user_age + years_from_now}")
    years_from_now += 10;