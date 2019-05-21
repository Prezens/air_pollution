import requests
from bs4 import BeautifulSoup
import json
import pandas as pd


def get_html():
    r = requests.get('https://airkaz.org/bishkek.php')
    return r.text


def response_data(html):
    data = []
    soup = BeautifulSoup(html, 'html.parser')
    script = soup.find_all('script')[5].text
    script_format = script[script.find('['):]
    sensors_data = json.loads(script_format)

    for sensor in sensors_data:
        if sensor['city'] == 'Бишкек':
            data.append(sensor)

    return data


def main():
    request = get_html()
    data = response_data(request)
    print(data)

    data_frame = pd.DataFrame(data)
    print(data_frame)

    data_frame.to_csv('data.csv', index=False, mode='a', encoding='utf-8')


if __name__ == '__main__':
    main()
