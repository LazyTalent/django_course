a, b, c = list(map(int, input("Please, enter 3 numbers here:\n").split()))

# task1
uniq_set = {a, b, c}
if len(uniq_set) == 3:
    print("Error", end="\n\n\n")
else:
    print("Yes", end="\n\n\n")

# task2
sum_list = [a + b, a + c, b + c]
flaq = False
for s in sum_list:
    if s in (a, b, c):
        print("Yes", end="\n\n\n")
        flaq = True
        break
if not flaq:
    print("No", end="\n\n\n")

# task3
print(f"Task 3: {sum(range(15))} \n\n\n")


# task4

is_weekend = lambda x: "weekend" if x else "weekday"

my_calendar = {"Monday": (0, False),
               "Tuesday": (1, False),
               "Wednsday": (2, False),
               "Thursday": (3, False),
               "Friday": (4, False),
               "Saturday": (5, True),
               "Sunday": (6, True)}
for day in my_calendar.keys():
    print(f"Day number {my_calendar[day][0]} is {day}; It's {is_weekend(my_calendar[day][1])}")

