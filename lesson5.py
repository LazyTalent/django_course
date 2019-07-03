import numpy as np
import pandas as pd
import calendar


def f1():  # task 1
    pass


f2 = lambda x: 2*x  # task 2

f3 = lambda x: "Yes" if x % 2 == 0 else "No"  # task 3

f4 = lambda x, y: "Yes" if x > 10 else "No"  # task 4

f5 = lambda x, y: x % y  # task 5


def my_decor(some_func):  # task 6
    def wrapper(data):
        print(f"Function {some_func.__name__} has started\n--------------------------")
        some_func(data)
        print(f"\nFunction {some_func.__name__} has finished\n---------------------------")

    return wrapper


@my_decor
def f6(data):
    attachment = pd.DataFrame(data, columns=["Avoidant", "Anxious", "Fearful", "Secure"],
                              index=["Toni Stark", "Anakin Skywalker", "Will Hunting", "Captain America"])
    print(attachment)


f7 = lambda x: round((np.sin(x))**2, 4)  # task 7

f8 = lambda x: True if x < 0 else False  # task 8


def f9(x):  # task 9
    x *= 10


def f10(random_list):  # task 10
    # return min(random_list), max(random_list) - it would be much more logical
    my_max = -1e6
    my_min = 1e6
    for elem in random_list:
        if elem > my_max:
            my_max = elem
        if elem < my_min:
            my_min = elem

    return my_min, my_max


f11 = lambda year: calendar.isleap(year)  # task 11


def season(month):  # task 12
    if month in range(3, 6):
        return "Spring"
    elif month in range(6, 9):
        return "Summer"
    elif month in range(9, 12):
        return "Fall"
    else:
        return "Winter"


def date(day, month, year):  # task 13
    try:
        calendar.weekday(year, month, day)
        return True
    except ValueError:
        return False


def fix_list(broken_list):  # task 14
    fix_func = lambda x: True if (isinstance(x, int) or isinstance(x, float)) and not isinstance(x, bool) else False
    broken_list = list(filter(fix_func, broken_list))
    broken_list = sorted(broken_list)
    return broken_list


def main():
    data = np.eye(4)
    random_list = np.random.randint(low=-10, high=10, size=20)
    random_year = np.random.randint(low=0, high=2500)
    random_month = np.random.randint(low=1, high=13)
    random_date = {"day": np.random.randint(low=-10, high=38),
                   "month": np.random.randint(low=-10, high=20),
                   "year": np.random.randint(low=-1000, high=2200)}

    x = 8
    y = 3
    task_14_list = [16, -17, 2, 78.7, False, False, {'True': True}, 555, 12, 23, 42, 'DD']
    f1()
    print(f"Task 2: x = {x};  f(x) = {f2(x)}")
    print(f"Task 3: x = {x};  f(x) = {f3(x)}")
    print(f"Task 4: x = {x}; y = {y}; f(x) = {f4(x, y)}")
    print(f"Task 5: x = {x}; y = {y}; f(x) = {f5(x, y)}")
    print("Task 6:")
    f6(data)
    print(f"Tasks 7&8:\nIt's our list:\n{random_list}")
    print(f"This is the square of the sine of all numbers:\n{list(map(f7, random_list))}")
    print(f"There are all negative values from our list :\n{list(filter(f8, random_list))}")
    print("--------------------------------\nTask 9:")
    print("Functions f1-f5 are pure, f9 and fix_list not\n")
    print(f"Task 10: Our list is the same as before. Min = {f10(random_list)[0]}, Max = {f10(random_list)[1]}")
    print(f"Task 11: {random_year} - our year. It is {'not leap' if not f11(random_year) else 'leap'}")
    print(f"Task 12: {random_month} - the number of our month. It is {season(random_month)}")
    print(f"\n-----------------------------------\nTask 13:")
    print(f"Random date:\n{random_date}")
    print(f"It's {'correct' if date(**random_date) else 'incorrect'} date")
    print("\n---------------------------------\n")
    print(f"Task 14:\nOur list:\n {task_14_list}")
    print(f"The output:\n {fix_list(task_14_list)}")


if __name__ == '__main__':
    main()

