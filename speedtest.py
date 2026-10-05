"""Замер скорости интернета: 10 последовательных загрузок файла по URL."""
import time
import urllib.request

url = input("URL файла: ").strip()
request = urllib.request.Request(url, headers={"User-Agent": "speedtest/1.0"})

total_bytes, total_time = 0, 0.0
for i in range(1, 11):
    start = time.perf_counter()
    with urllib.request.urlopen(request, timeout=60) as resp:
        size = len(resp.read())
    elapsed = time.perf_counter() - start
    total_bytes += size
    total_time += elapsed
    print(f"Запрос {i:2}: {size / 2**20:.2f} МБ за {elapsed:.2f} с")

mb = total_bytes / 2**20
print(f"\nСреднее время запроса: {total_time / 10:.2f} с")
print(f"Скачано всего: {mb:.2f} МБ")
print(f"Скорость: {mb / total_time:.2f} МБ/с")
