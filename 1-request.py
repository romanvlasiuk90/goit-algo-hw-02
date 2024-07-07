import queue
import random
import time
import threading

# Створення черги заявок
request_queue = queue.Queue()

# Функція для генерації нових заявок
def generate_request():
    request_id = random.randint(1, 99)
    print(f"CTRL+C для зупинки роботи")
    request = f"Заявка-{request_id}"
    print(f"Згенеровано: {request}")
    request_queue.put(request)

# Функція для обробки заявок
def process_request():
    while True:
        if not request_queue.empty():
            request = request_queue.get()
            print(f"Обробка: {request}")
            # Імітація часу обробки заявки
            time.sleep(random.randint(1, 3))
            print(f"Завершено: {request}")
        else:
            print("Черга пуста. Очікування нових заявок...")
            time.sleep(2)

# Головний цикл програми
def main():
    try:
        # Створення потоку для обробки заявок
        processing_thread = threading.Thread(target=process_request)
        processing_thread.daemon = True
        processing_thread.start()
        while True:
            generate_request()
            # Імітація часу між генерацією заявок
            time.sleep(random.randint(1, 5))
    except KeyboardInterrupt:
        print("Програму перервано та зупинено.")

if __name__ == "__main__":
    main()