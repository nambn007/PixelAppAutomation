import requests

import requests


def get_user_id(account_name:str) -> str:
    headers = {
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'Referer': 'https://www.pixels.tips/players/657e74354bba74cc55c63407',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
    }
    params = {
        'x-sveltekit-invalidated': '11',
    }
    response = requests.get(f'https://www.pixels.tips/players/{account_name}/__data.json', params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        last_slash_index = data['location'].rfind('/')
        result = data['location'][last_slash_index + 1:]
        return result
    else:
        print("Failed to retrieve data. Status code:", response.status_code)
if __name__ == '__main__':
    print(get_user_id('hd2218586.ron'))