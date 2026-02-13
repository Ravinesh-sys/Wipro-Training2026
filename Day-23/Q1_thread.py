import requests
import threading
import time

urls = [
    "https://example.com/data1",
    "https://example.com/data2",
    "https://example.com/data3",
    "https://example.com/data4"
]

def download_file(url, filename):
    response = requests.get(url)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(response.text)

# Sequential download
start_seq = time.time()

for i, url in enumerate(urls, start=1):
    filename = f"data{i}.txt"
    download_file(url, filename)

end_seq = time.time()
print("Sequential Time:", end_seq - start_seq)

# Threading download
start_thread = time.time()
threads = []

for i, url in enumerate(urls, start=1):
    filename = f"data{i}.txt"
    t = threading.Thread(target=download_file, args=(url, filename))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end_thread = time.time()
print("Threading Time:", end_thread - start_thread)
