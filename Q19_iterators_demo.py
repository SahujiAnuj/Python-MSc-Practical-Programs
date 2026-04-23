# Program 19: Demonstrate the use of Iterators

# 1. Using built-in iterator on a list
my_list = [10, 20, 30, 40]
my_iter = iter(my_list)

print("Iterating using next() function:")
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

# 2. Custom Iterator Class
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 5:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

print("\nIterating using a Custom Class (1 to 5):")
my_class = MyNumbers()
my_iterator = iter(my_class)

for x in my_iterator:
    print(x)
