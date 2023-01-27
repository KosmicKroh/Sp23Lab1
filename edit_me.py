# Linear Search for Max in List - Author: Justin Kroh
# I am adding a comment now! Let's see what happens.
def FindMax(lst):
    """return the maximum element"""

    current_max = lst[0]

    for i in range(len(lst)-1):
        if (lst[i+1]>current_max):
            current_max = lst[i+1]

    return current_max

test_list = [17*i % 2023 for i in range(10000)]

print(FindMax(test_list))
