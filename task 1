import queue
import random
import time

def generate_request(request_queue, request_id):
    #Створює нову заявку та додає її до черги
    request_data = f"Заявка #{request_id} (клієнт {random.randint(100, 999)})"
    request_queue.put(request_data)
    print(f"\nНова заявка додана до черги: {request_data}")
    print(f"Заявок у черзі: {request_queue.qsize()}")
    return request_id + 1

def process_request(request_queue):
    #Обробляє першу заявку у черзі, якщо черга не пуста
    if not request_queue.empty():
        processed_request = request_queue.get()
        print(f"\n Обробляється заявка: {processed_request}")
        print(f"Залишилось заявок у черзі: {request_queue.qsize()}")
    else:
        print("\n Черга пуста - немає заявок для обробки.")

def main():
    request_queue = queue.Queue()
    request_id = 1
    
    print("Сервісний центр розпочав роботу. Для виходу натисніть Ctrl+C")
    
    try:
        while True:
            # Імітація випадкового часу між заявками
            time.sleep(random.uniform(0.5, 2))
            
            # Генеруємо нову заявку з ймовірністю 70%
            if random.random() < 0.7:
                request_id = generate_request(request_queue, request_id)
            
            # Обробляємо заявку з ймовірністю 60%
            if random.random() < 0.6:
                process_request(request_queue)
                
    except KeyboardInterrupt:
        print("\nСервісний центр завершує роботу...")
        print(f"Усього оброблено заявок: {request_id - 1}")
        print(f"Залишилось у черзі: {request_queue.qsize()}")

if __name__ == "__main__":
    main()