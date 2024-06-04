from flask import Flask, request, redirect
from urllib.parse import urlencode
import requests
import logging
import asyncio
import websockets
from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, AUTHORIZATION_ENDPOINT, TOKEN_ENDPOINT, WS_URL

app = Flask(__name__)


@app.route('/')
def index():
    params = {
        'client_id': CLIENT_ID,
        'redirect_uri': REDIRECT_URI,
        'response_type': 'code',
        'scope': 'openid'
    }
    auth_url = f'{AUTHORIZATION_ENDPOINT}?' + urlencode(params)
    return redirect(auth_url)

@app.route('/callback')
def callback():
    auth_code = request.args.get('code')
    print("AUTH CODE")
    print(auth_code)
    logging.info("Obtained Auth code")

    data = {
        'grant_type': 'authorization_code',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': REDIRECT_URI,
        'code': auth_code
    }
    response = requests.post(TOKEN_ENDPOINT, data=data)
    print(response.json())
    if response.status_code == 200:
        access_token = response.json()['access_token']
        asyncio.run(connect_to_websocket(access_token))
        return f'Token obtained successfully: {access_token}'
    else:
        return 'Failed to obtain token'


async def connect_to_websocket(access_token):
    print("Connect to Web Socket and get the Subscription Info")
    url_with_token = WS_URL + '&access_token=' + access_token
    try:
        async with websockets.connect(url_with_token) as websocket:
            print("Connected to WebSocket")
            async for message in websocket:
                print(f"Received message: {message}")
    except Exception as e:
        print(f"Error during connection: {e}")


if __name__ == '__main__':
    app.run(debug=True)
