# only the last ones. That's a bit boring :(

from random import randint

truth = "Brendan Gleeson is really great Irish actor"
print(f"Task 2: {truth[2]}", end="\n---------------------\n")
print(f"Task 3: {truth[-2]}", end="\n---------------------\n")
print(f"Task 4: {truth[:5]}", end="\n---------------------\n")
print(f"Task 5: {truth[:-2]}", end="\n---------------------\n")
print(f"Task 6: {truth[::2]}", end="\n---------------------\n")
print(f"Task 7: {truth[1::2]}", end="\n---------------------\n")
print(f"Task 8: {truth[::-1]}", end="\n---------------------\n")
print(f"Task 9: {truth[::-2]}", end="\n---------------------\n")
print(f"Task 10: {len(truth)}", end="\n\n-------------------------------\n\n")

# Now it's about lists

list_1 = [randint(-20, 20) for _ in range(50)]
print("List 1: ", list_1)
print(f"Task 1:\nMin = {min(list_1)}; Max = {max(list_1)}")

uniq_set = set()
bad_elements = set()
for elem in list_1:  # a bit weird but fast way to find unique elements
    if elem in uniq_set:
        bad_elements.add(elem)
    else:
        uniq_set.add(elem)

print(f"Task 4:\nThis elements an't unique: {bad_elements}", end="\n\n")

binary_1 = [0 if i % 2 == 0 else 1 for i in range(50)]
binary_2 = [1] + [0]*48 + [1]

print(f"Task 2: {binary_1}", end="\n\n")
print(f"Task 3: {binary_2}", end="\n-------------------\n")


# The last one

print(f"Here is the string: {truth}")
center = len(truth)//2
print(f"Final task: {truth[center - 2: center + 2]}")