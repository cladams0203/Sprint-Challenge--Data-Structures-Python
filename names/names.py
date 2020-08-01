import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# -----------------my improved solution--------------
start_time2 = time.time()
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def insert(self, value):
        if self.value > value:
            if self.left == None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        if self.value <= value:
            if self.right == None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
    def contains(self, target):
        if (self.value == target):
            return True
        if (self.value > target):
            if (self.left == None):
                return False
            if (self.left.value == target):
                return True
            else:
                return self.left.contains(target)
        if (self.value <= target):
            if (self.right == None):
                return False
            if (self.right.value == target):
                return True
            else:
                return self.right.contains(target)

name_tree = BSTNode(names_1[0])
duplicates2 = []
for i in names_1:
    name_tree.insert(i)

for i in names_2:
    if name_tree.contains(i):
        duplicates2.append(i)

end_time2 = time.time()
print (f"{len(duplicates2)} duplicates:\n\n{', '.join(duplicates2)}\n\n")
print (f"runtime: {end_time2 - start_time2} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

#---------Stretch with a Dictionary-------------
start_time3 = time.time()

name_dictionary = {}
duplicates3 = []
for i in names_1:
    name_dictionary[i] = True
for i in names_2:
    if i in name_dictionary:
        duplicates3.append(i)

end_time3 = time.time()

print (f"{len(duplicates3)} duplicates:\n\n{', '.join(duplicates3)}\n\n")
print (f"runtime: {end_time3 - start_time3} seconds")
