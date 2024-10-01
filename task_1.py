import queue
import random
import time

# Створити чергу заявок
request_queue = queue.Queue()


# Функція для генерації нових заявок
def generate_request():
    request_id = random.randint(1000, 9999)
    print(f"Згенеровано заявку з ID: {request_id}")
    request_queue.put(request_id)


# Функція для обробки заявок
def process_request():
    if not request_queue.empty():
        request_id = request_queue.get()
        print(f"Обробка заявки з ID: {request_id}")
    else:
        print("Черга пуста, немає заявок для обробки.")


# Головний цикл програми
try:
    while True:
        generate_request()
        process_request()
        time.sleep(1)  # Затримка для імітації часу обробки
except KeyboardInterrupt:
    print("Програму завершено користувачем.")
