import time
from time import sleep
from threading import Thread

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i} \n')
            time.sleep(0.1)

            print(f'Завершилась запись в файл {file_name}')

start_time = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time = time.time()
ttl_time = end_time - start_time
print(f'Время выполнения функций: {ttl_time:.6f} секунд')

start_time2 = time.time()
thread_1 = Thread(target=write_words, args=(10, 'example5.txt'))
thread_2 = Thread(target=write_words, args=(30, 'example6.txt'))
thread_3 = Thread(target=write_words, args=(200, 'example7.txt'))
thread_4 = Thread(target=write_words, args=(100, 'example8.txt'))

thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()

thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()
end_time2 = time.time()
ttl_time2 = end_time2 - start_time2
print(f'Время выполнения потоков: {ttl_time2:.6f} секунд')

print(f'Время выполнения потоков быстрее времени выполнения функций на:{ttl_time - ttl_time2:.6f} секунд')




