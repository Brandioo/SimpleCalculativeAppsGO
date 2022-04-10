import requests
import threading

links = ["https://reqbin.com/echo/get/json/page/1"]

def fetch_results(list_of_links):
    results = []
    for link in list_of_links:
        response = requests.get(link)
        if response.code == 200:
            items = response.json()["items"]
            results.append(items)
            print(items)
    return results
first_chunk = links[:len(links)//3]
second_chunk = links[len(links)//3:]
thread1 = threading.Thread(target= fetch_results, args = (first_chunk,))
thread2 = threading.Thread(target= fetch_results, args = (second_chunk,))
thread1.start()
thread2.start()







