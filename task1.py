import queue
import random
import time
import threading

# Створити чергу заявок
request_queue = queue.Queue()

# Унікальний ідентифікатор заявки
request_id = 0

stop_event = threading.Event()

def generate_request():
    global request_id
    while not stop_event.is_set():
        time.sleep(random.uniform(0.5, 2))  # Затримка для імітації часу між заявками
        request_id += 1
        request = f"Request-{request_id}"
        request_queue.put(request)
        print(f"Generated {request}")

def process_request():
    while not stop_event.is_set():
        if not request_queue.empty():
            request = request_queue.get()
            print(f"Processing {request}")
            time.sleep(random.uniform(1, 3))  # Імітація часу обробки заявки
            print(f"Processed {request}")
        else:
            print("Queue is empty, waiting for new requests...")
            time.sleep(1)  # Затримка перед перевіркою черги знову

# Запуск потоків для генерації і обробки заявок
generator_thread = threading.Thread(target=generate_request)
processor_thread = threading.Thread(target=process_request)

generator_thread.start()
processor_thread.start()

# Підтримка роботи потоків (Ctrl+C для завершення)
try:
    while True:
        user_input = input("Press 'Enter' to terminate the program: ")
        if user_input.strip().lower() == "":
            print("Stopping the program...")
            stop_event.set()  # Встановити прапорець для зупинки потоків
            generator_thread.join()  # Дочекатися завершення потоку генерації
            processor_thread.join()  # Дочекатися завершення потоку обробки
            print("Program stopped.")
            break
except Exception as e:
    print(f"An error occurred: {e}")





