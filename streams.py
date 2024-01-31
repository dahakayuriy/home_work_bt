import threading
import random
import time

# 1
data = [random.randint(1, 100) for _ in range(10)]

def process_data(data):
  
    sorted_data = sorted(data)
    print("Processed data:", sorted_data)

def threaded_process_data(data):
 
    half_length = len(data) // 2

   
    data_part1 = data[:half_length]
    data_part2 = data[half_length:]

    thread1 = threading.Thread(target=process_data, args=(data_part1,))
    thread2 = threading.Thread(target=process_data, args=(data_part2,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

if __name__ == "__main__":
    print("Original data:", data)

    process_data(data)

    print("\nThreaded processing:")
    
    threaded_process_data(data)

################################################
#2
data = [random.randint(1, 100) for _ in range(10**6)]  

def process_data(data):
    sorted_data = sorted(data)
   

def threaded_process_data(data):
    half_length = len(data) // 2
    data_part1 = data[:half_length]
    data_part2 = data[half_length:]

    thread1 = threading.Thread(target=process_data, args=(data_part1,))
    thread2 = threading.Thread(target=process_data, args=(data_part2,))

    start_time = time.time()

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Threaded processing time:", elapsed_time)

if __name__ == "__main__":
    start_time = time.time()

    process_data(data)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Sequential processing time:", elapsed_time)

    print("\nThreaded processing:")
    threaded_process_data(data)