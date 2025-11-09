# ================================================================
# File: 08_Real_World_Examples_of_Generators.py
# Topic: Real-World Use Cases of Generators in Python
# ================================================================

"""
Generators are extremely useful in **real-world Python applications**
where performance, memory efficiency, and lazy evaluation are important.

They allow us to handle **large data**, **infinite sequences**, and **streaming data**
without loading everything into memory at once.

Below are several practical examples demonstrating how generators
are used in production-grade Python code.
"""

# ------------------------------------------------
# 1️⃣ Example: Reading Large Files Efficiently
# ------------------------------------------------
"""
Problem:
Reading a large file into memory using `readlines()` can cause memory issues.

Solution:
Use a generator to read one line at a time.
"""

def read_large_file(file_path):
    """Generator that yields one line at a time from a large file."""
    with open(file_path, "r") as file:
        for line in file:
            yield line.strip()

# Example Usage (uncomment to test)
# for line in read_large_file("large_dataset.txt"):
#     print(line)


# ------------------------------------------------
# 2️⃣ Example: Streaming Data (Simulating Real-Time Data)
# ------------------------------------------------
"""
In data streaming or IoT systems, generators can simulate real-time data flow.
"""

import time
import random

def sensor_data_stream():
    """Simulate a sensor that continuously yields readings."""
    while True:
        yield random.uniform(20.0, 30.0)  # Random temperature value
        time.sleep(1)

# Example Usage (uncomment to simulate)
# for data in sensor_data_stream():
#     print("Sensor reading:", round(data, 2))


# ------------------------------------------------
# 3️⃣ Example: Paginating API Responses
# ------------------------------------------------
"""
APIs often return paginated responses. Generators can be used to fetch
each page only when needed, reducing unnecessary API calls.
"""

def fetch_api_pages(total_pages):
    """Simulate paginated API data retrieval."""
    for page in range(1, total_pages + 1):
        yield f"Fetched data from page {page}"

# Example Usage
for page_data in fetch_api_pages(3):
    print(page_data)


# ------------------------------------------------
# 4️⃣ Example: Data Pipeline using Generators
# ------------------------------------------------
"""
Generators can be chained together to form **data pipelines**,
where each stage processes and passes data to the next stage.
"""

def get_data():
    for i in range(1, 6):
        yield i

def square_data(numbers):
    for num in numbers:
        yield num ** 2

def filter_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num

# Combine generators into a pipeline
data_pipeline = filter_even(square_data(get_data()))
print("\nProcessed Data Pipeline Output:", list(data_pipeline))
# Output: [4, 16]


# ------------------------------------------------
# 5️⃣ Example: Infinite Sequence Generator
# ------------------------------------------------
"""
Generators are ideal for creating infinite sequences, such as natural numbers,
without consuming infinite memory.
"""

def infinite_numbers(start=1):
    """Generate an infinite sequence of numbers."""
    while True:
        yield start
        start += 1

# Example: Print first 5 numbers from infinite generator
import itertools
print("\nFirst 5 natural numbers:", list(itertools.islice(infinite_numbers(), 5)))


# ------------------------------------------------
# 6️⃣ Example: Lazy Evaluation in Large Computations
# ------------------------------------------------
"""
Generators allow computations to be evaluated lazily,
which means they compute results only when needed.
"""

def compute_square(numbers):
    for num in numbers:
        yield num ** 2

nums = range(1, 6)
squares = compute_square(nums)
print("\nSquares (lazy evaluation):")
for sq in squares:
    print(sq)


# ------------------------------------------------
# 7️⃣ Example: Log File Monitor (Tail Utility)
# ------------------------------------------------
"""
A generator can mimic the Unix 'tail -f' command,
which continuously monitors a log file for new lines.
"""

import os

def follow_file(file_path):
    """Continuously yield new lines as they are added to a file."""
    with open(file_path, "r") as file:
        file.seek(0, os.SEEK_END)  # Go to end of file
        while True:
            line = file.readline()
            if not line:
                time.sleep(0.5)
                continue
            yield line.strip()

# Example Usage (uncomment to test)
# for new_line in follow_file("system.log"):
#     print("New Log Entry:", new_line)


# ------------------------------------------------
# 8️⃣ Example: Database Record Streaming
# ------------------------------------------------
"""
When working with large datasets in databases,
generators help retrieve records in batches, avoiding memory overflow.
"""

def fetch_records_in_batches(total_records, batch_size):
    """Simulate fetching records in chunks."""
    for start in range(0, total_records, batch_size):
        yield list(range(start + 1, min(start + batch_size + 1, total_records + 1)))

# Example Usage
print("\nDatabase Records (in batches):")
for batch in fetch_records_in_batches(10, 3):
    print(batch)


# ------------------------------------------------
# 9️⃣ Example: Prime Number Generator
# ------------------------------------------------
"""
A generator can efficiently produce prime numbers without storing all of them.
"""

def generate_primes(limit):
    """Yield prime numbers up to a given limit."""
    for num in range(2, limit + 1):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num

print("\nPrime numbers up to 20:", list(generate_primes(20)))


# ------------------------------------------------
# 🔟 Key Takeaways
# ------------------------------------------------
"""
✅ Generators are perfect for:
   - Large file processing
   - Streaming and real-time data
   - Lazy evaluation and pipelines
   - Database or API pagination
   - Infinite sequences

✅ Benefits:
   - Memory-efficient
   - Clean, readable, and scalable code
   - Ideal for data-driven and backend applications
"""

# ================================================================
# Summary:
# Generators in real-world applications enable efficient handling
# of large or infinite data streams, enhance scalability,
# and help write cleaner, high-performance Python code.
# ================================================================
