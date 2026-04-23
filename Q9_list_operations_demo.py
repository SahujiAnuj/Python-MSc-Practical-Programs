# Program 09: Demonstration of List Operations in Python

def display(step, lst):
    print(f"{step:<30} → {lst}")


# ----------- INITIAL LIST -----------

lst = [30, 10, 50, 20, 40]

print("=" * 60)
print("LIST OPERATIONS DEMONSTRATION")
print("=" * 60)

display("Initial List", lst)


# ----------- OPERATIONS -----------

# Append
lst.append(60)
display("After append(60)", lst)

# Insert
lst.insert(2, 99)
display("After insert(2, 99)", lst)

# Extend
lst.extend([70, 80])
display("After extend([70,80])", lst)

# Remove
lst.remove(99)
display("After remove(99)", lst)

# Pop (last)
removed = lst.pop()
display(f"After pop() → removed {removed}", lst)

# Pop (index)
removed = lst.pop(1)
display(f"After pop(1) → removed {removed}", lst)

# Sort (ascending)
lst.sort()
display("After sort()", lst)

# Sort (descending)
lst.sort(reverse=True)
display("After sort(reverse=True)", lst)

# Reverse
lst.reverse()
display("After reverse()", lst)


# ----------- FINAL OUTPUT -----------

print("-" * 60)
print("Final List:", lst)
print("=" * 60)
