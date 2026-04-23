# Program 10: Find Second Smallest and Second Largest (Without Built-ins)

def second_largest(lst):
    if len(lst) < 2:
        return None

    largest = lst[0]
    second = None

    for num in lst[1:]:
        if num > largest:
            second = largest
            largest = num
        elif num != largest:
            if second is None or num > second:
                second = num

    return second


def second_smallest(lst):
    if len(lst) < 2:
        return None

    smallest = lst[0]
    second = None

    for num in lst[1:]:
        if num < smallest:
            second = smallest
            smallest = num
        elif num != smallest:
            if second is None or num < second:
                second = num

    return second


# ---------------- MAIN PROGRAM ----------------

print("=" * 60)
print("SECOND MIN & MAX FINDER")
print("=" * 60)

nums = list(map(int, input("Enter numbers (space-separated): ").split()))

s_min = second_smallest(nums)
s_max = second_largest(nums)

print("\n[Result]")
print("List            :", nums)
print("Second Smallest :", s_min if s_min is not None else "Not Available")
print("Second Largest  :", s_max if s_max is not None else "Not Available")

print("=" * 60)
