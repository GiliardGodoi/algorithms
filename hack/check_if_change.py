
import requests
import time
from bs4 import BeautifulSoup

def get_content(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f"{response.status_code=}")
    content = response.content.decode()
    html = BeautifulSoup(content, 'html.parser')
    return html


NUM_MAX_ITERATION = 100

url = "https://giliardgodoi.github.io"

html = get_content(url)
div = html.find(id='regular')

for i in range(NUM_MAX_ITERATION):
    content = get_content(url)
    div_2 = html.find(id='regular')
    if div.text == div_2.text:
        print(f"{i} >> Página não foi modificada!")
        print("Esperando...")
    else :
        print(f"{i} >> PÁGINA MODIFICADA!! ^.^")

    time.sleep(1800)