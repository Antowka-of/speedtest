"""Замер скорости интернета: 10 последовательных загрузок файла по URL."""
import argparse
import sys
import time
import urllib.request

REQUESTS = 10


def download(url):
    """Скачивает файл целиком, возвращает (байты, секунды)."""
    # Некоторые серверы отклоняют запросы без User-Agent (403)
    request = urllib.request.Request(url, headers={"User-Agent": "speedtest-script/1.0"})
    start = time.perf_counter()
    with urllib.request.urlopen(request, timeout=60) as resp:
        size = len(resp.read())
    return size, time.perf_counter() - start


def main():
    parser = argparse.ArgumentParser(description="Замер скорости загрузки по URL")
    parser.add_argument("url", help="адрес тяжёлого файла, например картинки")
    args = parser.parse_args()

    total_bytes = 0
    total_time = 0.0
    for i in range(1, REQUESTS + 1):
        try:
            size, elapsed = download(args.url)
        except Exception as e:
            sys.exit(f"Запрос {i} не удался: {e}")
        total_bytes += size
        total_time += elapsed
        print(f"Запрос {i:2}: {size / 1024 / 1024:.2f} МБ за {elapsed:.2f} с")

    mb = total_bytes / 1024 / 1024
    speed = mb / total_time
    print()
    print(f"Среднее время запроса: {total_time / REQUESTS:.2f} с")
    print(f"Скачано всего:         {mb:.2f} МБ")
    print(f"Скорость:              {speed:.2f} МБ/с ({speed * 8:.2f} Мбит/с)")


if __name__ == "__main__":
    main()
