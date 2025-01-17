import requests
import re
from multiprocessing import Pool

req = requests.Session()

req.headers = {"Cookie":"ВСТАВЬ СЮДА СВОИ КУКИ", "Host": "hh.ru", "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15"}

def send_req(item):
    print(item)
    check = req.post('https://hh.ru//applicant/vacancy_response/popup', data={"_xsrf":"СУДА НУЖНО ВСТАВИТЬ СВОЙ _xsrf ТОКЕН", "letter": """ВСТАВЬ СЮДА СВОЕ ПИСЬМО""", "lux": True, "withoutTest": "no", "hhtmFromLabel": "undefined", "hhtmSourceLabel": "undefined"})

    print(check.status_code, item)
    if check.status_code != 200:
        if check.json()['error' ] == 'negotiations-limit-exceeded':
            return False

if __name__ == "__main__":
    n = 0
    sendet = 0
    pool = Pool(processes=70)
    while True:
        data = req.get(f"СЮДА ВСТАВЬ СВОЙ ЗАПРОС&page={n}").text
        links = re.findall('https://hh.ru/vacancy/(\d*)?', data, re.DOTALL)
        if links == []:
            break
        check = pool.map(send_req, links)
        if False in check:
            break
    pool.close()
    pool.join()