import json

import requests

def get_price(id_item:str,pid:str) -> int:
    headers = {
        'authority': 'pixels-server.pixels.xyz',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'origin': 'https://play.pixels.xyz',
        'referer': 'https://play.pixels.xyz/',
        'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    }

    params = {
        'pid': pid,
        'v': '1712683071488',
    }
    response = requests.get(f'https://pixels-server.pixels.xyz/v1/marketplace/item/{id_item}', params=params,
                            headers=headers).__dict__['_content'].decode('utf-8')
    data_dict = json.loads(response)
    result = data_dict['listings']
    result2 = result[0]
    result3 = result2['price']
    return result3



if __name__ == '__main__':
    a = get_price("itm_Iron_Ore","65f5dd9fca1af871f13456ea")
    print(type(a))

