# Задача: Написать скрипт на bash, python или groovy, 
# который будет контролировать потребление памяти и генерировать 
# предупреждение путем отправки HTTP запроса на API.
import requests
import time
import os

THRESHOLD = 1000
API_ENDPOINT = "http://your-api-endpoint.com/alarm"

while True:
    free_mem = int(os.popen('free -m | awk \'NR==2{print $4}\'').read())
    
    if free_mem < THRESHOLD:
        payload = {"alarm": "Low Memory", "free_memory": free_mem}
        requests.post(API_ENDPOINT, data=payload)
    
    time.sleep(60)

