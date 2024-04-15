import requests


def get_pixel_balance(wallet_adress:str) -> float:

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'content-type': 'application/json',
        'origin': 'https://app.roninchain.com',
        'referer': 'https://app.roninchain.com/',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    }

    json_data = {
        'ownerAddress': wallet_adress,
        'tokenStandards': [
            'ERC20',
        ],
    }

    response = requests.post('https://skynet-api.roninchain.com/ronin/tokens/balances/search', headers=headers,
                             json=json_data)
    result = response.text
    return result
    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    # data = '{"ownerAddress":"0xe23f09388142db5b47578cf246bfd0a2a8a57202","tokenStandards":["ERC20"]}'
    # response = requests.post('https://skynet-api.roninchain.com/ronin/tokens/balances/search', headers=headers, data=data)



def get_usdt_balance(wallet_adress:str):
    'https://skynet-api.roninchain.com/ronin/accounts/0x1cd561f05aa3802d9ff76b56c15f174f9a068674'
    pass