import concurrent.futures
import datetime

import requests


def send_request(original_url):
    url = "http://127.0.0.1:8080/api/tinyurl"
    headers = {'Content-Type': 'application/json'}
    data = {"url": original_url, "request_ts": datetime.datetime.now().isoformat(), "client_app": "API"}
    response = requests.post(url, json=data, headers=headers)
    return response.json()


if __name__ == "__main__":

    original_urls = [f"url_ams_{i}.com" for i in range(66000, 66500)]
    # original_urls.extend([f"url_12{i}.com" for i in range(5)])
    # original_urls.sort()
    start_time = datetime.datetime.now()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(send_request, original_url) for original_url in original_urls]

        for future in concurrent.futures.as_completed(results):
            print(datetime.datetime.now(), future.result())

    print(datetime.datetime.now().second - start_time.second)

# 10, 500 --> 12
# 1, 500 --> 37
# 5, 500 --> 12
# 100, 500 --> 19
# 50, 500 --> 12
# 3, 500 --> 13





