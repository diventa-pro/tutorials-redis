import threading
import time
import random

# Define a function for the thread
def print_numbers():
    for i in range(10):
        time.sleep( random.randint(0,4) )
        print(i)

def print_letters():
    for letter in 'abcdefghij':
        time.sleep( random.randint(0,4) )
        print(letter)

# Create two threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()

print("Both threads are finished")
