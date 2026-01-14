class NumberIterator:
    def _init_(self, limit):
        self.limit = limit
        self.value = 1

    def _iter_(self):
        return self

    def _next_(self):
        if self.value > self.limit:
            raise StopIteration
        current_value = self.value
        self.value += 1
        return current_value

def fibonacci_generator(n):
    a, b = 0, 1
    count = 0

    while count < n:
        yield a
        a, b = b, a + b
        count += 1



class NumberIterator:
    def _init_(self, n):      # <-- n must be here
        self.n = n
        self.current = 1

    def _iter_(self):
        return self

    def _next_(self):
        if self.current <= self.n:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration


# Using Iterator
print("Using Iterator:")
iterator_obj = NumberIterator(5)

for num in iterator_obj:
    print(num)



def number_generator(n):
    for i in range(1, n + 1):
        yield i


print("\nUsing Generator:")
for num in number_generator(5):
    print(num)







