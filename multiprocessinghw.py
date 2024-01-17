import multiprocessing

def process_data(data_chunk):
    return len(data_chunk.split())

def main():
    with open("large_data.txt", "r", encoding="utf-8") as file:
        data = file.read()

    num_processes = multiprocessing.cpu_count()

    data_chunks = [data[i:i + len(data) // num_processes] for i in range(0, len(data), len(data) // num_processes)]

    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.map(process_data, data_chunks)

    total_words = sum(results)

    print(f"Total words in the dataset: {total_words}")

if __name__ == "__main__":
    main()