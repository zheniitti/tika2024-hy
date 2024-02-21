# toteutus 1
import time, random
def count_even(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result
# toteutus 2
def count_even2(numbers):
    return sum(x % 2 == 0 for x in numbers)

numbers = [random.randint(0, 100000) for _ in range(1, 10**(8-1))]
start_time = time.time()
count_even2(numbers)
end_time = time.time()

print("time:", round(end_time - start_time, 2), "s")
