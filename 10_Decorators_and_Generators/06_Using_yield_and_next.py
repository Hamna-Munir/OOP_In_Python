# ================================================================
# File: 06_Using_yield_and_next.py
# Topic: Understanding yield and next() in Python Generators
# ================================================================

"""
In Python, **`yield`** and **`next()`** are two key components that define how generators work.

- The `yield` keyword is used to **pause** and **resume** function execution.
- The `next()` function is used to **retrieve the next value** from a generator.

When a generator function is called, it **does not execute immediately**.
Instead, it returns a generator object.  
When you call `next()` on that object, the function runs until it hits a `yield` statement.
It then:
    - Returns the yielded value.
    - Pauses its execution (saving its state).
    - Resumes exactly from where it left off the next time `next()` is called.
"""

# ------------------------------------------------
# 1️⃣ Basic Example: yield vs return
# ------------------------------------------------

def demo_yield():
    yield 1
    yield 2
    yield 3

gen = demo_yield()
print("Generator created:", gen)  # Output: <generator object demo_yield at 0x...>

print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3

# Once all values are yielded, calling next() again raises StopIteration
try:
    print(next(gen))
except StopIteration:
    print("No more values. Generator is exhausted.")


# ------------------------------------------------
# 2️⃣ Using yield in a Loop
# ------------------------------------------------
"""
The generator pauses at each yield and resumes from that exact point.
"""

def countdown(n):
    print("Countdown starting...")
    while n > 0:
        yield n
        n -= 1

cd = countdown(3)
print(next(cd))  # Output: 3
print(next(cd))  # Output: 2
print(next(cd))  # Output: 1
try:
    print(next(cd))
except StopIteration:
    print("Countdown finished!")


# ------------------------------------------------
# 3️⃣ Understanding Execution Flow
# ------------------------------------------------
"""
Each time `next()` is called:
    - Execution resumes after the last yield.
    - The local variables retain their values.
    - The function continues until it reaches the next yield or ends.

Example flow:
    ┌─────────────────────────────┐
    │ def simple_gen():           │
    │     yield "Step 1"          │
    │     yield "Step 2"          │
    │     yield "Step 3"          │
    └─────────────────────────────┘

Execution:
    g = simple_gen()
    next(g) → "Step 1"
    next(g) → "Step 2"
    next(g) → "Step 3"
"""

def simple_gen():
    print("Starting generator")
    yield "Step 1"
    print("After first yield")
    yield "Step 2"
    print("After second yield")
    yield "Step 3"
    print("Generator completed")

g = simple_gen()
print(next(g))  # Executes until first yield
print(next(g))  # Resumes until next yield
print(next(g))  # Final yield
try:
    print(next(g))
except StopIteration:
    print("All steps done!")


# ------------------------------------------------
# 4️⃣ Using for Loop with Generators
# ------------------------------------------------
"""
When you use a `for` loop on a generator, it automatically calls `next()`
and handles `StopIteration` internally.
"""

def numbers():
    for i in range(1, 4):
        yield i

print("Iterating using for loop:")
for num in numbers():
    print(num)


# ------------------------------------------------
# 5️⃣ Generator Internals — Using __next__()
# ------------------------------------------------
"""
Internally, the `next()` function calls the generator’s `__next__()` method.
"""

gen = numbers()
print("Manual iteration using __next__():")
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
try:
    print(gen.__next__())
except StopIteration:
    print("Generator exhausted internally!")


# ------------------------------------------------
# 6️⃣ Sending Data Back to a Generator (Advanced)
# ------------------------------------------------
"""
You can send values back into a generator using the `.send()` method.
This allows two-way communication with the generator.

Syntax:
    value = generator.send(data)

Example: A simple running sum generator.
"""

def running_total():
    total = 0
    while True:
        number = yield total
        if number is None:
            break
        total += number

gen = running_total()
print(next(gen))      # Initialize generator → Output: 0
print(gen.send(5))    # Add 5 → Output: 5
print(gen.send(10))   # Add 10 → Output: 15
print(gen.send(20))   # Add 20 → Output: 35
try:
    print(gen.send(None))  # Stop iteration
except StopIteration:
    print("Generator stopped.")


# ------------------------------------------------
# 7️⃣ Practical Example: Paginated Data Loader
# ------------------------------------------------
"""
Generators are ideal for fetching paginated or batched data efficiently.
"""

def load_data_in_batches(data, batch_size):
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]

dataset = list(range(1, 11))  # Example dataset
for batch in load_data_in_batches(dataset, 3):
    print("Loaded batch:", batch)


# ------------------------------------------------
# 8️⃣ Example: Reading Large Files Line-by-Line
# ------------------------------------------------
"""
This approach avoids reading entire files into memory.
"""

def read_file(filename):
    with open(filename, "r") as f:
        for line in f:
            yield line.strip()

# Example (uncomment to test with actual file)
# for line in read_file("data.txt"):
#     print(line)


# ------------------------------------------------
# 9️⃣ Infinite Generator with next()
# ------------------------------------------------
"""
Generators can be infinite, producing data continuously without stopping.
You can control them manually using next().
"""

def infinite_counter(start=1):
    while True:
        yield start
        start += 1

counter = infinite_counter()
for _ in range(5):
    print(next(counter))  # Prints 1 to 5 (continues infinitely if not stopped)


# ------------------------------------------------
# 🔟 Key Takeaways
# ------------------------------------------------
"""
✅ `yield` → Pauses function execution and returns a value.
✅ `next()` → Retrieves the next value from a generator.
✅ Generators remember their state between calls.
✅ When the generator is exhausted, `StopIteration` is raised.
✅ `for` loops handle iteration automatically.
✅ Use `.send()` for two-way communication with generators.
✅ Ideal for:
   - Streaming data
   - Handling large files
   - Creating pipelines
   - Managing infinite sequences
"""


# ================================================================
# Summary:
# yield → Creates and pauses generators
# next() → Retrieves the next item and resumes execution
# Generators → Efficient, stateful, and memory-friendly iterators
# ================================================================
