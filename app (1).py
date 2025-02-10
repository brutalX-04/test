from flask import Flask, request, jsonify
import requests, json

app = Flask(__name__)

def get_cookies(username):
    try:
        session = requests.Session()
        headers = {
            'authority': 'www.instagram.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'dpr': '1.600000023841858',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
            'sec-ch-ua-full-version-list': '"Not A(Brand";v="8.0.0.0", "Chromium";v="132.0.6961.0"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"SM-A037F"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"13.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
            'viewport-width': '980',
        }
        session.get(f'https://www.instagram.com/{username}/', headers=headers, proxies={'https': 'http://gnscsrsa:hw7c8cugn89z@198.23.239.134:6540'})
        return session

    except Exception as e:
        return 'Error'


def get_profile(username, session):
    try:
        cook = session.cookies.get_dict()
        headers = {
            'authority': 'www.instagram.com',
            'accept': '/',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'referer': 'https://www.instagram.com/brutalid_/',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
            'sec-ch-ua-full-version-list': '"Not A(Brand";v="8.0.0.0", "Chromium";v="132.0.6961.0"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"SM-A037F"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"13.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
            'x-asbd-id': '129477',
            'x-csrftoken': cook['csrftoken'],
            'x-ig-app-id': '1217981644879628',
            'x-ig-www-claim': '0',
            'x-requested-with': 'XMLHttpRequest',
        }

        params = {
            'username': username,
        }
        response = session.get('https://www.instagram.com/api/v1/users/web_profile_info/',params=params,headers=headers, proxies={'https': 'http://gnscsrsa:hw7c8cugn89z@198.23.239.134:6540'}).json()

        return response

    except Exception as e:
        return jsonify({"message": 'Failled fetch data'})

# Endpoint GET yang menerima satu atau lebih parameter
@app.route('/api', methods=['GET'])
def check():
    # Mengambil parameter
    username = request.args.get('username')

    # Membuat respon
    if username:
        session = get_cookies(username)
        if session != 'Error':
            data = get_profile(username, session)
            return jsonify(data)
    else:
        return jsonify({"message": 'params requiered'})


if __name__ == '__main__':
    app.run(debug=True, port=5010)