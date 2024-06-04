import requests
import logging
import asyncio
import websockets
import json

# Import required config properties from config.py, if required change the informaiton relavent to prod domain
from config import TOKEN_ENDPOINT, WS_URL, USERNAME, PASSWORD, CLIENT_ID, CLIENT_SECRET, GRANT_TYPE, SCOPE


# Function to obtain access token by authenticating via username and password
async def get_access_token():
    data = {
        'grant_type': GRANT_TYPE,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'username': USERNAME,
        'password': PASSWORD,
        'scope': SCOPE
    }

    response = requests.post(TOKEN_ENDPOINT, data)

    if response.status_code == 200:
        access_token = response.json()['access_token']
        logging.info("Token obtained successfully: %s", access_token)
        return access_token
    else:
        logging.error("Failed to obtain token: %s", response.text)
        return None

# Using the access token connect to Web Socket and wait for the message
async def connect_to_websocket(access_token):
    logging.info("Connect to web socket and get the subscription Info")

    url_with_token = WS_URL + '&access_token=' + access_token
    try:
        async with websockets.connect(url_with_token) as websocket:
            logging.info("Connected to WebSocket")
            async for message in websocket:
                pretty_message = json.dumps(json.loads(message), indent=4)
                print(f"Received subscription message :\n{pretty_message}")
    except Exception as e:
        print(f"Error during connection: {e}")


async def main():
    access_token = await get_access_token()

    if access_token:
        logging.info("Access token obtained : ", access_token)
        # Use token to connect to web socket using the token
        await connect_to_websocket(access_token)
    else:
        print("Failed to get access token.")



if __name__ == '__main__':
    # Configure the root logger
    #logger = logging.getLogger()
    #logger.setLevel(logging.DEBUG)
    asyncio.run(main())
