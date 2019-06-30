# task 1&2
variable_1 = 12345
variable_2 = "something extraordinary"
print(f"Task 1&2: {variable_2} and {variable_1}\n\n")

# task 3&4
a, b = list(map(int, input("Please, enter 2 integer numbers here:\n").split()))
n_min = min(a, b)
n_max = max(a, b)
number = 2 ** n_min
print(f"a + b = {a + b}\n\n")
for i in range(n_min, n_max + 1):  # It's instead of A += 5 from your's example
    print(f"2^{i} = {number}", end="; ")
    number *= 2

print("\n\n")

# task 5
print(f"a = {a}; b = {b}\n")
a, b = b, a  # wow (now wow)
print(f"a = {a}; b = {b}")


